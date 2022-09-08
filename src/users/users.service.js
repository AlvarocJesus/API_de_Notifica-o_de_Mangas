const UsersRepository = require('./users.repository');

class UserService {
	constructor() {
		this.userRepository = new UsersRepository();
	}

	async save(body) {
		try {
			const user = await this.userRepository.save(body);

			if (!user) {
				throw new Error('Failed created user');
			}

			return user;
		} catch (err) {
			throw new Error(err);
		}
	}

	async getAll() {
		try {
			const users = await this.userRepository.findAll();

			if (users.length <= 0) {
				throw new Error('Users not found');
			}

			return users;
		} catch (err) {
			throw new Error(err.message);
		}
	}
}

module.exports = UserService;
