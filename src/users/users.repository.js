const { PrismaClient } = require('@prisma/client');

// const prisma = new PrismaClient();
class UsersRepository {
	constructor() {
		this.prisma = new PrismaClient();
	}

	async save(body) {
		try {
			return await this.prisma.user.create({
				data: {
					name: body.name,
					email: body.email,
					password: body.password,
				},
			});
		} catch (err) {
			throw new Error(err);
		}
	}

	async findAll() {
		try {
			return await this.prisma.user.findMany({
				include: {
					manga: true,
				},
			});
		} catch (err) {
			throw new Error(err);
		}
	}
}

module.exports = UsersRepository;
