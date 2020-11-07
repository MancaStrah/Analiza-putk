# Funkcije, ki vzamejo lastnost, zajeto s htmlja, in
# jo uredijo (npr. če ima neka lastnost več različnih
# poimenovanj (npr. velikost jajc: 'large, 'big'), se 
# tukaj združijo v eno skupno ime za lažjo analizo podatkov)

# Problem je, da na to stran uporabniki sami vnesejo podatke
# o vrstah, in zato niso konsistentni.


def uredi_views(ogledi):
    '''Odstrani ločila iz niza in ohrani samo številke'''
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
        purpose.append('eggs')
        purpose.append('meat')
    if 'egg' in breed_purpose:
        if 'eggs' not in purpose:
            purpose.append('eggs')
    if 'meat' in breed_purpose:
        if 'meat' not in purpose:
            purpose.append('meat')
    if 'ornament' in breed_purpose:
        purpose.append('ornamental')
    if 'pet' in breed_purpose:
        purpose.append('pet')
    if len(purpose) == 0:
        return None
    else:
        return purpose

def uredi_comb(comb):
    greben = []
    if 'any' in comb:
        greben.append('any')
    else: 
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
    if len(greben) == 0:
        return None
    else:
        return greben


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
    elif any(beseda in egg_productivity for beseda in ['medium', 'average' , 'fair']):
        eggs.append('medium')
    elif any(beseda in egg_productivity for beseda in ['low', 'poor', 'bad']):
        eggs.append('low')
    return vrni_pravilno(eggs)

def uredi_egg_size(egg_size):
    size = []
    if any(beseda in egg_size for beseda in ['large', 'big']):
        size.append('large')
    elif any(beseda in egg_size for beseda in ['average', 'medium']):
        size.append('medium')
    elif any(beseda in egg_size for beseda in ['small']):
        size.append('small')
    return vrni_pravilno(size)

def uredi_egg_colour(egg_colour):
    barve = [
        'beige', 'black', 'blue', 'brown', 'copper',
        'cream', 'gold', 'gray', 'green', 'lavender',
        'maroon', 'olive', 'orange', 'peach', 'pink',
        'porcelain' , 'red', 'salmon', 'silver', 'tan',
        'white', 'yellow'
    ]
    colour = []
    for barva in barve:
        if barva in egg_colour.lower():
            colour.append(barva)
    if len(colour) == 0:
        return None
    else: 
        return colour

def uredi_temperament(temperament):
    temp = []
    if any(beseda in temperament for beseda in ['agressive', 'wild', 'flight']):
        temp.append('agressive')
    if any(beseda in temperament for beseda in ['lively', 'curious', 'alert', 'funny', 'moderate', 'noisy', 'active']):
        temp.append('lively')
    if any(beseda in temperament for beseda in ['calm', 'shy', 'quiet']):
        temp.append('calm')
    if any(beseda in temperament for beseda in ['docile', 'easily', 'handle']):
        temp.append('docile')
    if any(beseda in temperament for beseda in ['good', 'kind', 'pet', 'friend']):
        temp.append('friendly')
    if len(temp) == 0:
        return None
    else: 
        return temp

def uredi_breed_colour(breed_colour):
    colour = []
    if 'any' in breed_colour or 'variety' in breed_colour or 'all' in breed_colour:
        colour.append('any')
    else:
        barve = [
        'beige', 'black', 'blue', 'brown', 'copper',
        'cream', 'gold', 'gray', 'green', 'lavender',
        'maroon', 'olive', 'orange', 'peach', 'pink',
        'porcelain' , 'red', 'salmon', 'silver', 'tan',
        'white', 'yellow'
        ]  
        for barva in barve:
            if barva in breed_colour:
                colour.append(barva)
        if 'cuckoo' in breed_colour:
            if 'black' not in colour:
                colour.append('black')
            if 'white' not in colour:
                colour.append('white')
        if 'dark' in breed_colour:
            if 'brown' not in colour:
                colour.append('brown')
        if 'tinted' in breed_colour:
            if 'cream' not in colour:
                colour.append('cream')
    if len(colour) == 0:
        return None
    else: 
        return colour

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
    if any(beseda in tolerance for beseda in ['all', 'average', 'depend', 'fair', 'good', 'most']):
        tol.append('any')
    elif 'hard' in tolerance or 'bad' in tolerance:
        if (beseda in tolerance for beseda in ['heat', 'hot', 'warm']):
            tol.append('colder better')
        elif 'cold' in tolerance:
            tol.append('warmer better')
    elif any(beseda in tolerance for beseda in ['heat', 'hot', 'warm']):
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





