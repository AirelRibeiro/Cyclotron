# Cyclotron

Este é um projeto que implementa um algoritmo para simular um ciclotron. O algoritmo é escrito em Python e inclui diferentes casos para acelerar partículas como elétrons, prótons e nêutrons.

## Executando o projeto

Certifique-se de ter o Python instalado em seu sistema. Se precisar intala-lo, [acesse aqui a documentação](https://www.python.org/doc/)

1. Clone este repositório para o seu computador.

```
git clone git@github.com:AirelRibeiro/Cyclotron.git
```

2. Navegue até o diretório do projeto:

```
cd Cyclotron
```

3. Execute o seguinte comando para executar o projeto:

```
python3 cyclotron.py
```

4. Você poderá especificar o tipo da partícula e o tamanho da matriz, para então ver no console o resultado da aceleração.

###

## Executando os testes

Certifique-se de ter o Pytest instalado em seu sistema. Se precisar intala-lo, [acesse aqui a documentação](https://docs.pytest.org/en/7.1.x/getting-started.html)

1. Uma vez instalado o Pytest, no console, execute o coma do abaixo:

```
pytest -s
```

2. Indique a partícula e a matriz, ela será exibida no console junto ao resultado dos testes. Exemplo:

```
Digite o tipo  de partícula (e, p ou n): e
Digite o tamanho da matriz: 6

['e', 'e', 'e', 'e', 'e', 'e']
['1', '1', '1', '1', '1', 'e']
['1', '1', '1', '1', '1', 'e']
['1', '1', '1', '1', '1', 'e']
['1', '1', '1', '1', '1', 'e']
['1', '1', '1', '1', '1', 'e']

```

### Sinta-se à vontade para testar o código do `cyclotron.py` com diferentes partículas e tamanhos de matriz. Bem como para alterar o código e modificar os testes. Divirta-se!
