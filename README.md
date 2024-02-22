# Proyecto de RI

## Aurores:
-Jose Carlos Pendas Rodriguez
-Max Bengochea More

## Modelo Usado:
-Sistema de Recomendacion basado en contenido
## Como ejecutar:
1-Doble clic en el archivo startup.
2-Abrira una ventana con los libros disponibles en la carpeta data, asi que deberas marcar los libros leidos y calificarlos.
3-Luego abre la ventana de libros sugeridos con los libros que nuestro modelo determine que puedieran gustarte.

## Explicacion del modelo:
Para la implementacion del modelo se uso el algoritmo "One Hot Encode". Creamos una matriz nxm con n filas y m columnas donde en la posicion i,j se encuentra la calificacion que le otorgo el usuario al libro i dado que el genero j es un subconjunto de los generos del libro i. Luego sumamos cada columna para crear el perfil del usuarioformado por un vector de m posiciones que contiene el valor que le da al usuario al genero j en la posicion j del vector. Al final agregamos al vector el nomre de los autores de loslibros junto con la valoracion del libro para indica que a un usuario le pueden gustar libros por los autores ademas de por los generos. Luego, creamos el mismo vector que creamos al principio pero esta vez con todos los libros que no ha leido el ususario. En esta matriz se mantienen las mismas columnas (union de los generos de los libros que leyo el usuario) pero en la posicion i,j almacenara el valor que le otorga el usuario al genero j si el genero j es un subconjntos de los generos del libro i. Para finalizar sumamos los elementos de cada fila y ese es el valor de cada libro, guardamos estos vectores, ordenamos descendentemente y devolvemos los 6 primeros del conjunto, ya que estan ordenados segun su valor de mayor a menor, por lo que devolveria los 7 libros de mayor puntaje.

Guia para la implementacion del algoritmo (One Hot Encoded):
https://www.statdeveloper.com/recomendaciones-basado-en-contenido-en-python

## Insuficiencias de la implementacion:
La obtencion de la metadata se realiza haciendo una busqueda interna en los documentos .epub en la seccion que especifica la metadata, por lo que nuestra implementacion se ve propensa a dar resultados erroneos debido a metadata inexistente o falsa. Una solucion podria basarse en asegurar que la metadata este correcta usando alguna api externa para accader a la informacion faltante o comprobar que esta sea correcta
