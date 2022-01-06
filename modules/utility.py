import random 

# Utiltiy / Generic Functions 

# Return Random Number between Range
def randomBetweenRange(minV,maxV):
	return random.random()*(maxV-minV)+minV


# Funciton to "Evenly Round" / Fix disribution of rounding
def evenRounding(minValue,maxValue):
	minV = min(minValue,maxValue) - 0.5
	maxV = max(minValue,maxValue) + 0.499
	return round(randomBetweenRange(minV,maxV))