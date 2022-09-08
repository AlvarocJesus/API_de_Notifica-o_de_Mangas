const { Router } = require('express');
const UsersController = require('./users.controller');

const userRoutes = Router();
const usersController = new UsersController();

userRoutes.get('/users', usersController.getAllUsers);
userRoutes.get('/');
userRoutes.post('/users', usersController.save);
userRoutes.patch('/');
userRoutes.delete('/');

module.exports = userRoutes;
