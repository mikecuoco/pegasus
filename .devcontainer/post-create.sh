#!/bin/bash
set -e

echo "Setting up Pegasus..."

# Install system dependencies
sudo apt-get update -qq
sudo apt-get install -y --no-install-recommends libfftw3-dev default-jdk

# Install pegasus (with all extras including rpy2)
pip install -e ".[all]"

# Install testing tools
pip install pytest pytest-cov

# Clone test data if not present
if [ ! -d "tests/data" ]; then
    echo "Fetching test data..."
    git clone https://github.com/lilab-bcb/pegasus-test-data.git ./tests/data
fi

echo "✓ Setup complete! Run 'pytest tests/' to test."

