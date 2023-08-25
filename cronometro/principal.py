from cronometro import Cronometro

c= Cronometro()
for i in range(5000):
    if c.segundo.valor//10==0:
        if c.minuto.valor//10==0:
            if c.hora.valor//10==0:
                print("0"+str(c.hora.valor)+":0"+str(c.minuto.valor)+":0"+str(c.segundo.valor))
            else:
                print(str(c.hora.valor)+":0"+str(c.minuto.valor)+":0"+str(c.segundo.valor))
        else:
            if c.hora.valor//10==0:
                print("0"+str(c.hora.valor)+":"+str(c.minuto.valor)+":0"+str(c.segundo.valor))
            else:
                print(str(c.hora.valor)+":"+str(c.minuto.valor)+":0"+str(c.segundo.valor))
    else:
        if c.minuto.valor//10==0:
            if c.hora.valor//10==0:
                print("0"+str(c.hora.valor)+":0"+str(c.minuto.valor)+":"+str(c.segundo.valor))
            else:
                print(str(c.hora.valor)+":0"+str(c.minuto.valor)+":"+str(c.segundo.valor))
        else:
            if c.hora.valor//10==0:
                print("0"+str(c.hora.valor)+":"+str(c.minuto.valor)+":"+str(c.segundo.valor))
            else:
                print(str(c.hora.valor)+":"+str(c.minuto.valor)+":"+str(c.segundo.valor))
    c.avanzar()