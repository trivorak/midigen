#!/bin/bash

function getTime() {
	local timestamp=$(date +%s);
	echo $timestamp;
}

# Get New Timestamp
timestamp="$(getTime)"

# Clear last set of images
rm input.png
rm input.txt
rm output.png
rm output.mid
rm outputColorLines.png
rm test.svg
rm outputBWLines.png
rm outputPixels.png

# Start New Session
raspistill -o input.png
xxd -p input.png input.txt
python3 ~/git/midigen/research/drawlines.py
python3 ~/git/midigen/research/drawcolorlines.py
python3 ~/git/midigen/research/drawpixel.py
python3 ~/git/midigen/research/svgcolorlines.py
convert input.png -monochrome -filter point -resize 1000x128 output.png
python3 ~/git/imgnoise/trial.py

# Copy files to folder for timelaps
cp input.png timelaps/input/"input_"$timestamp".png"
cp output.png timelaps/output/"output_"$timestamp".png"
cp output.mid timelaps/midi/"midi_"$timestamp".mid"
cp outputColorLines.png timelaps/colorlines/"colorline_"$timestamp".png"
cp test.svg timelaps/svglines/"svglines_"$timestamp".svg"
cp outputBWLines.png timelaps/bwlines/"bwlines_"$timestamp".png"
cp outputPixels.png timelaps/pixels/"drawpixel_"$timestamp".png"

# Need Folders #
################
#	timelaps
# 		input
# 		output
# 		midi
# 		colorlines
# 		svglines
# 		bwlines
# 		pixels
