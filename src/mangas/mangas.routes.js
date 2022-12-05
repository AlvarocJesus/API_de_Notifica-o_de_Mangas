const { Router } = require('express');
const MangasController = require('./mangas.controller');

const MangaRoutes = Router();

const mangasController = new MangasController();

MangaRoutes.post('/mangas', mangasController.createManga);
MangaRoutes.get('/mangas', mangasController.getManga);
MangaRoutes.get('/mangas/:userId/:manga', mangasController.getMangaById);

module.exports = MangaRoutes;
