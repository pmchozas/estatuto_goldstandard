#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 14:41:07 2025

@author: pmchozas
"""

# EXTRAER TEXTO DE PDF
'''

import pdfplumber

# Nombre del archivo PDF de entrada
pdf_path = "data/dicc_victor.pdf"
# Nombre del archivo de salida
txt_path = "salida.txt"

# Extraer texto del PDF
with pdfplumber.open(pdf_path) as pdf:
    texto = "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])

# Guardar el texto en un archivo .txt
with open(txt_path, "w", encoding="utf-8") as txt_file:
    txt_file.write(texto)

print(f"Texto extraído y guardado en {txt_path}")
'''

#EXTRAER TÉRMINOS (EMPIEZAN POR ASTERISCO)
'''
# Nombre de los archivos
txt_path = "salida.txt"  # Archivo de entrada
output_path = "filtrado.txt"  # Archivo de salida

# Lista para almacenar las líneas filtradas
lineas_filtradas = []

# Leer el archivo y extraer líneas que comienzan con "*"
with open(txt_path, "r", encoding="utf-8") as archivo:
    for linea in archivo:
        linea = linea.strip()  # Eliminar espacios en blanco al inicio y final
        if linea.startswith("*"):  
            lineas_filtradas.append(linea[1:].strip())  # Agregar sin "*"

# Guardar las líneas filtradas en un nuevo archivo
with open(output_path, "w", encoding="utf-8") as archivo_salida:
    archivo_salida.write("\n".join(lineas_filtradas))

print(f"Líneas filtradas guardadas en {output_path}")
'''

#LOWERCASE

# Nombre de los archivos
input_path = "filtrado.txt"  # Archivo de entrada con líneas filtradas
output_path = "filtrado_lowercase.txt"  # Archivo de salida en minúsculas

# Leer el archivo, convertir a minúsculas y guardar en otro archivo
with open(input_path, "r", encoding="utf-8") as archivo_entrada:
    lineas = [linea.strip().lower() for linea in archivo_entrada]

# Guardar las líneas en minúsculas en un nuevo archivo
with open(output_path, "w", encoding="utf-8") as archivo_salida:
    archivo_salida.write("\n".join(lineas))

print(f"Líneas en minúsculas guardadas en {output_path}")
