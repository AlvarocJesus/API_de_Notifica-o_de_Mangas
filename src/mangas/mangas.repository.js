const { PrismaClient } = require('@prisma/client');

const prisma = new PrismaClient();
class MangasRepository {
	/* constructor() {
		this.prisma = new PrismaClient();
	} */

	async createManga(mangaBody, userId) {
		try {
			console.log({ userId, tipo: typeof userId });
			return await prisma.manga.create({
				data: {
					title: mangaBody.title,
					total_chapter: mangaBody.total_chapter,
					// user_id: userId,
					user: { connect: { id: parseInt(userId) } },
				},
			});
		} catch (err) {
			console.log({ err });
			throw new Error(err);
		}
	}

	async getManga() {
		try {
			const mangas = await prisma.manga.findMany();

			return mangas;
		} catch (err) {
			throw new Error(err);
		}
	}
}

module.exports = MangasRepository;
