import re
import json
import string
import orodja
import urejanje

vzorec_bloka = re.compile(
    r'<div\sclass="structItem structItem--item\s.*?js-inlineModContainer\sjs-itemListItem-.*?>'
    r'.*?'
    r'<div\sclass="structItem-itemTagLine">'
    r'.*?</div>.*?</div>.*?</div>',
    flags=re.DOTALL
)

vzorec_putke = re.compile(
    r'<div class="structItem-title">\s*?'
    r'<a href="(?P<link>.*?)" class="" data-tp-primary="on">(?P<breed>.*?)</a>'
    r'.*?'
    r'<dt>Views</dt>'
    r'.*?'  
    r'<div class="structItem-itemTagLine">'
    r'\s*?'
    r'(?P<about>.*?)'
    r'\s*?</div>',
    flags=re.DOTALL
)

vzorec_komentarjev = re.compile(
    r'<dt>Comments</dt>'
    r'.*?'
    r'<dd><a href=".*?" class="u-concealed">(?P<number_of_comments>.*?)</a></dd>'
    r'.*?',
    flags=re.DOTALL
)

vzorec_reaction_score = re.compile(
    r'(<dt>Reaction score</dt>)?'
    r'.*?'
    r'<dd>(?P<reaction_score>.*?)</dd>',
    flags=re.DOTALL
    )

vzorec_number_of_reviews = re.compile(
    r'<dt>Reviews</dt>'
    r'.*?'
    r'<dd><a href=".*?" class="u-concealed">(?P<number_of_reviews>.*?)</a></dd>',
    flags=re.DOTALL
)

vzorec_ocena = re.compile(
    r'<span class="u-srOnly">'
    r'(?P<mark>.*)star\(s\)</span>',
    flags=re.DOTALL

)

vzorec_ratings = re.compile(
    r'<span class="ratingStarsRow-text">\s*?'
    r'(?P<ratings>.*?)ratings?.*?</span>',
    flags=re.DOTALL
)


def izloci_podatke_putke(blok):
    putka = re.search(vzorec_putke, blok).groupdict()
    vrsta = string.capwords(putka['breed'].strip().replace('?','').replace('&#039;', '\' ' ).replace('&quot;',''))
    ok_vrsta = odstrani_reci_v_oklepajih(vrsta)
    putka['breed'] = ok_vrsta
    putka['link'] = 'https://www.backyardchickens.com' + putka['link']
    #Če je zabeležena ocena:
    ocena = vzorec_ocena.search(blok)
    if ocena:
        putka['mark'] = float(ocena['mark'])
    else:
        putka['mark'] = None
    #Če zabeležen rating:
    ratings = vzorec_ratings.search(blok)
    if ratings:
        putka['number of ratings'] = int(ratings['ratings'].strip())
    else: 
        putka['number of ratings'] = None
    #Če je število komentarjev zabeleženo.
    stevilo_komentarjev = vzorec_komentarjev.search(blok)
    if stevilo_komentarjev:
        putka['number of comments'] = int(stevilo_komentarjev['number_of_comments'])
    else: 
        putka['number of comments'] = None
    #Če je zabeleženo število reviewsov.
    number_of_reviews = vzorec_number_of_reviews.search(blok)
    if number_of_reviews:
        putka['number of reviews'] = int(number_of_reviews['number_of_reviews'])
    else: 
        putka['number of reviews'] = None
    # putka['kratek opis'] = putka['kratek_opis'].strip()
    try:
        del putka['about']
    except KeyError:
        pass
    return putka



def putke_na_strani(st_strani):
    url = (
    'https://www.backyardchickens.com/'
    'reviews/categories/chicken-breeds.2/'
    f'?page={st_strani}'
    )
    ime_datoteke = f'zajeti-podatki\\putke-stran-{st_strani}.html'
    orodja.shrani_spletno_stran(url, ime_datoteke)
    vsebina = orodja.vsebina_datoteke(ime_datoteke)
    for blok in vzorec_bloka.finditer(vsebina):
        yield izloci_podatke_putke(blok.group(0))

def zajemi_putko():
    for stran in range(1,11):
        count = 0
        for putka in putke_na_strani(stran):
            count += 1
            url = putka['link']
            vrsta = odstrani_reci_v_oklepajih(putka['breed'].replace('?',''))
            ime_datoteke = f'zajete-putke-po-vrstah\\{vrsta}.html'
            orodja.shrani_spletno_stran(url, ime_datoteke)


############################
#Vzorci za posamezno putko.#
############################

