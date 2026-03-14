import re
import os

HTML_FILE = 'about-us.html'

def read_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(path, content):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

about_html = read_file(HTML_FILE)

# Split the file to construct contact.html
import re
match_archive = re.search(r'<section class="about-archive">', about_html)
match_footer = re.search(r'<section class="footer">', about_html)

if match_archive and match_footer:
    top_part = about_html[:match_archive.start()]
    bottom_part = about_html[match_footer.start():]
    
    # Update Meta for Contact
    top_part = re.sub(r'<title>.*?</title>', r'<title>Kontakt – Zobatec</title>', top_part)
    top_part = re.sub(r'name="description" content="[^"]+"', r'name="description" content="Nehmen Sie Kontakt mit Zobatec auf. Wir freuen uns auf Ihre Zerspanungsprojekte und Anfragen."', top_part)
    top_part = re.sub(r'Über Zobatec – Lohnfertigung & mechanische Bearbeitung', r'Kontakt – Zobatec', top_part)
    
    # Banner Text change
    top_part = re.sub(r'>Schweizer Präzision durch Fachwissen und Flexibilität.<', r'>Kontaktieren Sie uns<', top_part)
    top_part = re.sub(r'>Wir bieten zuverlässige CNC-Lohnfertigung und mechanische Bearbeitung. Schnell, unkompliziert und termingerecht.<', r'>Egal ob Einzelteile, Serienfertigung oder komplexe Hartbearbeitung. Wir sind bereit für Ihr Projekt.<', top_part)

    contact_section = """
    <section class="contact-form-section" style="padding: 100px 5%; background-color: #0b0c10; color: #fff;">
        <div style="max-width: 800px; margin: 0 auto; background: #1f2833; padding: 50px; border-radius: 12px; box-shadow: 0 10px 30px rgba(0,0,0,0.5);">
            <h2 style="font-size: 32px; font-weight: 600; font-family: 'IBM Plex Sans', sans-serif; margin-bottom: 30px; margin-top:0;">Schreiben Sie uns</h2>
            
            <form action="https://hook.eu2.make.com/YOUR_WEBHOOK_URL_HERE" method="POST" style="display: flex; flex-direction: column; gap: 20px;">
                
                <div style="display: flex; gap: 20px; width: 100%;">
                    <div style="flex: 1; display:flex; flex-direction:column; gap:8px;">
                        <label for="name" style="font-size: 14px; color: #c5c6c7;">Name *</label>
                        <input type="text" id="name" name="name" required style="padding: 15px; background: #0b0c10; border: 1px solid #4a4e69; color: #fff; border-radius: 6px; font-size: 16px; width: 100%; box-sizing: border-box;" placeholder="Max Muster">
                    </div>
                    <div style="flex: 1; display:flex; flex-direction:column; gap:8px;">
                        <label for="firma" style="font-size: 14px; color: #c5c6c7;">Firma</label>
                        <input type="text" id="firma" name="firma" style="padding: 15px; background: #0b0c10; border: 1px solid #4a4e69; color: #fff; border-radius: 6px; font-size: 16px; width: 100%; box-sizing: border-box;" placeholder="Muster GmbH">
                    </div>
                </div>

                <div style="display: flex; gap: 20px; width: 100%;">
                    <div style="flex: 1; display:flex; flex-direction:column; gap:8px;">
                        <label for="email" style="font-size: 14px; color: #c5c6c7;">E-Mail *</label>
                        <input type="email" id="email" name="email" required style="padding: 15px; background: #0b0c10; border: 1px solid #4a4e69; color: #fff; border-radius: 6px; font-size: 16px; width: 100%; box-sizing: border-box;" placeholder="max@muster.ch">
                    </div>
                    <div style="flex: 1; display:flex; flex-direction:column; gap:8px;">
                        <label for="telefon" style="font-size: 14px; color: #c5c6c7;">Telefonnummer</label>
                        <input type="tel" id="telefon" name="telefon" style="padding: 15px; background: #0b0c10; border: 1px solid #4a4e69; color: #fff; border-radius: 6px; font-size: 16px; width: 100%; box-sizing: border-box;" placeholder="+41 79 123 45 67">
                    </div>
                </div>

                <div style="display:flex; flex-direction:column; gap:8px;">
                    <label for="message" style="font-size: 14px; color: #c5c6c7;">Nachricht *</label>
                    <textarea id="message" name="message" required rows="5" style="padding: 15px; background: #0b0c10; border: 1px solid #4a4e69; color: #fff; border-radius: 6px; font-size: 16px; font-family: inherit; resize: vertical; width: 100%; box-sizing: border-box;" placeholder="Wie können wir Ihnen weiterhelfen?"></textarea>
                </div>

                <button type="submit" style="margin-top: 10px; padding: 18px 30px; background: #c5a880; color: #000; border: none; border-radius: 6px; font-size: 16px; font-weight: 600; cursor: pointer; transition: background 0.3s;" onmouseover="this.style.background='#b0936f'" onmouseout="this.style.background='#c5a880'">Nachricht senden</button>

            </form>
        </div>
    </section>
    """
    
    contact_html = top_part + contact_section + bottom_part
    write_file('contact.html', contact_html)
    print("Created contact.html")

# Replace Links in index.html, about-us.html and contact.html
files = ['index.html', 'about-us.html', 'contact.html']

for fn in files:
    if os.path.exists(fn):
        content = read_file(fn)
        # Update href attributes pointing to contact or contact-us
        content = re.sub(r'href="/contact-us"', r'href="/contact.html"', content)
        content = re.sub(r'href="/contact"', r'href="/contact.html"', content)
        content = re.sub(r'href="contact-us.html"', r'href="/contact.html"', content)
        
        # Ensure active nav state in contact.html if needed
        if fn == 'contact.html':
            content = content.replace('aria-current="page" class="navigation-link w-nav-link w--current"', 'class="navigation-link w-nav-link"')
            # Find the contact link and make it active (roughly)
            content = re.sub(r'(<a href="/contact.html" class="navigation-link w-nav-link)>', r'\1 w--current" aria-current="page">', content)
            
        write_file(fn, content)
        print(f"Updated links in {fn}")
