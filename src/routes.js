import { Router } from 'express';
import MangaRoutes from './mangas/mangas.routes';

const routes = Router();

routes.use(MangaRoutes);

export default routes;
