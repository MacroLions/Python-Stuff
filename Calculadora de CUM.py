materias=int(input("Ingrese cuantas materias ha cursado: "))
uv = 0
unidadesMerito = 0
print("")
for i in range(materias-1):
    print("Materia "+str(i+1)+": ")
    uvMateria=int(input("Ingrese cuantas UV vale la materia: "))
    notaMateria=float(input("Ingrese cual fue su nota en esa materia: "))
    uv = uv + uvMateria
    unidadesMerito= unidadesMerito+(uvMateria*notaMateria)
    print("")

CUM=float(unidadesMerito/uv)

print("Su CUM es: "+str(CUM))
