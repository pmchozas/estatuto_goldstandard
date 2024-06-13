#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 15:34:29 2024

@author: pmchozas
"""

import re

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

nombre_archivo = 'data/estatuto_es.txt'

# Leer el contenido del archivo
with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
    texto = archivo.read()

articulos = extraer_articulos(texto)
for idx, articulo in enumerate(articulos, start=1):
    nombre_archivo_articulo = f'articulo_{idx}.txt'
    with open(nombre_archivo_articulo, 'w', encoding='utf-8') as archivo_articulo:
        archivo_articulo.write(articulo)

