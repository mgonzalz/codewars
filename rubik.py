n = int(input("Ingrese el tamaño del cubo: "))
print(n)
triangulo_arriba= "/\\" #Triangulos definidos
lado_arriba="_\\" #Lados definidos
triangulo_abajo="\\/"
lado_abajo="_/"
def cube(n):
    cubo_arriba = [] #Lista para el cubo
    for i in range(n): #Ciclo para parte de arriba
        cubo_arriba.append(" "*(n-i-1)+triangulo_arriba*(i+1)+lado_arriba*n) #Permite agregar elementos a la lista
    cubo_abajo = []
    for i in range(n): #Ciclo para parte abajo
        cubo_abajo.append(" "*i+triangulo_abajo*(n-i)+lado_abajo*(n))
    cubo = cubo_arriba + cubo_abajo #Concatena las dos listas
    return '\n'.join(cubo) #Permite unir los elementos de la lista
if __name__ == "__main__":
    print(cube(n))
