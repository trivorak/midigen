import random

# Create Blank Array
b = []
# Scale
major = [0,2,4,5,7,9,11]

# Main Functions
# Generic
# Return Random Number between Range

def ranBetweenRange(min,max):
	return random.random()*(max-min)+min


# Return Random Musical Root Number 
# 0.5 - 12.49 to keep rounding even across all numbers
def ranRootNote():
	return round(ranBetweenRange(0.5,12.49))
	
root = ranRootNote()
root = root - 12

for i in range (0, len(major)*12):
	resultValue = ((root+major[i%len(major)])+(12*divmod(i,len(major))[0]))
	if resultValue >= 128:
		break
	elif resultValue >= 0:
		b.append(resultValue)
	
	
# Test		
print('Root = ' + str(root+12))
print(b)
