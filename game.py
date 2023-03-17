from random import choice, randrange
from datetime import datetime
# Operadores posibles
operators = ["+", "-", "*", "/"]
# Cantidad de cuentas a resolver
times = 5
# Contador inicial de tiempo.
# Esto toma la fecha y hora actual.
init_time = datetime.now()
#Inicializo una variable para contabilizar 
cantok = 0
print(f"¡Veremos cuanto tardas en responder estas {times} operaciones!")
for i in range(0, times):
    # Se eligen números y operador al azar
    number_1 = randrange(10)
    number_2 = randrange(10)
    operator = choice(operators)
    #Se verifica si hay una división por 0, modificando el 
    #rango de valores que debe tomar el número 2 de ser necesario
    if (operator == "/") and (number_2 == 0):
        number_2 = randrange(1,10)
    #Se realiza la cuenta
    match operator:
        case "+":
            res = number_1 + number_2
        case "*":
            res = number_1 * number_2
        case "/":
            res = number_1 / number_2
        case "-":
            res = number_1 - number_2
    # Se imprime la cuenta.
    print(f"{i+1}- ¿Cuánto es {number_1} {operator} {number_2}?")
    # Le pedimos al usuario el resultado
    result = input("resultado: ")
    if (result == res ):
        cantok += 1
        print(f"\n ¡El resultado es correcto!")
    else:
        print(f"\n ¡El resultado es incorrecto!")

# Al terminar toda la cantidad de cuentas por resolver.
# Se vuelve a tomar la fecha y la hora.
end_time = datetime.now()
# Restando las fechas obtenemos el tiempo transcurrido.
total_time = end_time - init_time
# Mostramos ese tiempo en segundos.
print(f"\n Tardaste {total_time.seconds} segundos.")
#Informamos la cantidad de respuestas correctas e incorrectas
print(f"\n Tuviste {cantok} respuestas correctas y {times - cantok} respuestas incorrectas")