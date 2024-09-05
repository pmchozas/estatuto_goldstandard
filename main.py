#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 15:34:29 2024

@author: pmchozas
"""

import re
import json
import os

def extraer_articulos(texto):
    # Expresión regular para encontrar "artículo" seguido de un número
    pattern = re.compile(r'(Artículo \d+)')
    
    # Encuentra todas las apariciones del patrón en el texto
    matches = list(pattern.finditer(texto))
    
    articulos = []
    for i in range(len(matches)):
        # Inicio del artículo actual
        start = matches[i].start()
        
        # Fin del artículo actual: inicio del siguiente artículo o fin del texto
        end = matches[i + 1].start() if i + 1 < len(matches) else len(texto)
        
        # Extraer el texto del artículo
        articulo_texto = texto[start:end].strip()
        articulos.append(articulo_texto)
    
    return articulos
'''
# separar articulos estatuto 

nombre_archivo = 'data/estatuto_es.txt'

# Leer el contenido del archivo
with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
    texto = archivo.read()

articulos = extraer_articulos(texto)
for idx, articulo in enumerate(articulos, start=1):
    nombre_archivo_articulo = f'articulo_{idx}.txt'
    with open(nombre_archivo_articulo, 'w', encoding='utf-8') as archivo_articulo:
        archivo_articulo.write(articulo)    

'''
'''
# Sacar pref labels y alt labels de la terminología en json
term_list=[]
term_file= "data/terminology.json"
with open(term_file, 'r', encoding='utf-8') as archivo:
    datos = json.load(archivo)
    count=0
i=0

for clave, valor in datos.items():
    if isinstance(valor, list):
        print(f"{clave}:")
        for i, item in enumerate(valor):
            pref_label_list = item.get('http://www.w3.org/2004/02/skos/core#altLabel', [])
            filtered_json = next((item for item in pref_label_list if item.get('@language') == 'es'), None)
            if filtered_json != None:
                pref_label= filtered_json.get('@value')
                
                print("ESTO ES PREF")
                print(pref_label)
                term_list.append(pref_label)


term_file='alt_terms.txt'
with open(term_file, 'w') as file:
    for item in term_list:
        file.write(f"{item}\n")

'''

#Buscar términos en artículos estatuto

def check_words_in_file(file_path, words):
    appearing_terms=[]
    with open(file_path, 'r') as file:
        content = file.read()
        for word in words:
            #print(word)
            if word in content:
                # print('YES')
                # print(word)
                appearing_terms.append(word)
                
        return appearing_terms


term_file='data/all_terms.txt'
with open(term_file, 'r') as file:
    terms = [line.strip() for line in file]
   

folder_path='data/articles'
files = os.listdir(folder_path)
text_files = [file for file in files if file.endswith('.txt')]

out_folder_path="data/terms"

for text_file in text_files:
    file_path = os.path.join(folder_path, text_file)
    out_path = os.path.join(out_folder_path, text_file)
    found = check_words_in_file(file_path, terms)
    #print(found)
    if found:
        print(f"archivo {text_file}")
        with open(out_path, 'w') as file:
            for term in found:
                file.write(f"{term}\n")






















