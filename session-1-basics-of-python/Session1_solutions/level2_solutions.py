def getSum(lowB, upB):
	result = 0
	for number in range(lowB, upB):
		result+=number

	return result

#testcase:
print(getSum(2,4))
