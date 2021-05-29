# ROADMAP

Como um projeto que poderá ter continuidade, segue algumas ideias de implementações futuras.

## TO-DO

- Essencial
   - [ ] Implementação de pesquisa para o front end
   - [ ] APIKEY
   - [ ] limitação de API query
   - [ ] Refresh Token
   - [ ] Melhorar e limpar Dockerfile e docker-compose
   - [ ] Definir ambientes de teste, produção e desenvolvimento
   - [ ] Documentar chamadas de rota
   - [ ] Adicionar mais testes unitários
   - [ ] Adicionar docstring explicativo em todas as rotas
- Front-end
   - [ ] Adicionar Lib para relatório de analises
   - [ ] Verifique o dimensionamento nos principais navegadores
   - [ ] Menus
   - [ ] Adicionar links de visualização
- Gerenciador de arquivos
   - [ ] O nome do arquivo no banco de dados e pesquisa
   - [ ] Data/hora modificada
   - [ ] Armazene/exiba estatísticas do arquivo carregado
   - [ ] Uploads subsequentes
   - [ ] Barra de Ferramentas Genérica
   - [ ] Botões para entradas e seleções de pedidos de crédito
   - [ ] Adicionar extração via PDF
   - [ ] Adicionar movimento de notas via drag and drop

## REGRAS DO NEGÓCIO

- [ ] Ao retornar os pedidos deve ser inteligente o suficiente para retornar por prioridade
- [ ] Crie validações:
   - [ ] Você não pode criar uma pedido com concluído
   - [ ] Você não pode atualizar a data de criação
   - [ ] Eu não pude excluir uma pedido até que feito
- [ ] Cada usuário terá apenas uma lista de pedidos

## ANÁLISE

- [ ] Use o tutorial [Importando arquivos JSON para Data Science](https://towardsdatascience.com/lots-of-json-29873d3abfdf), para dar um get all na base e formatar os dados separados para criar modelos
- [ ] Veja a implementação de uma frente separada, semelhante à [Ferramenta de teste de dados estruturados](https://search.google.com/structured-data/testing-tool)
- [ ] Se possível, teste o Sklearn para testar [Similaridade entre comentários](https://medium.com/@octaviofisica/similaridade-entre-coment%C3%A1rios-20d1812b6dc4)
- [ ] Ao separar os URLs, teste o [micawber](https://github.com/coleifer/micawber),para extrair valor do URL
- [ ] Depois de definir e estruturar os dados, aplique técnicas como [Machine Learning for Cybersecurity 101](https://towardsdatascience.com/machine-learning-for-cybersecurity-101-7822b802790b)

***
