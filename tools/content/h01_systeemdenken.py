# -*- coding: utf-8 -*-
"""Waarom systeemdenken: het geheel zien in plaats van de losse delen."""


def bouw(p):
    p.tekst(
        'Waar deze cursus over gaat',
        '<p>Duurzaamheid is geen kwestie van één probleem oplossen. Het gaat over '
        'systemen waarin ecologie, economie en samenleving voortdurend op elkaar '
        'inwerken. Wie alleen naar losse onderdelen kijkt, mist de dynamiek eronder — '
        'en komt bedrogen uit.</p>'
        '<p>Deze cursus geeft je de fundamenten: hoe je in systemen leert kijken, waar '
        'de grenzen van de aarde liggen, hoe de circulaire economie werkt en wat '
        'klimaatverandering betekent voor het werk hier in Nederland. Vier '
        'onderwerpen, negen korte hoofdstukken, met bij elk een stappenplan en een '
        'oefening die je meteen op je eigen werk kunt toepassen.</p>')

    p.tekst(
        'Het verhaal van de katten in Borneo',
        '<p>In de jaren vijftig bestreed de Wereldgezondheidsorganisatie malaria op '
        'Borneo door huizen te besproeien met DDT. De muggen verdwenen, en de malaria '
        'nam af. Zo bekeken: probleem opgelost.</p>'
        '<p>Maar het gif kwam ook terecht in kakkerlakken. Die werden gegeten door '
        'hagedissen, en die door katten. De katten gingen dood. Zonder katten nam de '
        'rattenpopulatie explosief toe, en met de ratten kwamen tyfus en pest. '
        'Uiteindelijk moest het leger katten met parachutes boven het gebied '
        'droppen.</p>'
        '<p>Dit is geen anekdote over een blunder. Het is wat er stelselmatig gebeurt '
        'als je één schakel aanpakt zonder de rest van het systeem te zien. Elke '
        'ingreep werkt door in verbindingen die je niet in beeld had.</p>')

    p.video(
        'Systeemdenken in drie minuten',
        '<p>Deze korte animatie vertelt het verhaal van Borneo en laat zien waarom '
        'systeemdenken meer is dan een modewoord.</p>',
        aanbieder='vimeo', bron='99791239',
        titel='Systems thinking: a cautionary tale (cats in Borneo)',
        duur='3 minuten')

    p.tekst(
        'Wat systeemdenken is',
        '<p>Systeemdenken is een manier van kijken waarbij je let op <b>samenhang, '
        'interacties en patronen</b> binnen en tussen systemen, in plaats van op losse '
        'onderdelen. Je kijkt niet alleen naar de gebeurtenis die je ziet, maar naar '
        'de structuur die hem voortbrengt.</p>'
        '<p>Dat levert drie dingen op die je anders mist:</p>'
        '<ul>'
        '<li><b>Verbanden.</b> Je ziet dat een maatregel op het ene vlak doorwerkt op '
        'het andere — en waar dat pijn gaat doen.</li>'
        '<li><b>Terugkoppelingen.</b> Je ziet welke processen zichzelf versterken of '
        'juist afremmen, en waarom sommige problemen blijven terugkomen.</li>'
        '<li><b>Hefbomen.</b> Je ziet waar een kleine ingreep veel effect heeft, in '
        'plaats van hard duwen op de plek waar het het meest zichtbaar is.</li>'
        '</ul>')

    p.video(
        'En wat is duurzaamheid dan precies?',
        '<p>Een heldere visuele uitleg van wat duurzaamheid inhoudt en waarom de drie '
        'dimensies onlosmakelijk samenhangen.</p>',
        aanbieder='youtube', bron='zx04Kl8y4dE',
        titel='What is Sustainability (UCLA)',
        duur='3 minuten, Engelstalig')

    p.accordeon(
        'Vijf begrippen die de rest van de cursus dragen',
        '<p>Deze kom je vanaf hier steeds tegen. Klap ze open en kom er later op '
        'terug als een term je ontglipt.</p>',
        [
            {'title': 'Systeemdenken',
             'body': '<p>Een manier van kijken waarbij je let op samenhang, '
                     'interacties en patronen binnen en tussen systemen, in plaats van '
                     'op losse onderdelen.</p>'},
            {'title': 'Duurzaamheid',
             'body': '<p>Het streven naar balans tussen ecologische, economische en '
                     'sociale belangen, zodat zowel huidige als toekomstige generaties '
                     'kunnen voorzien in hun behoeften. De klassieke formulering komt '
                     'uit het Brundtland-rapport van de Verenigde Naties '
                     '(1987).</p>'},
            {'title': 'Triple Bottom Line',
             'body': '<p>Een benadering waarbij organisaties hun prestaties meten op '
                     'drie vlakken: <i>people</i> (sociaal), <i>planet</i> '
                     '(ecologisch) en <i>profit</i> (economisch). Het maakt zichtbaar '
                     'dat winst niet de enige uitkomst is die telt.</p>'},
            {'title': 'SDG’s — Sustainable Development Goals',
             'body': '<p>Zeventien internationale doelen van de Verenigde Naties voor '
                     'een duurzame, eerlijke en welvarende wereld in 2030. Ze '
                     'benadrukken dat milieu, maatschappij en economie aan elkaar vast '
                     'zitten. Je vindt ze op '
                     '<a href="https://sdgs.un.org/goals" target="_blank" '
                     'rel="noopener">sdgs.un.org/goals</a>.</p>'},
            {'title': 'Systeemgrenzen',
             'body': '<p>De afbakening van wat je wél en niet meeneemt in je analyse. '
                     'Dit is de meest onderschatte keuze die je maakt: waar je de '
                     'grens legt, bepaalt welke effecten je ziet en welke buiten beeld '
                     'blijven — en dus welke oplossing eruit rolt.</p>'},
        ])

    p.aandacht(
        'Systeemgrenzen zijn een keuze, geen gegeven',
        '<p>Reken je de CO₂-uitstoot van een elektrische auto alleen tijdens het '
        'rijden, dan is hij schoon. Neem je de productie van de accu mee, dan wordt '
        'het beeld anders. Neem je ook de stroommix mee waarmee hij laadt, dan '
        'verandert het opnieuw.</p>'
        '<p>Geen van die drie is fout. Maar wie zijn systeemgrens niet expliciet maakt, '
        'kan elk gewenst antwoord produceren — en dat gebeurt vaker dan je denkt. '
        'Benoem daarom altijd waar je de grens legt en waarom.</p>')

    p.tekst(
        'Stappenplan: systeemdenkend naar een vraagstuk kijken',
        '<p>Zes stappen die je op vrijwel elk duurzaamheidsvraagstuk kunt loslaten. '
        'Reken op een uur voor een eerste ronde.</p>'
        '<ol>'
        '<li><b>Beschrijf wat je ziet gebeuren, niet wat je denkt dat het probleem '
        'is.</b> "Er ligt veel afval bij de containers" is een waarneming; "mensen '
        'zijn te lui om te scheiden" is al een verklaring. Begin bij de waarneming.</li>'
        '<li><b>Bepaal je systeemgrens en schrijf hem op.</b> Wat neem je mee, wat '
        'laat je buiten beschouwing, en waarom? Dit is stap twee, niet een detail voor '
        'later.</li>'
        '<li><b>Benoem de onderdelen en wie erover gaat.</b> Welke partijen, processen '
        'en middelen zitten binnen je grens? Wie beslist waarover?</li>'
        '<li><b>Teken de verbindingen.</b> Wat beïnvloedt wat, en in welke richting? '
        'Gebruik pijlen; het hoeft niet mooi te zijn.</li>'
        '<li><b>Zoek de terugkoppelingen.</b> Zit er ergens een lus die zichzelf '
        'versterkt of afremt? Daar zit meestal de reden dat het probleem blijft '
        'bestaan.</li>'
        '<li><b>Zoek de hefboom.</b> Waar zou een kleine ingreep het meeste effect '
        'hebben? Dat is zelden de plek waar het probleem het duidelijkst zichtbaar '
        'is.</li>'
        '</ol>')

    p.invulvelden(
        'Oefening: jouw eerste systeemanalyse',
        '<p>Neem een vraagstuk uit je eigen werk of studie — iets waar je zelf mee te '
        'maken hebt. Loop de zes stappen langs. Deze analyse gebruik je verderop in de '
        'cursus opnieuw, dus kies iets waar je echt iets mee wil.</p>',
        [
            ('h01-vraagstuk', 'Stap 1 — Wat zie je gebeuren?',
             'Een waarneming, nog geen verklaring'),
            ('h01-grens', 'Stap 2 — Waar leg je de systeemgrens, en waarom?',
             'Wat neem je mee, wat laat je erbuiten?'),
            ('h01-onderdelen', 'Stap 3 — Welke partijen en processen zitten erbinnen?',
             'En wie gaat waarover?'),
            ('h01-verbindingen', 'Stap 4 — Welke verbindingen zie je?',
             'Wat beïnvloedt wat, en in welke richting?'),
            ('h01-lus', 'Stap 5 — Zit er een terugkoppeling in die het probleem in '
             'stand houdt?',
             'Iets dat zichzelf versterkt of afremt'),
            ('h01-hefboom', 'Stap 6 — Waar zit volgens jou de hefboom?',
             'Kleine ingreep, groot effect'),
        ])

    p.knoppenrij(
        'Meenemen',
        '<p>Kopieer je analyse naar je eigen aantekeningen. In hoofdstuk 9 werk je hem '
        'af tot een onderbouwde keuze.</p>')

    p.vraag(
        'Even checken',
        'Een stad kampt met luchtvervuiling door autoverkeer, met gezondheidsklachten '
        'en economische kosten als gevolg. Wat is een systeemdenkende aanpak?',
        [
            ('De verbanden tussen verkeersbeleid, ruimtelijke ordening en '
             'gezondheidszorg analyseren en daar samenhangende maatregelen op '
             'baseren.', True),
            ('De boetes voor vervuilende voertuigen verhogen om gedrag af te '
             'dwingen.', False),
            ('Inzetten op schonere brandstoffen, en de rest laten voor wat het is.', False),
            ('Meer bomen planten om de luchtkwaliteit te verbeteren.', False),
        ],
        feedback={
            'title': 'Even checken',
            'correct': '<p>Precies. De andere drie zijn allemaal ingrepen op één plek '
                       'in het systeem. Ze kunnen best werken, maar zonder zicht op de '
                       'verbanden weet je niet wat je elders veroorzaakt — en dat is '
                       'precies wat er in Borneo misging.</p>',
            '_incorrect': {'final': '<p>Nog niet. Alle drie de andere antwoorden pakken '
                                    'één schakel aan. Dat is geen systeemdenken maar '
                                    'symptoombestrijding: je verplaatst het probleem in '
                                    'plaats van het op te lossen.</p>'},
            '_partlyCorrect': {'final': '<p>Nog niet helemaal.</p>'}
        })
