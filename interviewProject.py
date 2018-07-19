import urllib.request, json
import requests

def intersection(list1, list2):
	combine = [company for company in list1 if company in list2]
	return combine

def main():

	print('Compare as many sets as you want! (Not just 2)')
	numberOfSets = input('Enter # of sets to compare: ')
	
	if numberOfSets == "":
		numberOfSets = int(2)
	else:
		numberOfSets = int(numberOfSets)
	if numberOfSets < 2:
		numberOfSets = 2

	x = 1
	data_sets = []
	while x < numberOfSets+1:
		inputed =input('Enter Data Set '+str(x)+': ')
		if inputed == "":
			if x == 1:
				data_sets.append("favorites")
				print("Empty -> Assigning to favorites")
			else:
				data_sets.append("search-engines")
				print("Empty -> Assigning to search-engines.json")
		else:
			data_sets.append(inputed)
		x = x + 1

	address = 'https://s3.amazonaws.com/challenge.getcrossbeam.com/public/' #<data-set>.json'

	x = 0
	allData = []
	while x < len(data_sets):
		fullAddress = address+data_sets[x]+".json"
		print(fullAddress)

		with urllib.request.urlopen(fullAddress) as url:
			data = json.loads(url.read().decode())
			#print(data)
		allData.append(data)
		x = x + 1

	x = 0
	sortedData = []
	while x < len(allData):
		oneSet = []
		data = allData[x]
		for y in data.items():
			for z in y[1]:
				for a in z.items():
					if (a[0] == "name"):
						oneSet.append(a[1].lower())
						#print(a[1].lower())
						#print(oneSet)
		sortedData.append(oneSet)
		#rint(sortedData[x])
		x = x + 1

	sizeOfSets = []
	similarities = []

	print("Cool Solution:")

	x = 0
	while x < len(sortedData):
		print()
		print(str(x)+") "+str(data_sets[x])+" has "+str(len(sortedData[x]))+" companies:")
		sizeOfSets.append(len(sortedData[x]))
		print(sortedData[x])
		y = x + 1
		while y < len(sortedData):
			print("With "+str(len(intersection(sortedData[x],sortedData[y])))+" companies that overlap with "+str(data_sets[y])+" ("+str(y)+")") 
			similarities.append(len(intersection(sortedData[x],sortedData[y])))
			y = y + 1
		x = x + 1

	print()
	print("Boring Solution (| seperates sets vs overlaps:")
	for value in sizeOfSets:
		print(value, end=" ")
	print('| ', end=" ")
	for value in similarities:
		print(value, end=" ")

main()