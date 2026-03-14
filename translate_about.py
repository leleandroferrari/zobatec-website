import re

with open('about-us.html', 'r', encoding='utf-8') as f:
    html = f.read()

def repl(pattern, replacement):
    global html
    html = re.sub(pattern, replacement, html, flags=re.MULTILINE | re.DOTALL)

# Header
repl(r'lang="en"', r'lang="de-CH"')
repl(r'<title>About Manukit.*?<\/title>', r'<title>Über Zobatec – Lohnfertigung & mechanische Bearbeitung</title>')
repl(r'name="description" content="[^"]+"', r'name="description" content="Erfahren Sie mehr über Zobatec: CNC Fräsen, CNC Drehen, Hartbearbeitung und Einzelteilfertigung mit Schweizer Präzision und Flexibilität."')
repl(r'property="og:title" content="[^"]+"', r'property="og:title" content="Über Zobatec – Lohnfertigung & mechanische Bearbeitung"')
repl(r'property="og:description" content="[^"]+"', r'property="og:description" content="Erfahren Sie mehr über Zobatec: CNC Fräsen, CNC Drehen, Hartbearbeitung und Einzelteilfertigung mit Schweizer Präzision und Flexibilität."')
repl(r'property="twitter:title" content="[^"]+"', r'property="twitter:title" content="Über Zobatec – Lohnfertigung & mechanische Bearbeitung"')
repl(r'property="twitter:description" content="[^"]+"', r'property="twitter:description" content="Erfahren Sie mehr über Zobatec: CNC Fräsen, CNC Drehen, Hartbearbeitung und Einzelteilfertigung mit Schweizer Präzision und Flexibilität."')

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

# About Banner
html = html.replace('>Powering Industry Through Expertise and Execution.<', '>Schweizer Präzision durch Fachwissen und Flexibilität.<')
html = html.replace('>We deliver reliable engineering, construction, and industrial services that help businesses build, scale, and operate with confidence.<', '>Wir bieten zuverlässige CNC-Lohnfertigung und mechanische Bearbeitung. Schnell, unkompliziert und termingerecht.<')

# Who We Are
html = html.replace('>WHO WE ARE<', '>ÜBER ZOBATEC<')
html = html.replace('>proven on the ground<', '>Frisch, motiviert, flexibel<')
html = html.replace('>We support industrial and B2B projects with structured processes, experienced teams, and a focus on safe, dependable execution from start to finish. Our work is grounded in clear planning, disciplined site coordination, and\n                                consistent quality control, ensuring projects are delivered to specification, on schedule, and with minimal operational risk.<', '>Wir unterstützen Industrie- und B2B-Projekte mit hoher Flexibilität, modernen Prozessen und einem starken Fokus auf Kundennähe. Unsere Arbeit basiert auf klarer Kommunikation und konsequenter Qualitätssicherung, damit Ihre Bauteile pünktlich und exakt nach Spezifikation geliefert werden.<')
html = html.replace('>about us<', '>Mehr über uns<')
html = html.replace('>Trusted by Industry Partners<', '>Referenzen aus der Schweizer Industrie<')

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

# Our Approach
html = html.replace('>Our Approach<', '>UNSER ANSATZ<')
html = html.replace('>Planning to Performance<', '>Von der Vorbereitung zum Präzisionsteil<')
html = html.replace('>A snapshot of the types of components and assemblies we produce across different industries and specifications.<', '>Wie wir arbeiten: Klar strukturiert und qualitätsbewusst vom ersten Kontakt bis zur Auslieferung.<')

html = html.replace('>Strategic Planning<', '>Auftragsklärung<')
html = html.replace('>We start by understanding project goals, site conditions, and potential risks. \xa0from the beginning.<', '>Wir starten mit dem genauen Verständnis Ihrer Anforderungen, Bauteilspezifikationen und Wunschtermine.<')

