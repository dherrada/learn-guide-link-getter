from googlesearch import search

query = "site:learn.adafruit.com install library zip"


with open('links.txt', 'w') as f:
    for j in search(query, tld='com', num=50, stop=2300, pause=3):
        print(j)
        f.write(''.join(j)+'\n')

