const formulario = document.querySelector('form');
const nomeInput = document.querySelector('#nome');
const matriculaInput = document.querySelector('#matricula');
const cargaHorariaTotalInput = document.querySelector('#cargaHorariaTotal');
const cargaHorariaCursadaInput = document.querySelector('#cargaHorariaCursada');
const alunosTbody = document.querySelector('#alunos');

formulario.addEventListener('submit', function(evento) {
  evento.preventDefault();

  const nome = nomeInput.value;
  const matricula = matriculaInput.valueAsNumber;
  const cargaHorariaTotal = cargaHorariaTotalInput.valueAsNumber;
  const cargaHorariaCursada = cargaHorariaCursadaInput.valueAsNumber;
  const cargaHorariaRestante = cargaHorariaTotal - cargaHorariaCursada;

  const alunos = JSON.parse(localStorage.getItem('alunos')) || [];

  const aluno = {
    nome,
    matricula,
    cargaHorariaTotal,
    cargaHorariaCursada,
    cargaHorariaRestante
  };

  if (aluno.cargaHorariaCursada > aluno.cargaHorariaTotal) {
    aluno.cargaHorariaCursada = aluno.cargaHorariaTotal;
  }

  alunos.push(aluno);
  localStorage.setItem('alunos', JSON.stringify(alunos));

  atualizarTabela();
  mostrarMensagem(`Aluno ${nome} cadastrado com sucesso!`);
  formulario.reset();
});

function atualizarTabela() {
  alunosTbody.innerHTML = '';

  const alunos = JSON.parse(localStorage.getItem('alunos')) || [];

  for (const aluno of alunos) {
    const tr = document.createElement('tr');

    const tdNome = document.createElement('td');
    tdNome.textContent = aluno.nome;
    tr.appendChild(tdNome);

    const tdMatricula = document.createElement('td');
    tdMatricula.textContent = aluno.matricula;
    tr.appendChild(tdMatricula);

    const tdCargaHorariaTotal = document.createElement('td');
    tdCargaHorariaTotal.textContent = aluno.cargaHorariaTotal;
    tr.appendChild(tdCargaHorariaTotal);

    const tdCargaHorariaCursada = document.createElement('td');
    tdCargaHorariaCursada.textContent = aluno.cargaHorariaCursada;
    tr.appendChild(tdCargaHorariaCursada);

    const tdCargaHorariaRestante = document.createElement('td');
    tdCargaHorariaRestante.textContent = aluno.cargaHorariaRestante;
    tr.appendChild(tdCargaHorariaRestante);

    alunosTbody.appendChild(tr);
  }
}

function mostrarMensagem(mensagem) {
  const resultado = document.querySelector('#resultado');
  resultado.textContent = mensagem;
  setTimeout(function() {
    resultado.textContent = '';
  }, 2000);
}

const limparLocalStorageButton = document.querySelector('#limparLocalStorage');
limparLocalStorageButton.addEventListener('click', function() {
  localStorage.clear();
  atualizarTabela();
  mostrarMensagem('Local Storage limpo com sucesso!');
});

cargaHorariaCursadaInput.addEventListener('input', function() {
  const cargaHorariaTotal = cargaHorariaTotalInput.valueAsNumber;
  let cargaHorariaCursada = cargaHorariaCursadaInput.valueAsNumber;

  if (cargaHorariaCursada > cargaHorariaTotal) {
    cargaHorariaCursada = cargaHorariaTotal;
    cargaHorariaCursadaInput.value = cargaHorariaCursada;
  }
});
