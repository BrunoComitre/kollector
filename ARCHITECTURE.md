# Arquitetura

A pasta Kollector se destina a ideia de ser um módulo python que possa ser compartilhado, por isso leva o nome da api.
Pode parecer redundante uma pasta kollector dentro de outra pasta kollector, mas a primeira se destina a API com arquivos e comnfigurações já a segunda é um módulo que poderá ser incorporado ou compartilhado na comunidade python

Dentro de de kollection existe src e tests, onde os arquivos.py do início são para subir a aplicação flask, a pasta tests se destina apenas a arquivos de teste da aplicação, e dentro de src possuimos a pasta domain, extentions

src/significa source e é o **código bruto** antes da minificação ou concatenação ou alguma outra compilação - usada para ler / editar o código.

a pasta domain se trata da criação da lógica e toda regra de negócio proprietário.
a pasta extensions se trata a dependencias de terceiros que estou utilizando na minha aplicação


Índice
- [Arquitetura](#arquitetura)
  - [`.vscode/`](#vscode)
  - [Why](#why)
    - [Overview](#overview)
    - [Começo rápido](#começo-rápido)
    - [Deploy com Docker](#deploy-com-docker)
    - [Rotas Web](#rotas-web)
  - [`app/` - Pasta das Aplicações](#app---pasta-das-aplicações)
    - [`api/`](#api)
      - [api_v1](#api_v1)
    - [`core/`](#core)
    - [`db/`](#db)
    - [`models/`](#models)
    - [`payloads/`](#payloads)
  - [`docs/` - Documentação do projeto](#docs---documentação-do-projeto)
  - [`insomnia_tests/` - Arquivos de rotas](#insomnia_tests---arquivos-de-rotas)
  - [`requirements/` - Arquivos de dependências](#requirements---arquivos-de-dependências)
  - [`scripts/` - Teste de unidade e UI](#tests---teste-de-unidade-e-ui)
  - [`tests/`](#tests)
- [Extra](#extra)
  - [Por que `MongoDB` e não banco de dados"x"?](#por-que-mongodb-e-não-banco-de-dados-x)
  - [Migrations/criação de banco de dados](#migrationscriação-de-banco-de-dados)
  - [Environment](#environment)

&nbsp;

***

## `.vscode/`

Certifique-se de seguir as mesmas diretrizes especificadas em [`settings.json`](.vscode/settings.json).

Todos os arquivos de configuração existem na pasta [`.vscode`](.vscode/) e **deve ser rastreado pelo git**.

   - [`launch.json`](.vscode/launch.json) (SE NECESSÁRIO). É onde todos os scripts de linha de comando pré-configurados estão como a execução de um debugar o ambiente de desenvolvimento;
   - [`settings.json`](.vscode/settings.json) é responsável pelas configurações do editor, como comprimento de linha, regras e formatar automaticamente ao salvar.

### Extensões vscode úteis

- React Native Tools (id: msjsdiag.vscode-react-native);
- ES7 React/Redux/GraphQL/React-Native snippets (id: dsznajder.es7-react-js-snippets);

É altamente recomendável, pelo menos, adicionar as extensões `React Native Tools` e `ES7 React/Redux/GraphQL/React-Native snippets`, pois fornecem uma quantidade absurda de recursos.

> Você pode copiar o id e pesquisar no mercado vscode para encontrá-los.

***

## `app/` - Pasta das Aplicações

Armazena todos os arquivos necessários (e gerados) para gerar compilações para a plataforma Docker.

## Why

> Você pode pular esta explicação, esta é apenas uma visão geral sobre o tema de por que decidimos ir com este
> abordagem arquitetônica.

À primeira vista (olhando o nome das pastas superiores), com o objetivo de definir suas camadas e as respectivas interações, você pode se questionar se este projeto está usando [clean architecture](http://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html), [design orientado por domínio (DDD)](https://martinfowler.com/bliki/DomainDrivenDesign.html) ou mesmo algumas partes de [MVVM](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93viewmodel). Agora, quando você começa a ler e encontrar qual parte depende do que - e do que eles esperam para executar suas responsabilidades -, você pode se perguntar sobre as coisas como "entidades não são mapeadas para modelos!", "onde estão os casos de uso?" e perguntas sobre o fato de que essa abordagem **não segue esses princípios de arquitetura**. Por que é que?

Bem, a arquitetura limpa foi originalmente planejada para aplicativos robustos/corporativos que precisam lidar com uma tonelada de complexidade da lógica de negócios e dependências altamente detalhadas - como bibliotecas, estruturas e quaisquer recursos externos.Embora este seja um cenário frequente no estado atual dos aplicativos de software, **este projeto definitivamente não é o caso de um cenário altamente complexo** - pode evoluir para ser complexo o suficiente, mas não excederá a complexidade de ser um Cliente consumidor de REST que **se concentra** muito mais na camada de apresentação do que em qualquer outra coisa.

Hoje em dia, projetos de arquitetura mais simples como MVC/MVVM/MVP são muito mais comuns em aplicativos clientes devido a isso fato: uma arquitetura supercomplexa e de alto padrão não fornece nenhum valor significativo - eles tornam as coisas mais difíceis e mais lento, sem nenhum benefício claro além de separar várias camadas **para separá-las**. Mas eles vêm com um preço: não há uma distinção clara entre **Lógica de negócios e manipulação de dados** se você não fazer cumprir tais padrões.

Não, não removeremos a separação clássica da relação "Visualizar <-> Lógica de Negócios <-> Dados", é só que, neste caso, **pensamos que seguir cada canto e recanto de parte dessas arquiteturas seria uma superengenharia**, portanto tornando as coisas mais lentas apenas para seguir alguns princípios que não se aplicam necessariamente a este caso. Esta abordagem certamente não faz sentido (ou mesmo ser completamente inutilizada) para alguns, mas pode ser bom para outros. [Xkcd relevante](https://xkcd.com/927/).

Uma coisa extra: isso é fortemente influenciado por muitas opiniões pessoais. As dependências externas deste projeto continuarão mudando conforme o tempo passa, o React também segue evoluindo, e temos que nos adaptar de forma a manter a consistência, integridade e escalabilidade de nossa solução. Portanto, é provável que haja (ou existam) melhores formas de atingir as mesmas metas/objetivos, e para isso, procuramos em sua ajuda para fazer com que a arquitetura deste projeto forneça continuamente uma boa experiência de desenvolvedor para adicionar novos recursos, atualize os antigos e mantenha esses bugs desagradáveis ​​longe. 

### Overview

TODO: Adicionar arquiterura por pastas dos projetos


### Começo rápido

O environment foi criado através do tutorial: [Criando Environment](https://www.codegrepper.com/code-examples/python/create+a+virtual+environment+with+python+3.9)

```
#------FOR LINUX/MAC---------#
python create virtualenvpython 
pip install virtualenv # install first
cd projectfolder # go to project folder
python -m venv ./venv # Create a virtual environment named venv
source env/bin/activate # start the file  to start the environment

#-------FOR WINDOWS----------#
#installing venv
py -m pip install --user virtualenv
#creating virtual env
py -m venv env
#activating virtual env
cd \venv
. bin/activate
```

Se você precisa encontrar o PATH do Pipenv:
``` $ pipenv --venv ```

Para rodar o Pipenv:
``` $ pipenv shell ```

Criar Rede Docker:
``` $ docker network create kollector-network ```

Construir Imagem:
``` $ docker-compose build ```

Rodar Container:
``` $ docker-compose up ``` ou  ``` $ docker-compose up -d ```, para modo detached.

Parar Container:
``` $ docker-compose stop ```

Rodar Teste:
``` $ docker-compose exec web pytest . ```

Executar:
``` $ ipython -i test.py ``` ou ``` $ python3 -i test.py ```

Para executar o aplicativo de depuração da web, use:
``` $ uvicorn app.main:app --reload ```

Você verá a aplicação rodando em: ``` http://127.0.0.1:8000/ ```

Em seguida, crie o arquivo .env (ou renomeie e modifique .env) na raiz do projeto e defina as variáveis de ambiente para o aplicativo:

```
touch .env
echo "PROJECT_NAME=FastAPI" >> .env
echo DATABASE_URL=mongo://$MONGO_USER:$MONGO_PASSWORD@$MONGO_HOST:$MONGO_PORT/$MONGO_DB >> .env
echo ALLOWED_HOSTS='"127.0.0.1", "localhost"' >> .env
```

### Deploy com Docker

Você deve ter as ferramentas docker e docker-compose instaladas para trabalhar com o material desta seção. Primeiro, crie o arquivo .env como na seção Começo rápido ou modifique o exemplo .env MONGO_HOST deve ser especificado como db ou docker-compose.yml modificado. Depois é só executar:

``` docker-compose up -d ```

O aplicativo estará disponível no ``` localhost//127.0.0.1 ``` em seu navegador.


### Rotas Web

Todas as rotas estão disponíveis em ``` /docs ``` ou ```/redoc ```, caminhos com Swagger* ou ReDoc.

- [Documentação docs](http://localhost:8000/docs)
- [Documentação redoc](http://localhost:8000/redoc)

* [Swagger](https://swagger.io/) - Swagger é uma estrutura de software de código aberto suportada por um grande ecossistema de ferramentas que ajuda os desenvolvedores a projetar, criar, documentar e consumir serviços da web RESTful.

## `app/` - Pasta das Aplicações

Armazena todos os arquivos necessários (e gerados) para gerar compilações para a plataforma Docker.

### `api/` - Pasta das Versões

Ponto de entrada para as aplicações Python, onde a maior parte da *ação* acontecerá.

#### `api_v1/` - Pasta do Projeto

Referente a malhor manutenibilidade para versçoes de aplicação e rotas.

### `core/`

Logica e Regras de Negócio da Aplicação

### `db/`

Responsável pela configurações de acesso ao Banco de Dados

### `models/`

Estrutura de modelos de dados usados na aplicação

### `payloads/`

Cargas úteis referente a aplicação.

***

## `docs/` - Documentação do projeto

Armazena todos os arquivos referente a extensões de documentos necessários (e gerados) para documentar o projeto.

***

## `insomnia_tests/` - Rotas de Teste

[Insomnia](https://insomnia.rest/download). Criação de rotas por meio do desenvolvimento de API com design orientado a especificações. Centralizando os padrões e fluxo de trabalho de API que funcione com as ferramentas existentes.

***

## `requirements/` - Dependências do projeto

Armazena todos os arquivos referente as dependências do Projeto.

***

## `scripts/` - Arquivos executáveis

`scripts/` tem alguns scripts utilitários, como uma maneira fácil de executar `tests` dentro e `run-tests.sh` para executar todos os testes de uma vez.

`` `shell
Necessário Implementação
`` `

***

## `tests/` - Teste de unidade e UI

Nada fora do comum aqui, nós simplesmente fazemos um espelho da estrutura de pastas `app/` dentro de `test/`. Ou seja, se tiver-mos um arquivo que é `app/api/example.html`, teríamos um espelho `test/api/example.html`.

### `utils/`

Funcionalidade compartilhada entre todos os casos de teste.

### `fixtures/`

Testes[fixtures](https://en.wikipedia.org/wiki/Test_fixture#Software) - aqui está um [Uma Boa Resposta](https://stackoverflow.com/a/14684400/8558606) explicando o que eles representam. Em nosso cenário, eles geralmente representam dados brutos, modelos ou entidades.

***

### `web/`

Armazena todos os arquivos necessários (e gerados) para gerar compilações para a plataforma da web. Atualmente não compatível.

***

# Extra

Esses são pontos que não estão diretamente relacionados à estrutura de pastas e cada responsabilidade, mas coisas que também
permeia o conhecimento necessário para compreender totalmente esta arquitetura.

## Por que `MongoDB` e não banco de dados"x"?

[`MongoDB`](https://github.com/mongodb) é um dos poucos bancos de dados realmente fáceis de usar, suporta web e fornece uma quantidade razoável de funcionalidade, como reatividade e consultas complexas.

Usamos [MongoDB](https://docs.mongodb.com/manual/installation/) para consultas de banco de dados, para instalar.

Depois de instalar o MongoDB, crie um banco de dados;

TODO: Adicionar Shell se existir
```shell
➜  Adicionar Shell se existir
```

***

## Migrations/criação de banco de dados

TODO: Estudar o que é o migrations, descobrindo uma forma mais útil, implementar na pasta scripts

```shell
➜  Adicionar Shell se existir
```

***

## Environment

Se você estiver usando o IDE `vscode`, há os [arquivos de configuração de inicialização](.vscode/launch.json) para você executar automaticamente e depurar o aplicativo.

E é isso, os ambientes atualmente suportados são: `DEV` e `PROD`.

***
