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
		values.append("0" * (7-len(format(inputString[i:i+1]))) + format(inputString[i:i+1])) #If bit string length is less than 7, pad the beginning with 0's
		print(values[i])
	for i in values:
		if i not in uniqueValues:
			uniqueValues.append(i)
	for i in range(0, len(uniqueValues)):
		frequencies.append(values.count(uniqueValues[i]))
		total += values.count(uniqueValues[i])
	for i in range(0, len(frequencies)):
		frequencies[i] = math.fabs((frequencies[i]/total)*math.log(frequencies[i]/total,2)) #Shannon entropy -pilog2(pi)
		entropy += frequencies[i]
	return entropy

x, y = getUserInput()

print("Entropy of ", x, " is ", computeShannonEntropy(x), " \nEntropy of ", y, " is  ", computeShannonEntropy(y), "\n")
