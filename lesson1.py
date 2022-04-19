#1. Поработайте с переменными, создайте несколько, выведите на экран.
#Запросите у пользователя некоторые числа и строки и сохраните в переменные, затем выведите на экран.

a = 10
b = 2
c = a*b
print(c)
a = int(input('Insert a number'))
b = str(input('Insert a row'))

#2. Пользователь вводит время в секундах.
#Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

time = int(input('Insert time in seconds'))
time1 = time//3600
min = (time % 3600)%60
sec = (time % 3600)%60

if len(str(time1)) == 1:
    time1 = '0'+str(time1)
if len(str(min)) == 1:
    min = '0'+str(min)
if len(str(sec)) == 1:
    sec = '0'+str(sec)
print(str(time1) + ':' + str(min) + ':' + str(sec))


#3. Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

n = int(input('Insert N'))
sum  = n + int(str(n)+str(n)) + int(str(n)+str(n)+str(n))
print(sum)




#4. Пользователь вводит целое положительное число.
#Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.



a = input('Insert a number ')
maxnum = 0
for i in a:
    while int(i) > maxnum:
        maxnum = int(i)
print(maxnum)




##5. Запросите у пользователя значения выручки и издержек фирмы. Определите,
# с каким финансовым результатом работает фирма.
# Например, прибыль — выручка больше издержек, или убыток — издержки больше выручки.
# Выведите соответствующее сообщение.

income = input('Enter your income: ')
expenses = input('Enter your expenses: ')
if income > expenses:
    print('Profit')
else:
    print('Loss')




##6. Если фирма отработала с прибылью, вычислите рентабельность выручки. Это отношение прибыли к выручке.
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчёте на одного сотрудника.

income = int(input('Enter your income: '))
expenses = int(input('Enter your expenses: '))
if income > expenses:
    r = float(((income - expenses)/income))
print(f'Net profit: {r}')
staff = int(input('Enter the quantity of your employees: '))
profit_per_person = (income - expenses)//staff
print(f'Profit per person: {profit_per_person}')




#7. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10% относительно предыдущего.
# Требуется определить номер дня, на который результат спортсмена составит не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.

km = int(input('Enter your distance: '))
progr = int(input('Enter your expected progress: '))
day = 1
while km < progr:
    day = day + 1
    km = km + km*0.1
else:
    print(day)

