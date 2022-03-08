#!/bin/bash

function getTime() {
	local timestamp=$(date +%s);
	echo $timestamp;
}

# Get New Timestamp
timestamp="$(getTime)"

# Clear Up last set of images
./cleanup.sh

# Start New Session
raspistill -o input.png
convert input.png -filter point -resize 512x512 smallinput.png
xxd -p smallinput.png input.txt
python3 ~/git/midigen/research/drawlines.py
python3 ~/git/midigen/research/drawcolorlines.py
python3 ~/git/midigen/research/drawpixel.py
convert input.png -monochrome -filter point -resize 1000x128 output.png
python3 ~/git/imgnoise/trial.py

# Copy files to folder for timelaps
cp input.png timelaps/input/"input_"$timestamp".png"
cp output.png timelaps/output/"output_"$timestamp".png"
cp output.mid timelaps/midi/"midi_"$timestamp".mid"
cp outputColorLines.png timelaps/colorlines/"colorline_"$timestamp".png"
cp outputBWLines.png timelaps/bwlines/"bwlines_"$timestamp".png"
cp outputPixels.png timelaps/pixels/"drawpixel_"$timestamp".png"

