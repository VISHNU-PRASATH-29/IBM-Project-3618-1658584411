import random
a=random.random()   #temperature
b=random.random()   #humidity
print("==========================================================================")
print("==Pgm to notice if the temp and humidity level is good or not in a place==")
print("==========================================================================")
print("==The random  temperature generated is :",a)
print("==The random  humidity generated is :",b)
if a>80:
    if b>80:
        print("==Hazarpredected")
    else:
        print("==High temperature")
elif a==80:
    print("==Temperature is  high... the ace is need to be cool off...         ==")
else:
    print("==All good in your place you are safe... \n==The temp and the humidity level is good ")
    print("======================================================================")
