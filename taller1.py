def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "La división por cero no está definida en los números reales"

print("Seleccione la operacion:")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")

choice = input("Haga su elección (1/2/3/4): ")

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

if choice == '1':
    print(num1, "+", num2, "=", add(num1, num2))
elif choice == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))
elif choice == '3':
    print(num1, "*", num2, "=", multiply(num1, num2))
elif choice == '4':
    print(num1, "/", num2, "=", divide(num1, num2))
else:
    print("Entrada inválida")