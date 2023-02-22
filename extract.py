import urllib.request
import tarfile

url = "https://github.com/reductstore/mnist_png/blob/master/mnist_png.tar.gz?raw=true"
file_name = "mnist_png.tar.gz"

# Download the file from the URL
urllib.request.urlretrieve(url, file_name)

# Extract the files from the tar archive
tar = tarfile.open(file_name, "r:gz")
tar.extractall()
tar.close()