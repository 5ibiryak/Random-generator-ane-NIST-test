from scipy import special
import math

print("Два конгруэнтных оператора")
print("Введите количество генереруемых чисел")
number=1000 #размер выходной последовательности
print("Значения для первого конгруэнтного генератора")
print("Введите множитель A")
a1=35
print("Введите начальное значение x")
x01=84
print("Введите приращение b")
b1=62
print("Введите модуль m")
mod1=113
print("Значения для второго конгруэнтного генератора")
print("Введите множитель A")
a2=78
print("Введите начальное значение x")
x02=29
print("Введите приращение b")
b2=52
print("Введите модуль m")
mod2=87
print("Введите модуль m для генератора")
mod3=127
i=0
arr=[]
for i in range (int(number)):
        x1=(int(a1)*int(x01)+int(b1))%int(mod1)
        #print(x1)
        x01=x1
        x2=(int(a2)*int(x02)+int(b2))%int(mod2)
        #print(x2)
        x02=x2
        xmain=(int(x2)+int(x1))%int(mod3)
        #print(xmain)
        arr.append(xmain>>2 & 0x1)
