# Funkcije, ki vzamejo lastnost, zajeto s htmlja, in
# jo uredijo (npr. če ima neka lastnost več različnih
# poimenovanj (npr. velikost jajc: 'large, 'big'), se 
# tukaj združijo v eno skupno za lažjo analizo podatkov)


def uredi_views(ogledi):
    ok_ogledi = ''
    for znak in ogledi:
        if znak in '0123456789':
            ok_ogledi += znak
    return ok_ogledi

def uredi_breed_purpose(breed_purpose):
    purpose = []
    if 'brooding' in breed_purpose:
        purpose.append('brooding')
    if 'dual' in breed_purpose or 'duel' in breed_purpose:
        purpose.append('dual purpose')
    if 'egg' in breed_purpose:
        purpose.append('eggs')
    if 'meat' in breed_purpose:
        purpose.append('meat')
    if 'ornament' in breed_purpose:
        purpose.append('ornamental')
    if 'pet' in breed_purpose:
        purpose.append('pet')
    if purpose == ['eggs', 'meat'] or purpose == ['meat', 'eggs']:
        purpose = ['dual purpose']
    return vrni_pravilno(purpose)

def uredi_comb(comb):
    greben = []
    if 'any' in comb:
        greben.append('any')
    if 'buttercup' in comb:
        greben.append('buttercup')
    if 'cushion' in comb:
        greben.append('cushion')
    if 'pea' in comb:
        greben.append('pea')
    if 'rose' in comb:
        greben.append('rose')
    if 'single' in comb:
        greben.append('single')
    if 'strawberry ' in comb:
        greben.append('strawberry')
    if 'v-shaped' in comb:
        greben.append('v-shaped')
    if 'walnut' in comb:
        greben.append('walnut')
    return vrni_pravilno(greben)

def uredi_broodiness(broodiness):
    broody = None
    if any(beseda in broodiness for beseda in ['very', 'frequent', 'extreme', 'often']):
        broody = 'frequent'
    elif any(beseda in broodiness for beseda in ['average', 'moderate']):
        broody = 'average'
    elif any(beseda in broodiness for beseda in ['non', 'poor']):
        broody = 'poor'
    elif any(beseda in broodiness for beseda in ['occasional', 'rare', 'seldom', 'depends']):
        broody = 'rare'
    return broody


def uredi_egg_productivity(egg_productivity):
    eggs = []
    if any(beseda in egg_productivity for beseda in ['excellent', 'good', 'high']):
        eggs.append('high')
    if any(beseda in egg_productivity for beseda in ['medium', 'fair']):
        eggs.append('medium')
    if any(beseda in egg_productivity for beseda in ['low', 'poor']):
        eggs.append('low')
    return vrni_pravilno(eggs)

def uredi_egg_size(egg_size):
    size = []
    if any(beseda in egg_size for beseda in ['large', 'big']):
        size.append('large')
    if any(beseda in egg_size for beseda in ['average', 'medium']):
        size.append('medium')
    if any(beseda in egg_size for beseda in ['small']):
        size.append('small')
    return vrni_pravilno(size)

def uredi_egg_colour(egg_colour):
    colour = []
    if 'blue' in egg_colour:
        colour.append('blue')
    if 'green' in egg_colour:
        colour.append('green')
    if 'brown' in egg_colour:
        colour.append('brown')
    if 'cream' in egg_colour:
        colour.append('cream')
    if 'tan' in egg_colour:
        colour.append('tan')
    if 'white' in egg_colour:
        colour.append('white')
    if 'olive' in egg_colour:
        colour.append('olive')
    if 'pink' in egg_colour:
        colour.append('pink')
    return vrni_pravilno(colour)

def uredi_temperament(temperament):
    temp = []
    if any(beseda in temperament for beseda in ['agressive', 'wild', 'flighty']):
        temp.append('agressive')
    if any(beseda in temperament for beseda in ['lively', 'curious','alert','moderate','noisy', 'active']):
        temp.append('lively')
    if any(beseda in temperament for beseda in ['calm', 'shy', 'quiet']):
        temp.append('calm')
    if any(beseda in temperament for beseda in ['docile', 'easily', 'handle']):
        temp.append('docile')
    if any(beseda in temperament for beseda in ['good', 'kind', 'friend']):
        temp.append('friendly')
    return vrni_pravilno(temp)

def uredi_breed_colour(breed_colour):
    colour = []
    if 'red' in breed_colour:
        colour.append('red')
    if 'white' in breed_colour:
        colour.append('white')
    if 'black' in breed_colour or 'tinted' in breed_colour:
        colour.append('black')
    if 'blue' in breed_colour:
        colour.append('blue')
    if 'silver' in breed_colour:
        colour.append('silver')
    if 'cuckoo' in breed_colour:
        colour.append('black')
        colour.append('white')
    if 'dark' in breed_colour:
        colour.append('brown')
    if 'yellow' in breed_colour:
        colour.append('yellow')
    if 'cream' in breed_colour:
        colour.append('cream')
    if 'orange' in breed_colour:
        colour.append('orange')
    if 'porcelain' in breed_colour:
        colour.append('porcelain')
    if 'salmon' in breed_colour:
        colour.append('salmon')
    if 'any' in breed_colour or 'variety' in breed_colour:
        colour.append('any')
    return vrni_pravilno(colour)

def uredi_breed_size(breed_size):
    size = []
    if any(beseda in breed_size for beseda in ['heavy', 'large']):
        size.append('large')
    elif any(beseda in breed_size for beseda in ['bantam', 'small']):
        size.append('small')
    elif any(beseda in breed_size for beseda in ['medium', 'any']):
        size.append('medium')
    return vrni_pravilno(size)

def uredi_climate_tolerance(tolerance):
    tol = []
    if any(beseda in tolerance for beseda in ['all', 'average', 'depend','fair', 'good', 'most']):
        tol.append('any')
    if 'hard' in tolerance:
        if (beseda in tolerance for beseda in ['heat', 'hot']):
            tol.append('colder better')
        elif 'cold' in tolerance:
            tol.append('warmer better')
    elif any(beseda in tolerance for beseda in ['heat', 'hot']):
            tol.append('warmer better')
    elif 'cold' in tolerance:
        tol.append('colder better')
    return vrni_pravilno(tol)

def vrni_pravilno(seznam):

    if len(seznam) == 1:
        return seznam[0]
    if len(seznam) == 0:
        return None
    else:
        return seznam





