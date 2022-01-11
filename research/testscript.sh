#!/bin/bash

function getTime() {
	local timestamp=$(date +%s);
	echo $timestamp;
}

# Get New Timestamp
timestamp="$(getTime)"

# Make backup copies
rm input.png
rm output.png
rm output.mid

# Start New Session
raspistill -o input.png
convert input.png -monochrome -filter point -resize 1000x128 output.png
python3 ~/git/imgnoise/trial.py

cp output.png timelaps/output/"output_"$timestamp".png"
cp output.mid timelaps/midi/"midi_"$timestamp".mid"


