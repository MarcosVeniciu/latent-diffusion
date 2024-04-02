import os


base = "churches/imgs"

def abrir_diretorio(dir):
	for item in os.listdir(dir):
		novo_dir = dir + "/" + item
		print(item)
		abrir_diretorio(novo_dir)
		
		
		

abrir_diretorio(base)
