# -*- coding: utf-8 -*-
"""Kennischeck over de hele cursus, plus je eigen systeemanalyse."""

TOETS = 'kennischeck-fundamenten'
DREMPEL = 75


def bouw(p):
    p.tekst(
        'Kennischeck',
        '<p>Acht vragen over de hele cursus. Het zijn geen definitievragen: bij elke '
        'vraag staat een situatie waarin je moet kiezen wat je doet of wat je '
        'concludeert.</p>'
        '<p>Je hebt %d%% nodig om te slagen en je mag het zo vaak proberen als je '
        'wilt. Je uitslag verschijnt onderaan zodra je alle vragen hebt '
        'ingestuurd.</p>' % DREMPEL)

    p.vraag(
        'Vraag 1 — systeemgrenzen',
        'Twee adviesbureaus rekenen de CO₂-uitstoot van dezelfde elektrische bestelbus '
        'door en komen op heel verschillende uitkomsten. Wat is de meest waarschijnlijke '
        'verklaring?',
        [
            ('Ze hebben een andere systeemgrens gekozen — bijvoorbeeld wel of niet de '
             'productie van de accu en de stroommix meegerekend.', True),
            ('Een van de twee heeft een rekenfout gemaakt.', False),
            ('CO₂-uitstoot is nu eenmaal niet betrouwbaar te meten.', False),
            ('Het ene bureau is objectiever dan het andere.', False),
        ],
        feedback={
            'title': 'Vraag 1',
            'correct': '<p>Klopt. Verschillende systeemgrenzen leveren verschillende '
                       'antwoorden op, en beide kunnen kloppen. Daarom is de eerste '
                       'vraag bij elk cijfer: wat is meegerekend?</p>',
            '_incorrect': {'final': '<p>Nog niet. Je hoeft geen fout of kwade wil aan '
                                    'te nemen: als je de grens anders legt, meet je '
                                    'iets anders. Dat is precies waarom je hem '
                                    'expliciet maakt.</p>'},
            '_partlyCorrect': {'final': '<p>Nog niet helemaal.</p>'}
        })

    p.vraag(
        'Vraag 2 — de drie dimensies',
        'Een gemeente vervangt alle straatverlichting door led. Energieverbruik daalt '
        'flink. Welke vraag hoort er in een integrale afweging nog bij?',
        [
            ('Wat het sociaal betekent — bijvoorbeeld of de nieuwe verlichting overal '
             'even veilig aanvoelt — en wat er met de oude armaturen gebeurt.', True),
            ('Of de terugverdientijd korter is dan vijf jaar.', False),
            ('Of de leverancier ISO-gecertificeerd is.', False),
            ('Geen enkele; minder energie is per definitie beter.', False),
        ],
        feedback={
            'title': 'Vraag 2',
            'correct': '<p>Goed. De ecologische winst is duidelijk, maar de sociale en '
                       'de materiaalkant vallen makkelijk buiten beeld — precies de '
                       'dimensie waar meestal niemand eigenaar van is.</p>',
            '_incorrect': {'final': '<p>Nog niet. Terugverdientijd en certificering zijn '
                                    'nuttige vragen, maar ze blijven binnen één '
                                    'dimensie. Een integrale afweging betrekt alle '
                                    'drie.</p>'},
            '_partlyCorrect': {'final': '<p>Nog niet helemaal.</p>'}
        })

    p.koppelvraag(
        'Vraag 3 — planetaire grenzen',
        'Koppel elk verschijnsel aan de planetaire grens waar het bij hoort.',
        rijen=[
            ('Algenbloei en dode zones in het oppervlaktewater',
             'Stikstof- en fosforkringloop'),
            ('CO₂-concentratie in de atmosfeer', 'Klimaatverandering'),
            ('Soorten die verdwijnen en ecosystemen die veerkracht verliezen',
             'Biodiversiteitsverlies'),
            ('Beschikbaarheid van schoon water onder druk', 'Zoetwatergebruik'),
        ],
        opties=['Stikstof- en fosforkringloop', 'Klimaatverandering',
                'Biodiversiteitsverlies', 'Zoetwatergebruik'],
        feedback={
            'title': 'Vraag 3',
            'correct': '<p>Goed. Merk op dat deze vier in de praktijk aan elkaar '
                       'vastzitten: de Nederlandse stikstofcrisis raakt alle vier '
                       'tegelijk.</p>',
            '_incorrect': {'final': '<p>Nog niet. Kijk per verschijnsel welk proces uit '
                                    'het aardsysteem eronder ligt: lucht, water, '
                                    'voedingsstoffen of leven.</p>'},
            '_partlyCorrect': {'final': '<p>Deels goed. Kijk nog eens naar de regels '
                                        'die je fout had.</p>'}
        })

    p.vraag(
        'Vraag 4 — de R-ladder',
        'Een organisatie wil circulairder worden en zet als eerste maatregel gescheiden '
        'afvalbakken op elke verdieping. Wat is hier de kanttekening bij?',
        [
            ('Recyclen staat laag op de R-ladder; de treden erboven — weigeren, '
             'verminderen, hergebruiken — leveren meer op en kosten vaak minder.', True),
            ('Gescheiden inzamelen werkt in de praktijk nooit.', False),
            ('Het is een goede eerste stap; hoger op de ladder komt vanzelf.', False),
            ('Afvalscheiding hoort niet bij circulariteit.', False),
        ],
        feedback={
            'title': 'Vraag 4',
            'correct': '<p>Precies. Afvalbakken zijn zichtbaar en pijnloos, en daarom '
                       'begint bijna iedereen daar. De winst zit erboven: bij wat je '
                       'niet inkoopt en wat je langer gebruikt.</p>',
            '_incorrect': {'final': '<p>Nog niet. Afvalscheiding is nuttig en hoort er '
                                    'zeker bij — het punt is de volgorde. Begin '
                                    'bovenaan de ladder en werk naar beneden, niet '
                                    'andersom.</p>'},
            '_partlyCorrect': {'final': '<p>Nog niet helemaal.</p>'}
        })

    p.vraag(
        'Vraag 5 — circulair is niet vanzelf duurzaam',
        'Een bedrijf zet een terugnamesysteem op waarbij gebruikte producten door het '
        'hele land worden opgehaald, centraal gerefurbisht en weer verzonden. Wat moet '
        'je controleren voordat je dit duurzaam noemt?',
        [
            ('Of het sluiten van de kringloop netto winst oplevert — het transport en '
             'de bewerking kunnen meer kosten dan ze besparen.', True),
            ('Of de producten er na refurbishen nog netjes uitzien.', False),
            ('Of er een certificaat aan hangt.', False),
            ('Niets; een kringloop sluiten is altijd beter dan weggooien.', False),
        ],
        feedback={
            'title': 'Vraag 5',
            'correct': '<p>Klopt. Circulariteit is een middel, geen doel. De vraag is '
                       'altijd of de kring netto wat oplevert, en daarvoor moet je '
                       'rekenen — bijvoorbeeld met een levenscyclusanalyse.</p>',
            '_incorrect': {'final': '<p>Nog niet. Een kringloop kost energie en '
                                    'transport. Er zijn genoeg terugnamesystemen die '
                                    'per saldo slechter uitpakken dan lokaal nieuw '
                                    'maken.</p>'},
            '_partlyCorrect': {'final': '<p>Nog niet helemaal.</p>'}
        })

    p.vraag(
        'Vraag 6 — klimaatcijfers lezen',
        'Welke bewering telt mee voor het koolstofbudget?',
        [
            ('De totale uitstoot in tonnen CO₂ is dit jaar gedaald.', True),
            ('De uitstoot per product is met dertig procent gedaald.', False),
            ('De uitstoot per euro omzet is gehalveerd.', False),
            ('De uitstoot per medewerker is lager dan het branchegemiddelde.', False),
        ],
        feedback={
            'title': 'Vraag 6',
            'correct': '<p>Goed. Alleen absolute uitstoot telt voor het budget. De '
                       'andere drie zijn efficiëntiecijfers: ze kunnen dalen terwijl '
                       'de totale uitstoot stijgt.</p>',
            '_incorrect': {'final': '<p>Nog niet. Alle drie de andere zijn '
                                    'verhoudingsgetallen. Ze zeggen iets over hoe '
                                    'efficiënt er gewerkt wordt, maar niets over '
                                    'hoeveel CO₂ er werkelijk de lucht in gaat.</p>'},
            '_partlyCorrect': {'final': '<p>Nog niet helemaal.</p>'}
        })

    p.vraag(
        'Vraag 7 — feedback en kantelpunten',
        'Wat maakt kantelpunten in het klimaatsysteem zo verontrustend?',
        [
            ('Zodra ze gepasseerd zijn, keert het systeem niet vanzelf terug — later '
             'afkoelen draait het proces niet meer om.', True),
            ('Ze zijn precies te voorspellen, waardoor uitstel geen risico is.', False),
            ('Ze treden alleen op bij zeer grote temperatuurstijgingen.', False),
            ('Ze worden gecompenseerd door negatieve feedback.', False),
        ],
        feedback={
            'title': 'Vraag 7',
            'correct': '<p>Precies. Dat is ook waarom het koolstofbudget een echte '
                       'deadline is en geen boekhoudkundige afspraak: sommige '
                       'veranderingen kun je niet terugkopen.</p>',
            '_incorrect': {'final': '<p>Nog niet. Kantelpunten zijn juist slecht '
                                    'voorspelbaar, en de dempende mechanismen zijn te '
                                    'zwak om ze te compenseren. Het onomkeerbare is '
                                    'wat ze gevaarlijk maakt.</p>'},
            '_partlyCorrect': {'final': '<p>Nog niet helemaal.</p>'}
        })

    p.vraag(
        'Vraag 8 — lock-in doorbreken',
        'Gerecycled plastic blijft duurder dan nieuw plastic, waardoor er weinig in '
        'recycling wordt geïnvesteerd, waardoor het duur blijft. Wat is de meest '
        'kansrijke aanpak?',
        [
            ('Een combinatie van marktprikkels en regelgeving, zodat de lus zelf '
             'verandert in plaats van één schakel.', True),
            ('Alleen innovatie stimuleren; als de techniek beter wordt, lost het zich '
             'op.', False),
            ('Alleen belasting heffen op nieuw plastic.', False),
            ('Afwachten tot de olieprijs stijgt.', False),
        ],
        feedback={
            'title': 'Vraag 8',
            'correct': '<p>Klopt. Een lock-in wordt in stand gehouden door meerdere '
                       'schakels tegelijk. Aan één knop draaien wordt meestal '
                       'opgevangen door de rest van de lus.</p>',
            '_incorrect': {'final': '<p>Nog niet. Elk van de andere antwoorden pakt één '
                                    'schakel aan of wacht op iets van buiten. Bij een '
                                    'zelfversterkende lus is dat zelden genoeg.</p>'},
            '_partlyCorrect': {'final': '<p>Nog niet helemaal.</p>'}
        })

    p.tekst(
        'Jouw systeemanalyse',
        '<p>Tot slot breng je alles samen. Door de hele cursus heb je aan hetzelfde '
        'vraagstuk gewerkt: je tekende het systeem in hoofdstuk 1, toetste het op de '
        'drie dimensies in hoofdstuk 2, volgde de stof door de sferen in hoofdstuk 3, '
        'zocht je planetaire grens in hoofdstuk 4, keek naar de kringloop in 5 en 6, '
        'schatte de klimaatimpact in 7 en zocht de lus in 8.</p>'
        '<p>Hieronder maak je er één onderbouwde keuze van. Dat is de vertaalslag '
        'waar het uiteindelijk om gaat: van begrijpen naar beslissen.</p>')

    p.invulvelden(
        'Van analyse naar keuze',
        '<p>Vul dit in en kopieer het naar je eigen aantekeningen. Een analyse die '
        'alleen in deze browser staat, verandert niets.</p>',
        [
            ('h09-vraagstuk', 'Waar gaat je vraagstuk over, in twee zinnen?',
             'Zoals het er nu voor staat, na acht hoofdstukken'),
            ('h09-systeem', 'Wat is het belangrijkste dat je systeemanalyse opleverde?',
             'De verbinding of de lus die je eerst niet zag'),
            ('h09-grens', 'Welke planetaire grens raak je, en hoe hard?',
             'Met je getal uit hoofdstuk 4'),
            ('h09-keuze', 'Welke maatregel kies je? Eén, concreet.',
             'Met de R-trede erbij als het over materiaal gaat'),
            ('h09-afruil', 'Welke afruil zit erin? Wat lever je in waarvoor?',
             'Ecologisch, economisch of sociaal'),
            ('h09-onzeker', 'Wat weet je niet, en hoe kom je erachter?',
             'Onwetendheid benoemen hoort bij een goede onderbouwing'),
            ('h09-eerste', 'Wat is je eerste stap, en wanneer zet je hem?',
             'Klein en met een datum'),
            ('h09-meten', 'Waaraan zie je over een jaar of het gewerkt heeft?',
             'Eén getal of één waarneembaar verschil'),
        ])

    p.knoppenrij(
        'Meenemen',
        '<p>Kopieer je analyse en zet je eerste stap meteen in je agenda. Dat is het '
        'verschil tussen een cursus en een verandering.</p>')


def uitslag(p):
    """Komt in een eigen artikel onder de vragen te staan."""
    p.uitslag(
        TOETS, drempel=DREMPEL,
        voldoende='Voldoende. Je hebt de fundamenten te pakken. Ga nu terug naar je '
                  'systeemanalyse hierboven en zet je eerste stap in je agenda.',
        onvoldoende='Dat is nog niet voldoende. Loop de hoofdstukken van de vragen '
                    'die je fout had nog eens door en probeer het daarna opnieuw. Je '
                    'mag het zo vaak proberen als je wilt.')
