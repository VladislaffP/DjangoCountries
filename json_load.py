import os
import json
import sqlite3
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoCountries.settings")
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
from MainApp.models import Language
from MainApp.models import Country

#блок 1 загрузка стран

#connection = sqlite3.connect('db.sqlite3')
#cursor = connection.cursor()

#traffic = json.load(open('countries.json'))
#columns = ['country', 'languages']
#for row in traffic:
#    keys = tuple(row[c] for c in columns)
#    cursor.execute('insert into MainApp_country(country) values(?)', [keys[0]])

#connection.commit()
#connection.close()

#блок 2 загрузка языков
with open('countries.json') as f:
    tmp = json.load(f)
langs = []
for l1 in tmp:
    for l2 in l1['languages']:
        if l2 not in langs:
            langs.append(l2)

langs.sort();
#print(langs);

c1 = Country.objects.get(country='Benin')
l1 = Language.objects.get(language='Afar')

print(c1.id)
print(l1.id)
print(tmp)

for l1 in tmp:
    c1 = Country.objects.get(country=l1['country'])
    for l2 in l1['languages']:
        ln = Language.objects.get(language=l2)
        c1.languages.add(ln)
        print(c1, ln)

#for l0 in langs:
#    print(l0)
#    l1 = Language(language=l0)
#    l1.save()

#блок 3 загрузка связей

