#калькулято зп)
diameter = float(input("введите диамер трубы mm: "))
long = float(input("введите длинну M: "))
people = float(input("сколько человек участвовало: ")) 
#coman = input("если это командировка нажмите + : ")
day = float(input("количество дней на производство работ: "))

if diameter <= 110:
	b = long * 4  # Предыдущее значение 4.3 коэфициент за 110 трубу
	c = b / people
	d = c / day
	#if coman == "+":
	#	q = d + 9
	#	w = c + 9
	    #print(str(w) + " byn" + " сумма за объект   " + str(q) + " byn" + " сумма в день")
	print(str(c) + " byn" + " сумма за объект,   " + str(d) + " byn" + " сумма в день")
	print(str(c) + " byn" + " сумма за объект,   " + str(d) + " byn" + " сумма в день")

elif diameter >= 110:
	b = diameter / 27.5    # предыдущее значение 26   (110 / 4.3)
	c = long * b
	d = c / people
	f = d / day
	#дописать
	print(str(d) + " byn" + " сумма за объект,   " + str(f) + " byn" + " сумма в день")
	#print(d)




input()
