
L1 = ['a', 'b', 'c']
L2 = ['b', 'd']

# For common elements
print("For finding common elements")
for val in L1:
	if val in L2:
		print(val)


# For non common elements
print("\n For non-common elements")
L3 = L1 + L2
for elem in L3:
	if (elem not in L1) or (elem not in L2):
		print(elem)