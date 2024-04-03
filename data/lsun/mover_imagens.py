import os


cont = 0

def sub_pasta(dir):
    global cont
    if cont == 50000: print(cont)
    if cont == 100000: print(cont)
    if cont == 120000: print(cont)
    
    lista = os.listdir(dir)
    for item in lista:
        if item[len(item)-4:] == "webp":
            origem = os.path.join(dir, item)
            destino = os.path.join("churches", item)
            #print(origem)
            #print(destino)
            #print("\n\n")
            os.rename(origem, destino)
            cont = cont +1
        else:
            sub_pasta(os.path.join(dir, item))
    

diretorio = "churches/imgs"
sub_pasta(diretorio)
print(cont)