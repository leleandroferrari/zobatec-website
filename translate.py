import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

def repl(pattern, replacement):
    global html
    html = re.sub(pattern, replacement, html, flags=re.MULTILINE | re.DOTALL)

# Header
repl(r'lang="en"', r'lang="de-CH"')
repl(r'<title>Manukit.*?<\/title>', r'<title>Zobatec – CNC Lohnfertigung & mechanische Bearbeitung</title>')
repl(r'name="description" content="[^"]+"', r'name="description" content="Ihre kompetente CNC-Fertigung in Bubikon: Fräsen, Drehen, Hartbearbeitung sowie Kleinserien & Einzelteile. Schnell, unkompliziert, termingerecht für B2B."')
repl(r'property="og:title" content="[^"]+"', r'property="og:title" content="Zobatec – CNC Lohnfertigung & mechanische Bearbeitung"')
repl(r'property="og:description" content="[^"]+"', r'property="og:description" content="Ihre kompetente CNC-Fertigung in Bubikon: Fräsen, Drehen, Hartbearbeitung sowie Kleinserien & Einzelteile. Schnell, unkompliziert, termingerecht für B2B."')
repl(r'property="twitter:title" content="[^"]+"', r'property="twitter:title" content="Zobatec – CNC Lohnfertigung & mechanische Bearbeitung"')
repl(r'property="twitter:description" content="[^"]+"', r'property="twitter:description" content="Ihre kompetente CNC-Fertigung in Bubikon: Fräsen, Drehen, Hartbearbeitung sowie Kleinserien & Einzelteile. Schnell, unkompliziert, termingerecht für B2B."')

# Menus
html = html.replace('>About<', '>Über uns<')
html = html.replace('>services<', '>Dienstleistungen<')
html = html.replace('>Services<', '>Dienstleistungen<')
html = html.replace('>PAGES<', '>SEITEN<')
html = html.replace('>Main Pages<', '>Hauptseiten<')
html = html.replace('>Projects<', '>Projekte<')
html = html.replace('>Product<', '>Produkte<')
html = html.replace('>Blog<', '>Blog<')
html = html.replace('>Company<', '>Unternehmen<')
html = html.replace('>Contact Us<', '>Kontakt<')
html = html.replace('>Services single<', '>Dienstleistung Detail<')
html = html.replace('>Blogs single<', '>Blog Detail<')
html = html.replace('>Projects Single<', '>Projekt Detail<')
html = html.replace('>PRoducts Single<', '>Produkt Detail<')
html = html.replace('>Utility Pages<', '>Hilfsseiten<')
html = html.replace('>Password Protected<', '>Passwortgeschützt<')
html = html.replace('>Changelog<', '>Ziele & Log<')
html = html.replace('>Style Guide<', '>Styleguide<')
html = html.replace('>404 Not found<', '>404 Fehler<')
html = html.replace('>License<', '>Lizenzen<')
html = html.replace('>blogs<', '>Blog<')
html = html.replace('>Manufacturing for industrial and B2B service companies Webflow template.<', '>Ihre kompetente CNC-Fertigung in Bubikon für Industrie- und B2B-Kunden.<')
html = html.replace('>Get Template<', '>Kontakt aufnehmen<')

# Hero section
html = html.replace('>INDUSTRIAL &amp; B2B SERVICES<', '>PRÄZISE CNC LOHNFERTIGUNG<')
html = html.replace('>Built to support complex industrial operations<', '>CNC-Bearbeitung auf höchstem Niveau<')
html = html.replace('>We deliver reliable engineering, construction, and industrial services that help businesses build, scale, and operate with confidence.<', '>Wir sind Zobatec aus Bubikon. Schnell, unkompliziert und termingerecht fertigen wir Ihre Einzelteile und Kleinserien. Persönliche Kundennähe und höchste Qualität stehen bei uns an erster Stelle.<')
html = html.replace('>View all Projects<', '>Unsere Fertigung<')
html = html.replace('>Reducing Downtime Across Industrial Operations<', '>Flexible & motivierte Umsetzung für B2B Industrie<')
html = html.replace('>Contact us<', '>Kontaktieren Sie uns<')

