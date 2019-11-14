#!/usr/bin/python3
import math

def getUserInput():
	firstString = input("Enter first string to compare:")
	secondString = input("Enter second string to compare:")
	return firstString, secondString

def computeShannonEntropy(inputString):
	total = 0
	entropy = 0
	values = []
	frequencies = []
	uniqueValues = []
	for i in range(0, len(inputString)):
		values.append("0" * (7-len(bin(int.from_bytes(inputString[i:i+1].encode(), 'big'))[2:])) + bin(int.from_bytes(inputString[i:i+1].encode(), 'big'))[2:]) #If bit string length is less than 7, pad the beginning with 0's
	for i in values: #Transform a list into a 'set'
		if i not in uniqueValues:
			uniqueValues.append(i) #really just a list with unique elements
	for i in range(0, len(uniqueValues)): #for each unique value, count its occurance
		frequencies.append(values.count(uniqueValues[i]))
		total += values.count(uniqueValues[i]) #keep a running total, could just use len(), but we already have to have this loop
	for i in range(0, len(frequencies)): 
		entropy += math.fabs((frequencies[i]/total)*math.log(frequencies[i]/total,2)) #Shannon entropy -pilog2(pi)
	return entropy

x, y = getUserInput()

print("Entropy of ", x, " is ", computeShannonEntropy(x), " \nEntropy of ", y, " is  ", computeShannonEntropy(y), "\n")
