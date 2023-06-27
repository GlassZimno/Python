#Glass Zimny
#25/11/2021
import webbrowser
import time

pages = ("https://www.kassoon.com/",
         "https://donjon.bin.sh/",
         "https://www.worldanvil.com/world/57dd375b-8ddd-41e5-8d7f-caa584b9e87f/summary",
         "https://www.dndbeyond.com/characters/61246727/QWuEDJ",
         "https://www.dndbeyond.com/characters/69748292/L9CGCa",
         "https://www.dndbeyond.com/profile/simply_caelan/characters/69945589",
         "https://roll20.net/welcome",
         "https://drive.google.com/file/d/16Pm3WsuczrSwcH5iK97myaueeZ8pdjnw/view",
         "https://drive.google.com/file/d/16TQfUxO5B1FapEYc63pvMXLV_hGsqUNv/view",
         "https://probabletrain.itch.io/dungeon-scrawl",
         "https://app.reroll.co/select-character",
         "https://www.worldanvil.com/w/nargura-smolbeanboi/a/session-1-article?preview=true",
         "https://www.fantasynamegenerators.com/dungeons-and-dragons.php",
         "https://ezfibuilds.github.io/NPC-Thought-Starter-Generator/")


for i in range(len(pages)):
  time.sleep(1)
  webbrowser.open(pages[i])
print("done")
