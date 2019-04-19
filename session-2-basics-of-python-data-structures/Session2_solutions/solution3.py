#!/usr/bin/python
# Solution for Learn.py session 2's project level 3: Shakespearean Dictionary
# This solution does not permanently modify the strings.
# However, solutions that permanently modify the strings are also accepted.

import sys

ShakespeareanDict = {
	"art": "are",
	"ay": "yes",
	"be": "is",
	"doth": "does",
	"morrow": "tomorrow",
	"oft": "often",
	"till": "until",
	"wilt": "will",
	"thou": "you",
	"Thou": "You",
	"thine": "your"
}

s1 = "Parting is such sweet sorrow, That I shall say good night till it be morrow"
s2 = "The fool doth think he is wise, but the wise man knows himself to be a fool"
s3 = "Blow, blow, thou winter wind! Thou art not so unkind as man's ingratitude"
s4 = "This above all: to thine own self be true"
s5 = "Our doubts are traitors, and make us lose the good we oft might win, by fearing to attempt"

list = [s1, s2, s3, s4, s5]

for i in list:
	temp_arr = i.split(' ')
	for word in temp_arr:
		if word in ShakespeareanDict.keys():
			i = i.replace(word, ShakespeareanDict[word])
	print i