html = html.replace('>Skilled Execution<', '>Bearbeitung<')
html = html.replace('>Our experienced team delivers each phase with precision and care. We follow proven workflows, industry standards.<', '>Dank fortschrittlicher Zerspanungstechnologien produzieren wir effizient und in höchster Schweizer Fertigungsgüte.<')

html = html.replace('>Quality &amp; Accountability<', '>Qualität &amp; Kontrolle<')
html = html.replace('>We monitor progress closely and maintain strict quality control throughout\xa0\xa0and accountability ensure reliable.<', '>Wir überwachen den gesamten Prozess und führen exakte Endkontrollen durch, bevor die Teile unser Haus verlassen.<')

# Our Vision
html = html.replace('>Our Vision<', '>UNSERE VISION<')
html = html.replace('>Vision Built on Reliability<', '>Partnerschaft und Verlässlichkeit<')
html = html.replace('>Key figures showing production volume and operational consistency.<', '>Zobatec steht für direkte Kommunikation und hohe Flexibilität im Maschinen- und Apparatebau.<')

html = html.replace('>Long-Term Partnerships<', '>Langfristige Partnerschaften<')
html = html.replace('>Empowering smarter investing through digital platforms simplify wealth management.<', '>Wir streben nach vertrauensvollen Kundenbeziehungen und massgeschneiderten CNC-Lösungen.<')

html = html.replace('>Sustainable Industrial Growth<', '>Effizienz & Wirtschaftlichkeit<')
html = html.replace('>Streamlining processes with intelligent systems that boost efficiency, reduce costs, and drive.<', '>Optimierte Fertigungsprozesse, um die Durchlaufzeiten zu verkürzen und Ihre Kosten zu senken.<')

html = html.replace('>Excellence Through Execution<', '>Kompromisslose Ausführung<')
html = html.replace('>Innovative technologies driving sustainable growth through clean energy and eco-friendly solutions.<', '>Modernste Fertigungsverfahren garantieren die geforderte Präzision auf den Mikrometerbereich.<')

html = html.replace('>Trusted Industry Partner<', '>Ihr B2B Experte<')
html = html.replace('>Advancing healthcare through innovative biological research, diagnostics, and life-saving.<', '>Zuverlässige Produktion für anspruchsvolle Branchen wie Medizinaltechnik und Automation.<')

html = html.replace('>Sustainable Growth<', '>Flexibel als Startup<')
html = html.replace('>We support industrial and B2B projects with structured processes, experienced teams.<', '>Kurze Wege und direkte Entscheidungen ermöglichen es uns flexibel auf Änderungen zu reagieren.<')

html = html.replace('>Safety First Culture<', '>Qualitätskultur<')
html = html.replace('>A focus on safe, dependable execution from start to finish work is grounded in clear planning.<', '>Höchste Qualität, termingerechte Produktion und persönliche Betreuung von Anfang bis Ende.<')

# Start a discussion CTA
html = html.replace('>START A DISCUSSION<', '>LASSEN SIE UNS REDEN<')
html = html.replace('>Plan Your Next Run<', '>Planen Sie Ihr nächstes Projekt<')
html = html.replace('>Share your requirements and constraints. We’ll help determine the right production approach.<', '>Teilen Sie uns Ihre Anforderungen mit. Wir helfen Ihnen, den richtigen Ansatz für Ihre Zerspanungsteile zu finden.<')
html = html.replace('>Talk to Production<', '>Kontakt aufnehmen<')

# Footer
html = html.replace('>Manufacturing and industrial services focused on controlled output and dependable delivery.<', '>Ihre CNC-Fertigung im Zürcher Oberland – schnell, flexibel und in höchster Schweizer Qualität.<')
html = html.replace('>connect<', '>Kontakt<')
html = html.replace('>explore<', '>Entdecken<')
html = html.replace('>utilities<', '>Optionen<')
html = html.replace('>password protection<', '>Passwortschutz<')
html = html.replace('>© Copyright - Manukit<', '>© Copyright - Zobatec<')

with open('about-us.html', 'w', encoding='utf-8') as f:
    f.write(html)
