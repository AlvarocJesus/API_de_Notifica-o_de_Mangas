const { Router } = require('express');
const MangaRoutes = require('./mangas/mangas.routes');
const userRoutes = require('./users/users.routes');

const routes = Router();

routes.use(userRoutes);
routes.use(MangaRoutes);

routes.get('/teste', (req, res) => {
	console.log('entrou na primeira rota');
	return res.json({ message: 'Oi' });
});

module.exports = routes;
