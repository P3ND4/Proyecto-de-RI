#dependencias
import shutil

#guardar el toc leido en la linea donde leo content
def parse_toc(toc: str):
  parse = toc.split('/')
  response = parse[1]
  return response.split('"')[0]

#guardar el nombre del epub dada la ruta completa
def parse_epub(path: str):
  epub = path.split('/')
  return epub[len(epub) - 1].split('.')[0]

#borrar folders
def rem_dir(dir: list):
  for d in dir:
      shutil.rmtree(d)
      print('Succesful delete')
    
#ordenar un dicionario por sus valores en orden descendente y devuelve hasta los 10  primeros elementos 
def elements_sort_dict(dict: dict) -> dict:
  result = {}
  sort = {}
  i = 0
  
  #ordenar por valores de mayor a menor y crear una lista de tuplas (clave, valor)
  sorted_items = sorted(dict.items(), key=lambda x: x[1], reverse=True)

  #crear un nuevo diccionario a partir de las tuplas ordenadas
  for element in sorted_items:
    sort[element[0]] = element[1]
  
  while i < 10 and i < len(sort):
    for element in sort.keys():
      result[element] = sort[element]
    
    i +=1 
    
  return sort
