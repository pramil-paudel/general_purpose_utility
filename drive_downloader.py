import gdown

url = 'https://drive.google.com/uc?id=1Uzpf8L72q45XoO-jdw96B_qsWkz2ICNP'
output = 'face_data_download.zip'
gdown.download(url, output, quiet=False)