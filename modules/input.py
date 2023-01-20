with open ("input.txt","r") as f:
    a = f.read()

# Remove Carriage Returns
a = a.replace('\n','')

#Convert to string
a = str(a)

# Create blank list
aList = []
aListInt = []

# Split by every 2 characters and append to "blank list"
for i in range(0,len(a),2):
    aList.append(a[i:i+2])

# Loop hex to int into new list
for element in aList:
    aListInt.append(int(element,16))