vzorec_breed_purpose = re.compile(
    r'<dt>Breed Purpose</dt>'
    r'.*?'
    r'<dd>\s*?'
    r'(?P<breed_purpose>.*?)'
    r'</dd>',
    flags=re.DOTALL
)

vzorec_comb = re.compile(
    r'<dt>Comb</dt>'
    r'.*?'
    r'<dd>\s*?'
    r'(?P<comb>.*?)'
    r'</dd>',
    flags=re.DOTALL
)

vzorec_broodiness = re.compile(
    r'<dt>Broodiness</dt>'
    r'.*?'
    r'<dd>\s*?'
    r'(?P<broodiness>.*?)'
    r'</dd>',
    flags=re.DOTALL
)

vzorec_climate_tolerance = re.compile(
    r'<dt>Climate Tolerance</dt>'
    r'.*?'
    r'<dd>\s*?'
    r'(?P<climate_tolerance>.*?)'
    r'</dd>',
    flags=re.DOTALL
)

vzorec_egg_productivity = re.compile(
    r'<dt>Egg Productivity</dt>'
    r'.*?'
    r'<dd>\s*?'
    r'(?P<egg_productivity>.*?)'
    r'</dd>',
    flags=re.DOTALL
)

vzorec_egg_size = re.compile(
    r'<dt>Egg Size</dt>'
    r'.*?'
    r'<dd>\s*?'
    r'(?P<egg_size>.*?)'
    r'</dd>',
    flags=re.DOTALL
)

vzorec_egg_colour = re.compile(
    r'<dt>Egg Color</dt>'
    r'.*?'
    r'<dd>\s*?'
    r'(?P<egg_colour>.*?)'
    r'</dd>',
    flags=re.DOTALL
)

vzorec_breed_temperament = re.compile(
    r'<dt>Breed Temperament</dt>'
    r'.*?'
    r'<dd>\s*?'
    r'(?P<breed_temperament>.*?)'
    r'</dd>',
    flags=re.DOTALL
)

vzorec_breed_colours = re.compile(
    r'<dt>Breed Colors/Varieties</dt>'
    r'.*?'
    r'<dd>\s*?'
    r'(?P<breed_colours>.*?)'
    r'</dd>',
    flags=re.DOTALL
)

vzorec_breed_size = re.compile(
    r'<dt>Breed Size</dt>'
    r'.*?'
    r'<dd>\s*?'
    r'(?P<breed_size>.*?)'
    r'</dd>',
    flags=re.DOTALL
)

vzorec_number_of_views = re.compile(
    r'<dt>Views</dt>'
    r'.*?'
	r'<dd>(?P<number_of_views>.*?)</dd>',
    flags=re.DOTALL
)



def podrobno_poglej_putko(vrsta):
    putka = {}
    with open(f'zajete-putke-po-vrstah\\{vrsta}.html', 'r', encoding='utf-8') as d:
        vsebina = d.read()
        #
        number_of_views = vzorec_number_of_views.search(vsebina)
        if number_of_views:
            ogledi = number_of_views['number_of_views'].strip()
            ok_ogledi = urejanje.uredi_views(ogledi)
            putka['number of views'] = int(ok_ogledi)
        else:
            putka['number of views'] = None
        breed_purpose = vzorec_breed_purpose.search(vsebina)
        if breed_purpose:
            namen = breed_purpose['breed_purpose'].strip().lower()
            ok_namen = urejanje.uredi_breed_purpose(namen)
            putka['breed purpose'] = ok_namen
        else:
            putka['breed purpose'] = None
        #
        comb = vzorec_comb.search(vsebina)
        if comb:
            greben = comb['comb'].strip().lower()
            ok_greben = urejanje.uredi_comb(greben)
            putka['comb'] = ok_greben
        else:
            putka['comb'] = None
        #
        broodiness = vzorec_broodiness.search(vsebina)
        if broodiness:
            broody = broodiness['broodiness'].lower()
            ok_broody = urejanje.uredi_broodiness(broody)
            putka['broodiness'] = ok_broody
        else:
            putka['broodiness'] = None
        #
        climate_tolerance = vzorec_climate_tolerance.search(vsebina)
        if climate_tolerance:
            tol = climate_tolerance['climate_tolerance'].strip().lower()
            ok_tol = urejanje.uredi_climate_tolerance(tol)
            putka['climate tolerance'] = ok_tol
        else:
            putka['climate tolerance'] = None
        #
        egg_productivity = vzorec_egg_productivity.search(vsebina)
        if egg_productivity:
            eggs = egg_productivity['egg_productivity'].strip().lower()
            ok_eggs = urejanje.uredi_egg_productivity(eggs)
            putka['egg productivity'] = ok_eggs
        else:
            putka['egg productivity'] = None
        #
        egg_size = vzorec_egg_size.search(vsebina)
        if egg_size:
            size = egg_size['egg_size'].strip().lower()
            ok_size = urejanje.uredi_egg_size(size)
            putka['egg size'] = ok_size
        else:
            putka['egg size'] = None
        #
        egg_colour = vzorec_egg_colour.search(vsebina)
        if egg_colour:
            barva = egg_colour['egg_colour'].strip().lower()
            ok_barva = urejanje.uredi_egg_colour(barva)
            putka['egg colour'] = ok_barva
        else:
            putka['egg colour'] = None
        #
        breed_temperament = vzorec_breed_temperament.search(vsebina)
        if breed_temperament:
            temp = breed_temperament['breed_temperament'].strip().lower()
            ok_temp = urejanje.uredi_temperament(temp)
            putka['breed temperament'] = ok_temp
        else:
            putka['breed temperament'] = None
        #
        breed_colours = vzorec_breed_colours.search(vsebina)
        if breed_colours:
            barva = breed_colours['breed_colours'].strip().lower()
            ok_barva = urejanje.uredi_breed_colour(barva)
            putka['breed colours'] = ok_barva
        else:
            putka['breed colours'] = None
        #
        breed_size = vzorec_breed_size.search(vsebina)
        if breed_size:
            size = breed_size['breed_size'].strip().lower()
            ok_size = urejanje.uredi_breed_size(size)
            putka['breed size'] = ok_size
        else:
            putka['breed size'] = None
    return putka
        
