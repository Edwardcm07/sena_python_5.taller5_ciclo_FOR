# TALLER 5 PYTHON
# AUTOR: EDUAR ALEJANDRO CANO MONTOYA
# FECHA: 27 DE SEPTIEMBRE DE 2022

from datetime import date
hoy = date.today()    #fecha actual
print("Hoy es el dia: ", hoy)
print()
print("TALLER 5 CICLOS ITERATIVOS CON LA SENTENCIA FOR")
print()
num1=int(input("digite el primer número: "))
num2=int(input("digite el segundo número (mayor): "))
print("ciclo para el primer numero")
for i in range(num1):
    print(i)
print("fin del ciclo")

print()
print("ciclo desde el primer numero hasta el el segundo numero")
for i in range(num1,num2):
    print(i)
print("fin del ciclo")

print()
print("ciclo desde el primer numero hasta el segundo numero con incrementos de 2")
for i in range(num1,num2,2):
    print(i)
print("fin del ciclo")

print()
empresa=input("digite el nombre de la empresa: ")
empresa=empresa.lower()
for character in empresa:
    print(character)
print("fin del ciclo")

print()
print("FIN")

