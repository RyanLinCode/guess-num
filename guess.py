#猜數字 要告訴他 比答案大/小

import random

r = random.randint(1, 100)

count = 0

while True:
	count += 1

	num = input('請猜數字：')
	num = int(num)
	if num == r:
		print('你猜中了！')
		print('這是你猜的猜第', count ,'次')
		break
	elif num > r:
		print('比答案大')
	elif num < r:
		print('比答案小')
	print('這是你猜的猜第', count ,'次')
