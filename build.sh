#!/bin/bash

# Download and extract Tesseract prebuilt binaries
wget https://example.com/path/to/tesseract.tar.gz
tar -xvf tesseract.tar.gz

# Move Tesseract binaries to /usr/local/bin (or any other suitable location in the PATH)
mv tesseract/bin/* /usr/local/bin/

# Optionally, remove the downloaded archive and extracted directory to save space
rm tesseract.tar.gz
rm -r tesseract