# Who We Are
html = html.replace('>WHO WE ARE<', '>ÜBER ZOBATEC<')
html = html.replace('>proven on the ground<', '>Frisch, motiviert, flexibel<')
html = html.replace('>We support industrial and B2B projects with structured processes, experienced teams, and a focus on safe, dependable execution from start to finish. Our work is grounded in clear planning, disciplined site coordination, and\n                                consistent quality control, ensuring projects are delivered to specification, on schedule, and with minimal operational risk.<', '>Als junge, professionelle mechanische Werkstatt in der Schweiz fertigen wir im Lohnverfahren für Ihre anspruchsvollsten Projekte. Ob Maschinenbau oder Medizinaltechnik – auf uns können Sie zählen. Erleben Sie den Unterschied einer direkten, unkomplizierten Zusammenarbeit. Wir legen grossen Wert auf persönlichen Kundenkontakt und eine exakte, termingerechte Lieferung.<')
html = html.replace('>about us<', '>Mehr über uns<')
html = html.replace('>Trusted by Industry Partners<', '>Referenzen aus der Schweizer Industrie<')

# Capabilities
html = html.replace('>CORE MANUFACTURING SERVICES<', '>UNSERE DIENSTLEISTUNGEN<')
html = html.replace('>Capabilities That Scale<', '>Kernkompetenzen in der Zerspanung<')
html = html.replace('>Our capabilities support a broad range of technical requirements, materials, and industry standards, &nbsp;helping you get the parts and products you depend on.<', '>Dank modernster Technologien und hohem Fachwissen bewältigen wir auch anspruchsvolle Teile. Vertrauen Sie auf Schweizer Präzision – massgeschneidert für Ihre spezifischen Anforderungen.<')

html = html.replace('>Assembly &amp; Finishing<', '>CNC Fräsen<')
html = html.replace('>Part integration, surface treatment, and final checks before delivery.<', '>Präzise 3- bis 5-Achs-Fräsbearbeitung für komplexe Geometrien und Baugruppen.<')

html = html.replace('>Metal Forming &amp; Fabrication<', '>CNC Drehen<')
html = html.replace('>Shaping, cutting, and joining metal parts for functional industrial use.<', '>Komplexe Drehteile nach Mass, effizient und mit höchsten Genauigkeiten gefertigt.<')

html = html.replace('>Plastic Production<', '>Hartbearbeitung<')
html = html.replace('>Molded and fabricated plastic components for technical applications.<', '>Bearbeitung von gehärteten Stählen und anspruchsvollen Materialien für maximale Haltbarkeit.<')

html = html.replace('>Precision Machining<', '>Kleinserien &amp; Einzelteile<')
html = html.replace('>Component manufacturing built around tolerance control and material accuracy.<', '>Massgeschneiderte Produktion von Prototypen, Ersatzteilen sowie flexiblen Kleinserien.<')

# Output at Scale
html = html.replace('>OUTPUT AT SCALE<', '>QUALITÄT & ZUVERLÄSSIGKEIT<')
html = html.replace('>Measured Production Output<', '>Was uns auszeichnet<')
html = html.replace('>Key figures showing production volume and operational consistency.<', '>Zuverlässige Lieferung und hohe Kundenzufriedenheit stehen bei Zobatec im Fokus.<')

html = html.replace('>KEY STAT · 001<', '>STATISTIK · 001<')
html = html.replace('>Production Output<', '>Erfolgreiche Einsätze<')
html = html.replace('>Structural Components Produced<', '>Bearbeitete Bauteile<')

html = html.replace('>KEY STAT · 002<', '>STATISTIK · 002<')
html = html.replace('>Manufacturing Delivery<', '>Auftragsausführung<')
html = html.replace('>Machined Parts Delivered<', '>Ausgelieferte Präzisionsteile<')

html = html.replace('>KEY STAT · 003<', '>STATISTIK · 003<')
html = html.replace('>Delivery Performance<', '>Termintreue<')
html = html.replace('>On-Time Production Rate<', '>Termingerechte Lieferungen<')

