fruits = []
fruits.extend(range(1,100001))

pares = []
impares = []

for i in fruits:
    if i%2 == 0:
        pares.append(i)
    else:
        impares.append(i)

numerosEnteros ={
    "pares" : pares,
    "impares": impares
}

if __name__ == "main":
    main()
def main:



