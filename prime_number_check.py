def prime_number(number):
	if number >=2:
		for i in range (2, number):
			if number%i ==0:
				print('No! Sorry, This is not prime number')
				break
			print('Yes! This is prime number')
			break
		
	else:
		print('Please give input number greater 1 beacause prime number started from equal or greater 2')

if __name__=="__main__":
	number = int(input('Enter Number: '))
	prime_number(number)
