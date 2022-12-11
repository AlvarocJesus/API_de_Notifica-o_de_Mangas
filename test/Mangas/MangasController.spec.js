const MangasService = require('../../src/mangas/mangas.service');

describe('Manga Controller', () => {
	const mangasService = new MangasService();

	describe('(POST) /mangas', () => {
		it('should return successfully when created mangas in list user', async () => {
			const manga = { nome: 'Titulo teste' };

			const { body } = await mangasService.createManga(manga).expect(201);

			expect(body).toEqual(expect.ObjectContaining(manga));
		});
	});
});
