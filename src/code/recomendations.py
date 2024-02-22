#dependencias
from epub import extract_metadata
import os

#metodos auxiliares
from utils import elements_sort_dict

#devuelve las recomendaciones con sus metadatas
def recomend(epubs: dict) -> dict:
  books_read = extract_metadata(list(epubs.keys()), ['genres'])
  return extract_metadata(books_recomended(books_read, epubs), ['title', 'creator', 'genres', 'date'])
  
#puntuacion de los libros que no ha leido el usuario
def books_recomended(books_read: dict, books_cal: dict) -> list:
  data_unread = extract_metadata(books_unread(books_read), ['title', 'genres'])
  user_preferences = user_score(books_read, books_cal)
  result = {}
  
  #iniciar todos los libros con 0
  for key in data_unread.keys():
    result[f'data/{key}.epub'] = 0
  
  for key in data_unread.keys():
    for genre in data_unread[key]['genres'].split(','):
      if genre in user_preferences.keys():
          result[f'data/{key}.epub'] += user_preferences[genre]
  
  return list(elements_sort_dict(result).keys())

#libros que no ha leido
def books_unread(books_read: dict) -> list:
  result = []
  
  for file in os.listdir('data'):
    if file.replace('.epub', '') not in books_read.keys():
      result.append(f'data/{file}')
  
  return result

#preferencia del usuario
def user_score(books_read: dict, books_cal: dict) -> dict:
  result = {}
  
  for element in books_read.keys():
    for genre in books_read[element]['genres'].split(','):
      try:
        result[genre] += books_cal[f'data/{element}.epub']
      except:
        result[genre] = books_cal[f'data/{element}.epub']
  
  return result

