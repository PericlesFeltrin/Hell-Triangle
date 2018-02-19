# Hell-Triangle
Hell-Triangle Challenge

## Problem
Given a triangle of numbers, find the maximum total from top to bottom Example:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;6

&nbsp;&nbsp;&nbsp;3 5

&nbsp;&nbsp;9 7 1

4 6 8 4

In this triangle the maximum total is:  6 + 5 + 7 + 8 = 26

An element can only be summed with one of the two nearest elements in the next row. For example: The element 3 in the 2nd row can only be summed with 9 and 7, but not with 1
Your code will receive an (multidimensional) array as input. The triangle from above would be: example = [[6],[3,5],[9,7,1],[4,6,8,4]]

## Algorithm

No algoritmo temos uma busca em profundidade, que vai do topo para base do triângulo. Esse algoritmo foi desenvolvido com recursividade, assim, pode ser que haja algumas limitações e um consumo de considerável para grandes quantidades de dados.

#### Language
A linguagem de programação escolhida foi o Python, pela facilidade de trabalhar com estrutura de dados como, listas e matrizes, testes e execução. Também por ter uma vasta biblioteca de módulos, que podem ser acoplados ao código.


####  Run Algorithm

Para realizar a execução é necessário ter instalado o [Python](https://www.python.org). Abrir o Terminal, acessar a pasta que está o arquivo, e só assim realizar o comando abaixo.

Obs.: Execução normal, com apenas um dado(Hell Triangle) de entrada via terminal.
```sh
python main.py
```
Obs.: Execução com um arquivo de entrada, com vários dados(Hell Triangle) de entrada.
```sh
python main_input_txt.py < inputs.txt
```

## Tests

Os testes foram criados com o framework de testes doctest, que já está acoplado ao Python. O framework foi escolhido pela facilidade de implementação e execução dos testes.

#### Run Tests Cases
Obs.: Acessar o terminal, e após a pasta em que se encontra o arquivo.
```sh
	python -m doctest -v tests.txt
```
