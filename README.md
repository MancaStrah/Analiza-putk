# Analiza putk

Projektna naloga z naslovom "Analiza putk" za predmet Programiranje 1 v 2. letniku študija matematike na FMF.

## Podatki:
Analizirala bom podatke o kokošjih vrstah, njihovih lastnostih in priljubljenosti. Te podatke sem zajela s spletne strani [BackYard Chickens](https://www.backyardchickens.com/reviews/categories/chicken-breeds.2/).

Za vsako kokošjo vrsto sem zajela:
- ime vrste;
- oceno, število ocen, število ogledov, število komentarjev vrste;
- namen vzreje vrste;
- velikost, barvo in količino jajc;
- temperament, velikost in barvo vrste;
- obliko grebena;
- podnebno toleranco,
- tendenco gnezdenja (sedenja na jajcu in skrbi zanj).

V mapi `obdelani-podatki` se nahaja json datoteka, kjer so zapisani vsi zajeti podatki za posamezno vrsto kokoši, poleg tega pa so tam še csv datoteke - ena (`putke.csv`) vsebuje vse razen gnezdenih podatkov za posamezno vrsto. Podatki, kjer več vrednosti pripada isti vrsti (namen vzreje, barva vrste, barva jajc, oblika grebena in temperament), pa so zapisani v svojih csv datotekah.
Podatke sem zajela s funkcijami, zapisanimi v datoteki `zajemi-in-analiziraj-putko.py`, uporabila pa sem tudi knjižnici `orodja.py` in `urejanje.py`. 

## Hipoteze:
Hipoteze bom razdelila glede to, ali se nanašajo na kokoši same (torej na lastnosti kokoši) ali na njihovo priljubljenost (torej na odzive uporabnikov te spletne strani nanje).

- Največ ogledov imajo vrste, ki jih vzrejajo predvsem zaradi jajc.
- Večina najbolje ocenjenih kokoši je nesnic.

- Ornamentalne kokoši ležejo manjša jajca in to počnejo redkeje.
- Kokoši, ki jih vzrejajo tako za meso kot tudi za jajca, so večje od tistih, ki jih vzrejajo le za jajca.
- Večina kokoši ima greben v obliki lista. 

[<img src="https://www.backyardchickens.com/reviews/sebright.10870/cover-image">](https://www.backyardchickens.com/)

