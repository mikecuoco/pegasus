#!/bin/bash
set -e

echo "Setting up Pegasus development environment..."

# 1. Install all system dependencies
# This includes Git, Java, CMake, R, and all C/C++ libraries
echo "Installing system dependencies..."
sudo apt update -q
sudo apt install -y --no-install-recommends \
    libfftw3-dev \
    default-jdk \
    git \
    git-lfs \
    cmake \
    r-base \
    r-base-dev \
    gfortran \
    libblas-dev \
    liblapack-dev \
    libcurl4-openssl-dev \
    libssl-dev \
    libxml2-dev \
    cargo \
    libfontconfig1-dev \
    libcairo2-dev \
    libxt-dev \
    libharfbuzz-dev \
    libfribidi-dev \
    libfreetype-dev \
    libpng-dev \
    libtiff5-dev \
    libjpeg-dev \
    libhdf5-dev \
    libgsl-dev \
    libgslcblas0 \
    libgmp-dev \
    libmpfr-dev

# Clean up apt cache to save space
sudo apt-get clean && sudo rm -rf /var/lib/apt/lists/*

# 2. Install Seurat R package
echo "Installing Seurat R package..."
sudo R -e 'install.packages("SeuratObject", repos="http://cran.rstudio.com/")'

# 3. Install Python packages
echo "Installing Python packages for Pegasus..."
pip install --upgrade pip
pip install flake8 pytest setuptools wheel cython
pip install "zarr==2.*"
pip install git+https://github.com/lilab-bcb/pegasusio@master
# This installs the main pegasuspy package in editable mode with all extras.
pip install -e .[louvain,tsne,torch,forceatlas,scvi,pseudobulk,rpy2]

# 4. Clone test data
if [ ! -d "tests/data" ]; then
    echo "Fetching test data..."
    git clone https://github.com/lilab-bcb/pegasus-test-data.git ./tests/data
else
    echo "Test data already present."
fi

echo "✓ Setup complete!"


