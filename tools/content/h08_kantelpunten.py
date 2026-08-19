# -*- coding: utf-8 -*-
"""Kantelpunten, feedbackloops en de energietransitie in Nederland."""


def bouw(p):
    p.tekst(
        'Waarom het klimaat niet netjes geleidelijk reageert',
        '<p>Het is verleidelijk om je klimaatverandering voor te stellen als een '
        'schuifregelaar: meer uitstoot, meer opwarming, en als je terugdraait gaat het '
        'weer de andere kant op. Zo werkt het niet, en dat komt door twee mechanismen '
        'die je moet kennen om de urgentie te begrijpen.</p>')

    p.beeld(
        'feedbackloops.svg',
        alt='Twee cirkelvormige schema’s naast elkaar. Links een versterkende lus: '
            'opwarming leidt tot het smelten van ijs, waardoor donker oceaanwater meer '
            'zonlicht opneemt, waardoor de opwarming toeneemt en de lus zichzelf '
            'aandrijft. Rechts een dempende lus: opwarming leidt tot meer '
            'plantengroei en opname van CO₂ door oceanen, waardoor de opwarming iets '
            'wordt afgeremd. Onder de twee lussen een lijn die geleidelijk stijgt en '
            'dan abrupt omslaat, met daarbij de tekst kantelpunt: het moment waarop '
            'een systeem in een nieuwe toestand terechtkomt die niet vanzelf '
            'terugkeert.',
        onderschrift='Versterkende lussen jagen verandering aan, dempende remmen af. '
                     'Bij een kantelpunt slaat het systeem om.')

    p.accordeon(
        'Drie mechanismen',
        '<p>Deze drie verklaren waarom klimaatverandering zich anders gedraagt dan een '
        'schuifregelaar.</p>',
        [
            {'title': 'Positieve feedback — de versterker',
             'body': '<p>Een verandering veroorzaakt processen die diezelfde '
                     'verandering vergroten. Als permafrost ontdooit, komt methaan '
                     'vrij, een krachtig broeikasgas dat de opwarming versnelt, '
                     'waardoor er meer permafrost ontdooit.</p>'
                     '<p>Zo ook het albedo-effect: ijs weerkaatst zonlicht, maar zodra '
                     'het smelt neemt donker oceaanwater de warmte juist op. '
                     '"Positief" betekent hier zichzelf versterkend, niet '
                     'gunstig.</p>'},
            {'title': 'Negatieve feedback — de rem',
             'body': '<p>Processen die veranderingen dempen en het systeem stabiel '
                     'houden. Oceanen en planten nemen een deel van de CO₂ op; bij '
                     'hogere temperaturen ontstaat soms extra bewolking die zonlicht '
                     'weerkaatst.</p>'
                     '<p>Die remmen bestaan echt, maar ze zijn op dit moment niet '
                     'krachtig genoeg om de snelheid van de menselijke invloed bij te '
                     'benen. Erop rekenen is geen strategie.</p>'},
            {'title': 'Kantelpunten — het omslagmoment',
             'body': '<p>Kritieke drempels waarbij een kleine verandering het systeem '
                     'in een nieuwe toestand duwt die niet vanzelf terugkeert. Bekende '
                     'voorbeelden: het smelten van de Groenlandse ijskap, het '
                     'afsterven van het Amazonewoud, het verdwijnen van '
                     'koraalriffen.</p>'
                     '<p>Het onaangename eraan: passeer je zo’n punt, dan helpt later '
                     'afkoelen niet meer. Het proces loopt door. Daarom is het '
                     'koolstofbudget uit het vorige hoofdstuk geen boekhoudkundige '
                     'exercitie maar een echte deadline.</p>'},
        ])

    p.aandacht(
        'Feedbackloops zitten niet alleen in het klimaat',
        '<p>Hetzelfde mechanisme zit in vrijwel elk hardnekkig vraagstuk. In de '
        'plasticmarkt: lage olieprijzen maken nieuw plastic goedkoper dan gerecycled, '
        'waardoor er minder in recycling wordt geïnvesteerd, waardoor gerecycled '
        'plastic duur en schaars blijft — een versterkende lus die de markt op zijn '
        'plek houdt.</p>'
        '<p>Dat noemen we een <b>lock-in</b>: een systeem dat vastzit in een patroon '
        'door investeringen, regelgeving of gewoontes, ook als er betere alternatieven '
        'zijn. Wie een lock-in wil doorbreken, moet aan de lus komen — niet aan het '
        'symptoom.</p>')

    p.tekst(
        'De energietransitie hier: van succes naar knelpunt',
        '<p>Nederland is de afgelopen jaren hard gegaan met zon en wind: grote '
        'windparken op zee, zonnepanelen op vrijwel elk dak dat het aankan. Op '
        'papier precies wat er moest gebeuren. Kolen zijn er trouwens nog niet uit '
        '— vier centrales draaien nog, en pas vanaf 2030 mag er geen kolen meer '
        'verstookt worden voor elektriciteit. Bij hoge gasprijzen draaien ze zelfs '
        'harder, wat op zichzelf al een lock-in laat zien.</p>'
        '<p>En juist dat succes veroorzaakt het volgende probleem. Het '
        'elektriciteitsnet is ontworpen voor een wereld waarin stroom van een paar '
        'grote centrales naar veel afnemers gaat. Nu wordt er overal opgewekt én '
        'overal meer afgenomen, door warmtepompen, elektrisch vervoer en '
        'elektrificerende industrie. Het net zit vol.</p>'
        '<p>Dat heet <b>netcongestie</b>, en het is inmiddels de belangrijkste rem op '
        'de transitie. Bedrijven wachten jaren op een aansluiting. Woonwijken lopen '
        'vertraging op. Verduurzamingsprojecten kunnen niet door omdat er geen '
        'capaciteit is — met als wrange uitkomst dat een duurzaam project soms '
        'strandt op de duurzame ambities van iedereen samen.</p>')

    p.accordeon(
        'Wat helpt tegen netcongestie',
        '<p>Er is geen enkele maatregel die het oplost. Deze vier samen wel.</p>',
        [
            {'title': 'Het net uitbreiden',
             'body': '<p>Noodzakelijk, en traag. Kabels leggen kost jaren aan '
                     'vergunningen, personeel en geld. Het gebeurt, maar het is nooit '
                     'het antwoord op de vraag van vandaag.</p>'},
            {'title': 'Vraag en aanbod op elkaar afstemmen',
             'body': '<p>Niet iedereen hoeft tegelijk te pieken. Met slimme sturing '
                     'kun je laden, koelen en produceren verschuiven naar momenten '
                     'waarop er ruimte is. Dit levert het snelst resultaat en vraagt '
                     'de minste beton.</p>'},
            {'title': 'Opslag',
             'body': '<p>Batterijen op wijk- of bedrijfsniveau vangen pieken op en '
                     'leveren terug wanneer het nodig is. Effectief lokaal, maar het '
                     'moet wel in het landelijke systeem passen — anders los je het '
                     'ene knelpunt op en creëer je het volgende.</p>'},
            {'title': 'Samen aansluiten',
             'body': '<p>Bedrijven op een terrein die hun aansluiting delen en '
                     'onderling verdelen. Organisatorisch ingewikkeld, technisch '
                     'eenvoudig — en precies het soort oplossing dat je alleen ziet '
                     'als je naar het systeem kijkt in plaats van naar je eigen '
                     'aansluiting.</p>'},
        ])

    p.tekst(
        'Stappenplan: een lock-in of knelpunt te lijf',
        '<p>Werkt voor netcongestie, voor plastic, en voor de meeste taaie '
        'vraagstukken.</p>'
        '<ol>'
        '<li><b>Teken de lus.</b> Wat versterkt wat? Zoek de cirkel waarin het '
        'probleem zichzelf in stand houdt. Zonder die cirkel op papier blijf je aan '
        'symptomen trekken.</li>'
        '<li><b>Zoek waar de lus het zwakst is.</b> Ergens zit een schakel die met '
        'weinig moeite te doorbreken is — een prijs, een regel, een gewoonte, een '
        'ontbrekend stukje informatie.</li>'
        '<li><b>Kijk of je kunt verschuiven in plaats van vergroten.</b> Bij '
        'netcongestie: niet meer capaciteit vragen, maar je vraag verplaatsen. Dat is '
        'bijna altijd sneller en goedkoper.</li>'
        '<li><b>Zoek partijen met hetzelfde knelpunt.</b> Lock-ins doorbreek je zelden '
        'alleen. Wie zit er nog meer vast, en kun je samen iets wat je apart niet '
        'kunt?</li>'
        '<li><b>Begin klein en meet.</b> Eén afdeling, één terrein, één maand. Een '
        'werkend klein voorbeeld overtuigt beter dan een goed onderbouwd plan.</li>'
        '</ol>')

    p.invulvelden(
        'Oefening: jouw taaie vraagstuk',
        '<p>Gebruik het vraagstuk uit hoofdstuk 1, of neem netcongestie als het in je '
        'werk speelt.</p>',
        [
            ('h08-lus', 'Teken de lus in woorden: wat versterkt wat?',
             'Beschrijf de cirkel'),
            ('h08-zwak', 'Waar is die lus het zwakst?',
             'Een prijs, een regel, een gewoonte, ontbrekende informatie'),
            ('h08-verschuif', 'Kun je iets verschuiven in plaats van vergroten?',
             'Vaak sneller en goedkoper'),
            ('h08-samen', 'Wie zit er nog meer vast, en wat kun je samen?',
             'Lock-ins doorbreek je zelden alleen'),
            ('h08-klein', 'Wat is de kleinste proef die je binnen een maand kunt '
             'doen?',
             'Eén afdeling, één terrein, één maand'),
        ])

    p.knoppenrij('Meenemen', '<p>Dit is het laatste bouwsteentje voor je eindanalyse in hoofdstuk 9.</p>')

    p.vraag(
        'Even checken',
        'Een gemeente wil een woonwijk bouwen maar loopt vast op netcongestie. Welke '
        'aanpak past het best bij wat je in dit hoofdstuk hebt gelezen?',
        [
            ('Lokale opslag combineren met het verschuiven van de vraag, en '
             'samenwerken met andere partijen op het net.', True),
            ('Wachten tot de netbeheerder het net heeft uitgebreid.', False),
            ('Minder woningen bouwen.', False),
            ('Lobbyen bij de netbeheerder voor voorrang.', False),
        ],
        feedback={
            'title': 'Even checken',
            'correct': '<p>Precies. Wachten en lobbyen laten de lus intact — je hoopt '
                       'dat iemand anders de capaciteit vergroot. Verschuiven, opslaan '
                       'en samenwerken grijpen aan op het systeem zelf, en werken '
                       'bovendien sneller.</p>',
            '_incorrect': {'final': '<p>Nog niet. Wachten en lobbyen veranderen niets '
                                    'aan het knelpunt zelf, en minder bouwen is het '
                                    'probleem naar de woningmarkt verplaatsen. De '
                                    'winst zit in verschuiven en delen.</p>'},
            '_partlyCorrect': {'final': '<p>Nog niet helemaal.</p>'}
        })
