import random

import requests
from bs4 import BeautifulSoup
import time
import pandas as pd

GENERATE_CSV = True
STARTING_URL = 'https://lumigo.pl/sitemap.xml'

PRODUCT_NAME = []  # nazwa
PRODUCT_DESCRIPTION = []  # opis
PRODUCT_OLD_PRICE = []  # cena bez rabatu
PRODUCT_NEW_PRICE = []  # cena z rabatem
TIME_LIMIT = []  # termin realizacji
# delivery similar
# return similar
PRODUCT_ON_SALE = []  # is on sale
DISCOUNT_PERCENT = []  # rabat
DISCOUNT_VALUE = []  # rabat promocja
CATALOG_NUMBER = []  # numer katalogowy
PRODUCT_TYPE = []  # rodzaj
PRODUCT_PURPOSE = []  # przeznaczenie
PRODUCT_STYLE = []  # stylistyka
PRODUCT_SET = []  # seria
DIFFERENT_SIZES = []  # inny rozmiary
REALISATION = []  # wykonanie
COLORS = []  # kolorystyka
DIAMETER = []  # szrednica
ANOTHER_COLORS = []  # inne colory
SIZES = []  # wymiary
DEPTH = []  # głębokość
HEADLINING = []  # podsufitka
LIGHT_COLOR = []  # barwa światła
LIGHT_BEAM = []  # strumien swiatła
SHADE = []  # klosz
BULB_INCLUDED = []  # żarówka w komplecie
BUILT_IN_LED = []  # wbudowany led
MATERIAL_TYPE = []  # rodzaj materialu
MANUFACTURER = []  # firma
LAMP_HANDLE = []  # żarówka/trzonek
MAX_POWER = []  # maksymalna moc
WIRE_LENGTH = []  # przewód
ALERTS = []  # alerts
BASE_SIZE = []  # Podstawa
LAMPSHADE = []  # Abażur
MAX_LENGTH = []  # Maksymalny zwis
PRODUCT_AVAILABLE = []
FEATURES = []  # cechy
IMAGE_LINKS = []
IMAGE_ALTS = []
QUANTITY = []

soup = BeautifulSoup(requests.get(STARTING_URL).text, 'xml')
product_sitemaps_links = []

for loc in soup.select('loc', limit=11):
    product_sitemaps_links.append(loc.text)
product_sitemaps_links.pop(0)
product_sitemaps_links.pop(0)

products_links = []

for i in range(len(product_sitemaps_links)):
    # time.sleep(0.5)
    current_path = product_sitemaps_links[i]
    links_list = BeautifulSoup(requests.get(current_path).text, 'xml')
    for loc in links_list.select('url > loc', limit=120):
        products_links.append(loc.text)
    for url in links_list.select('url', limit=120):
        links = ""
        alts = ""
        for img in url.select('image'):
            links = links + img.find('image:loc').text.replace('s', '', 1) + ','
            alt = img.find('image:title')
            if alt is not None:
                alts = alts + alt.text + ','
            else:
                alts = alts + ','
        IMAGE_LINKS.append(links)
        IMAGE_ALTS.append(alts.replace('&', '').replace('#', '').replace('|', ''))

# h1 = name

