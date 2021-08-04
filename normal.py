normalList = []

def getDifference(input):
	return max(input) - min(input)

def getMin(input):
	return min(input)

# For Debugging
def getMax(input):
	return max(input)

def normal(data, min, diff):
	return (data-min)/diff

# Main Loop
def normalLoop(input):
	minVal = getMin(input)
	diffVal = getDifference(input)

	for element in input:
		normalList.append(normal(element,minVal,diffVal))

def getNormalList():
	return normalList

# Standard Process
def process(input):
	normalLoop(input)
	return getNormalList()
