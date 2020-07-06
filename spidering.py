
import sqlite3
import urllib.error
import ssl
from urllib.parse import urljoin
from urllib.parse import urlparse
from urllib.request import urlopen
from bs4 import BeautifulSoup

def first_spider():
    thing1 = input("Enter something you want to research: ")
    if len(thing1) < 1:
        thing1  = "Julia"
    if thing1.lower() == "stop":
        return "break"

    thingys = thing1.split()
    thingys[0] = thingys[0].capitalize()

    thing = "_".join(thingys)

    url = 'https://en.wikipedia.org/wiki/' + thing
    print(url)
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE


    html = urllib.request.urlopen(url, context=ctx).read()
    file = BeautifulSoup(html, 'html.parser')
    words = file(["h1", "h2", "h3", "h4", "h5", "h6", "span","li"])
    num_times = {}
    for x in words:
        ant = x.text

        if "Wikipedia" in ant:
            continue
        indivies = ant.split()
        for x in indivies:
            x = x.strip(")")
            x = x.strip("(")
            x = x.strip(".")
            x = x.strip('"')
            x = x.strip(',')
            x = x.strip('}')

            if x.lower() in thing1.lower():
                continue
            bad = ["pages","disambiguation", "[edit]"]
            if x in bad:
                continue
            if len(x) < 5:
                continue

            num_times[x] = num_times.get(x, 0) + 1
    return num_times


while True:

    num_times = first_spider()
    if num_times == "break":
        break

    num_times = sorted(num_times, key=num_times.get, reverse=True)


    first = num_times[0]
    print(first)
