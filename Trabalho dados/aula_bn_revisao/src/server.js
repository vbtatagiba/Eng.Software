const express = require("express"); // Importa o módulo Express
const app = express(); // Cria uma instância do aplicativo Express
const mongoose = require('mongoose'); // Importa o módulo Mongoose para interagir com o MongoDB
const userRoutes = require("../src/routes/userRoutes"); // Importa as rotas relacionadas aos usuários

const PORT = 3000; // Define a porta em que o servidor será executado

// Conecta ao MongoDB
mongoose.connect('mongodb+srv://vbtatagiba77:mu104510@cluster.examcas.mongodb.net/?retryWrites=true&w=majority&appName=Cluster',
    { useNewUrlParser: true, useUnifiedTopology: true }
).then(() => {
    console.log("Conexão com o MongoDB estabelecida com sucesso");
}).catch(error => {
    console.log("Erro ao conectar ao MongoDB:", error);
});

app.use(express.json()); // Middleware para permitir o parsing de JSON no corpo das requisições

app.use('/api/users', userRoutes); // Associa as rotas relacionadas aos usuários ao prefixo '/api/users'

app.listen(PORT, () => {
    console.log(`Servidor está conectado na porta ${PORT}`); // Inicia o servidor na porta especificada
});
