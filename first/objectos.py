from operator import truediv


class Automovil():
    largoChasis = 250
    __ruedas    = 4                         # private variable 
    estado      = False
    def arrancarMotor(self, arrancamos):
        self.estado = arrancamos
    def whatIsRuedas(self):
        return self.__ruedas    
    def __chequeo_interno(self):            # private method
        self.gasolina = 'ok'
        self.aceite   = 'ok'
        if(self.gasolina == 'ok' and self.aceite == 'ok'):
            print('Podemos iniciar la marcha')
            return True
        else: 
            print('rellene de gasolina y aceite')
            return False

bwm = Automovil()
print(bwm.largoChasis, bwm.whatIsRuedas(), bwm.estado)
bwm.arrancarMotor(True)
print(bwm.largoChasis, bwm.whatIsRuedas(), bwm.estado)