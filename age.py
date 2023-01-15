driving = input ('請問你有沒有開過車:')
age = input ('請問您今年幾歲:')

age = int (age)                 #casting

if driving == '有':
	if age >= 18:
		print ('沒問題，您是可以開車的年齡')
	elif age <18:
		print ('奇怪，您不是可以駕駛的年紀')
	else:
		print ('請以整數作答')
elif driving == '沒有':
	if age >=18:
		print ('可以快去考駕照了喔')
	elif age < 18:
		print ('小事啦，當個守法小公民')
	else:
		print ('請以整數作答')
else:
	print ('請以「有」或「沒有」作答')