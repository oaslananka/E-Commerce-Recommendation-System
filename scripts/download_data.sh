#!/bin/bash

echo "Downloading datasets..."

wget -P ../data/raw/ https://files.grouplens.org/datasets/movielens/ml-latest-small.zip
unzip ../data/raw/ml-latest-small.zip -d ../data/raw/
rm ../data/raw/ml-latest-small.zip

echo "The datasets were successfully downloaded and opened."
