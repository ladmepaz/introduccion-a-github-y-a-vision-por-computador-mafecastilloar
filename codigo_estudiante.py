# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 17:00:25 2024

@author: jfrui
"""

# Completa las funciones de abajo de acuerdo a la descripción de los parámetros de entrada y salida

import numpy as np
from PIL import Image

def leer_imagen(ruta_imagen):
    # Abrir la imagen
    img = Image.open (ruta_imagen) # Insertar código aquí
        
    return img

image = leer_imagen("data/imagen0.png")
image.show()

def obtener_info_imagen(img):
    # Obtener el número de canales
    modo = img.mode
    if modo == 'L':  # Escala de grises
        num_canales = 1 # Ingresa valor aquí
    elif modo == 'RGB':  # Imagen RGB
        num_canales = 3 # Ingresa valor aquí
    elif modo == 'RGBA':  # Imagen RGBA
        num_canales = 4 # Ingresa valor aquí
    else:
        num_canales = len(modo)  # Otros modos de imagen
    
    # Obtener las dimensiones de la imagen
    dimensiones = img.size  # Ingresa valor aquí para obtener (ancho, alto)
    
    return num_canales, dimensiones

num_canales, dimensiones = obtener_info_imagen(image)
print("numero del canal", num_canales)
print("dimenciones", dimensiones)

def imagen_a_arreglo(img):
    # Convertir la imagen a un arreglo de NumPy
    arreglo = np.array(img) # Insertar código aquí
    return arreglo

arreglo = imagen_a_arreglo(image)
print("Tipo de dato", type(arreglo))
print("Forma del arreglo", arreglo.shape)

def estadisticas_intensidad(arreglo_img):
    # Calcular el promedio y la desviación estándar
    promedio = np.mean(arreglo_img) # Insertar código aquí
    desviacion_estandar = np.std(arreglo_img) # Insertar código aquí
    
    return promedio, desviacion_estandar

estadisticas = estadisticas_intensidad(arreglo)
print("Estadisticas de intensidad", estadisticas)

def estadisticas_por_canal(arreglo_img):
    # Verificar el número de dimensiones del arreglo
    if len(arreglo_img.shape) == 2:
        # Imagen de un solo canal
        promedio = np.mean(arreglo_img) # Insertar código aquí
        desviacion_estandar = np.std(arreglo_img) # Insertar código aquí
        resultados = {
            'Canal_1': {
                'Promedio': promedio,
                'Desviación Estándar': desviacion_estandar
            }
        }
    elif len(arreglo_img.shape) == 3:
        # Imagen de múltiples canales
        resultados = {}
        num_canales = arreglo_img.shape[2]
        
        for canal in range(num_canales): # Insertar código aquí
            promedio = np.mean(arreglo_img[:, :, canal])
            desviacion_estandar = np.std(arreglo_img[:, :, canal])
            resultados[f'Canal_{canal+1}'] = {
                'Promedio': promedio,
                'Desviación Estándar': desviacion_estandar
            }
    else:
        raise ValueError("El arreglo de imagen debe tener 2 o 3 dimensiones.")
    
    return resultados

estadisticas_1 = estadisticas_por_canal(arreglo)
print("Estadisticas de intensidad por canal", estadisticas_1)