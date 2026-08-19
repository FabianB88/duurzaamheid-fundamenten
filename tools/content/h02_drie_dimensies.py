# -*- coding: utf-8 -*-
"""De drie dimensies van duurzaamheid en hoe ze samenhangen."""


def bouw(p):
    p.tekst(
        'Duurzaamheid als een huis',
        '<p>Duurzaamheid gaat over drie dingen tegelijk, en de verhouding ertussen is '
        'makkelijker te vatten met een beeld: een huis.</p>'
        '<p>Het huis staat voor onze welvaart — de manier waarop we leven, werken en '
        'groeien. Daarbinnen zit alles wat we belangrijk vinden: gezondheid, '
        'veiligheid, comfort, onderwijs, werk.</p>'
        '<p>Maar elk huis rust op een fundament, en dat fundament is de aarde zelf: de '
        'waterkringloop, de vruchtbaarheid van de bodem, een stabiel klimaat, de '
        'biodiversiteit. Verzwakt dat fundament, dan verliest het huis zijn '
        'draagkracht. Je kunt kamers blijven bijbouwen en de gevel blijven schilderen, '
        'maar zonder stevige basis zakt het langzaam in.</p>')

    p.beeld(
        'huis-drie-dimensies.svg',
        alt='Een huis in drie lagen. Onderaan het fundament: de ecologische dimensie, '
            'met gezonde ecosystemen, schoon water, vruchtbare bodem en een stabiel '
            'klimaat. Daarboven de muren en het dak: de economische dimensie, de '
            'manier waarop we waarde maken en verdelen, binnen de draagkracht van het '
            'fundament. Binnenin het interieur: de sociale dimensie, met welzijn, '
            'gelijkheid, veiligheid en meedoen. Een pijl langs de zijkant geeft aan '
            'dat de drie lagen elkaar beïnvloeden: raakt er één uit balans, dan '
            'verliest het geheel zijn stabiliteit.',
        onderschrift='Ecologie is het fundament, economie de structuur, het sociale '
                     'het leven dat zich erin afspeelt.')

    p.accordeon(
        'De drie dimensies, één voor één',
        '<p>Ze zijn niet gelijkwaardig in de zin dat je ze kunt uitruilen. Ze zitten '
        'in elkaar.</p>',
        [
            {'title': 'Ecologisch — het fundament',
             'body': '<p>Het behoud van natuurlijke systemen, biodiversiteit en het '
                     'respecteren van de draagkracht van de aarde. Zonder gezonde '
                     'ecosystemen, schoon water, vruchtbare grond en een stabiel '
                     'klimaat kan geen mens en geen economie floreren.</p>'
                     '<p><b>Bijvoorbeeld:</b> klimaatverandering tegengaan met '
                     'hernieuwbare energie, ecosystemen herstellen door '
                     'herbebossing.</p>'},
            {'title': 'Economisch — de structuur',
             'body': '<p>De manier waarop we waarde maken en verdelen, zonder de '
                     'hulpbronnen te ondermijnen waarop die waarde rust. Innovatie en '
                     'groei blijven belangrijk, maar binnen de draagkracht van het '
                     'fundament.</p>'
                     '<p><b>Bijvoorbeeld:</b> investeren in technologie die energie '
                     'bespaart of afval omzet in nieuwe producten, en zorgen dat '
                     'welvaart eerlijk terechtkomt.</p>'},
            {'title': 'Sociaal — het interieur',
             'body': '<p>Rechtvaardigheid, welzijn en de rol van mensen. Gelijke '
                     'kansen, goede arbeidsomstandigheden, gemeenschappen betrekken '
                     'bij besluiten. Een duurzaam huis is niet alleen stevig gebouwd, '
                     'het is ook een plek waar iedereen zich thuis voelt en kan '
                     'meedoen.</p>'
                     '<p><b>Bijvoorbeeld:</b> armoede bestrijden via onderwijs, '
                     'ongelijkheid op de werkvloer aanpakken.</p>'},
        ])

    p.aandacht(
        'Uit balans is uit balans',
        '<p>Een stevig fundament zonder rechtvaardige samenleving is leeg. Een '
        'welvarend interieur zonder ecologische basis is tijdelijk. En een '
        'rechtvaardige samenleving zonder economische structuur is kwetsbaar.</p>'
        '<p>Vandaar dat "duurzaam" zelden betekent dat je op één knop drukt. Bijna elke '
        'echte maatregel raakt alle drie, en meestal niet allemaal even gunstig. Dat '
        'expliciet maken is het werk.</p>')

    p.accordeon(
        'Hoe de systemen op elkaar inwerken',
        '<p>Vier voorbeelden waarin je de drie dimensies tegelijk ziet werken.</p>',
        [
            {'title': 'Klimaat',
             'body': '<p>Veroorzaakt door fossiele brandstoffen, ontbossing en '
                     'industrie <i>(economisch)</i>, met gevolgen voor ecosystemen en '
                     'zeespiegel <i>(ecologisch)</i>, waarbij kwetsbare gemeenschappen '
                     'het hardst worden geraakt omdat zij het minste geld hebben om '
                     'zich aan te passen <i>(sociaal)</i>.</p>'},
            {'title': 'Voedsel',
             'body': '<p>Een groeiende bevolking en beperkte hulpbronnen zetten de '
                     'productie onder druk. Traditionele landbouw put de bodem uit en '
                     'vervuilt water. Precisielandbouw en het tegengaan van '
                     'voedselverspilling helpen — maar dat vraagt samenwerking tussen '
                     'boeren, bedrijven, overheden en consumenten, en dat is een '
                     'sociaal vraagstuk.</p>'},
            {'title': 'Steden',
             'body': '<p>Steden zijn economische motoren én kampen met luchtvervuiling, '
                     'files, woningtekort en ongelijkheid. Groene infrastructuur en '
                     'openbaar vervoer helpen, maar alleen als gemeenschappen bij de '
                     'besluitvorming worden betrokken. Anders verbeter je de stad voor '
                     'sommigen en verdringt je anderen.</p>'},
            {'title': 'Energie',
             'body': '<p>De vraag groeit, de fossiele voorraad krimpt. Zon, wind en '
                     'opslag bieden een alternatief, en de transitie levert nieuwe '
                     'banen op. Tegelijk zit er een verdelingsvraag in: wie betaalt de '
                     'netuitbreiding, en wie profiteert het eerst? Daar komen we in '
                     'hoofdstuk 8 op terug.</p>'},
        ])

    p.tekst(
        'Stappenplan: een plan toetsen op de drie dimensies',
        '<p>Gebruik dit als je een voorstel, project of maatregel beoordeelt. Het kost '
        'twintig minuten en het haalt de blinde vlek eruit.</p>'
        '<ol>'
        '<li><b>Schrijf op wat het plan oplevert op elk van de drie vlakken.</b> Niet '
        'alleen waar het voor bedoeld is — ook wat het onbedoeld raakt.</li>'
        '<li><b>Zoek de dimensie die het slechtst scoort.</b> Er is er bijna altijd '
        'één die het kind van de rekening is. Meestal is dat het sociale, omdat '
        'niemand daar eigenaar van is.</li>'
        '<li><b>Vraag door op het fundament.</b> Kan dit plan ook op lange termijn, of '
        'teert het in op iets wat niet aangroeit — bodem, water, grondstof, '
        'vertrouwen?</li>'
        '<li><b>Benoem de afruil hardop.</b> Wat lever je in waarvoor? Een plan zonder '
        'zichtbare afruil is meestal een plan waarvan iemand de rekening nog '
        'krijgt.</li>'
        '<li><b>Zoek één aanpassing die de zwakste dimensie optilt</b> zonder de '
        'andere twee onderuit te halen. Dat is bijna altijd mogelijk, maar zelden de '
        'eerste ingeving.</li>'
        '</ol>')

    p.invulvelden(
        'Oefening: toets je eigen vraagstuk',
        '<p>Pak het vraagstuk uit hoofdstuk 1 erbij en loop de stappen langs.</p>',
        [
            ('h02-eco', 'Wat raakt het ecologisch?',
             'Positief én negatief'),
            ('h02-econ', 'Wat raakt het economisch?', 'Kosten, baten, wie betaalt'),
            ('h02-soc', 'Wat raakt het sociaal?',
             'Wie profiteert, wie draagt de last'),
            ('h02-zwakste', 'Welke dimensie komt er het slechtst uit, en waarom?',
             'Vaak de sociale, omdat niemand er eigenaar van is'),
            ('h02-afruil', 'Welke afruil zit er in? Wat lever je in waarvoor?',
             'Benoem het hardop'),
            ('h02-aanpassing', 'Welke aanpassing tilt de zwakste dimensie op?',
             'Zonder de andere twee onderuit te halen'),
        ])

    p.knoppenrij('Meenemen', '<p>Neem je afruil mee naar hoofdstuk 9; daar maak je er een onderbouwde keuze van.</p>')

    p.vraag(
        'Even checken',
        'Welke dimensie van duurzaamheid vormt het fundament waarop de andere twee '
        'rusten?',
        [
            ('De ecologische dimensie — zonder gezonde ecosystemen, water, bodem en '
             'klimaat kunnen economie en samenleving niet bestaan.', True),
            ('De economische dimensie, want zonder geld kun je niets '
             'verduurzamen.', False),
            ('De sociale dimensie, want mensen maken de keuzes.', False),
            ('Alle drie zijn precies gelijkwaardig en uitwisselbaar.', False),
        ],
        feedback={
            'title': 'Even checken',
            'correct': '<p>Klopt. De drie zijn alle drie nodig, maar ze zijn niet '
                       'uitwisselbaar: economie en samenleving spelen zich áf binnen '
                       'wat de aarde aankan, niet ernaast. Dat is precies waarom '
                       'planetaire grenzen — het volgende deel — zo belangrijk '
                       'zijn.</p>',
            '_incorrect': {'final': '<p>Nog niet. Geld en mensen zijn onmisbaar, maar '
                                    'ze rusten allebei op iets: een leefbare aarde. Val '
                                    'het fundament weg, dan houdt de rest ook op — '
                                    'andersom niet.</p>'},
            '_partlyCorrect': {'final': '<p>Nog niet helemaal.</p>'}
        })
