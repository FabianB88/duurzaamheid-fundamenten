# -*- coding: utf-8 -*-
"""De R-ladder en circulaire businessmodellen, met de textielcasus."""


def bouw(p):
    p.tekst(
        'Niet alle circulariteit is evenveel waard',
        '<p>"We recyclen" klinkt circulair, maar recyclen staat vrij laag op de '
        'ladder. Bij elke recyclingronde verlies je kwaliteit en kost het energie om '
        'materiaal weer bruikbaar te maken. Wat je níet hoeft te produceren, is altijd '
        'beter dan wat je goed verwerkt.</p>'
        '<p>Daar gaat de <b>R-ladder</b> over: een rangorde van circulaire strategieën '
        'waarin hoger betekent dat er meer waarde behouden blijft. Het is het meest '
        'praktische gereedschap uit deze cursus, omdat je er elke maatregel langs kunt '
        'leggen en meteen ziet of je aan de goede kant bezig bent.</p>')

    p.beeld(
        'r-ladder.svg',
        alt='Een trap met zes treden, van hoog naar laag. Bovenaan Refuse, weigeren: '
            'het product of de verpakking helemaal niet gebruiken. Daaronder Reduce, '
            'minder gebruiken. Dan Reuse, opnieuw gebruiken. Dan Repair, repareren. '
            'Dan Recycle, tot nieuwe grondstof verwerken. Onderaan Recover, energie '
            'terugwinnen door verbranding. Een pijl langs de trap geeft aan dat hoger '
            'op de trap meer waardebehoud betekent en lager meer verlies.',
        onderschrift='Hoe hoger op de trap, hoe meer waarde je behoudt. Recyclen is '
                     'nuttig, maar het is niet de top.')

    p.accordeon(
        'De treden, met voorbeelden uit organisaties',
        '<p>Bij elke trede staat wat het in de praktijk betekent voor een organisatie '
        'als de jouwe.</p>',
        [
            {'title': 'Refuse — weigeren',
             'body': '<p>Onnodige producten of verpakkingen helemaal niet gebruiken. '
                     'Dit voorkomt afval bij de bron en is daarom de krachtigste '
                     'trede — en meestal ook de goedkoopste.</p>'
                     '<p><b>Voorbeeld:</b> geen plastic verpakking meer inkopen, maar '
                     'kiezen voor leveren zonder verpakking of in retouremballage.</p>'},
            {'title': 'Reduce — verminderen',
             'body': '<p>Minder grondstof en minder afval per eenheid product. Via '
                     'efficiëntere processen, ander materiaal, of simpelweg minder '
                     'bestellen.</p>'
                     '<p><b>Voorbeeld:</b> een productieproces aanpassen zodat er '
                     'minder restmateriaal ontstaat.</p>'},
            {'title': 'Reuse — hergebruiken',
             'body': '<p>Producten of materialen opnieuw inzetten in dezelfde functie. '
                     'De levensduur van de grondstof rekt op zonder dat er iets '
                     'bewerkt hoeft te worden.</p>'
                     '<p><b>Voorbeeld:</b> herbruikbare transportverpakking in plaats '
                     'van wegwerpdozen.</p>'},
            {'title': 'Repair — repareren',
             'body': '<p>Kapotte producten herstellen in plaats van vervangen. Dit '
                     'vraagt vaak om een ontwerp waarin onderdelen los te krijgen '
                     'zijn, en om iemand die het kan.</p>'
                     '<p><b>Voorbeeld:</b> een reparatieservice aanbieden voor oudere '
                     'modellen in plaats van klanten naar een nieuw exemplaar te '
                     'sturen.</p>'},
            {'title': 'Recycle — recyclen',
             'body': '<p>Afgedankt materiaal verwerken tot nieuwe grondstof. Nuttig, '
                     'maar er gaat kwaliteit verloren en het kost energie. Zie het als '
                     'het vangnet, niet als het doel.</p>'
                     '<p><b>Voorbeeld:</b> textielafval inzamelen en verwerken tot '
                     'nieuwe garens.</p>'},
            {'title': 'Recover — terugwinnen',
             'body': '<p>Energie terugwinnen door verbranding. De onderste trede: het '
                     'materiaal is weg, alleen de warmte blijft over. Beter dan '
                     'storten, en verder een teken dat het eerder in de keten is '
                     'misgegaan.</p>'},
        ])

    p.aandacht(
        'De valkuil: beginnen bij Recycle',
        '<p>Vrijwel elke organisatie begint onderaan de ladder, omdat recyclen '
        'zichtbaar is, meetbaar en niemand pijn doet. Een aparte bak neerzetten voelt '
        'als vooruitgang.</p>'
        '<p>Maar de treden erboven leveren veel meer op en kosten vaak minder. Ze zijn '
        'alleen ongemakkelijker, want ze raken aan wat je inkoopt, hoe je ontwerpt en '
        'wat je klanten gewend zijn. Begin daarom bovenaan en werk naar beneden, niet '
        'andersom.</p>')

    p.accordeon(
        'Drie businessmodellen die het mogelijk maken',
        '<p>Een strategie werkt pas als er een verdienmodel onder zit. Deze drie kom '
        'je het vaakst tegen.</p>',
        [
            {'title': 'Product-as-a-Service',
             'body': '<p>De producent blijft eigenaar; de klant betaalt voor het '
                     'gebruik. Daarmee draaien de prikkels om: waar het klassieke '
                     'model beloont dat een product snel wordt vervangen, verdient de '
                     'aanbieder hier juist aan lang meegaan en makkelijk '
                     'repareren.</p>'
                     '<p><b>Voorbeeld:</b> Signify (het vroegere Philips Lighting) '
                     'verkoopt licht in plaats van lampen: de klant betaalt voor '
                     'verlichting, Signify blijft eigenaar van de armaturen en '
                     'haalt ze aan het eind terug. Hoe langer een armatuur '
                     'meegaat, hoe beter dat uitkomt voor de leverancier — precies '
                     'andersom dan bij verkoop per stuk.</p>'
                     '<p>Let op: het model is geen garantie. Zie de textielcasus '
                     'hieronder.</p>'},
            {'title': 'Deelplatforms',
             'body': '<p>Producten gezamenlijk gebruiken in plaats van individueel '
                     'bezitten. Hetzelfde aantal mensen bediend met minder spullen — '
                     'en dus minder productie.</p>'
                     '<p><b>Voorbeeld:</b> Peerby, waarop je gereedschap en apparaten '
                     'leent van buurtgenoten. Ook binnen een organisatie werkt dit: '
                     'één goede boormachine per afdeling in plaats van vijf.</p>'},
            {'title': 'Levensduurverlenging',
             'body': '<p>Repareren, opknappen en upgraden in plaats van vervangen. '
                     'Vraagt om demonteerbaar ontwerp én om een cultuur waarin '
                     'repareren normaal is.</p>'
                     '<p><b>Voorbeeld:</b> het Worn Wear-programma van Patagonia, waar '
                     'gebruikte kleding wordt ingezameld, hersteld en opnieuw '
                     'verkocht. iFixit doet hetzelfde van onderaf, met handleidingen '
                     'waarmee mensen zelf kunnen repareren.</p>'},
        ])

    p.tekst(
        'Casus: textiel in Nederland',
        '<p>Textiel laat de hele ladder in één sector zien. Nederland produceert '
        'jaarlijks grote hoeveelheden textielafval, terwijl er relatief weinig van '
        'wordt gerecycled. Fast fashion, korte levensduur en mengweefsels maken '
        'verwerking lastig — een katoen-polyestermix is nauwelijks te scheiden.</p>'
        '<p>Tegelijk gebeurt er van alles. <b>Loop.a life</b> maakt nieuwe truien van '
        'oude kleding, zonder water en zonder verfstoffen, en produceert lokaal om '
        'transport te beperken.</p>'
        '<p>En dan is er <b>MUD Jeans</b>, jarenlang hét Nederlandse voorbeeld '
        'van Product-as-a-Service: je leasede een spijkerbroek en stuurde hem na '
        'gebruik terug. Het merk stopte met dat leasemodel omdat het op schaal niet '
        'rendabel bleek, ging verder met repareren, doorverkopen en recyclen, en '
        'werd op 5 augustus 2026 failliet verklaard. Een doorstart is niet '
        'uitgesloten.</p>'
        '<p>Dat is geen voetnoot maar de kern van dit hoofdstuk. Een hoge trede op '
        'de R-ladder is ecologisch gezien beter, maar alleen als het verdienmodel '
        'eronder standhoudt. En een sector kantelt niet van goede voorbeelden '
        'alleen — zolang de omgeving fast fashion blijft belonen, blijft de '
        'koploper klein en kwetsbaar. Daarover gaat het volgende deel van de '
        'cursus.</p>')

    p.tekst(
        'Stappenplan: kies een R-strategie die je echt kunt uitvoeren',
        '<ol>'
        '<li><b>Begin bovenaan de ladder, niet onderaan.</b> Kun je dit product of '
        'deze verpakking helemaal weigeren? Zo niet, kun je minder gebruiken? Ga pas '
        'omlaag als een trede echt niet kan.</li>'
        '<li><b>Schrijf per trede op waaróm hij niet kan.</b> Vaak blijkt de reden '
        '"zo doen we het altijd" te zijn, en dat is geen reden.</li>'
        '<li><b>Kies de hoogste trede die haalbaar is</b> en formuleer hem als één '
        'concrete actie met een eigenaar.</li>'
        '<li><b>Zoek het verdienmodel erbij.</b> Wie betaalt, wie bespaart, en wie '
        'moet er iets anders gaan doen? Zonder antwoord blijft het een goed '
        'voornemen.</li>'
        '<li><b>Bepaal hoe je het meet.</b> Eén getal is genoeg: kilo’s, stuks, '
        'euro’s. Zonder meting weet je over een jaar niet of het werkte.</li>'
        '</ol>')

    p.invulvelden(
        'Oefening: klim de ladder af',
        '<p>Neem het product uit hoofdstuk 5 en loop de treden van boven naar beneden '
        'langs.</p>',
        [
            ('h06-refuse', 'Refuse — kan het helemaal weg? Zo nee, waarom niet?',
             'Wees streng; "dat kan niet" vraagt een reden'),
            ('h06-reduce', 'Reduce — kan er minder van? Hoeveel?',
             'Probeer een getal te noemen'),
            ('h06-reuse', 'Reuse — kan het opnieuw gebruikt worden, en door wie?', ''),
            ('h06-repair', 'Repair — is het te repareren? Wat zou daarvoor moeten '
             'veranderen?', ''),
            ('h06-keuze', 'Welke trede kies je, en wat is de ene concrete actie?',
             'Met een eigenaar erbij'),
            ('h06-model', 'Wie betaalt, wie bespaart, wie moet iets anders gaan doen?',
             'Het verdienmodel eronder'),
            ('h06-meten', 'Welk getal ga je meten?',
             'Kilo’s, stuks of euro’s — één is genoeg'),
        ])

    p.knoppenrij('Meenemen', '<p>Zet je actie en je meetgetal in je aantekeningen; ze komen terug in hoofdstuk 9.</p>')

    p.koppelvraag(
        'Even checken',
        'Koppel elke maatregel aan de R-strategie waar hij bij hoort.',
        rijen=[
            ('Geen gratis plastic tasjes meer aanbieden', 'Refuse'),
            ('Herbruikbare kratten gebruiken voor intern transport', 'Reuse'),
            ('Een kapotte laptop laten maken in plaats van vervangen', 'Repair'),
            ('Ingezameld textiel verwerken tot nieuwe garens', 'Recycle'),
        ],
        opties=['Refuse', 'Reuse', 'Repair', 'Recycle'],
        feedback={
            'title': 'Even checken',
            'correct': '<p>Goed. Merk op dat de eerste twee voorkómen dat er iets '
                       'nieuws nodig is, en de laatste pas in actie komt als het '
                       'product al is afgedankt. Dat is precies het verschil tussen '
                       'boven en onder aan de ladder.</p>',
            '_incorrect': {'final': '<p>Nog niet. Vraag je per maatregel af: voorkom ik '
                                    'hier gebruik, verleng ik de levensduur, of '
                                    'verwerk ik iets dat al afval is?</p>'},
            '_partlyCorrect': {'final': '<p>Deels goed. Kijk nog eens naar de regels '
                                        'die je fout had.</p>'}
        })
