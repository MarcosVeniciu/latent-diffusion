import os


base = "churches/imgs"

def abrir_diretorio(dir):
	for item in os.listdir(dir):
		print(item)
		
		

abrir_diretorio(base)
