#requests este folosit pentru a face cereri serverului
import requests
#bs4 este folosit pentru html parsing
from bs4 import BeautifulSoup as soup

#de la cuvant se formateaza url-ul la care se va face apel
def get_link(cuvant):
    #modifica linkul in functie de cuvantul cautat
    #url = 'https://www.dictionarroman.ro/?c={}'.format(cuvant)
    url = "https://dexonline.ro/definitie/{}".format(cuvant)
    return url

#descarca pagina si o salveaza intr-o variabila si intoarce documentul html
def get_page_html(url):
    #preia linkul potrivit si face o cerere pentru html-ul paginii
    r = requests.get(url)
    #page = html-ul pur
    page = r.text
    r.close()
    return page

#extrage doar textul primei definitii din tot fisierul html
def get_def(page):
    #html parsing
    page_soup = soup(page, 'html.parser')
    definitie = page_soup.find('span', {'class':'def'})
    return definitie.get_text()

#functia finala care trece prin toate etapele si ajunge de la cuvant la definitie
def get_text(cuvant):
    link = get_link(cuvant)
    pagina = get_page_html(link)
    definitie = get_def(pagina)
    return definitie

#ia ca input mesajul de pe discord
def defineste(mesaj):
    #inlatura comanda
    mesaj = mesaj.replace("!dex", "")
    #inlatura orice spatiu
    mesaj = mesaj.replace(" ", "")
    #returneaza definitia pentru cuvantul extras din mesaj
    return mesaj, get_text(mesaj)

###print(get_text('solutie'))

#######test run
###link=get_link('test')
###pagina = get_page_html(link)
###definitie_test = get_def(pagina)
###print(definitie_test)
