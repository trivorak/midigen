import random

majorScale = [0,2,4,5,7,9,11]
naturalMinorScale = [0,2,3,5,7,8,10]
harmonicMinorScale = [0,2,3,5,7,8,11]
melodicMinorScale = [0,2,3,5,7,9,11]
dorianScale = [0,2,3,5,7,9,10]
locrianScale = [0,1,3,4,7,8,10]
lydianScale = [0,2,4,6,7,9,11]
mixolydianScale = [0,2,4,5,7,9,10]
phrygianScale =[0,1,3,5,7,8,10]
pentatonicMajorScale = [0,2,4,7,9]
pentatonicMinorScale = [0,3,5,7,10]

scales = [majorScale, naturalMinorScale, harmonicMinorScale, melodicMinorScale, dorianScale, locrianScale, lydianScale, mixolydianScale, phrygianScale, pentatonicMajorScale, pentatonicMinorScale]

def getAllScales():
	return scales

def getScaleCount():
	return len(scales)

def getScale(array, i):
	return array[i]