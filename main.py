# Einfache Python Script, um RSS-Feeds beliebiger Webseiten anzuzeigen.

import feedparser
import webbrowser

rss_url = input("Gib den Link des RSS Feeds ein:")

feed = feedparser.parse(rss_url)

article_links = feed.entries

for index, entry in enumerate(article_links):
    title = entry.title
    link = entry.link
    published = entry.published
    formatted_title = f"\033[1;32m{title}\033[0m"
    print(f"{index + 1}. {formatted_title}")
    print(f"   Veröffentlicht: {published}")
    print(f"   Link: {link}")
    print("-" * 50)

while True:
        article_number = int(input("Gib die Nummer des Artikels ein, den du öffnen möchtest: "))
        if 1 <= article_number <= len(article_links):
            webbrowser.open(article_links[article_number - 1].link)
        else:
            print(f"Ungültige eingabe. Wähle eine Nummer zwischen 1 und {len(article_links)} ")
