#requests este folosit pentru a face cereri serverului
import requests
#bs4 este folosit pentru html parsing
from bs4 import BeautifulSoup as soup


def generate_link(cuvant):
    url = 'https://www.dictionarroman.ro/?c={}'.format(cuvant)
    return url

#descarca pagina si o salveaza intr-o variabila si intoarce documentul html
def fetch_page_html(url):
    #preia linkul potrivit si face o cerere pentru html-ul paginii
    r = requests.get(url)
    #page = html-ul pur
    page = r.text
    r.close()
    return page

#extrage doar textul primei definitii din tot fisierul html
def return_def(page):
    page_soup = soup(page, 'html.parser')
    definitie = page_soup.find('span', {'class':'def'})
    return definitie.get_text()

class Dictionar:
    def fetch_definition(self, cuvant):
        link = generate_link(cuvant)
        pagina = fetch_page_html(link)
        definitie = return_def(pagina)
        return definitie

