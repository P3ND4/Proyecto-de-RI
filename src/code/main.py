from recomendations import books_recomended
from epub import extract_metadata

books_read = extract_metadata(['data/epub3.epub'], ['genres'])
print(extract_metadata(books_recomended(books_read), ['title', 'creator', 'genres', 'date']))