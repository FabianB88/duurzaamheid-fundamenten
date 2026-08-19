# -*- coding: utf-8 -*-
"""Van lineair naar circulair: waarom take-make-waste vastloopt."""


def bouw(p):
    p.tekst(
        'Nemen, maken, weggooien',
        '<p>Het economische model waarop onze welvaart is gebouwd, werkt in één '
        'richting: grondstoffen winnen, er producten van maken, gebruiken, weggooien. '
        '<i>Take, make, waste.</i> Het heeft ons enorm veel opgeleverd, en het loopt '
        'nu vast op twee dingen tegelijk.</p>'
        '<p><b>Ecologisch</b> omdat het onvermijdelijk grondstoffen uitput en afval '
        'produceert — je kunt het efficiënter maken, maar de richting blijft '
        'dezelfde. <b>Economisch</b> omdat bedrijven afhankelijk blijven van eindige '
        'grondstoffen en van aanvoerketens die steeds vaker haperen.</p>'
        '<p>De circulaire economie draait die richting om: kringlopen sluiten, waarde '
        'behouden, afval voorkomen in plaats van verwerken.</p>')

    p.beeld(
        'lineair-circulair.svg',
        alt='Twee schema’s naast elkaar. Links het lineaire model als een rechte lijn '
            'van grondstof winnen, produceren, gebruiken naar afval, met bij elke stap '
            'verlies van waarde en een afvalberg aan het eind. Rechts het circulaire '
            'model als een gesloten kring van ontwerpen, produceren, gebruiken, '
            'onderhouden en terugnemen, waarbij materialen steeds opnieuw de kring in '
            'gaan en alleen een kleine reststroom overblijft.',
        onderschrift='Links verdwijnt waarde bij elke stap; rechts blijft hij in de '
                     'kring.')

    p.video(
        'De circulaire economie in drie minuten',
        '<p>De Ellen MacArthur Foundation legt uit waarom afval en vervuiling geen '
        'ongelukje zijn maar een ontwerpkeuze — en wat er verandert als je die keuze '
        'anders maakt.</p>',
        aanbieder='youtube', bron='kc_icBPWoQo',
        titel='Eliminate Waste and Pollution — Ellen MacArthur Foundation',
        duur='3 minuten, Engelstalig')

    p.tekst(
        'Wat er precies verandert',
        '<p>Circulair werken is meer dan beter recyclen. Het raakt vier dingen, en '
        'recycling is daarvan de minst interessante.</p>'
        '<ul>'
        '<li><b>Ontwerpen voor hergebruik.</b> Producten zo maken dat ze te '
        'demonteren, repareren en hergebruiken zijn. Dit is de plek waar het meeste '
        'wordt beslist: 80 procent van de milieu-impact van een product ligt vast in '
        'de ontwerpfase.</li>'
        '<li><b>Gebruik in plaats van bezit.</b> Modellen waarin je least of deelt '
        'in plaats van koopt. Dat verandert de prikkel: wie eigenaar blijft, wil dat '
        'het lang meegaat.</li>'
        '<li><b>Slimme materiaalstromen.</b> Gerecyclede of biobased grondstoffen in '
        'plaats van nieuwe, schaarse materialen.</li>'
        '<li><b>Modulair bouwen.</b> Onderdelen die je los kunt vervangen of '
        'upgraden, zodat één kapot onderdeel niet het hele product afschrijft.</li>'
        '</ul>')

    p.aandacht(
        'Circulair is niet automatisch duurzaam',
        '<p>Een kringloop sluiten kost energie. Een product dat je vijf keer heen en '
        'weer transporteert om het te refurbishen, kan een grotere voetafdruk hebben '
        'dan een nieuw exemplaar dat om de hoek gemaakt wordt.</p>'
        '<p>Circulariteit is dus een middel, geen doel. De vraag blijft altijd: '
        '<b>levert deze kringloop netto winst op?</b> Daarvoor moet je rekenen, en '
        'daar is de levenscyclusanalyse voor.</p>')

    p.tekst(
        'De levenscyclusanalyse in het kort',
        '<p>Een <b>LCA</b> beoordeelt de milieueffecten van een product of dienst over '
        'de héle levensduur: grondstofwinning, productie, transport, gebruik, '
        'onderhoud en afdanking. Zo wordt zichtbaar waar in de keten de grootste '
        'belasting zit, en dus waar verbeteren zin heeft.</p>'
        '<p>De methode is internationaal vastgelegd in ISO 14040. Dat klinkt formeel, '
        'maar het punt is eenvoudig: als je niet afspreekt wat je meetelt, kan '
        'iedereen zijn eigen gunstige antwoord produceren. Precies de systeemgrens uit '
        'hoofdstuk 1, nu met een norm eromheen.</p>'
        '<p>Je hoeft zelf geen LCA te kunnen uitvoeren. Wel moet je kunnen lezen wat '
        'erin staat, en de twee vragen stellen die er altijd toe doen: <b>welke '
        'systeemgrens is gehanteerd</b>, en <b>waarmee is vergeleken</b>?</p>')

    p.tekst(
        'Stappenplan: een product van lineair naar circulair denken',
        '<p>Pak een product of dienst die je kent. Reken op een half uur.</p>'
        '<ol>'
        '<li><b>Teken de huidige route.</b> Van grondstof tot afval, met alle stappen '
        'ertussen. Waar komt het vandaan, waar gaat het heen?</li>'
        '<li><b>Markeer waar waarde verdwijnt.</b> Op welk punt wordt iets dat nog '
        'bruikbaar was, afval? Meestal zijn er twee of drie van die punten.</li>'
        '<li><b>Vraag per punt: waarom gebeurt dat?</b> Is het ontwerp, de prijs, de '
        'logistiek, of gewoon gewoonte? Het antwoord bepaalt welke ingreep '
        'werkt.</li>'
        '<li><b>Bedenk hoe de stroom terug kan.</b> Wie zou het terugnemen, en waarom '
        'zou die dat willen? Zonder een partij met belang gaat geen kringloop '
        'draaien.</li>'
        '<li><b>Toets op netto winst.</b> Kost het sluiten van de kring niet meer '
        'energie, transport of materiaal dan het bespaart? Bij twijfel: zoek een LCA '
        'van een vergelijkbaar product.</li>'
        '<li><b>Bepaal wat je in het ontwerp zou veranderen.</b> Terug naar stap één '
        'van het product, want daar wordt het meeste beslist.</li>'
        '</ol>')

    p.invulvelden(
        'Oefening: jouw product, twee routes',
        '<p>Kies iets concreets uit je eigen werk: een product dat je inkoopt, iets '
        'wat je organisatie weggooit, of een dienst die je levert.</p>',
        [
            ('h05-product', 'Welk product of welke dienst neem je?',
             'Iets waar je zelf mee te maken hebt'),
            ('h05-route', 'Wat is nu de route van grondstof tot afval?',
             'Noem de stappen'),
            ('h05-verlies', 'Waar verdwijnt de waarde?',
             'Op welk punt wordt bruikbaar spul afval?'),
            ('h05-waarom', 'Waarom gebeurt dat daar? Ontwerp, prijs, logistiek of '
             'gewoonte?',
             'Het antwoord bepaalt welke ingreep werkt'),
            ('h05-terug', 'Hoe zou de stroom terug kunnen, en wie heeft er belang bij?',
             'Zonder belanghebbende draait geen kringloop'),
            ('h05-netto', 'Levert het sluiten van de kring netto winst op? Waarop '
             'baseer je dat?',
             'Eerlijk antwoord; "weet ik niet" mag ook'),
            ('h05-ontwerp', 'Wat zou je in het ontwerp veranderen?',
             'Daar wordt het meeste beslist'),
        ])

    p.knoppenrij('Meenemen', '<p>In het volgende hoofdstuk kies je er een concrete strategie bij.</p>')

    p.vraag(
        'Even checken',
        'Wat is het belangrijkste verschil tussen de lineaire en de circulaire '
        'economie?',
        [
            ('De lineaire economie is gericht op gebruiken en weggooien; de circulaire '
             'op waarde behouden en kringlopen sluiten.', True),
            ('De lineaire economie minimaliseert afval, de circulaire maximaliseert '
             'het.', False),
            ('In de circulaire economie worden producten nooit hergebruikt.', False),
            ('De lineaire economie stimuleert delen en leasen.', False),
        ],
        feedback={
            'title': 'Even checken',
            'correct': '<p>Klopt. En let op de nuance uit dit hoofdstuk: circulair is '
                       'geen garantie. Een kringloop die meer energie kost dan hij '
                       'bespaart, is alleen op papier duurzaam.</p>',
            '_incorrect': {'final': '<p>Nog niet — de andere drie draaien de begrippen '
                                    'om. Kern: lineair loopt in één richting van '
                                    'grondstof naar afval, circulair houdt materialen '
                                    'in omloop.</p>'},
            '_partlyCorrect': {'final': '<p>Nog niet helemaal.</p>'}
        })
