from math import * #Importa todo del modulo math para realizar las operaciones necesarias

#=== Definicion de las funciones para el calculo del area y el perimetro de las figuras planas===
def square_Area(side):
    area = side**2
    return area

def square_Perimeter(side):
    perimeter = 4*side
    return perimeter

def rectangle_Area(a_side,b_side):
    area = a_side * b_side
    return area

def rectangle_Perimeter(a_side,b_side):
    perimeter = 2*a_side + 2*b_side
    return perimeter

def triangle_Area(base,height):
    area = (base*height)/2
    return area

def triangle_Perimeter(a_side,b_side,c_side):
    perimeter = a_side + b_side + c_side
    return perimeter

def diamond_Area(d, c):
    area = (d*c)/2
    return area

def diamond_Perimeter(side):
    perimeter = 4*side
    return perimeter

def parallelogram_Area(a_side, height):
    area = a_side*height
    return area

def parallelogram_Perimeter(a_side, b_side):
    perimeter = 2*a_side + 2*b_side
    return perimeter

def trapeze_Area(a_side, b_side, height):
    area = ((a_side + b_side)/2) * height
    return area

def trapeze_Perimeter(a_side, b_side, c_side, d_side):
    perimeter: a_side + b_side + c_side + d_side
    return perimeter

def regPolygon_Area(perimeter, apothem):
    area = (perimeter * apothem) / 2
    return area

def regPolygon_Perimeter(a_side, n_sides):
    perimeter = n_sides * a_side
    return perimeter

def circle_Area(r):
    area = 2*pi*(r**2)
    return area

def circle_Perimeter(r):
    perimeter = 2*pi*r
    return perimeter

#=== Definicion de las funciones para el calculo del volumen de solidos regulares ===
def cube_Volume(side):
    volume = side**3
    return volume

def prism_Volume(base, height):
    volume = base * height
    return volume

def pyramid_Volume(base, height):
    volume = (base * height)/3
    return volume

def cylinder_Volume(r, height):
    volume = pi*(r**2)*height
    return volume

def cone_Volume(r, height):
    volume = (pi*(r**2)*height)/3
    return volume

def sphere_Volume(r):
    volume = (4*pi*(r**3))/3
    return volume

# ============ Definicion de las funciones de los menus ============
def main_menu():
    print('Bienvenido. Que desea realizar?:')
    print('1. Calcular el area y perimetro de una figura plana')
    print('2. Calcular el volumen de un solido regular')
    print('3. Salir')
    opc = input()
    return opc

def flatFigure_menu():
    print('\n Sobre que figura plana desea realizar el calculo del area y perimetro?:')
    print('1. Cuadrado')
    print('2. Rectangulo')
    print('3. Tringulo')
    print('4. Rombo')
    print('5. Paralelogramo')
    print('6. Trapecio')
    print('7. Poligono regular')
    print('8. Circulo')
    opc = input()
    return opc

def regSolids_menu():
    print('\n Sobre que solido regular desea realizar el calculo del volumen?:')
    print('1. Cubo')
    print('2. Prisma')
    print('3. Piramide')
    print('4. Cilindro')
    print('5. Cono')
    print('6. Esfera')
    opc = input()
    return opc

# ============ Definicion de las funciones de impresion de los resultados ============

def print_flatFigure(fig, perimeter, area):
    print(f'El perimetro del {fig} es {perimeter} y el area es {area} \n')

def print_regSolids(fig, volume):
    print(f'El volumen del {fig} es {volume} \n')

# ===== Definicion de las funciones de operacion sobre la seleccion del usuario =====

