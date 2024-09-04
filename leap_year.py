def leap_year():
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
