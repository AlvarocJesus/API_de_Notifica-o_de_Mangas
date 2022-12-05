describe('Manga Controller', () => {
	describe('(POST) /mangas', () => {
		it('should return successfully when created mangas in list user', async () => {
			const manga = { nome: 'Titulo pika' };

			const { body } = await service.save(manga);

			expect(body).toEqual(manga);
		});
	});
});
