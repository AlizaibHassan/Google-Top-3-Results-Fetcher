import requests
import urllib
import pandas as pd
from requests_html import HTMLSession
from requests_html import HTML


def get_source(url):
    """Return the source code for the provided URL. 

    Args: 
        url (string): URL of the page to scrape.

    Returns:
        response (object): HTTP response object from requests_html. 
    """

    try:
        session = HTMLSession()
        response = session.get(url)
        return response

    except requests.exceptions.RequestException as e:
        print(e)

def scrape_google(query):

    query = urllib.parse.quote_plus(query)
    response = get_source("https://www.google.co.uk/search?q=" + query)

    links = list(response.html.absolute_links)
    google_domains = ('https://www.google.', 
                      'https://google.', 
                      'https://webcache.googleusercontent.', 
                      'http://webcache.googleusercontent.', 
                      'https://policies.google.',
                      'https://support.google.',
                      'https://maps.google.')

    for url in links[:]:
        if url.startswith(google_domains):
            links.remove(url)

    return links




f = open('kws.txt')
f1 = open('1.txt','w+')
f2 = open('2.txt','w+')
f3 = open('3.txt','w+')

line = f.readline()
cnt=0
while line:
    
    line=line.replace("\n","")
    s=scrape_google(line)
    print(s)
    print(cnt)
    cnt+=1
    
    
    f1.write(s[0])
    f1.write("\n")
    f2.write(s[1])
    f2.write("\n")
    f3.write(s[2])
    f3.write("\n")

    line = f.readline()
    
print("complete")
f.close()
f1.close()
f2.close()
f3.close()
