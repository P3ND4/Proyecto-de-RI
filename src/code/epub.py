#dependencias
import zipfile
import os

#metodos auxiliares
from utils import parse_epub, rem_dir

#descomprimir un epub
def epub_unzip(fileName: str):
  try:
    z = zipfile.ZipFile(fileName)
    fileDir = fileName.replace('.epub', '')

    for name in z.namelist():
        z.extract(name, fileDir)
    
    z.close() 
    print("Successfully unpacked the epub.")
    return
    
  except Exception as e:
    print(e)
    return

        
  except Exception as e:
    print(e)

#extraer la metadata dado un tag de la metadata
def extract_metadata(epubs: list, tags: list) -> dict:
  #carpetas que se descomprimieron
  folders: list = []
  
  try:
    #descomprimir ambos epubs
    for epub in epubs:
      epub_unzip(epub)
      folders.append(epub.replace('.epub', ''))
  
  finally:
    #estructura donde se almacenara la data
    metadata_info: dict = {}
    
    for epub in epubs:
      dir = f"{epub.replace('.epub', '')}/OEBPS/content.opf"
      metadata_info[parse_epub(epub)] = {}
      i = 0
      
      with open(dir, 'r') as f:
        metadata_stage = False
        
        for line in f.readlines():
          if metadata_stage:
            if f'dc:{tags[i]}' in line:
              metadata_info[parse_epub(epub)][tags[i]] = line.split('>')[1].split('<')[0]
              i += 1 
              
              if i == len(tags):
                break
              
          if 'metadata' in line:
            metadata_stage = True
      
  rem_dir(folders) 
  return metadata_info
