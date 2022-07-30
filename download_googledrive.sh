#!/bin/bash
#!/bin/bash
#SBATCH -p gpu
#SBATCH --gres="gpu:titanxp:1"
#SBATCH -c 4
#SBATCH --mem=32G
#SBATCH --time=48:00:00
#SBATCH -J train_test_separator
#SBATCH -o slurm-%j.out

python3 drive_downloader.py