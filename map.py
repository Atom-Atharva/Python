# Function to determine length
def myFunc(a):
    return len(a)


# List
myList = ("apple", "banana", "cherry")

# Map Function
x = map(myFunc, myList)

# Print map object
print(x)

# Convert object into list by list constructor
print(list(x))