# a = podrobno_poglej_putko('Silkie')


#pomozni funkciji
def odstrani_reci_v_oklepajih(string):
    nov = ''
    count = 0
    for znak in string:
        if znak == '(':
                count += 1
        if count > 0:
            if znak == ')':
                count -= 1
        elif count == 0:
                nov += znak
    return nov

def merge_two_dicts(x, y):
    z = x.copy()   # start with x's keys and values
    z.update(y)    # modifies z with y's keys and values & returns None
    return z


def izloci_gnezdene_podatke(putke):
    egg_colour, temperament, breed_colour = [], [], []
    for putka in putke:
        if putka['egg colour'] == None:
            putka.pop('egg colour')
            egg_colour.append({'breed': putka['breed'], 'egg colour': None})
        else:
            for jajce in putka.pop('egg colour'):
                egg_colour.append({'breed': putka['breed'], 'egg colour': jajce})
        if putka['breed temperament'] == None:
            putka.pop('breed temperament')
            temperament.append({'breed': putka['breed'], 'temperament': None})
        else:
            for temp in putka.pop('breed temperament'):
                temperament.append({'breed': putka['breed'], 'temperament': temp})
        if putka['breed colours'] == None:
            breed_colour.append({'breed': putka['breed'], 'breed colour': None})
            putka.pop('breed colours')
        else:
            for barva in putka.pop('breed colours'):
                breed_colour.append({'breed': putka['breed'], 'breed colour': barva})
    
    egg_colour.sort(key=lambda putka: (putka['breed'], putka['egg colour']))
    temperament.sort(key=lambda putka: (putka['breed'], putka['temperament']))
    breed_colour.sort(key=lambda putka: (putka['breed'], putka['breed colour']))

    return egg_colour, temperament, breed_colour

  
# putke = []
# zajemi_putko()
# for st_strani in range(1,11):
#     for putka in putke_na_strani(st_strani):
#         vrsta = putka['breed']
#         dodaten_slovar = podrobno_poglej_putko(vrsta)
#         nova_putka = merge_two_dicts(putka, dodaten_slovar)
#         putke.append(nova_putka)
# putke.sort(key=lambda putka: putka['breed'])
# orodja.zapisi_json(putke,'obdelani-podatki\\putke.json')
with open('obdelani-podatki\\putke.json') as d:
    putke = json.load(d)

egg_colour, temperament, breed_colour = izloci_gnezdene_podatke(putke)
orodja.zapisi_csv(
    putke,
    ["link", "breed","mark","number of ratings","number of comments","number of reviews","number of views","breed purpose","comb","broodiness","climate tolerance", "egg productivity","egg size","breed size"], 
    'obdelani-podatki\\putke.csv'
)
orodja.zapisi_csv(egg_colour, ['breed', 'egg colour'], 'obdelani-podatki\\barva_jajc.csv')
orodja.zapisi_csv(temperament, ['breed', 'temperament'], 'obdelani-podatki\\temperament.csv')
orodja.zapisi_csv(breed_colour, ['breed', 'breed colour'], 'obdelani-podatki\\barva_vrste.csv')