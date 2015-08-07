def lcm(a, b):
	return a * b / gcd(a, b)
 
def gcd(a, b):
	if (a % b == 0 or b % a == 0):
		return math.min(a, b)
	else:
		newNum = math.max(a, b) - (long)(math.max(a, b) / math.min(a, b)) * math.min(a, b)
		return gcd(newNum, math.min(a, b))
 
def linearCombo(a, b):
	if (a - b == gcd(a, b)):
		combo = {a, b}
    		return combo
	rem1 = Math.max(a, b)
	rem2 = Math.min(a, b)
	firstCoef1 = 1
	firstCoef2 = 0
	secondCoef1 = 0
	secondCoef2 = 1
	while (rem1 % rem2 != 0):
		divisor = (long)(rem1 / rem2)
		tempRem = rem1 - divisor * rem2
		tempFirstCoef = firstCoef1 - divisor * firstCoef2
		tempSecondCoef = secondCoef1 - divisor * secondCoef2
		rem1 = rem2
		rem2 = tempRem
		firstCoef1 = firstCoef2
		firstCoef2 = tempFirstCoef
		secondCoef1 = secondCoef2
		secondCoef2 = tempSecondCoef
	if (a > b):
		answer = {firstCoef2, secondCoef2};
		print (a + "(" + answer[0] + ")" + b + "(" + answer[1] + ") = " + gcd(a, b));
		return answer
	else:
		answer = {secondCoef2, firstCoef2}
		print (a + "(" + answer[0] + ") + " + b + "(" + answer[1] + ") = " + gcd(a, b));
		return answer
 
def modInverse(congruence):
		a = 1
		while ((congruence[0] * a) % congruence[2] != congruence[1]):
			a += 1
		arr = {1, a, congruence[2]};
		return arr
 
def incongruentSols(a, b, c):
	solutions = set()
	if (b % gcd(a, c) == 0):
		numSols = gcd(a, c);
		sol = (c + b * linearCombo(a, c)[0] / numSols) % c;
		for i in xrange(0, numSols):
			solutions.add((sol + c * i / numSols) % c)
	return solutions