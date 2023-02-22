from pathlib import Path
from time import time_ns
import asyncio
from reduct import Client, BucketSettings, QuotaType
import os
from PIL import Image

async def main():
    client = Client("http://localhost:8383")
    dataset_name = "mnist"
    blob_field = "image"
    bucket = await client.create_bucket("my-bucket",BucketSettings(quota_type=QuotaType.FIFO, quota_size=1_000_000_000),exist_ok=True,)
    folder_path = "./mnist_png/training"
    for filename in os.listdir(folder_path):
        label_path = os.path.join(folder_path, filename)
        for i in os.listdir(label_path):
            img_path=os.path.join(label_path,i)
            with open(img_path,'rb') as f:
                img_data=f.read()
            record = {
                "label": filename,
                blob_field: img_data
            }
            await bucket.write("entry-1", record, timestamp=12345)



if __name__ == "__main__":
    asyncio.run(main())