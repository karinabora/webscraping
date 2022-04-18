# Beautiful Soup is a Python library for pulling data out of HTML and XML files
from bs4 import BeautifulSoup
# pip install beautifulsoup4 ... from bs4 import BeautifulSoup >>> soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
import requests
# The requests module allows you to send HTTP requests using Python
import json
# JSON is a language-independent data format. JSON stands for JavaScript Object Notation · language-independent data interchange format. 
def adventure_movie():
    data="https://www.rottentomatoes.com/top/bestofrt/"
    advanced=requests.get(data)
    # GET is used to request data from a specified resource.
    htmlcontent=advanced.content
    # print(htmlcontent)
    soup=BeautifulSoup(htmlcontent,"html.parser")
    # The find() method returns all occurrences in the selection.
    table_tag=soup.find("table",class_="table")
    
    tr=table_tag.find_all("tr")
    # findall() module is used to search for “all” occurrences that match a given pattern.
    top_movie=[]
    serial_no=1
    for i in tr:
        movie_rank=i.find_all("td",class_="bold")
        for j in movie_rank:
            rank=j.get_text()
        movie_rating=i.find_all("span",class_="tMeterScore")
        for rate in movie_rating:
            rating=rate.get_text().strip()
            # The get_text() method returns the text inside the Beautiful Soup or Tag object as a single Unicode string.
        movie_name=i.find_all("a",class_="unstyled articleLink")
        for name in movie_name:
            title=name.get_text().strip()
            #get_text()=tag remove karna ka liye/ Remove spaces at the beginning and at the end of the string:
            #strip()=white space htana ka liye bhi
            list=title.split()
            year=list[-1][1:5]
            year1=int(year)
            name_lenght=len(list)-1
            name=""
            for l in range(name_lenght):
                name+=""
                name+=list[l]
            movie_name=name
        movie_reviews=i.find_all("td",class_="right hidden-xs")
        for rev in movie_reviews:
            reviews=rev.get_text()
        url=i.find_all("a",class_="unstyled articleLink")
        for i in url:
            link=i["href"]
            movie_link="https://www.rottentomatoes.com"+link
            # print(movie_link)
            details={"movie_rank":"","movie_rating":"","movie_name":"","movie_reviews":"","movie URL":"","year":""}
            details["movie_rank"]=rank
            details["movie_rating"]=rating
            details["movie_name"]=movie_name
            details["movie_reviews"]=reviews
            details["movie URL"]=movie_link
            details["year"]=year1
            top_movie.append(details.copy())
            # print(top_movie)

  
    with open('top_movie_1.json','w') as file:
        json.dump(top_movie,file,indent=4)
        return top_movie
adventure=adventure_movie() 
