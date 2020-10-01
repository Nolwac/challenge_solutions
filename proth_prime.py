import math

def is_prime(proth):
	"""
	This function takes a proth number and uses Proth theorem to determine if the proth number is a prime
	
	Proth theorem states that: given a proth number, p if a^((p-1)/2) = -1 mod p, 
	then p is a prime number, specially known as proth prime.
	
	It is important to note that proths primality test can report a prime number as not prime. But it can never report a composite number as prime.
	
	Also the computer may not be able to compute the value when it becomes to high
	"""
	try:
		for a in range(1, 1000):
			#doing the primality test using the first 1000 positive integers
			if math.pow(a, (proth - 1)/2) == -1%proth:
				return True
	except:
			print("The number ", proth, " provide resulted to a very high value during the computation, try a smaller proth number")
	return False


#below is a function to test the "is_prime" function
def test_proth_num(k, n):
	"""
	Proth numbers come in the form
	k*2^n + 1 where k and n are positive integers,  k is odd and 2^n > k
	"""
	if k%2 == 0:
		print("You must provide an odd number for k")
		return
	for i in range(1, n):#generating proth numbers for numbers ranging from 1 to n and checking if it is prime
		if math.pow(2, i) > k:#checking if condition for k in the math function for a proth number is satisfied
			proth_num = k*math.pow(2, i) + 1
			if is_prime(proth_num):
				print(proth_num, " is a proth prime")
			else:
				print(proth_num, " is not a proth prime")


test_proth_num(1, 10)