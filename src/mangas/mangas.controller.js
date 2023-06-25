const MangasService = require('./mangas.service');

const mangasService = new MangasService();
class MangasController {
	/* constructor() {
		this.mangasService = new MangasService();
	} */

	async createManga(req, res) {
		const mangaBody = req.body;
		const { userId } = req.headers;

		await mangasService.createManga(mangaBody, userId);

		res.status(201).json({ result: 'Manga adicionado com sucesso' });
	}

	async getManga(req, res) {
		const mangas = await mangasService.getManga();

		return res.status(200).json({ result: mangas });
	}

	async getMangaById(req, res) {
		const { userId, mangaId } = req.params;
		const manga = await mangasService.getMangaById(userId, mangaId);

		return res.status(200).json({ result: manga });
	}
}

module.exports = MangasController;
