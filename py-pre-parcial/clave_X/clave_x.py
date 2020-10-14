import math

"""
***************************************************************
@@ ejercicio 1 @@
un metodo python que haga la suma de 2 numeros
2+4 = 6
"""


class Suma:
    def __init__(self, numero1, numero2):
        self.__numero1 = numero1
        self.__numero2 = numero2

    # start-->
    def suma(self):
        result = self.__numero1 + self.__numero2
        return result


"""
***************************************************************
@@ ejercicio 2 @@
un metodo python que haga la multiplicacion de 3 numeros
2*4*5 = 40
"""


class Multiplicacion:
    def __init__(self, numero3, numero4, numero5):
        self.__numero3 = numero3
        self.__numero4 = numero4
        self.__numero5 = numero5

    # start-->
    def multiplicacion(self):
        result = self.__numero3 * self.__numero4 * self.__numero5
        return result


"""
***************************************************************
@@ ejercicio 3 @@
un metodo python que haga la suma de los numeros de la lista
numerosLista = [2,5,4,6,9,12]
"""
numerosLista = []


# start-->
def sumarLista(numerosLista):
    result = sum(numerosLista)
    return result


"""
***************************************************************
@@ ejercicio 4 @@
colocar este proyecto en github
colocar aca debajo la url
enviar la url al correo balbino_a@hotmail.com
"""


# github url-->
def getGithubUrl():
    return ""
