#!/usr/bin/python3

def finding_gcd(a,b):
	while(b!=0):
		result=b
		a,b=b,a%b
	return result

def test_finding_gcd():
	number1=21
	number2=12
	assert(finding_gcd(number1,number2)==3)
	print('Tests passed!')

if __name__=='__main__':
	test_finding_gcd()