def decrypt(message, key):
	result = ""

	for letter in message:

		if letter ==" ":
			result+=letter
		else:
			result += chr((ord(letter) + 65-key) % 26 + 65)
	return result

#test cases:
m1 = 'FH FLLA'
k1 = 7
print(decrypt(m1, k1))

m2 = 'JNXNAQN SBERIRE'
k2 = 13
print(decrypt(m2, k2))

m3 = 'FYRER DVREJ WRDZCP REU WRDZCP DVREJ EFSFUP XVKJ CVWK SVYZEU FI WFIXFKKVE'
k3 = 17
print(decrypt(m3, k3))
