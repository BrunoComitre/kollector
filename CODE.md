# Padrões de código para nossa API

Aqui estão as diretrizes básicas para manter nosso ecossistema saudável.

***

## Durante a codificação

- Classe como PascalCase.
- Variáveis e funções como camelCase.
- Máximo de coluna 80 (isso pode ser quebrado ao escrever Python).
- Salvar espaços em vez de tabulações no código-fonte.
- O recuo é de 4 espaços.
- Espaço entre os argumentos em uma chamada de função.
- Comece os nomes dos métodos com um verbo (tente ser o mais claro possível).
- Prefira nomes claros e verbosos do que nomes simples.
- Prefira a simplicidade à complexidade.
- Fique de olho nos erros `pylint` e nos avisos do Python/Black.
- Faça casos de teste tão frequentemente quanto possível e teste a funcionalidade e verificações de sanidade.
- Use `()` em torno de argumentos em chamadas de função, isso é mais fácil de identificar e encontrar argumentos.

***

## Ao adicionar novos módulos ao package.json
- *sempre* leia o `Pipfile` de uma dependência, queremos manter o mais baixo dependência com outros módulos possíveis, então se você quiser adicionar uma dependência que adicionam outras 20 coisas, certifique-se de que você realmente precisa disso.
- Prefira biblioteca em vez de frameworks, módulo em vez de biblioteca, código simples em vez de módulo.
- Não adicione uma dependência a uma função de 3 linhas (como o morto [leftpad](https://github.com/left-pad/left-pad/blob/master/index.js)), prefira escreva o seu próprio se for algo tão simples, queremos criar um `utils` com algumas funções comuns que usamos em nosso aplicativo (formato cpf, número de telefone bonito).

***

**Lembre-se**

Coisas simples que são melhor escritas à mão e têm mais flexibilidade.

***
