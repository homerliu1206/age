driving = input ('請問你有沒有開過車:')
age = input ('請問您今年幾歲:')

age = int (age)

if driving == '有':
	if age >= 18:
		print ('沒問題，您是可以開車的年齡')
	else:
		print ('奇怪，您不是可以駕駛的年紀')
else:
	print ('小事啦，當個守法小公民')