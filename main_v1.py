from datetime import datetime

from config.notify.Notify import Notify
from scrap import MangaBr,MangaOnline,oldiSussy,ReadManga,SussyToons

Notify().sendMessage(f"Hello World! {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")

# Region: Scrap.py
MangaOnline.MangaOnline().run()
MangaBr.MangaBr().run()
oldiSussy.OldiSussy().run()
ReadManga.ReadManga().run()
SussyToons.SussyToons().run()

# EndRegion

# Region: busca de mangas atualizados recentenmente e envio de mensagem

mangas = [] # db().getRecentlyMangaa()

Notify().sendMessage('Scrap finalizado!')

# EndRegion

Notify().sendMessage('Scrap finalizado!')