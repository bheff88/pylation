#!/bin/bash
wget -nv https://repo.continuum.io/archive/Anaconda3-4.2.0-Linux-x86_64.sh
bash Anaconda3-4.2.0-Linux-x86_64.sh -b -p ~/anaconda3
rm Anaconda3-4.2.0-Linux-x86_64.sh
echo 'export PATH="~/anaconda3/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
./anaconda3/bin/conda update -y conda
./anaconda3/bin/conda create -y -n CPU python=3.5 pickleshare pandas scipy h5py networkx
sudo apt install make gcc gfortran libncurses-dev
wget https://cdaweb.gsfc.nasa.gov/pub/software/cdf/dist/latest-release/linux/cdf36_4-dist-all.tar.gz
tar xf cdf36_4-dist-all.tar.gz
cd ~/cdf36_4-dist
make OS=linux ENV=gnu CURSES=yes FORTRAN=no UCOPTIONS=-O2 SHARED=yes -j4 all
make install
echo 'export CDF_BASE=$HOME/cdf-dist' >> ~/.bashrc
echo 'export CDF_INC=$CDF_BASE/include' >> ~/.bashrc
echo 'export CDF_LIB=$CDF_BASE/lib' >> ~/.bashrc
echo 'export LD_LIBRARY_PATH=$HOME/cdf-dist/lib:$LD_LIBRARY_PATH' >> ~/.bashrc
source ~/.bashrc
source ~/anaconda3/bin/activate CPU
rm -rf *.gz
pip install spacepy
