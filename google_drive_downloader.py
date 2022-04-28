import gdown

rice_university_face_data = "https://drive.google.com/u/0/uc?id=1Uzpf8L72q45XoO-jdw96B_qsWkz2ICNP&export=download"
reconstructed_images = "https://drive.google.com/u/0/uc?id=1vBMMpfs-vgglpPRBIwsati9ALnJGI-2d&export=download"

url = 'https://drive.google.com/u/0/uc?id=1vBMMpfs-vgglpPRBIwsati9ALnJGI-2d&export=download'

output = 'flatcam_data.tar.gz'
output2= 'ground_truth_face_images.tar.gz'

gdown.download(url, output, quiet=False)
gdown.download(url, output2, quiet=False)