#!/bin/bash
#!/bin/bash
#SBATCH -p gpu
#SBATCH --gres="gpu:titanxp:1"
#SBATCH -c 4
#SBATCH --mem=32G
#SBATCH --time=48:00:00
#SBATCH -J train_test_separator
#SBATCH -o slurm-%j.out

wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1Uzpf8L72q45XoO-jdw96B_qsWkz2ICNP' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1Uzpf8L72q45XoO-jdw96B_qsWkz2ICNP" -O face_data_set.tar.gz && rm -rf /tmp/cookies.txt