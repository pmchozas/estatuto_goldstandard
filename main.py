#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 15:34:29 2024

@author: pmchozas
"""

import re
import json
import os
'''
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
#SACAR OFFSET DE TÉRMINOS

#Buscar la posición de inicio y fin del término en el texto. 
def find_offset(termino, texto):
    posiciones = []
    indice = texto.find(termino)
    
    # Mientras encuentre el término en el texto
    while indice != -1:
        inicio = indice
        fin = inicio + len(termino)  # Fin es el índice del último carácter + 1
        posiciones.append((inicio, fin))
        
        # Buscar siguiente ocurrencia desde el último índice + 1
        indice = texto.find(termino, inicio + 1)
    
    return posiciones

#Ordenar lista de términos por número de tokens
def order_terms(terms):
    # Ordenar la lista de términos por el número de tokens (palabras), de mayor a menor
    return sorted(terms, key=lambda term: len(term.split()), reverse=True)

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


term_file='data/dic_victor_terms.txt'
with open(term_file, 'r') as file:
    terms = [line.strip() for line in file]
    terms = order_terms(terms)
   

folder_path='data/gold_standard/articles2024'
out_ann_path='data/gold_standard/brat_annotations_dic_victor'
files = os.listdir(folder_path)
text_files = [file for file in files if file.endswith('.txt')]

out_folder_path="data/test"



for text_file in text_files:
    counter=0
    
    file_path = os.path.join(folder_path, text_file)
    out_path = os.path.join(out_folder_path, text_file)
    
    found = check_words_in_file(file_path, terms)
    new_name=text_file.replace(".txt", "")
    ann_name= f'{new_name}.ann'
    ann_path=os.path.join(out_ann_path,ann_name)
    print(found)
    
    
    diccionarios = []
    if found:

        print(ann_path)
        for term in found: 
            
            print(term)
            with open(file_path, 'r') as file:
                text = file.read()
                positions=find_offset(term, text)
                print(positions)
    
                
                for pos in positions:
                    counter+=1
                    my_dict={
                        'id':"",
                        'type': "concept",
                        'start':0,
                        'end':0,
                        'term':""
                        }
                    my_dict['id']="T"+str(counter)
                    my_dict['term']=term
                    my_dict['start']=pos[0]
                    my_dict['end']=pos[1]
                    print(my_dict)
                    diccionarios.append(my_dict)
                    

                #print(diccionarios)
                with open(ann_path, mode='w') as file:
                    for my_dict in diccionarios:
                        file.write(f"{my_dict['id']}\t{my_dict['type']} {my_dict['start']} {my_dict['end']}\t {my_dict['term']}\n")
                            



















