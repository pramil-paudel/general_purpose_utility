#!/bin/bash
#!/bin/bash
#SBATCH -p gpu
#SBATCH --gres="gpu:k40:1"
#SBATCH -c 4
#SBATCH --mem=32G
#SBATCH --time=48:00:00
#SBATCH -J DATA_DOWNLOAD
#SBATCH -o slurm-%j.out
wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1HROmgviy4jUUUaCdvvrQ8PcqtNg2jn3G' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1HROmgviy4jUUUaCdvvrQ8PcqtNg2jn3G" -O utk_part_1.tar.gz  && rm -rf /tmp/cookies.txt