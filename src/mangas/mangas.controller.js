import MangasService from './mangas.service';

export default class MangasController {
	constructor() {
		this.mangasService = new MangasService();
	}

	async createManga(req, res) {
		const mangaBody = req.body;

		await this.mangasService.createManga(mangaBody);

		res.status(200).json({ result: 'Manga adicionado com sucesso' });
	}
}
