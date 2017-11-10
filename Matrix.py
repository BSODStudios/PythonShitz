import random
import time

def matrix():
	while True:

		random.seed()
		ppy = random.getrandbits(4448)
		print(ppy)

print("Are you ready to enter the matrix")
ready = input()

if (ready == "yes"):
	matrix()

else:
	print("I dont care")
	matrix()


