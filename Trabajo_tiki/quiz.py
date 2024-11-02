class Motor:
def _init_(self, tipo) :
self. tipo = tipo
class Coche:
def _init_(self, marca, tipo_motor):
self. marca = marca
self. motor = Motor (tipo_motor)
coche = Coche ("Toyota", "Eléctrico")
print (coche. motor. tipo)