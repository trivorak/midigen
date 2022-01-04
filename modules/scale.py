import random
import modules.scalelist as scalelist

# Main Functions
# Generic
# Return Random Number between Range
def randomBetweenRange(min,max):
	return random.random()*(max-min)+min


# Return Random Musical Root Number
# 0.5 - 11.49 to keep rounding even across all numbers
def randomRootNote():
	return round(randomBetweenRange(-0.5,11.49))


# Return Array of Scale Notes based on:
# Root = 0 - 11
# scale = what's your scale offset see major above
# scaleArray = Empty array
def generateScaleArray(root,scale,scaleArray):
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
