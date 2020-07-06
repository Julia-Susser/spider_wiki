import sqlite3
import urllib.error
import ssl
from urllib.parse import urljoin
from urllib.parse import urlparse
from urllib.request import urlopen
from bs4 import BeautifulSoup


def get_page():
    url = input("Enter a url")
    if len(url) < 1:
        url = "https://en.m.wikipedia.org/wiki/Turkey"


    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE


    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    tags_titles = soup(["h1", "h2", "h3", "h4", "h5", "h6", "span","li"])
    tag_data = soup("td")
    for tag in tag_data:
        print(tag.text)
    for tag in tags_titles:
        print(tag.text)
        #print(tag.text)
        #print("\n\n")


    print(len(tags_titles))
    tags_href = soup('a')
    for tag in tags_href:
        pass
get_page()
