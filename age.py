driving = input('是否曾經開過車?')
if driving != "是" and driving != "否":
	print('不要鬧了ˋ口ˊ')
	raise SystemExit
	
age = int(input('年齡:'))

if driving == '是':
	if age >= 18:
		print('守法的公民')
	else:
		print('抓到了!無照駕駛!')
elif driving == '否':
	if age >= 18:
		print('一時蹭車一時爽 一直蹭車一直爽')
	else:
		print('時間到再去考')
else:
	print('不要鬧了ˋ口ˊ')
	
	