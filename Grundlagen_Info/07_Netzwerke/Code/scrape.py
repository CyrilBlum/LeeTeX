import urllib3

def remove_html_tags(s):
    inTag = False
    out = ""

    for c in s:
        if c == '<':
            inTag = True
        elif c == '>':
          inTag = False
        elif not inTag:
            out = out + c
    return out

def replace_umlaute(s):
    di = {"Ã¤": "ä", "Ã¶": "ö", "Ã¼": "ü",
          "Ã„": "Ä", "Ã–": "Ö", "Ãœ": "Ü",
          "ÃŸ": "ß"}
    for key in di:
        s = s.replace(key, di[key])
    return s

url = "http://meteonews.ch/de/"
http = urllib3.PoolManager()
response = http.request('GET', url)
html = response.data.decode('utf-8')
html = remove_html_tags(html)
html = replace_umlaute(html)
start = html.find("Allgemeine Lage")
end = html.find("AutorIn")
html = html[start:end].strip()
print(html)