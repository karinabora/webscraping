from Task_1 import adventure
from bs4 import BeautifulSoup
import json
import requests
def get_movie_list_details(movies):
    j = 0
    new_list_1 = []
    while j<10:
        new_url = movies[j]["movie URL"]
        url = new_url
        requests_list = requests.get(url)
        soup = BeautifulSoup(requests_list.text,'html.parser')
        movie_find_2 = soup.find('ul',class_='content-meta info')
        movie_find_3 = movie_find_2.find_all('li',class_='meta-row clearfix')
        movie_bio = soup.find('div',class_='movie_synopsis clamp clamp-6 js-clamp').get_text().strip()
        my_dict = {}
        for i in movie_find_3:
            all_data = i.find('div',class_='meta-label subtle').get_text().strip()
            all_value = i.find('div',class_='meta-value').get_text().replace(" ","").strip().replace("\n","")
            my_dict['bio']=movie_bio
            my_dict.update({all_data:all_value})
        new_list_1.append(my_dict)
        j+=1
    with open('Task_5.json','w') as file:
        json.dump(new_list_1,file,indent=4)
    return new_list_1
get_movie_list_details(adventure)
