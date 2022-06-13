class Automovil():
    largoChasis = 250
    __ruedas    = 4       # variable privada no accesible desde fuera
    estado      = False

    def arrancarMotor(self):
        self.estado = True

bwm = Automovil()
print(bwm.largoChasis, bwm.ruedas, bwm.estado)
bwm.arrancarMotor()
print(bwm.largoChasis, bwm.ruedas, bwm.estado)