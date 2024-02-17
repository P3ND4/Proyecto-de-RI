#dependencias
import shutil

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
  
  #toma los 10 primeros elementos
  for element in sort.keys():
    if i < 10 and i < len(sort):
        result[element] = sort[element]
        i +=1 
    
  return result

