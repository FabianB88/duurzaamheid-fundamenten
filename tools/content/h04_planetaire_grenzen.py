# -*- coding: utf-8 -*-
"""Planetaire grenzen: de veilige ruimte en wat er gebeurt als je eroverheen gaat."""


def bouw(p):
    p.tekst(
        'De veilige ruimte om in te opereren',
        '<p>Een team wetenschappers onder leiding van Johan Rockström en Will Steffen '
        'stelde in 2009 een vraag die daarvoor nauwelijks zo scherp gesteld was: '
        '<i>hoeveel kan de aarde hebben voordat het misgaat?</i></p>'
        '<p>Hun antwoord is het raamwerk van de <b>planetaire grenzen</b>: negen '
        'processen die het aardsysteem stabiel houden, elk met een grens waarbinnen '
        'de mensheid veilig kan opereren. Blijf je erbinnen, dan blijft het systeem '
        'in de toestand waarin onze landbouw, steden en samenlevingen zijn '
        'ontstaan. Ga je eroverheen, dan neem je risico op veranderingen die je niet '
        'meer terugdraait.</p>'
        '<p>Het is geen doemverhaal maar een <b>meetlat</b>. En dat maakt het bruikbaar: '
        'je kunt er beleid, ontwerpen en projecten langs leggen.</p>'
        '<p>De meetlat wordt jaarlijks bijgewerkt in de <i>Planetary Health Check</i>. '
        'In 2023 stonden er zes grenzen op overschreden; in september 2025 kwam '
        '<b>verzuring van de oceanen</b> erbij als zevende. Alleen de ozonlaag en '
        'luchtvervuiling door aerosolen zitten nog binnen hun grens. Kijk dus bij '
        'elk cijfer dat je tegenkomt uit welk jaar het komt — ook dit.</p>')

    p.beeld(
        'planetaire-grenzen.svg',
        alt='Een cirkeldiagram met negen taartpunten, elk een planetaire grens. De '
            'binnenring is de veilige ruimte. Zeven punten steken buiten de ring uit '
            'en zijn donker gemarkeerd als overschreden: klimaatverandering, '
            'biodiversiteitsverlies, verandering in landgebruik, zoetwatergebruik, '
            'verstoring van de stikstof- en fosforkringloop, chemische '
            'verontreiniging en verzuring van de oceanen. Twee punten blijven '
            'binnen de ring: aantasting van de ozonlaag en luchtvervuiling door '
            'aerosolen.',
        onderschrift='Stand van de Planetary Health Check 2025: zeven van de negen '
                     'grenzen zijn overschreden. De ozonlaag laat zien dat '
                     'terugkeren binnen de grens kan.')

    p.tekst(
        'De negen grenzen',
        '<p>Klimaatverandering · verlies van biodiversiteit · verandering in '
        'landgebruik · zoetwatergebruik · verzuring van de oceanen · verstoring van de '
        'stikstof- en fosforkringloop · chemische verontreiniging · luchtvervuiling '
        'door aerosolen · aantasting van de ozonlaag.</p>'
        '<p>Ze zijn gekozen omdat ze allemaal essentieel zijn voor een stabiel '
        'aardsysteem <b>en omdat ze aan elkaar vastzitten</b>. Verlies van '
        'biodiversiteit vermindert de veerkracht van ecosystemen, waardoor die minder '
        'goed tegen klimaatverandering kunnen — en klimaatverandering versnelt op haar '
        'beurt het soortenverlies. Eén grens overschrijden maakt de volgende '
        'waarschijnlijker.</p>')

    p.aandacht(
        'De ozonlaag: het bewijs dat het kan',
        '<p>Van de negen grenzen is er één waar we ooit overheen gingen en waar we '
        'weer binnen zijn gekomen. Na het Montreal-protocol van 1987 werden '
        'cfk’s wereldwijd uitgefaseerd, en de ozonlaag herstelt zich sindsdien.</p>'
        '<p>Dat verhaal is belangrijker dan het lijkt. Het laat zien dat een '
        'planetaire grens geen natuurwet is waar je machteloos tegenover staat, maar '
        'een uitkomst van keuzes — mits het probleem scherp is, het alternatief '
        'bestaat, en er een afspraak komt die iedereen bindt.</p>')

    p.accordeon(
        'Wat er gebeurt bij overschrijding',
        '<p>Drie van de zeven overschreden grenzen, en wat dat concreet '
        'betekent.</p>',
        [
            {'title': 'Klimaatverandering',
             'body': '<p>Extremere weersomstandigheden: hevigere stormen, langdurige '
                     'droogte, intensere hittegolven. Dat raakt ecosystemen, '
                     'landbouwopbrengsten en de leefbaarheid van hele regio’s.</p>'
                     '<p>Zeespiegelstijging bedreigt kustgebieden, met migratie en '
                     'verlies van infrastructuur tot gevolg. De schade is bovendien '
                     'ongelijk verdeeld: wie het minst heeft bijgedragen, wordt vaak '
                     'het hardst geraakt.</p>'},
            {'title': 'Verlies van biodiversiteit',
             'body': '<p>Als soorten verdwijnen, haperen processen waar we op '
                     'rekenen: bestuiving, waterzuivering, bodemvruchtbaarheid. Dat '
                     'raakt de voedselproductie direct.</p>'
                     '<p>Belangrijker nog: ecosystemen verliezen hun veerkracht. Ze '
                     'kunnen minder goed tegen een verstoring, waardoor de volgende '
                     'schok harder aankomt.</p>'},
            {'title': 'Stikstof en fosfor',
             'body': '<p>Te veel stikstof en fosfor in het milieu, vooral uit landbouw '
                     'en industrie, verstoort natuurlijke kringlopen. Het gevolg is '
                     'eutrofiëring: water raakt overbelast met voedingsstoffen, '
                     'algen bloeien, zuurstof verdwijnt en er ontstaan dode zones in '
                     'meren, rivieren en zeeën.</p>'
                     '<p>Dit is de grens waar Nederland het hardst tegenaan loopt. Zie '
                     'de casus hieronder.</p>'},
        ])

    p.tekst(
        'Casus: de stikstofcrisis in Nederland',
        '<p>Nederland is het duidelijkste voorbeeld in Europa van één overschreden '
        'grens die een heel land raakt.</p>'
        '<p>Door intensieve veehouderij en kunstmest komt er veel meer stikstof in de '
        'natuur terecht dan die aankan. Kwetsbare gebieden als heidevelden en '
        'veengebieden raken overwoekerd door stikstofminnende planten — brandnetels, '
        'grassen — waardoor zeldzame soorten verdwijnen. Ecologisch verlies, '
        'rechtstreeks terug te voeren op één verstoorde kringloop.</p>'
        '<p>Maar het bleef niet ecologisch. Omdat de natuur wettelijk beschermd is, '
        'werden bouwprojecten stilgelegd die niet aan de stikstofregels voldeden. '
        'Boeren kregen te maken met ingrijpende maatregelen. Er volgden protesten en '
        'een maatschappelijk debat dat jaren aanhoudt.</p>'
        '<p>Dat is precies waar deze cursus over gaat: één overschreden planetaire '
        'grens werkt door in de economie en in de samenleving, en er is geen oplossing '
        'die alleen in de ecologische hoek zit.</p>')

    p.tekst(
        'Verdieping: wat is stikstof eigenlijk?',
        '<p>NOS op 3 legt in drie minuten uit wat stikstof is en waarom het in '
        'Nederland zo’n probleem werd. Deze video staat op nos.nl en laat zich niet '
        'insluiten, dus hij opent in een nieuw tabblad.</p>'
        '<p><a class="paginanav__knop paginanav__knop--stil" '
        'href="https://nos.nl/collectie/13901/video/2432122-wat-is-stikstof-en-waarom-is-het-een-probleem" '
        'target="_blank" rel="noopener">'
        '<span class="paginanav__label">Bekijken · 3 minuten</span>'
        '<span class="paginanav__titel">Wat is stikstof en waarom is het een '
        'probleem?</span></a></p>')

    p.tekst(
        'Stappenplan: welke grens raakt jouw werk?',
        '<p>Bijna elk project raakt er minstens één. De kunst is uitzoeken welke, en '
        'hoe hard.</p>'
        '<ol>'
        '<li><b>Loop de negen grenzen langs en streep aan wat je raakt.</b> Wees '
        'ruimhartig: indirect telt ook. Inkoop van beton raakt landgebruik én '
        'klimaat.</li>'
        '<li><b>Kies de grens waar jouw invloed het grootst is.</b> Niet de grootste '
        'grens, maar die waar jij daadwerkelijk aan kunt draaien.</li>'
        '<li><b>Zoek een getal.</b> Hoeveel is het, per jaar of per eenheid? Een ruwe '
        'orde van grootte is genoeg; zonder getal blijft het een mening.</li>'
        '<li><b>Kijk of je verplaatst of vermindert.</b> Gaat de belasting echt omlaag, '
        'of schuift hij naar een andere grens of een ander land?</li>'
        '<li><b>Benoem wie er nog meer aan draait.</b> Planetaire grenzen zijn '
        'zelden door één partij te verleggen; weten wie er nog aan tafel hoort is de '
        'helft van het werk.</li>'
        '</ol>')

    p.invulvelden(
        'Oefening: jouw grens',
        '<p>Pak je vraagstuk uit hoofdstuk 1 en de stofroute uit hoofdstuk 3 erbij.</p>',
        [
            ('h04-grenzen', 'Welke van de negen grenzen raakt jouw vraagstuk?',
             'Ook indirect telt mee'),
            ('h04-grootst', 'Op welke grens heb jij zelf de meeste invloed?',
             'Niet de grootste, maar de meest beïnvloedbare'),
            ('h04-getal', 'Welk getal hoort erbij, ruwweg?',
             'Per jaar of per eenheid; een orde van grootte volstaat'),
            ('h04-verplaats', 'Verminder je de belasting, of verplaats je hem?',
             'Wees hier eerlijk — dit is de lastigste vraag'),
            ('h04-wie', 'Wie draait er nog meer aan deze knop?',
             'Wie hoort er aan tafel?'),
        ])

    p.knoppenrij('Meenemen', '<p>Je grens en je getal komen terug in hoofdstuk 9.</p>')

    p.vraag(
        'Even checken',
        'Waarom is het naleven van planetaire grenzen economisch lastig, ondanks het '
        'belang op lange termijn?',
        [
            ('Omdat het vaak vraagt om offers op korte termijn die pas veel later '
             'renderen — en de kosten en baten bij verschillende partijen '
             'liggen.', True),
            ('Omdat planetaire grenzen alleen over ecologie gaan en geen economische '
             'kant hebben.', False),
            ('Omdat economische groei altijd in strijd is met ecologische '
             'duurzaamheid.', False),
            ('Omdat naleving alleen voordelen oplevert voor rijke landen.', False),
        ],
        feedback={
            'title': 'Even checken',
            'correct': '<p>Precies, en let op het tweede deel: het probleem is niet '
                       'alleen tijd maar ook verdeling. Wie de kosten draagt is vaak '
                       'niet wie de baten krijgt. Dat is waarom dit een politiek '
                       'vraagstuk is en niet alleen een technisch.</p>',
            '_incorrect': {'final': '<p>Nog niet. Groei en ecologie hoeven elkaar niet '
                                    'uit te sluiten — de ozonlaag laat zien dat het '
                                    'anders kan. De moeilijkheid zit in de timing van '
                                    'kosten en baten, en in wie ze draagt.</p>'},
            '_partlyCorrect': {'final': '<p>Nog niet helemaal.</p>'}
        })
