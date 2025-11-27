README — Sistema de Cadastro de Alunos (Python)

Este projeto é um sistema simples de cadastro de alunos desenvolvido em Python, utilizando um dicionário como base de dados em memória. Ele permite cadastrar, atualizar, deletar, buscar e listar alunos, além de gerar um relatório com estatísticas gerais das notas.

📌 Funcionalidades

O programa funciona por meio de um menu interativo, onde o usuário escolhe opções para manipular os dados dos alunos.

✔ 1. Cadastrar aluno

Solicita matrícula, nome e nota.

Impede matrículas duplicadas.

Valida nota (0 a 10).

Define automaticamente o status:

Aprovado → nota ≥ 7

Reprovado → nota < 7

✔ 2. Atualizar aluno

Permite alterar nome e nota.

Valida a nova nota.

Atualiza automáticamente o status (aprovado/reprovado).

✔ 3. Deletar aluno

Remove o aluno do sistema pela matrícula.

✔ 4. Listar alunos

Exibe todos os alunos cadastrados no formato:

matrícula | nome | nota | status

✔ 5. Buscar aluno

Pesquisa pela matrícula e exibe seus dados.

✔ 6. Relatório

Gera um relatório contendo:

Total de alunos

Média geral das notas

Quantos estão aprovados

Quantos estão reprovados

✔ 7. Sair do sistema

Finaliza o programa de forma segura.

🗂 Estrutura Interna

O sistema utiliza um dicionário Python como mini banco de dados:

Bd = {
    matricula: {
        "nome": "Nome do Aluno",
        "nota": 8.5,
        "status": "Aprovado"
    }
}


Não há persistência em arquivo. Os dados existem apenas enquanto o programa está rodando.

🖥 Como executar

Certifique-se de ter o Python 3 instalado.

Salve o código em um arquivo, por exemplo:

sistema_alunos.py


Execute no terminal/cmd:

python sistema_alunos.py


Use o menu numérico para navegar entre as opções.

🔧 Tecnologias Utilizadas

Python 3

Estruturas básicas:

dicionários

funções

loops

condicionais

tratamento de erros (try/except)

entrada de dados (input())