def opc_flatFigure(opc):
    print()
    match opc:
        case "1":
            side = float(input("Ingrese la medida del lado del cuadrado: "))
            area = square_Area(side)
            per = square_Perimeter(side)
            print_flatFigure('cuadradro', per, area)
        case "2":
            side_a = float(input("Ingrese el primer lado del rectangulo: "))
            side_b = float(input("Ingrese el segundo lado del rectangulo: "))
            per = rectangle_Perimeter(side_a, side_b)
            area = rectangle_Area(side_a, side_b)
            print_flatFigure('rectangulo', per, area)
        case "3":
            side_a = float(input("Ingrese la base del triangulo: "))
            side_b = float(input("Ingrese el segundo lado del triangulo: "))
            side_c = float(input("Ingrese el tercer lado del triangulo: "))
            height = float(input("Ingrese la altura del triangulo: "))
            per = triangle_Perimeter(side_a, side_b, side_c)
            area = triangle_Area(side_a, height)
            print_flatFigure('triangulo', per, area)
        case "4":
            d = float(input("Ingrese la diagonal mayor: "))
            c = float(input("Ingrese la diagonal menor: "))
            side = float(input("Ingrese la medida del lado del rombo: "))
            per = diamond_Perimeter(side)
            area = diamond_Area(d, c)
            print_flatFigure('rombo', per, area)
        case "5":
            side_a = float(input("Ingrese la base del paralelogramo: "))
            side_b = float(input("Ingrese el segundo lado: "))
            height = float(input("Ingrese la altura del paralelogramo: "))
            per = parallelogram_Perimeter(side_a, side_b)
            area = parallelogram_Area(side_a, height)
            print_flatFigure('paralelogramo', per, area)
        case "6":
            side_a = float(input("Ingrese la base del trapecio: "))
            side_b = float(input("Ingrese el techo del trapecio: "))
            side_c = float(input("Ingrese el tercer lado del trapecio: "))
            side_d = float(input("Ingrese el cuarto lado del trapecio: "))
            height = float(input("Ingrese la altura del trapecio: "))
            per = trapeze_Perimeter(side_a, side_b, side_c, side_d)
            area = trapeze_Area(side_a, side_b, height)
            print_flatFigure('trapecio', per, area)
        case "7":
            side = float(input("Ingrese la medida del lado del poligono: "))
            sides = float(input("Ingrese el numero de lados del poligono: "))
            ap = float(input("Ingrese el apotema del poligono: "))
            per = regPolygon_Perimeter(side, sides)
            area = regPolygon_Area(per, ap)
            print_flatFigure('poligono regular', per, area)
        case "8":
            r = float(input("Ingrese el radio del circulo: "))
            per = circle_Perimeter(r)
            area = circle_Area(r)
            print_flatFigure('circulo', per, area)
        case _:
            print("Opcion invalida")

def opc_regSolids(opc):
    print()
    match opc:
        case "1":
            side = float(input("Ingrese la medida del lado del cubo: "))
            vol = cube_Volume(side)
            print_regSolids('cubo', vol)
        case "2":
            base = float(input("Ingrese la superficie de la base del prisma: "))
            height = float(input("Ingrese la altura del prisma: "))
            vol = prism_Volume(base, height)
            print_regSolids('prisma', vol)
        case "3":
            base = float(input("Ingrese la superficie de la base de la piramide: "))
            height = float(input("Ingrese la altura de la piramide: "))
            vol = pyramid_Volume(base, height)
            print_regSolids('piramide', vol)
        case "4":
            r = float(input("Ingrese el radio del cilindro: "))
            height = float(input("Ingrese la altura del cilindro: "))
            vol = cylinder_Volume(r, height)
            print_regSolids('cilindro', vol)
        case "5":
            r = float(input("Ingrese el radio del cono: "))
            height = float(input("Ingrese la altura del cono: "))
            vol = cone_Volume(r, height)
            print_regSolids('cono', vol)
        case "6":
            r = float(input("Ingrese el radio de la esfera: "))
            vol = sphere_Volume(r)
            print_regSolids('esfera', vol)
        case _:
            print("Opcion invalida")

# =================== Programa Principal ===================
if __name__=='__main__':
    prog_active = True #Variable para mantener el programa corriendo hasta que el usuario desee salir

    while prog_active:

        #Menu Principal
        opc = main_menu()

        match opc:
            case "1":
                opc2 = flatFigure_menu()
                opc_flatFigure(opc2)
            case "2":
                opc3 = regSolids_menu()
                opc_regSolids(opc3)
            case "3":
                prog_active = False
            case _:
                print("Opcion invalida")

    print('\n Gracias. Adios!!!')