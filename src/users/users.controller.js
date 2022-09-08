const UserService = require('./users.service');

const userService = new UserService();
class UsersController {
	/* constructor() {
		this.userService = new UserService();
	} */

	async getAllUsers(req, res) {
		const users = await userService.getAll();
		return res
			.status(200)
			.json({ result: users, message: 'entrou na rota de users' });
	}

	async save(req, res) {
		const { body } = req;

		await userService.save(body);

		return res
			.status(201)
			.json({ result: 'Created user', message: 'Deu certo!' });
	}
}

module.exports = UsersController;
