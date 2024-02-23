# Proyecto de RI

## Autores:
-José Carlos Pendas Rodíguez
-Max Bengochea Moré

## Modelo Usado:
-Sistema de Recomendación basado en contenido
## Como ejecutar:
1-Abrir la consola en la cartpeta principal y escribir:
```bash
./startup.md
```
2-Abrira una ventana con los libros disponibles en la carpeta data, así que se deben marcar los libros leidos y calificarlos.

3-Luego abre la ventana de libros sugeridos con los libros que nuestro modelo determine que puedieran gustarte.

## Explicacion del modelo:
Para la implementación del modelo se usó el algoritmo "One Hot Encode". Se creó una matriz nxm con n filas y m columnas donde en la posicion i,j se encuentra la calificación que le otorgó el usuario al libro i dado que el género j es un subconjunto de los géneros del libro i. Luego se suma cada columna para crear el perfil del usuario formado por un vector de m posiciones que contiene el valor que le da el usuario al genero j en la posicion j del vector. Al final se agrega al vector el nombre de los autores de los libros junto con la valoración del libro para indicar que a un usuario le pueden gustar libros por los autores además de por los géneros. Luego, se la misma matriz que se creó al principio pero esta vez con todos los libros que no ha leido el ususario. En esta matriz se mantienen las mismas columnas (union de los generos de los libros que leyó el usuario) pero en la posicion i,j almacenará 1 si el género j es un subconjnto de los generos del libro i. Para finalizar, se realiza producto punto entre cada vector fila de la matriz por el vector del perfil del usuario, y este sería el valor del libro i. Ordenamos descendentemente y devolvemos los 6 primeros del conjunto, ya que están ordenados segun su valor de mayor a menor, por lo que devolvería los 6 libros de mayor puntaje.

Guía para la implementación del algoritmo (One Hot Encoded):
https://www.statdeveloper.com/recomendaciones-basado-en-contenido-en-python

## Insuficiencias de la implementacion:
La obtención de la metadata se realiza haciendo una búsqueda interna en los documentos .epub en la sección que especifica la metadata, por lo que nuestra implementación se ve propensa a dar resultados erróneos debido a metadata inexistente o falsa. Una solución podria basarse en asegurar que la metadata esté correcta usando alguna api externa para accader a la información faltante o comprobar que esta sea correcta

## Fuentes de Datos:
Documentos .epub escogidos al azar.
