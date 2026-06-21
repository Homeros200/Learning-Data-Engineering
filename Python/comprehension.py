domains = ['www.google.com',
           'openai.com',
           'localhost',
           'WWW.DATAWITHBARAA.COM']

cleaned = [
    d.lower().replace('www.','')
    for d in domains
    if '.' in d 
]

print(cleaned)

 