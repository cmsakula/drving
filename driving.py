country = input('which country are you from? ')
age = input('how old are you? ')
age = int(age)
if country == 'taiwan':
	if age >= 18:
		print('You may get a license')
	else:
		print('You may not drive')