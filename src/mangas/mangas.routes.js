const { Router } = require('express');
const MangasController = require('./mangas.controller');

const MangaRoutes = Router();

const mangasController = new MangasController();

MangaRoutes.get('/mangas', mangasController.getManga);
MangaRoutes.post('/mangas', mangasController.createManga);
/* MangaRoutes.post('/mangas', (req, res)=>{
  const a = req.
}); */

module.exports = MangaRoutes;
