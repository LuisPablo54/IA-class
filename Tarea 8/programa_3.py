#Tarea 8_3 Celsius a grados Fahrenheit y viseversa
#Luis Pablo López Iracheta 192301-9
'''
________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_______
_____¶¶¶¶¶¶_¶¶¶¶¶¶¶¶______¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_____
____¶¶¶¶¶__¶¶¶¶¶_______________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶___
__¶¶¶¶¶___¶¶¶¶¶¶________________¶¶¶¶¶¶¶¶¶¶__¶¶¶¶¶_
_¶¶¶¶¶___¶¶¶¶¶¶¶_________________¶¶¶¶¶¶¶¶¶___¶¶¶¶¶
__¶¶¶¶¶_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶__________¶¶¶¶¶_
___¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶______¶¶¶¶___
_____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶__¶¶¶¶¶____
______¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_____
________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_______
_________¶¶¶¶¶___________________¶¶¶¶¶¶¶¶¶________
___________¶¶¶¶_¶¶¶¶¶¶¶____________¶¶¶¶¶__________
____________¶¶¶¶¶¶¶¶¶¶¶¶¶__¶¶_¶¶¶¶¶¶¶¶¶___________
______________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_____________
_______________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶______________
________________¶¶¶¶¶___¶¶¶__¶¶¶¶¶________________
__________________¶¶¶¶¶_____¶¶¶¶¶_________________
___________________¶¶¶¶¶___¶¶¶¶¶__________________
_____________________¶¶¶¶¶¶¶¶¶____________________
______________________¶¶¶¶¶¶¶_____________________
________________________¶¶¶_______________________
No puede ser que me toco pasar otra vez, ya ponga otro 
metodo de seleccion porfa :(
'''

def Celsius(incremto):
    fahrenheit = (incremto * 9/5) + 32
    return fahrenheit
    
    
def Fahrenheit(incremto):
    celsius = (incremto - 32) * 5/9
    return celsius

print(" Incremto | Fahrenheit |  Celsius  ")
print("__________|____________|______________")


incremto = 0
for i in range(0, 21):
    resultadoCelsius = Celsius(incremto)
    resultadoFahrenheit = Fahrenheit(incremto)

    print("%6.0f    |  %7.2f   |    %6.2f"%(incremto, resultadoCelsius, resultadoFahrenheit ))


    incremto = incremto + 5