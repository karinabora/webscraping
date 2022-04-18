from Task_1 import adventure_movie
import json

scraping_data = adventure_movie()
def top_movie(movies):
    years = []
    for mov in movies:
        if mov['year'] not in years:
            years.append(mov['year'])
    movies_dic = {mov:[] for mov in years}
    for mov in movies:
        year = mov ['year']
        for update_year in years:
            # print(update_year,year)
            if (update_year) == (year):
                movies_dic[update_year].append(mov)
    with open('top_movie_2.json','w') as file:
        json.dump(movies_dic,file,indent=4)
    return movies_dic    
top_movie(scraping_data)  

