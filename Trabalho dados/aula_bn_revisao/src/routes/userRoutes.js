const express = require('express'); // Importa o módulo Express
const router = express.Router(); // Cria um novo objeto de roteador Express
const userController = require('../controllers/userController'); // Importa o controlador de usuário

// Define as rotas para manipular requisições relacionadas aos usuários
router.get('/', userController.getAllUsers); // Rota para obter todos os usuários (método GET)
router.post('/', userController.createUser); // Rota para criar um novo usuário (método POST)
router.put('/:id', userController.updateUser); // Rota para atualizar um usuário existente (método PUT)
router.delete('/:id', userController.deleteUser); // Rota para excluir um usuário existente (método DELETE)

module.exports = router; // Exporta o roteador para ser utilizado em outros arquivos
