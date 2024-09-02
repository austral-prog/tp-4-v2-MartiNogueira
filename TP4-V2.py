#EJERCICIO 1

#Queremos hacer un programa que nos calcule para una ecuación de 
#primer grado la distancia sobre la recta entre dos coordenadas cualquiera
#del eje X y además me informe de las coordenadas del eje Y a la que corresponde.



a = float(input("Ingrese el coeficiente A :"))
b = float(input("Ingrese el coeficiente B :"))

x1 = float(input("Ingrese el coeficiente X1 :"))
x2 = float(input("Ingrese el coeficiente X2 :"))

print(f"El coeficiente A de su ecuación de la recta es: {a}")
print(f"El coeficiente B de su ecuación de la recta es: {b}")
print(f"El coeficiente X1 de su ecuación de la recta es: {x1}")
print(f"El coeficiente X2 de su ecuación de la recta es: {x2}")

print(f"Para la siguiente ecuacion:")
print(f"\t Y = {a}X + {b}")


print("Dado los siguiente puntos :")
print(f"\t P1 ({x1}, {(a * x1) + b})")
print(f"\t P2 ({x2}, {(a * x2) + b})")

y1 = (a * x1) + b
y2 = (a * x2) + b

distancia = ((x2 - x1)**2 + (y2-y1)**2) **0.5
print(f"La distancia entre ellos es: {distancia}")


#EJERCICIO 2: LEAP YEAR 


def bis():
    year = int(input("Ingrese un año: "))

    if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
        print(f"{year} es bisiesto")
    else:
        print(f"{year} NO es bisiesto")

bis()
