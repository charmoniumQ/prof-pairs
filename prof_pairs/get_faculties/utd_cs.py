import re
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'http://cs.utdallas.edu/people/faculty/'
university = 'utdallas.edu'
school = 'ecs.utdallas.edu'
department = 'cs.utdallas.edu'

def get_faculties():
    raw_page = urlopen(url)
    page = BeautifulSoup(raw_page, 'lxml')
    for table in page.find_all('tbody'):
        for row in table.find_all('tr'):
            cells = list(row.find_all('td'))
            name = cells[0].find('a', href=True).text
            lastname, firstnames = re.sub('\xa0', ' ', name).split(', ')
            email = cells[1].find('a', href=True).text
            position = cells[0].text.split('\n')[2]
            phone = re.sub('\\D', '', cells[1].text[len(email):])
            yield dict(
                lastname=lastname,
                firstnames=firstnames,
                position=position,
                email=email,
                phone=phone,
                university=university,
                school=school,
                department=department,
            )
