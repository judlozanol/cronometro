class UnidadTiempo:
    def __init__(self):
        self.valor=0
        self.tope=0
    def avanzar(self):
        self.valor+=1
        if self.valor==self.tope:
            self.valor=0


if __name__=='__main__':
    u = UnidadTiempo()
    u.tope=10
    count=0
    while count<20:
        print(u.valor)
        u.avanzar()
        count+=1
