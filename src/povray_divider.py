def generate_pov_files(c1, c2, dirFrom, angle, mdt_list, orto_list):
	if len(orto_list) > 6:
		print("YEU")
		# TODO: Ordenar orto_list por nombre de la ortofoto (buscar como ordenar en listas). Esto no se si sirve porque 
		# 		por los nombres de las ortofotos podemos querer 2_1 y 3_1, pero pillaría 2_1 y 2_2. Ordenadamente serviría
		#		para partir a lo ancho.
		# TODO: Bucle pillando las 6 primeras, luego las 6 siguientes (así sucesivamente hasta el final de la lista)
		# TODO: Dentro del bucle ir generando los ficheros pov y renderizarlos
		# TODO: Juntar las imágenes
	else:
		print("OU")	