import random
import modules.scalelist as scalelist

# Main Functions
# Generic
# Return Random Number between Range
def randomBetweenRange(min,max):
	return random.random()*(max-min)+min


# Funciton to "Evenly Round" / Fix disribution of rounding
def evenRounding(minValue,maxValue):
	minV = min(minValue,maxValue) - 0.5
	maxV = max(minValue,maxValue) + 0.499
	return round(randomBetweenRange(minV,maxV))


# Return Random Musical Root Number
# 0.5 - 11.49 to keep rounding even across all numbers
def randomRootNote():
	return evenRounding(0,12)


# Return Array of Scale Notes based on:
# Root = 0 - 11
# scale = what's your scale offset see major above
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
	# Print Line for Debug Purposes
	# Delete Once Done
	print("Root Note = " + str(root+12))
	print("Scale = " + str(scale))
	return(scaleArray)


# Get Random Scale from scalelist module
# Scale count subtracting 1 for array indexing
def generateRandomScale():
	scaleCount = scalelist.getScaleCount() - 1
	randomIndex = evenRounding(0,scaleCount)

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