for i in range(len(products_links)):
    time.sleep(0.3)
    current_product_link = products_links[i]
    current_product = BeautifulSoup(requests.get(current_product_link).text, 'html.parser')
    # nazwa
    PRODUCT_NAME.append(current_product.find('h1').text)

    # opis
    PRODUCT_DESCRIPTION.append(current_product.find('div', attrs={'class': "left-data"})
                               .find('p').find_next_sibling().text)

    on_sale = current_product.find('p', attrs={'class': 'price-regular'})
    # not on sale
    if on_sale is None:
        PRODUCT_OLD_PRICE.append(current_product.find('p', attrs={'class': 'price-bold'}).text
                                 .replace(' ', '').replace('\n', '').replace('"', ''))
        PRODUCT_NEW_PRICE.append(0)
        PRODUCT_ON_SALE.append(0)
        DISCOUNT_VALUE.append(0)
        div = current_product.find('div', attrs={'class': "rabat-koszyk__txt col-md-10"})
        if div is not None:
            DISCOUNT_PERCENT.append(div.find('b').text)
        else:
            DISCOUNT_PERCENT.append('-')
    # on sale
    else:
        new_price = current_product.find('p', attrs={'class': 'price-bold'}).text \
            .replace(' ', '').replace('\n', '').replace('"', '').replace('zł', '')
        old_price = current_product.find('p', attrs={'class': 'price-regular'}).text \
            .replace(' ', '').replace('\n', '').replace('"', '').replace('zł', '')
        DISCOUNT_VALUE.append(round(float(old_price) - float(new_price), 3))
        PRODUCT_OLD_PRICE.append(old_price + ' zł')
        PRODUCT_ON_SALE.append(1)
        DISCOUNT_PERCENT.append('0%')

    # termin realizacji
    TIME_LIMIT.append(current_product.find('div', attrs={'class': "col-md-10 content"})
                      .find('p').find_next_sibling().text)

    # dostepny
    available = current_product.find('div', attrs={'class': "quantity"})
    if available is not None:
        PRODUCT_AVAILABLE.append(1)
        QUANTITY.append(random.randint(5, 100))
    else:
        PRODUCT_AVAILABLE.append(0)
        QUANTITY.append(0)

    ATTRIBUTES_DIVS = current_product.findAll('div', attrs={'class': 'col-md-3 col-sm-6 parameter'})

    ATTRIBUTES = {}

    for attr_no in range(len(ATTRIBUTES_DIVS)):
        content = ATTRIBUTES_DIVS[attr_no].find('p', attrs={'class': 'content'}).text
        ATTRIBUTES[ATTRIBUTES_DIVS[attr_no].find('p').text] = content

    ATTRIBUTE_NAMES = ["Numer katalogowy", "Rodzaj", "Przeznaczenie",
                       "Stylistyka", "Seria", "Inne rozmiary",
                       "Kolorystyka", "Inne kolory", "Wymiary (cm)",
                       "Średnica", "Podsufitka (cm)", "Barwa światła",
                       "Strumień światła", "Żarówka w komplecie", "Wbudowany LED",
                       "Rodzaj materiału", "Firma", "Żarówka/trzonek",
                       "Maksymalna moc", "Głębokość", "Wykonanie",
                       "Klosz", "Przewód (długość)", "Abażur (cm)",
                       "Podstawa (cm)", "Maksymalny zwis"]

    features = ''
    # numer katalogowy
    if "Numer katalogowy" in ATTRIBUTES.keys():
        CATALOG_NUMBER.append(ATTRIBUTES["Numer katalogowy"])
        features += 'Numer katalogowy:' + ATTRIBUTES["Numer katalogowy"].replace(',', '/') + ','
        ATTRIBUTES.pop("Numer katalogowy")
    else:
        CATALOG_NUMBER.append('-')

    # rodzaj
    if "Rodzaj" in ATTRIBUTES.keys():
        PRODUCT_TYPE.append('')
        PRODUCT_TYPE[len(PRODUCT_TYPE) - 1] = current_product.select_one(
            '.woocommerce-breadcrumb a:nth-of-type(2)').text
        features += "Rodzaj:" + ATTRIBUTES["Rodzaj"].replace(',', '/') + ','
        ATTRIBUTES.pop("Rodzaj")

    # przeznaczenie
    if "Przeznaczenie" in ATTRIBUTES.keys():
        PRODUCT_TYPE[len(PRODUCT_TYPE) - 1] += ',' + ATTRIBUTES["Przeznaczenie"].replace('Kuchnia',
                                                                                         'Kucznia i jadalnia')
        features += "Przeznaczenie:" + ATTRIBUTES["Przeznaczenie"].replace(',', '/') + ','
        ATTRIBUTES.pop("Przeznaczenie")

    # stylistyka
    if "Stylistyka" in ATTRIBUTES.keys():
        PRODUCT_TYPE[len(PRODUCT_TYPE) - 1] += ',' + ATTRIBUTES["Stylistyka"]\
            .replace('Styl nowoczesny', 'Nowoczesne')\
            .replace('Styl klasyczny', 'Klasyczne')\
            .replace('Styl skandynawski', 'Skandynawskie')\
            .replace('Styl glamour', 'Glamour')\
            .replace('industrialny', 'Industrialne')\
            .replace('Styl modern classic', 'Modern classic')
        features += "Stylistyka:" + ATTRIBUTES["Stylistyka"].replace(',', '/') + ','
        ATTRIBUTES.pop("Stylistyka")

    # seria
    if "Seria" in ATTRIBUTES.keys():
        features += "Seria:" + ATTRIBUTES["Seria"].replace(',', '/') + ','
        ATTRIBUTES.pop("Seria")

    # inny rozmiary
    if "Inne rozmiary" in ATTRIBUTES.keys():
        features += "Inne rozmiary:" + ATTRIBUTES["Inne rozmiary"].replace(',', '/') + ','
        ATTRIBUTES.pop("Inne rozmiary")

    # kolorystyka
    if "Kolorystyka" in ATTRIBUTES.keys():
        features += "Kolorystyka:" + ATTRIBUTES["Kolorystyka"].replace(',', '/') + ','
        ATTRIBUTES.pop("Kolorystyka")

    # inne colory
    if "Inne kolory" in ATTRIBUTES.keys():
        features += "Inne kolory:" + ATTRIBUTES["Inne kolory"].replace(',', '/') + ','
        ATTRIBUTES.pop("Inne kolory")

    # wymiary
    if "Wymiary (cm)" in ATTRIBUTES.keys():
        features += "Wymiary (cm):" + ATTRIBUTES["Wymiary (cm)"].replace(',', '/') + ','
        ATTRIBUTES.pop("Wymiary (cm)")

    # Średnica
    if "Średnica" in ATTRIBUTES.keys():
        features += "Średnica:" + ATTRIBUTES["Średnica"].replace(',', '/') + ','
        ATTRIBUTES.pop("Średnica")

    # podsufitka
    if "Podsufitka (cm)" in ATTRIBUTES.keys():
        features += "Podsufitka (cm):" + ATTRIBUTES["Podsufitka (cm)"].replace(',', '/') + ','
        ATTRIBUTES.pop("Podsufitka (cm)")

    # barwa światła
    if "Barwa światła" in ATTRIBUTES.keys():
        features += "Barwa światła:" + ATTRIBUTES["Barwa światła"].replace(',', '/') + ','
        ATTRIBUTES.pop("Barwa światła")

    # strumien swiatła
    if "Strumień światła" in ATTRIBUTES.keys():
        features += "Strumień światła:" + ATTRIBUTES["Strumień światła"].replace(',', '/') + ','
        ATTRIBUTES.pop("Strumień światła")

    # żarówka w komplecie
    if "Żarówka w komplecie" in ATTRIBUTES.keys():
        features += "Żarówka w komplecie:" + ATTRIBUTES["Żarówka w komplecie"].replace(',', '/') + ','
        ATTRIBUTES.pop("Żarówka w komplecie")

    # wbudowany led
    if "Wbudowany LED" in ATTRIBUTES.keys():
        features += "Wbudowany LED:" + ATTRIBUTES["Wbudowany LED"].replace(',', '/') + ','
        ATTRIBUTES.pop("Wbudowany LED")

    # rodzaj materialu
    if "Rodzaj materiału" in ATTRIBUTES.keys():
        features += "Rodzaj materiału:" + ATTRIBUTES["Rodzaj materiału"].replace(',', ' /') + ','
        ATTRIBUTES.pop("Rodzaj materiału")

    # firma
    if "Firma" in ATTRIBUTES.keys():
        MANUFACTURER.append(ATTRIBUTES["Firma"])
        ATTRIBUTES.pop("Firma")
    else:
        MANUFACTURER.append('-')

    # żarówka/trzonek
    if "Żarówka/trzonek" in ATTRIBUTES.keys():
        features += "Żarówka/trzonek:" + ATTRIBUTES["Żarówka/trzonek"].replace(',', '/') + ','
        ATTRIBUTES.pop("Żarówka/trzonek")

    # maksymalna moc
    if "Maksymalna moc" in ATTRIBUTES.keys():
        features += "Maksymalna moc:" + ATTRIBUTES["Maksymalna moc"].replace(',', '/') + ','
        ATTRIBUTES.pop("Maksymalna moc")

    # głębokość
    if "Głębokość" in ATTRIBUTES.keys():
        features += "Głębokość:" + ATTRIBUTES["Głębokość"].replace(',', '/') + ','
        ATTRIBUTES.pop("Głębokość")

    # wykonanie
    if "Wykonanie" in ATTRIBUTES.keys():
        features += "Wykonanie:" + ATTRIBUTES["Wykonanie"].replace(',', '/') + ','
        ATTRIBUTES.pop("Wykonanie")

    # przewód
    if "Przewód (długość)" in ATTRIBUTES.keys():
        features += "Przewód (długość):" + ATTRIBUTES["Przewód (długość)"].replace(',', '/') + ','
        ATTRIBUTES.pop("Przewód (długość)")

    # Alerts
    wazne = current_product.find('div', attrs={'class': 'col-md-3 col-sm-6 alert-parameter parameter'})
    if wazne is not None:
        alert = wazne.text
        features += "Ważne:" + alert + ','

    # Abażur
    if "Abażur (cm)" in ATTRIBUTES.keys():
        features += "Abażur (cm):" + ATTRIBUTES["Abażur (cm)"].replace(',', '/') + ','
        ATTRIBUTES.pop("Abażur (cm)")

    # podstawa
    if "Podstawa (cm)" in ATTRIBUTES.keys():
        features += "Podstawa (cm):" + ATTRIBUTES["Podstawa (cm)"].replace(',', '/') + ','
        ATTRIBUTES.pop("Podstawa (cm)")

    # Maksymalny zwis
    if "Maksymalny zwis" in ATTRIBUTES.keys():
        features += "Maksymalny zwis:" + ATTRIBUTES["Maksymalny zwis"].replace(',', '/') + ','
        ATTRIBUTES.pop("Maksymalny zwis")

    # klosz
    if "Klosz" in ATTRIBUTES.keys():
        features += "Klosz:" + ATTRIBUTES["Klosz"].replace(',', '/') + ','
        ATTRIBUTES.pop("Klosz")
    elif "Klosz (cm)" in ATTRIBUTES.keys():
        features += "Klosz (cm):" + ATTRIBUTES["Klosz (cm)"].replace(',', '/') + ','
        ATTRIBUTES.pop("Klosz (cm)")

    FEATURES.append(features)

    print("Product No. ", i)
    print(ATTRIBUTES)

if GENERATE_CSV:
    df = pd.DataFrame({'Active': 1,
                       'Id': CATALOG_NUMBER,
                       'Nazwa': PRODUCT_NAME,
                       'DateCreated': (
                               str(random.randint(1999, 2021)) + '-'
                               + str(random.randint(1, 12)) + '-'
                               + str(random.randint(1, 30))),
                       'Kategorii': PRODUCT_TYPE,
                       'Cena(brutto)': PRODUCT_OLD_PRICE,
                       'Promocja': PRODUCT_ON_SALE,
                       'Rabat': DISCOUNT_VALUE,
                       'Rabat %': DISCOUNT_PERCENT,
                       'Firma': MANUFACTURER,
                       'Termin realizacji': TIME_LIMIT,
                       'Opis': PRODUCT_DESCRIPTION,
                       'Dostępny': PRODUCT_AVAILABLE,
                       'Cechy': FEATURES,
                       'Quantity': QUANTITY,
                       'Images': IMAGE_LINKS})

    df.to_csv('TEST.csv', index=False, encoding='utf-8-sig', sep=';')
