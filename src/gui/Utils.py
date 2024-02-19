def Meta_to_str(dic:dict):
    result =[]
    for m in dic:
        result.append(f'{dic[m]["title"]} --- Author: {dic[m]["creator"]} --- Genres: {dic[m]["genres"]}')
    return result