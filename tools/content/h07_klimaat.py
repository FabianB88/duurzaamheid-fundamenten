# -*- coding: utf-8 -*-
"""Klimaat: het broeikaseffect, het koolstofbudget en waar de uitstoot vandaan komt."""


def bouw(p):
    p.tekst(
        'Eerst de natuurkunde, dan de discussie',
        '<p>Over klimaat wordt veel gediscussieerd, maar het mechanisme eronder is '
        'niet ingewikkeld. Als je dat helder hebt, kun je de meeste beweringen zelf '
        'wegen — en dat is precies wat dit hoofdstuk je moet opleveren.</p>'
        '<p>Het <b>broeikaseffect</b> is om te beginnen een natuurlijk en '
        'noodzakelijk verschijnsel. Gassen als koolstofdioxide (CO₂), methaan (CH₄) en '
        'lachgas (N₂O) houden warmte vast in de atmosfeer. Zonder dat effect zou de '
        'gemiddelde temperatuur op aarde ver onder het vriespunt liggen in plaats van '
        'rond de vijftien graden. Het broeikaseffect is dus niet het probleem.</p>'
        '<p>Het probleem is de <b>versterking</b> ervan. Door fossiele brandstoffen te '
        'verbranden, bossen te kappen en intensief landbouw te bedrijven, neemt de '
        'concentratie van die gassen toe. Er wordt meer warmte vastgehouden, en de '
        'gemiddelde temperatuur stijgt. De gevolgen zien we inmiddels ook hier: '
        'wateroverlast, hittegolven, droogte, bodemdaling.</p>')

    p.tekst(
        'Het koolstofbudget: hoeveel er nog in past',
        '<p>Het <b>koolstofbudget</b> is de hoeveelheid CO₂ die er nog uitgestoten kan '
        'worden voordat de opwarming een bepaalde grens passeert — bijvoorbeeld 1,5 of '
        '2 graden. Het is de meest bruikbare vertaling van klimaatwetenschap naar '
        'beleid, omdat het van een abstract probleem een <b>rekensom met een restant</b> '
        'maakt.</p>'
        '<p>En het maakt iets zichtbaar dat in een discussie over doelen vaak '
        'wegvalt: het budget is eindig en het loopt door. Hoe langer de uitstoot hoog '
        'blijft, hoe kleiner het restant en hoe drastischer de maatregelen later '
        'moeten zijn. Uitstel is geen neutrale keuze — het verplaatst de rekening en '
        'maakt hem groter.</p>')

    p.video(
        'Klimaatverandering in drie blokken van tien minuten',
        '<p>NOS op 3 legt klimaatverandering uit in drie delen: het verleden, het '
        'heden en de toekomst. Wil je alleen de kern, begin dan op minuut tien — dan '
        'kijk je twintig minuten. Dit is de enige lange video in deze cursus, en hij '
        'is het waard.</p>',
        aanbieder='youtube', bron='xRLbCYK_7fc',
        titel='Klimaatverandering in 3x10 minuten — NOS op 3',
        duur='32 minuten, Nederlandstalig')

    p.tekst(
        'Waar komt de uitstoot vandaan?',
        '<p>Niet elke sector draagt evenveel bij. Maar let op: <b>de indeling in '
        'sectoren is deels een keuze</b>, geen natuurgegeven. Valt de uitstoot van een '
        'product bij de fabrikant of bij de consument? Reken je de stroom voor een '
        'fabriek toe aan "energie" of aan "industrie"? Er bestaan overzichten waarin '
        'ruim 85 procent onder "energie" valt, en andere waarin diezelfde uitstoot '
        'over vier sectoren is verdeeld.</p>'
        '<p>Dat is precies de systeemgrens uit hoofdstuk 1, nu toegepast op '
        'statistiek. Vraag bij elk overzicht: <i>wie heeft deze indeling gemaakt, en '
        'wat valt er onder welke noemer?</i></p>')

    p.accordeon(
        'Vier sectoren, en waar de winst zit',
        '<p>Met die kanttekening over de indeling in het achterhoofd.</p>',
        [
            {'title': 'Energie',
             'body': '<p>Wereldwijd een van de grootste bronnen, vooral door '
                     'steenkool, olie en gas voor elektriciteit. Naast klimaateffecten '
                     'ook een gezondheidsvraagstuk, via luchtvervuiling.</p>'
                     '<p><b>Winst zit in:</b> de overstap naar zon en wind, plus '
                     'energiebesparing en opslag. Dit is de sector waar de transitie '
                     'het verst is — en waar hij nu vastloopt op het net. Hoofdstuk '
                     '8.</p>'},
            {'title': 'Industrie',
             'body': '<p>Energie-intensieve processen als staal- en '
                     'cementproductie. Tegelijk de motor van veel innovatie.</p>'
                     '<p><b>Winst zit in:</b> elektrificatie, circulaire grondstoffen '
                     'en alternatieve materialen — gerecycled staal, biobased '
                     'bouwmateriaal. Hier komt hoofdstuk 5 en 6 direct van pas.</p>'},
            {'title': 'Landbouw en voedsel',
             'body': '<p>Vooral methaan en lachgas, uit veeteelt en kunstmest. Raakt '
                     'meteen aan de stikstofgrens uit hoofdstuk 4 — dezelfde '
                     'activiteit, twee verschillende planetaire grenzen.</p>'
                     '<p><b>Winst zit in:</b> precisielandbouw, agroforestry en het '
                     'tegengaan van voedselverspilling. Dat laatste is de goedkoopste '
                     'maatregel die er is: voedsel dat niet wordt weggegooid, hoeft '
                     'niet geproduceerd te worden.</p>'},
            {'title': 'Transport en mobiliteit',
             'body': '<p>Wegverkeer, luchtvaart en scheepvaart samen goed voor een '
                     'groot deel van de wereldwijde uitstoot.</p>'
                     '<p><b>Winst zit in:</b> elektrisch rijden, gedeelde mobiliteit, '
                     'en vooral in ruimtelijke keuzes — een stad waarin je niet hoeft '
                     'te rijden, verslaat elke schone auto.</p>'},
        ])

    p.aandacht(
        'De vraag die je bij elk klimaatcijfer stelt',
        '<p><b>Waarover gaat dit getal precies, en waarmee wordt het vergeleken?</b> '
        'Een bedrijf dat "50 procent minder uitstoot" meldt, kan bedoelen: per product, '
        'per euro omzet, of in absolute zin. Dat zijn drie verschillende beweringen, '
        'en alleen de laatste betekent dat er daadwerkelijk minder CO₂ de lucht in '
        'gaat.</p>'
        '<p>Groeit een bedrijf harder dan het verduurzaamt, dan daalt de uitstoot per '
        'product en stijgt hij in totaal. Beide cijfers zijn waar. Alleen het tweede '
        'telt voor het koolstofbudget.</p>')

    p.tekst(
        'Stappenplan: de klimaatimpact van een keuze inschatten',
        '<p>Je hoeft geen klimaatwetenschapper te zijn om een verstandige inschatting '
        'te maken. Vijf stappen.</p>'
        '<ol>'
        '<li><b>Bepaal wat je vergelijkt.</b> Niet "is dit duurzaam", maar "is dit '
        'beter dan wát?" Zonder alternatief is er geen oordeel mogelijk.</li>'
        '<li><b>Kies je systeemgrens en schrijf hem op.</b> Alleen gebruik, of ook '
        'productie en afdanking? Terug naar hoofdstuk 1.</li>'
        '<li><b>Zoek de grootste post.</b> In vrijwel elke keten zit tachtig procent '
        'van de impact in één of twee stappen. Zoek die eerst; de rest is '
        'ruis.</li>'
        '<li><b>Reken absoluut, niet relatief.</b> Hoeveel ton CO₂ per jaar, niet '
        'hoeveel procent minder per eenheid.</li>'
        '<li><b>Vraag je af of het verschuift.</b> Wordt de uitstoot echt minder, of '
        'verhuist hij naar een leverancier, een ander land of een andere sector?</li>'
        '</ol>')

    p.invulvelden(
        'Oefening: één keuze doorrekenen',
        '<p>Neem een keuze die in je organisatie speelt of net gemaakt is. Bijvoorbeeld '
        'een reisbeleid, een inkoopkeuze of een verbouwing.</p>',
        [
            ('h07-keuze', 'Welke keuze neem je onder de loep?', ''),
            ('h07-vergelijk', 'Waarmee vergelijk je? Wat is het alternatief?',
             'Zonder alternatief is er geen oordeel'),
            ('h07-grens', 'Welke systeemgrens hanteer je?',
             'Alleen gebruik, of ook productie en afdanking?'),
            ('h07-grootste', 'Waar zit de grootste post in de keten?',
             'Meestal zit 80 procent in één of twee stappen'),
            ('h07-absoluut', 'Wat is de absolute uitkomst, ruwweg?',
             'Ton CO₂ per jaar; een orde van grootte is genoeg'),
            ('h07-schuif', 'Verdwijnt de uitstoot, of verschuift hij?',
             'Naar een leverancier, een land of een sector'),
        ])

    p.knoppenrij('Meenemen', '<p>Deze inschatting gebruik je in hoofdstuk 9 bij je onderbouwing.</p>')

    p.vraag(
        'Even checken',
        'Een bedrijf meldt trots dat de CO₂-uitstoot per product met veertig procent is '
        'gedaald. Wat moet je nog weten voordat je dit als goed nieuws telt?',
        [
            ('Of de absolute uitstoot ook gedaald is — bij voldoende groei kan die '
             'ondanks de daling per product zijn gestegen.', True),
            ('Of het bedrijf gecertificeerd is.', False),
            ('Of er ook naar water en afval wordt gekeken.', False),
            ('Niets — veertig procent minder is altijd goed nieuws.', False),
        ],
        feedback={
            'title': 'Even checken',
            'correct': '<p>Precies. Voor het koolstofbudget telt alleen de absolute '
                       'uitstoot. Een daling per eenheid is nuttige informatie over '
                       'efficiëntie, maar zegt niets over hoeveel CO₂ er werkelijk de '
                       'lucht in gaat.</p>',
            '_incorrect': {'final': '<p>Nog niet. Certificaten en andere thema’s zijn '
                                    'op zichzelf relevant, maar hier gaat het om iets '
                                    'anders: relatief versus absoluut. Groei kan een '
                                    'daling per product volledig opeten.</p>'},
            '_partlyCorrect': {'final': '<p>Nog niet helemaal.</p>'}
        })
