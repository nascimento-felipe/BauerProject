# Teste Técnico Bauer

Esse projeto é um teste técnico para a empresa bauer, voltado para o Backend com Django e com manipulação de dados com Pandas e apresentação em formato de gráfico com a biblioteca Chart.js

## Separação do projeto

O arquivo [urls.py](./vagas/vagas/urls.py) contém todas as rotas;

O arquivo [views.py](./vagas/vagas/views.py) contém a lógica de todas as rotas, atuando como um controller/service

A pasta [vagas](./vagas/templates/vagas/) contém todos os arquivos HTML do projeto.

## Rotas

/ --> Dashboard principal, onde terão os gráficos caso tenham dados

/listagem --> Listagem de todas as candidaturas, com a data, título e nome, por ordem do mais recente para o mais antigo.

/associacao --> Página para fazer associação de vagas, com dois "selects" para escolher o candidato e a vaga, fazendo a associação entre os dois. Caso a associação seja bem sucedida, o usuário é movido para a tela de listagem de candidaturas, onde pode conferir se a candidatura está feita corretamente.

/admin --> Página para adição, exclusão e alteração de usuários e demais modelos do sistema. Usei essa mesma do Django para facilitar a prototipação e acelerar a entrega.

## Por que Chart.js?

Optei por utilizar essa biblioteca por ter algum conhecimento e acelerar a entrega, uma vez que o tempo para esse projeto é contado

## Dados do banco

Tentei subir o banco já criado aqui nesse projeto para já ter alguns dados de teste. As credenciais são:

login: lama

senha: 123456

## Algumas melhorias que poderiam ser feitas

- [ ] Estilização, principalmente dos gráficos
- [ ] Analisar a performance durante as requisições GET no caso de um grande volume de dados
- [ ] Separação das funções nas views para deixar cada uma com uma responsabilidade, facilitando a manutenção

## Outras explicações

Não utilizei banco de dados relacionais mais robustos, como MySQl e Postgres porque achei que seria desnecessário, dado o tamanho do projeto. Também não criei outras branches no repositório porque estou trabalhando sozinho, então não existe perigo de conflito nos arquivos, mas sei trabalhar com PRs e issues com equipes.

Por fim, pensei de conteinerizar a aplicação para poder rodar independente da máquina e da versão do sistema, mas por conta de outros compromissos não conseguirei criar o arquivo a tempo.

Muito obrigado. 🙏
