const botaoResposta = document.getElementById("botao-resposta");
const mensagem = document.getElementById("mensagem");

botaoResposta.addEventListener("click", function() {
  mensagem.innerHTML = "Obrigado por aceitar ser minha namorada, [NOME DA SUA NAMORADA]! Você não sabe como me faz feliz!";
});
