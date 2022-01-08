'''Exercícios Teóricos | Capítulo 12

1) O que são e para que servem os métodos especiais?

Métodos especiais, ou métodos mágicos em Python, são métodos predefinidos em todos os objetos,
com invocação automática sob circunstâncias especiais. Eles normalmente não são chamados diretamente
pelo usuário mas podem ser overloaded (sobrescritos e alterados). Seus nomes começam e terminam com
sublinhados duplos chamados de dunder (uma expressão derivada de double underscore). As operações abaixo
são exemplos de métodos mágicos e como acioná-los, com o operador + e a função len().

Vemos que somar dois números usando o operador + aciona o método __add __ e
calcular o comprimento de um objeto usando a função len() equivale a usar seu método __len__().

Uma das principais vantagens de usar métodos mágicos é a possibilidade de elaborar
classes com comportamentos similares ou iguais aos de tipos internos.


2) Que vantagens há em esconder a representação dos objetos de uma classe do utilizador?

Os objetos considerados isoladamente pouco servem. Manipular objetos, além da sua criação, constitui a tarefa
principal de um programa. Essa manipulação fica a cargo de operações específicas para os objetos de um dado tipo.
Por exemplo, podemos somar, dividir e/ ou muliplicar números. Mas também, podemos fazer operações menos comuns, como
movimentar e/ou transformar uma imagem no seu negativo.

Um aspecto importante desta organização está no fato de podermos efetuar operações com os objetos
sem termos de nos preocupar com o modo como os mesmos se encontram representados internamente no computador.
Podemos afirmar, então, que a representação está escondida e que acedemos aos objetos pelo seu nome, explorando
o seu comportamento através das operações.

Essa associação forte entre objetos, com os seus atributos e as operações que com eles podemos efetuar,
é a base da chamada PROGRAMAÇÃO ORIENTADA AOS OBJETOS (POO).


3) O que se entende por interface pública?

O que o programador VÊ de um objeto é a sua interface (materializa um contrato entre o tipo de dados (a classe)
e os seus utilizadores, que lhe permite aceder a componentes do objeto e, eventualmente, modificá-lo através de um
conjunto de operações definidas para o mesmo.

Quando definimos uma classe, determinamos seus atributos (ex: numerador, denumerador), que, num dado momento,
definem o ESTADO do objeto. Quando definimos as operações possíveis com os objetos da classe (ex: soma, produto),
estamos a definir implicitamente o seu COMPORTAMENTO.

Quando definimos uma classe através de seus atributos e das operações que podemos efetuar com os objetos da classe
sem fazermos referência à implementação, dizemos que estamos a falar de TIPOS DE DADOS ABSTRATOS.


4) Que tipos de dados lineares conhece? E não lineares?

Dados lineares: pilhas (stacks) e filas (queues)
Dados não lineares: árvore binárias


5) O que é e para que serve o módulo ctypes?

Ctypes é uma interface de função externa que permite carregar bibliotecas dinâmicas que exportam
uma interface C. Com ele, você pode usar bibliotecas C de Python, por exemplo, libev, libpq.

ctypesé uma biblioteca de funções estrangeiras para Python. Fornece tipos de dados compatíveis com
C e permite chamar funções em DLLs ou bibliotecas compartilhadas. Ele pode ser usado para envolver essas
bibliotecas em Python puro.

a) Incapacidade de interagir com a API do intérprete. Ctypes é uma maneira de interagir com bibliotecas
C no lado do Python, mas não fornece uma maneira para o código C / C ++ interagir com o Python.

b) Exportando uma interface de estilo C. Os tipos podem interagir com as bibliotecas ABI neste estilo,
mas qualquer outra linguagem deve exportar suas variáveis, funções e métodos por meio de um wrapper C.

c) A necessidade de escrever wrappers. Eles devem ser escritos tanto no lado do código C ++ para compatibilidade
ABI com C quanto no lado Python para reduzir a quantidade de código clichê.

'''