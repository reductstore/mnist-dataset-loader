from time import time_ns
import asyncio
import os
from time import time_ns

from reduct import Client, BucketSettings, QuotaType


async def main():
    client = Client("http://localhost:8383")
    bucket = await client.create_bucket("my-bucket",
                                        BucketSettings(quota_type=QuotaType.FIFO, quota_size=1_000_000_000),
                                        exist_ok=True, )
    path = "./mnist_png"
    for foldername in os.listdir(path):
        dataset_name = foldername
        folder_path = os.path.join(path, dataset_name)
        for digit in os.listdir(folder_path):
            label_path = os.path.join(folder_path, digit)
            for i in os.listdir(label_path):
                img_path = os.path.join(label_path, i)
                with open(img_path, 'rb') as f:
                    img_data = f.read()
                labels = {
                    "digit": digit,
                    "dataset": "mnist"
                }
                ts = time_ns() / 1000
                await bucket.write("mnist-" + dataset_name, img_data, timestamp=ts, labels=labels, content_type="image/png")
            # async with bucket.read(dataset_name) as rec:
            #     data=await rec.read_all()
            #     print(data)


if __name__ == "__main__":
    asyncio.run(main())
