from . import scalelist as scalelist
from . import utility as utility

# Define Functions 

# Return Random Musical Root Number
# 0.5 - 11.49 to keep rounding even across all numbers
def randomRootNote():
	return utility.evenRounding(0,11)


# Return Array of Scale Notes based on:
# Root = 0 - 11
# scaleArray = Empty array
def generateScaleArray(root,scale,scaleArray):
	root -= 12
	scaleArray.clear()
	i = 0
	while True:
		resultValue = ((root+scale[i%len(scale)])+(12*divmod(i,len(scale))[0]))
		if resultValue >= 128:
			break
		elif resultValue >= 0:
			scaleArray.append(resultValue)
		i += 1
	
	return(scaleArray)


# Get Random Scale from scalelist module
# Scale count subtracting 1 for array indexing
def generateRandomScale():
	scaleCount = scalelist.getScaleCount() - 1
	randomIndex = utility.evenRounding(0,scaleCount)

	return scalelist.getScale(scalelist.getAllScales(),randomIndex)



# Return note based on note array
# Rounds down to nearest note
def snapToScale(scaleArray,note):
	for i in range(0, len(scaleArray)):
		if scaleArray[i] > note:
			return(scaleArray[i-1])
			break
		elif scaleArray[i] == note:
			return(scaleArray[i])
			break
