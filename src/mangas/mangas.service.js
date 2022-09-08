const MangasRepository = require('./mangas.repository');

class MangasService {
	constructor() {
		this.mangasRepository = new MangasRepository();
	}

	async createManga(mangaBody, userId) {
		const manga = await this.mangasRepository.createManga(mangaBody, userId);

		if (!manga) {
			throw new Error('Manga nao criado por falha na request');
		}

		return manga;
	}

	async getManga() {
		const mangas = this.mangasRepository.getManga();

		if (!mangas) {
			throw new Error('Mangas not found');
		}

		return mangas;
	}
}

module.exports = MangasService;
