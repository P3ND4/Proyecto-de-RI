#dependencias
from epub import extract_metadata
import os
import spacy

#metodos auxiliares
from utils import elements_sort_dict

#devuelve las recomendaciones con sus metadatas
def recomend(epubs: dict) -> dict:
  nlp = spacy.load('es_core_news_sm')
  books_read = extract_metadata(list(epubs.keys()), ['genres', 'creator'])
  return extract_metadata(books_recomended(books_read, epubs, nlp), ['title', 'creator', 'genres', 'date'])
  
#puntuacion de los libros que no ha leido el usuario
def books_recomended(books_read: dict, books_cal: dict, nlp) -> list:
  data_unread = extract_metadata(books_unread(books_read), ['title', 'genres', 'creator'])
  user_preferences = user_score(books_read, books_cal, nlp)
  result = {}
  
  #iniciar todos los libros con 0
  for key in data_unread.keys():
    result[f'data/{key}.epub'] = 0
  
  for key in data_unread.keys():
    for genre in data_unread[key]['genres'].split(','):
      genre1 = nlp(genre.lower())
      
      for genre_user in user_preferences.keys():
        genre2 = nlp(genre_user.lower())
        
        if genre1.similarity(genre2) > 0.7:
          result[f'data/{key}.epub'] += user_preferences[genre_user]
    
    if data_unread[key]['creator'] in user_preferences.keys():
      result[f'data/{key}.epub'] += user_preferences[data_unread[key]['creator']]
  
  return list(elements_sort_dict(result).keys())

#libros que no ha leido
def books_unread(books_read: dict) -> list:
  result = []
  
  for file in os.listdir('data'):
    if '.epub' in file and file.replace('.epub', '') not in books_read.keys():
      result.append(f'data/{file}')
  
  return result

#preferencia del usuario
def user_score(books_read: dict, books_cal: dict, nlp) -> dict:
  result = {}
  
  for element in books_read.keys():
    for genre in books_read[element]['genres'].split(','):
      genre1 = nlp(genre.lower())
      
      for genre_user in result.keys():
        genre2 = nlp(genre_user.lower())
        
        if genre1.similarity(genre2) > 0.7:
          result[genre_user] += books_cal[f'data/{element}.epub']
      
      result[genre] = books_cal[f'data/{element}.epub']
    
    #agregar al autor al perfil del usuario
    autor = books_read[element]['creator']

    try:
      result[autor] += books_cal[f'data/{element}.epub']
    except:
      result[autor] = books_cal[f'data/{element}.epub']
  
  return result

print(len(recomend({'data/epub1.epub': 5, 'data/epub5.epub': 5, 'data/epub9.epub': 4, 'data/epub2.epub': 1, 'data/epub3.epub': 8})))