html = html.replace('>KEY STAT · 004<', '>STATISTIK · 004<')
html = html.replace('>Built on Reliability<', '>Kundenfokus<')
html = html.replace('>Delivery Performance Accuracy<', '>Kundenzufriedenheit<')

# What We Produce
html = html.replace('>WHAT WE PRODUCE<', '>FERTIGUNGSPRODUKTE<')
html = html.replace('>Manufactured Components<', '>Unsere Fertigungsteile<')
html = html.replace('>A snapshot of the types of components and assemblies we produce across different industries and specifications.<', '>Wir fertigen für verschiedenste Branchen von Prototypen bis zu fertigen Einzelteilen – ganz nach ihren Spezifikationen.<')

html = html.replace('>Structural Metal Components<', '>Mechanische Bauteile<')
html = html.replace('>Load-bearing and fabricated steel elements<', '>Spezialteile für den modernen Maschinenbau<')
html = html.replace('>Load Bearing<', '>Präzision<')
html = html.replace('>Fabrication<', '>Maschinenbau<')

html = html.replace('>Precision Machined Parts<', '>Feinmechanik<')
html = html.replace('>Tight-tolerance mechanical components<', '>Hochpräzise Komponenten für die Medizinaltechnik<')
html = html.replace('>Machining<', '>Zerspanung<')
html = html.replace('>CNC<', '>Medtech<')

html = html.replace('>Assembled Industrial Sub-Units<', '>Spezialanfertigungen<')
html = html.replace('>Pre-assembled sections ready for integration<', '>Spezifische Lösungen nach Ihren Vorgaben<')
html = html.replace('>Modular<', '>Flexibel<')
html = html.replace('>Systems<', '>Einzelstücke<')

# Application Areas
html = html.replace('>APPLICATION AREAS<', '>EINSATZGEBIETE<')
html = html.replace('>Where Our Work Is Used<', '>Branchen & Anwendungen<')
html = html.replace('>Our manufacturing output supports systems, equipment, and products used in demanding operating environments.<', '>Unsere Teile und Komponenten finden in den unterschiedlichsten, anspruchsvollen Industrien ihre Anwendung.<')

html = html.replace('>Industrial Equipment<', '>Maschinenbau<')
html = html.replace('>Manufactured components used in heavy-duty production, material handling, and industrial processing systems.<', '>Fertigung von essenziellen Bauteilen, Sonderanfertigungen und Baugruppen für Produktionsanlagen.<')

html = html.replace('>automotive systems<', '>Automations- &' ' Robotik<') # Intentionally merged string
html = html.replace('>Precision parts supporting vehicle structures, mechanical assemblies, and automotive manufacturing operations.<', '>Hochpräzise Zerspanungskomponenten für Robotersysteme und automatisierte Fertigung.<')

html = html.replace('>Energy Infrastructure<', '>Apparatebau & Werkzeugbau<')
html = html.replace('>Components designed for power generation, transmission, processing, and large-scale energy systems.<', '>Beständige Konstruktionen und extrem präzise Einsätze für spezialisierte Werkzeuge.<')

html = html.replace('>Medical Manufacturing<', '>Medizinaltechnik<')
html = html.replace('>High-precision components produced to meet strict quality and regulatory requirements in medical applications.<', '>Qualitätsgeprüfte CNC-Teile für medizinaltechnische Geräte und chirurgische Instrumente.<')

# Operational Focus
html = html.replace('>OPERATIONAL FOCUS<', '>IHR VORTEIL<')
html = html.replace('>Why Clients Stay<', '>Warum Zobatec?<')
html = html.replace('>Our value is not speed alone—it’s control, predictability, and the ability to meet expectations without surprises.<', '>Persönlicher Kontakt, schnelle Reaktionszeiten und kompromisslose Zuverlässigkeit. Bei uns steht Ihr Auftrag im Zentrum.<')
html = html.replace('>work with us<', '>Ihre Anfrage<')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
