# -*- coding: utf-8 -*-
"""De aarde als systeem: vier sferen die op elkaar inwerken."""


def bouw(p):
    p.tekst(
        'Eén systeem, vier sferen',
        '<p>De aarde functioneert als één samenhangend systeem. Om erover te kunnen '
        'praten, verdelen wetenschappers het in vier <b>sferen</b>: de lithosfeer, de '
        'hydrosfeer, de atmosfeer en de biosfeer. Die verdeling is een hulpmiddel, '
        'geen werkelijkheid — in de praktijk lopen ze voortdurend in elkaar over.</p>'
        '<p>Juist dat overlopen is het punt. Een ingreep in de ene sfeer komt altijd '
        'ergens anders naar boven. Stikstof uit de landbouw begint in de lithosfeer '
        '(bodem), reist door de hydrosfeer (grondwater), belandt in de atmosfeer '
        '(ammoniak) en slaat neer in de biosfeer, waar zeldzame planten verdwijnen. '
        'Eén stof, vier sferen.</p>')

    p.beeld(
        'vier-sferen.svg',
        alt='Vier concentrische ringen die het aardsysteem tonen. Van buiten naar '
            'binnen: de atmosfeer, de luchtlaag die klimaat reguleert en tegen '
            'straling beschermt; de hydrosfeer, al het water in vloeibare, vaste en '
            'gasvorm; de lithosfeer, de aardkorst met gesteente, mineralen en bodem; '
            'en de biosfeer, al het leven, die als enige de andere drie doorsnijdt. '
            'Pijlen tussen de ringen geven aan dat stoffen en energie voortdurend van '
            'de ene sfeer naar de andere bewegen, met stikstof als voorbeeld dat door '
            'alle vier heen gaat.',
        onderschrift='De indeling is een hulpmiddel; in werkelijkheid lopen de sferen '
                     'in elkaar over.')

    p.accordeon(
        'De vier sferen',
        '<p>Klap ze open. Let bij elke sfeer op de laatste alinea: daar staat waar '
        'menselijk handelen ingrijpt.</p>',
        [
            {'title': 'Biosfeer — al het leven',
             'body': '<p>Planten, dieren, micro-organismen en hun ecosystemen. De '
                     'biosfeer houdt natuurlijke kringlopen in stand, zoals de '
                     'koolstofcyclus waarin planten CO₂ opnemen en zuurstof '
                     'vrijgeven.</p>'
                     '<p>De biosfeer legt koolstof vast en reguleert daarmee het '
                     'klimaat. Biodiversiteit is dus niet alleen mooi om te hebben — '
                     'het is de reden dat landbouw, visserij en '
                     'medicijnontwikkeling werken.</p>'},
            {'title': 'Atmosfeer — de lucht',
             'body': '<p>De luchtlaag rond de aarde: stikstof, zuurstof, CO₂, '
                     'waterdamp. Ze reguleert het klimaat en beschermt tegen '
                     'schadelijke straling.</p>'
                     '<p>Broeikasgassen houden warmte vast en maken de aarde '
                     'bewoonbaar. Door fossiele brandstoffen te verbranden nemen die '
                     'gassen toe, en verschuift het evenwicht. Daarover gaat '
                     'hoofdstuk 7.</p>'},
            {'title': 'Hydrosfeer — al het water',
             'body': '<p>Oceanen, zeeën, rivieren, meren, grondwater, ijs en '
                     'waterdamp. Water stuurt weerpatronen en is onmisbaar voor '
                     'voedselproductie, energie en transport.</p>'
                     '<p>Schoon en bereikbaar water houden is een van de grootste '
                     'opgaven van deze eeuw — vervuiling en klimaatverandering werken '
                     'hier tegelijk op in.</p>'},
            {'title': 'Lithosfeer — korst en bodem',
             'body': '<p>De aardkorst en de bovenste laag van de mantel: gesteente, '
                     'mineralen en bodem. De basis voor ecosystemen en voor landbouw, '
                     'mijnbouw en bouw.</p>'
                     '<p>Hieruit komen metalen, brandstoffen en bouwmaterialen. Het is '
                     'ook de sfeer die het traagst herstelt: een uitgeputte bodem of '
                     'een leeggehaalde mijn komt niet binnen een mensenleven '
                     'terug.</p>'},
        ])

    p.aandacht(
        'Waarom dit meer is dan aardrijkskunde',
        '<p>Zodra je een maatregel beoordeelt, is de vraag: <b>in welke sfeer grijp ik '
        'in, en waar komt het eruit?</b> Een luchtwasser in een stal verplaatst '
        'stikstof: de ammoniak komt niet in de lucht terecht, maar in het spuiwater '
        'dat erbij ontstaat. Biobrandstof verplaatst uitstoot '
        'van de atmosfeer naar landgebruik in de lithosfeer en biosfeer.</p>'
        '<p>Dat is geen argument om niets te doen. Het is een argument om te weten '
        'waar je het naartoe schuift, zodat je het bewust doet in plaats van per '
        'ongeluk.</p>')

    p.tekst(
        'Stappenplan: de sferen aflopen bij een maatregel',
        '<p>Kost tien minuten en voorkomt de klassieke verplaatsingsfout.</p>'
        '<ol>'
        '<li><b>Benoem in welke sfeer de maatregel aangrijpt.</b> Waar raak je het '
        'systeem als eerste aan?</li>'
        '<li><b>Volg de stof of de energie.</b> Wat gaat er ergens in, en waar komt '
        'het weer uit? Schrijf de route op, ook als je onzeker bent.</li>'
        '<li><b>Loop de andere drie sferen langs.</b> Gebeurt daar iets, positief of '
        'negatief? Zet bij elke sfeer minstens één zin.</li>'
        '<li><b>Kijk naar de tijdschaal per sfeer.</b> De atmosfeer reageert in jaren, '
        'de hydrosfeer in decennia, de lithosfeer in eeuwen. Een snelle winst in de '
        'ene sfeer kan een traag verlies in de andere zijn.</li>'
        '<li><b>Noteer wat je niet weet.</b> Dat is geen zwakte van je analyse maar '
        'een onderdeel ervan — en het vertelt je waar je iemand met meer verstand van '
        'zaken bij moet halen.</li>'
        '</ol>')

    p.invulvelden(
        'Oefening: volg de stof',
        '<p>Neem een concrete maatregel — uit je eigen vraagstuk, of anders: '
        '"we vervangen alle plastic bekers door kartonnen".</p>',
        [
            ('h03-maatregel', 'Welke maatregel neem je onder de loep?',
             'Iets concreets en afgebakends'),
            ('h03-aangrijp', 'In welke sfeer grijpt hij aan?',
             'Lithosfeer, hydrosfeer, atmosfeer of biosfeer'),
            ('h03-route', 'Volg de stof of energie: waar gaat het heen?',
             'Schrijf de route op, ook bij onzekerheid'),
            ('h03-andere', 'Wat gebeurt er in de andere drie sferen?',
             'Minstens één zin per sfeer'),
            ('h03-tijd', 'Op welke tijdschaal spelen die effecten?',
             'Jaren, decennia of eeuwen'),
            ('h03-onbekend', 'Wat weet je niet, en wie zou dat wel weten?',
             'Onwetendheid benoemen hoort bij de analyse'),
        ])

    p.knoppenrij('Meenemen', '<p>Bewaar je route; in het volgende hoofdstuk leg je hem naast de planetaire grenzen.</p>')

    p.vraag(
        'Even checken',
        'Wat gebeurt er met mensen als de hydrosfeer verstoord raakt, bijvoorbeeld '
        'doordat zoetwaterbronnen vervuild raken?',
        [
            ('Tekort aan schoon drinkwater, gezondheidsproblemen en economische '
             'schade — de verstoring loopt door naar de andere sferen en naar de '
             'samenleving.', True),
            ('Alleen een afname van biodiversiteit, zonder directe gevolgen voor '
             'mensen.', False),
            ('Alleen effecten in de atmosfeer, niet in menselijke activiteiten.', False),
            ('De biosfeer stopt volledig met functioneren.', False),
        ],
        feedback={
            'title': 'Even checken',
            'correct': '<p>Klopt. En let op het patroon: de verstoring blijft niet in '
                       'één sfeer. Water raakt gezondheid, landbouw en economie — '
                       'precies de samenhang uit het vorige hoofdstuk.</p>',
            '_incorrect': {'final': '<p>Nog niet. Het idee dat een verstoring binnen '
                                    'één sfeer blijft, is precies de denkfout die de '
                                    'sferen-indeling zichtbaar maakt. Water raakt '
                                    'alles.</p>'},
            '_partlyCorrect': {'final': '<p>Nog niet helemaal.</p>'}
        })
