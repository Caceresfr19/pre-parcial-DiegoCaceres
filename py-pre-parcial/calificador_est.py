from clave_X.clave_x import Suma, Multiplicacion, sumarLista, getGithubUrl

# --------------------------------------------------------

resultado = Suma(2, 4)
result = int(resultado.suma())
if result == 6:
    print("ejercicio01: pass")
else:
    print("ejercicio01: fail")

# --------------------------------------------------------

resultado = Multiplicacion(2, 4, 5)
result = int(resultado.multiplicacion())
if result == 40:
    print("ejercicio02: pass")
else:
    print("ejercicio02: fail")

# --------------------------------------------------------

numerosLista = [2, 5, 4, 6, 9, 12]
resultado = int(sumarLista(numerosLista))
result = resultado
if result == 38:
    print("ejercicio03: pass")
else:
    print("ejercicio03: fail")

# --------------------------------------------------------

result = getGithubUrl()
if not result == "":
    print("ejercicio04: pass")
else:
    print("ejercicio04: fail")

# --------------------------------------------------------
