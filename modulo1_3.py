def sumar(num1, num2):
    return num1+num2


def restar(num1, num2):
    return num1-num2


def multiplicar(num1, num2):
    return num1*num2


def dividir(num1, num2):
    return num1/num2


def mifuncion():
    selecc = int(input("1. Sumar\n2.Restar\n3.Multiplicar\n4.Dividir"))
    num1 = float(input("Ingrese la primera cantidad\n"))
    num2 = float(input("Ingrese la segunda cantidad\n"))

    if selecc == 1:
        print(sumar(num1, num2))
    elif selecc == 2:
        print(restar(num1, num2))
    elif selecc == 3:
        print(multiplicar(num1, num2))
    elif selecc == 4:
        print(dividir(num1, num2))

def main():

    mifuncion()


if __name__ == "__main__":
    main()


x = lambda a :a+10
print(x(5))

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))
