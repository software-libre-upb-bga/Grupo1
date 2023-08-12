def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

print("Seleccione la operacion:")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")

choice = input("Haga su elección (1/2/3): ")

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

if choice == '1':
    print(num1, "+", num2, "=", add(num1, num2))
elif choice == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))
elif choice == '3':
    print(num1, "*", num2, "=", multiply(num1, num2))
else:
    print("Entrada inválida")


