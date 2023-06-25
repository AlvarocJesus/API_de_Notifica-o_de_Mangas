const MangasService = require('../../src/mangas/mangas.service');

describe('Manga Controller', () => {
  const mangasService = new MangasService();

  describe('(POST) /mangas', () => {
    it('should return successfully when created mangas in list user', async () => {
      const manga = { nome: 'Titulo teste' };

      const { body: mangaSaved } = await mangasService.createManga(manga).expect(201);

      expect(mangaSaved).toEqual(expect.ObjectContaining(manga));
    });
  });
});
