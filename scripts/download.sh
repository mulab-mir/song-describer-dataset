#!/bin/bash

if [[ $(basename "$PWD") != "data" ]]; then
    if [[ $(basename "$PWD") == "scripts" ]]; then
        cd ../data || { echo "Failed to change directory to ../data"; exit 1; }
    else
        echo "Please run this script from the data directory or the scripts directory."
        exit 1
    fi
fi
if [[ $(basename "$PWD") != "data" ]]; then
    cd ../data || { echo "Failed to change directory to ../data"; exit 1; }
fi

# Set the Zenodo record id number
RECORD_ID="10072001"
# download main dataset file "song_describer.csv"
curl -L -O "https://zenodo.org/record/${RECORD_ID}/files/song_describer.csv"

# download audio data (> 3GB)
curl -L -O "https://zenodo.org/record/${RECORD_ID}/files/audio.zip"
unzip audio.zip
rm audio.zip

