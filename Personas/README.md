# Contenido

Recolecta los descriptores de las personas que se hayan encontrado en todos los frames. 

Se sigue la siguiente lógica (pseudo-código):
```python
# Recorrer frame por frame
for frame in frames:

  # Recorrer cada uno de los descriptores
  for descriptor in lista_de_descriptores:
  
    # Comparar con todos los descriptores guardados hasta ahora
    persona_existe = existen_descriptores_parecidos(descriptor)
    
    if(persona_existe):
      # Agregar descriptor a persona correspondiente
      agregar_descriptor_a_persona(descriptor)
      
     else:
      # Se crea una nueva persona que solo contiene este descriptor
      crear_nueva_persona(descriptor)
```

Es decir, se va revisando frame por frame y se agrupan los descriptores que son parecidos. 
Si en un frame se encuentra que hay un descriptor que no se parece a ningun anterior se asume
que se trata de una nueva persona.


# Estructura

- `Personas`
  - (Nombre de metodo de detección): Puede ser `RetinaFace` o `dlib`
    - (persona_xxx.npy): recolecta todos los descriptores de una persona en particular
