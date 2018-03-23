a = ['"some string"', '"true"', True, False, '"false"',\
 0, '"0"', 1, '"1"', '"1-0"', "1-0", "1-1"]
for i in a:
	if i:
		print('Значение переменной ', i, '\ttrue')
	else:
		print('Значение переменной ', i, '\tfalse')
