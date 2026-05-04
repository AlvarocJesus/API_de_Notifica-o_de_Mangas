from datetime import datetime

from config.notify.Notify import Notify
from infra.scrap import MangaBr, MangaOnline, ReadManga
from infra.scrap import oldiSussy
from infra.scrap import SussyToons

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