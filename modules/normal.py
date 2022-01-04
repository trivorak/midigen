normalList = []

def getDifference(input):
	return getMax(input) - getMin(input)

def getMin(input):
	return min(input)

def getMax(input):
	return max(input)

def normal(data, minimum, diff):
	return (data-minimum)/diff

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
