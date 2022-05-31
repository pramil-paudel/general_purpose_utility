from zdrive import Downloader

output_directory = "/Users/patthar/Downloads"
d = Downloader()

# folder which want to download from Drive
folder_id = '1Uzpf8L72q45XoO-jdw96B_qsWkz2ICNP'
d.downloadFolder(folder_id, destinationFolder=output_directory)