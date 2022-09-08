const MangasService = require('./mangas.service');

const mangasService = new MangasService();
class MangasController {
	/* constructor() {
		this.mangasService = new MangasService();
	} */

	async createManga(req, res) {
		const mangaBody = req.body;
		const { userid } = req.headers;

		await mangasService.createManga(mangaBody, userid);

		res.status(201).json({ result: 'Manga adicionado com sucesso' });
	}

	async getManga(req, res) {
		const mangas = await mangasService.getManga();

		return res.status(200).json({ result: mangas });
	}
}

module.exports = MangasController;
