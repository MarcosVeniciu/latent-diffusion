import os


base = "churches/imgs"

def abrir_diretorio(dir):
	for item in os.listdir(dir):
		print(item)
		
		

abir_diretorio(base)
