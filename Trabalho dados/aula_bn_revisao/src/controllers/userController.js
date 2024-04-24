const User = require("../models/User");

// Obtém todos os usuários
exports.getAllUsers = async (req, res) => {
    try {
        // Encontra todos os usuários no banco de dados
        const users = await User.find();
        // Retorna a lista de usuários com status 200 (OK)
        res.status(200).json(users);
    } catch (error) {
        // Se ocorrer um erro, retorna uma resposta com status 400 (Bad Request) e uma mensagem de erro
        res.status(400).json({ message: error.message });
    }
};

// Cria um novo usuário
exports.createUser = async (req, res) => {
    // Cria uma nova instância de User com os dados fornecidos no corpo da requisição
    const user = new User(req.body);
    try {
        // Salva o novo usuário no banco de dados
        const savedUser = await user.save();
        // Retorna o usuário recém-criado com status 201 (Created)
        res.status(201).json(savedUser);
    } catch (error) {
        // Se ocorrer um erro, retorna uma resposta com status 400 (Bad Request) e uma mensagem de erro
        res.status(400).json({ message: error.message });
    }
};

// Atualiza um usuário existente
exports.updateUser = async (req, res) => {
    const { id } = req.params;
    try {
        // Encontra e atualiza o usuário pelo ID fornecido
        const updatedUser = await User.findByIdAndUpdate(id, req.body, { new: true });
        // Se o usuário não for encontrado, retorna uma resposta com status 404 (Not Found) e uma mensagem
        if (!updatedUser) {
            return res.status(404).json({ message: "Usuário não encontrado" });
        }
        // Retorna o usuário atualizado com status 200 (OK)
        res.status(200).json(updatedUser);
    } catch (error) {
        // Se ocorrer um erro, retorna uma resposta com status 400 (Bad Request) e uma mensagem de erro
        res.status(400).json({ message: error.message });
    }
};

// Exclui um usuário existente
exports.deleteUser = async (req, res) => {
    const { id } = req.params;
    try {
        // Encontra e exclui o usuário pelo ID fornecido
        const deletedUser = await User.findByIdAndDelete(id);
        // Se o usuário não for encontrado, retorna uma resposta com status 404 (Not Found) e uma mensagem
        if (!deletedUser) {
            return res.status(404).json({ message: "Usuário não encontrado" });
        }
        // Retorna uma mensagem de sucesso com status 200 (OK)
        res.status(200).json({ message: "Usuário excluído com sucesso" });
    } catch (error) {
        // Se ocorrer um erro, retorna uma resposta com status 400 (Bad Request) e uma mensagem de erro
        res.status(400).json({ message: error.message });
    }
};
