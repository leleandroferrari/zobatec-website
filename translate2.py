import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Home Features
html = html.replace('>Stable production planning<', '>Stabile Produktionsplanung<')
html = html.replace('>Consistent workflows aligned to capacity and demand.<', '>Konsistente Abläufe, abgestimmt auf Kapazität und Bedarf.<')
html = html.replace('>Quality checks embedded in process<', '>Integrierte Qualitätsprüfungen<')
html = html.replace('>Verification built into every production stage.<', '>Strenge Kontrollen in jeder Phase der Fertigung.<')
html = html.replace('>Realistic lead times<', '>Realistische Lieferzeiten<')
html = html.replace('>Timelines based on actual operational capacity.<', '>Zeitpläne basierend auf tatsächlichen betrieblichen Kapazitäten.<')
html = html.replace('>Technical problem-solving mindset<', '>Lösungsorientierte Technik<')
html = html.replace('>Engineering-led resolution of production challenges.<', '>Lösung von Produktionsherausforderungen durch Erfahrung.<')

# Testimonials
html = html.replace('>PARTNER FEEDBACK<', '>KUNDENSTIMMEN<')
html = html.replace('>Trusted in Production<', '>Vertrauen in unsere Fertigung<')
html = html.replace('>Daniel Morris<', '>Daniel Müller<')
html = html.replace('>Operations Manager<', '>Produktionsleiter<')
html = html.replace('>Helen Carter<', '>Helen Schmidt<')
html = html.replace('>Manufacturing Lead<', '>Fertigungsleitung<')
html = html.replace('>James Whitfield<', '>Lukas Wechsler<')
html = html.replace('>Procurement Officer<', '>Einkaufsleiter<')
html = html.replace('>Michael Bennett<', '>Michael Baumgartner<')
html = html.replace('>Project Engineering Manager<', '>Projektleitung Technik<')
html = html.replace('>Output matched specification across multiple batches, with consistent quality maintained throughout production. Documentation and traceability were clear at every stage.”<', '>Die Ergebnisse entsprachen exakt den Spezifikationen über mehrere Chargen hinweg, mit konstant hoher Qualität. Dokumentation und Nachverfolgbarkeit waren in jeder Phase einwandfrei.”<')
html = html.replace('>Partnering with them transformed our manufacturing process. Their team optimized workflows, improved quality, and ensured timely delivery. We couldn’t ask for a better industrial partner.<', '>Die Zusammenarbeit hat unseren Fertigungsprozess enorm entlastet. Das Zobatec-Team ist zuverlässig, verbessert die Qualität und sorgt für pünktliche Lieferungen. Ein Top-Partner für die Industrie.<')
html = html.replace('>Their B2B services are tailored to meet our unique needs. The team’s expertise and responsiveness have made them an invaluable part of our supply chain.<', '>Ihre B2B-Dienstleistungen sind genau auf unsere individuellen Bedürfnisse zugeschnitten. Das Fachwissen und die schnelle Reaktionsfähigkeit des Teams machen sie zu einem unschätzbaren Teil unserer Lieferkette.<')
html = html.replace('>From concept to execution, they provide innovative solutions that save time and reduce costs. Their commitment to excellence sets them apart.<', '>Von der ersten Besprechung bis zur fertigen Ausführung bieten sie clevere Lösungen, die Zeit und Kosten sparen. Ihr Engagement für herausragende Leistung zeichnet sie aus.<')

# Blog Section
html = html.replace('>INSIGHTS &amp; UPDATES<', '>EINBLICKE &amp; NEUIGKEITEN<')
html = html.replace('>From the Production Floor<', '>Aus der Werkstatt<')
html = html.replace('>Thoughts, lessons, and practical insights drawn from our experience in manufacturing, engineering, and industrial delivery.<', '>Gedanken, Erkenntnisse und praxisnahe Tipps aus unserer Erfahrung in der Lohnfertigung, Mechanik und industriellen Lieferung.<')
html = html.replace('>Why Process Discipline Matters More Than Speed<', '>Warum Prozessdisziplin wichtiger ist als Geschwindigkeit<')
html = html.replace('>Balancing efficiency with control in industrial manufacturing environments.<', '>Effizienz und Kontrolle in industriellen Fertigungsumgebungen ausbalancieren.<')
html = html.replace('>Managing Production Risk in Complex Industrial Projects<', '>Umgang mit Produktionsrisiken in komplexen Industrieprojekten<')
html = html.replace('>How structured planning reduces disruption and improves delivery confidence.<', '>Wie strukturierte Planung Störungen reduziert und die Lieferzuverlässigkeit erhöht.<')
html = html.replace('>Integrating Smart Automation into Modern Production Lines<', '>Einsatz modernster Technologien in der Produktion<')
html = html.replace('>Automation That Powers the Next Generation of Production with Smart Automation<', '>Werkzeuge und Maschinen, die die nächste Generation der Fertigung antreiben.<')
html = html.replace('>more blogs<', '>Zum Blog<')

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

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
