import gdown

url = 'https://drive.google.com/u/0/uc?id=1vBMMpfs-vgglpPRBIwsati9ALnJGI-2d&export=download'
output = 'ground_truth_face_images.tgz'
gdown.download(url, output, quiet=False)