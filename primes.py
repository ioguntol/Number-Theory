import math

def isPrime(num):
	if num <= 3:
		return num > 1
	if num % 2 == 0 or num % 3 == 0:
		return False
	for factor in xrange(5, int(num ** 0.5) + 1, 6):
		if num % factor == 0 or num % (factor + 2) == 0:
			return False
	return True

def twinPrimes(num):
	primeList = []
	if num >= 5:
		primeList.append((3, 5))
	if num >= 7:
		primeList.append((5, 7))
	for x in xrange(0, num + 1, 30):
		if isPrime(x - 1) and isPrime(x + 1):
			primeList.append((x - 1, x + 1))
		if isPrime(x + 11) and isPrime(x + 13) and num >= x + 13:
			primeList.append((x + 11, x + 13))
		if isPrime(x + 17) and isPrime(x + 19) and num >= x + 19:
			primeList.append((x + 17, x + 19))
	return primeList
    
def sieve(n):
    size = (n - 1) // 2
    sieve = [True] * size
    i, p, primesList = 0, 3, [2]
    while p * p < n:
        if sieve[i]:
            primesList.append(p)
            j = 2 * i * i + 6 * i + 3
            while j < size:
                sieve[j] = False
                j = j + 2 * i + 3
        i += 1
        p += 2
    while i < size:
        if sieve[i]:
            primesList.append(p)
        i += 1
        p += 2
    return primesList
    
def atkin(num):
	primes = [0] * num
	# n = 3x^2 + y^2
	threexSquared = 3
	for dxSquared in xrange(0, 12 * int(math.sqrt(( num - 1 ) / 3)), 24):
		threexSquared += dxSquared
		y_limit = int(12 * math.sqrt(num - threexSquared) - 36)
		n = threexSquared + 16
		for dn in xrange(-12, y_limit + 1, 72):
			n += dn
			primes[n] = not primes[n]
		n = threexSquared + 4
		for dn in xrange(12, y_limit + 1, 72):
			n += dn
			primes[n] = not primes[n]
	# n = 4x^2 + y^2
	fourxSquared = 0
	for d4xSquared in xrange(4, 8 * int(math.sqrt((num - 1 ) / 4)) + 4, 8):
		fourxSquared += d4xSquared
		n = fourxSquared + 1
		if fourxSquared % 3:
			for dn in xrange(0, 4 * int(math.sqrt(num - fourxSquared)) - 3, 8):
				n += dn
				primes[n] = not primes[n]
		else:
			y_limit = 12 * int(math.sqrt(num - fourxSquared)) - 36
			n = fourxSquared + 25
			for dn in xrange(-24, y_limit + 1, 72):
				n += dn
				primes[n] = not primes[n]
			n = fourxSquared + 1
			for dn in xrange(24, y_limit + 1, 72):
				n += dn
				primes[n] = not primes[n]
    # n = 3x^2 - y^2 section
	xSquared = 1
	for x in xrange(3, int(math.sqrt(num / 2)) + 1, 2):
		xSquared += 4 * x - 4
		n = 3 * xSquared
		if n > num:
			min_y = ((int(math.sqrt(n - num)) >> 2) << 2)
			ySquared = min_y * min_y
			n -= ySquared
			s = 4 * min_y + 4
		else:
			s = 4
 		for dn in xrange(s, 4 * x, 8):
			n -= dn
			if n <= num and n % 12 == 11:
				primes[n] = not primes[n]
	xSquared = 0
	for x in xrange(2, int(math.sqrt(num / 2)) + 1, 2):
		xSquared += 4 * x - 4
		n = 3 * xSquared
		if n > num:
			min_y = ((int(math.sqrt(n - num)) >> 2) << 2) - 1
			yy = min_y*min_y
			n -= yy
			s = 4 * min_y + 4
		else:
			n -= 1
			s = 0
		for dn in xrange(s, 4 * x, 8):
			n -= dn
			if n <= num and n % 12 == 11:
				primes[n] = not primes[n]
	# remove squares        
	for n in xrange(5, int(math.sqrt(num)) + 1, 2):
		if primes[n]:
			for k in range(n * n, num, n * n):
				primes[k] = False
	return [2,3] + filter(primes.__getitem__, xrange(5, num, 2))

def primeFactorization(num):
	pFactor = []
	if isPrime(num):
		pFactor.append((num, 1))
	else:
		number = num
		primeList = primes(num)
		for prime in primeList:
			factorCount = 0
			while number % prime == 0:
				number /= prime
				factorCount += 1
			if factorCount > 0:
				pFactor.append((prime, factorCount))
	return pFactor

def ulamSpiral(size):
	row = size/2
	col = size/2
	direction = 0
	changeCount = -1
	count = 0
	length = 1
	spiral = [[0 for x in range(size)] for x in range(size)] 
	for a in xrange (0, size ** 2):
		spiral[row][col] = a + 1
		count += 1
		if (count == length):
			count = 0
			changeCount += 1
			direction += 1
			direction = ((direction - 1) % 4) + 1
		if (direction == 1):
			col += 1
		elif (direction == 2):
			row += 1
		elif (direction == 3):
			col -= 1
		elif (direction == 4):
			row -= 1
		if (changeCount == 2):
			length += 1
			changeCount = 0
	return spiral