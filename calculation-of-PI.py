#! /usr/bin/env python
# -*- coding: utf-8 -*-

'''
	Working formula 
			PI = 4.0 * ( 1 - 1/3 + 1/5 - 1/7 + 1/9 - ...)
'''

from threading import Thread as td
import time

maxLimit = 300000001
negSUM   = 0.0
posSUM   = 0.0

def minusPart():
	global negSUM
	global maxLimit
	start  = time.time()
	for n in range(3, maxLimit, 4): 
		negSUM += 1.0 / float(n)
	res = "\n\tNegative part = " + str(negSUM) + " calculated in " + str(round(time.time() - start, 2)) + ' secs'
	print(res)

def plusPart():
	global posSUM
	global maxLimit
	start = time.time()
	for n in range(5, maxLimit, 4):
		posSUM += 1.0 / float(n)

	res = "\n\tPositive part = " + str(posSUM) + " calculated in " + str(round(time.time() - start, 2)) + " secs\n"
	print(res)

def parallelCal():
	stTime = time.time()
	p1     = td(target=minusPart, args=())
	p2     = td(target=plusPart, args=())
	p1.start()
	p2.start()
	p1.join()
	p2.join()
	PI = 4.0 * ( 1 - negSUM + posSUM )
	print("\tPI            =", PI, "calculated in", round(time.time()-stTime, 2),'secs\n')


if __name__ == "__main__":
	parallelCal()
	
