

def get_soup():     
    url = "http://www.boxofficemojo.com/alltime/domestic.htm?page=1&p=.htm"
    page = urllib2.urlopen(url)
    return soup = BeautifulSoup(page)
    
def find_urls(soup):
    """ Finds all urls on website for individual people """
    movie_urls = soup.find(id='body').find_all('table')[1].find_all("a", attrs={'href': re.compile('movies/?')})
    # idm =[str(i).split(";") for i in movie_urls]
    urls = []
    for i in movie_urls:
        nam = i['href'].split("id=")
        nam2= nam[1].split(".")
        movie_name = nam2[0]
        return urls.append(get_url(movie_name))

def get_url(movie):
    """ For each movie name returns url"""
    return "http://www.boxofficemojo.com/movies/?id=%s.htm" % movie    
    
def get_movie_value(soup,field_name):
    """ takes a sting attribute of a movie on the page, 
    and returns the string in the next sibling object(the value for that attribute)"""
    obj = soup.find(text= re.compile(field_name))
    if not object:
        return None
    next_sibling = obj.findNextSibling()
    if next_sibling:
        return next_sibling.text
    else:
        return None
    
def get_directors():
    directors = soup.find_all('a',attrs={'href' : re.compile("/people/chart/[?]view=Director")})
    for director in directors:
        return director.text
    print len(directors)
    
def get_writers():
    writers = soup.find_all('a',attrs={'href' : re.compile("/people/chart/[?]view=Writer")})
    for writer in writers:
        return writer.text
        
def get_actors():
    actors = soup.find_all('a', attrs={'href' : re.compile("/people/chart/[?]view=Actor")})
    for actor in actors:
        return actor.text    
        
def get_producers():
    producers = soup.find_all('a',attrs={'href' : re.compile("/people/chart/[?]view=Producer")})
    for producer in producers:
        return producer.text
        
def get_composers():
    composers = soup.find_all('a',attrs={'href' : re.compile("/people/chart/[?]view=Composer")})
    for composer in composers:
        return composer.text
        
def get_domestic_foreign_gross:
    all=soup.find_all(class_='mp_box_content')
    table01 = all[0]
    ctn = 0
    for row in table01.find_all('tr'):
        col = row.find_all('td')
        return col[0].text.replace("+","")
        return col[1].text.replace("$","")
        
        
import urllib2
from bs4 import BeautifulSoup
import re
get_soup()
        

        
