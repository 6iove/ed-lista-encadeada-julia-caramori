---
# Lista Encadeada
Este repositório contém uma atividade desenvolvida no 4º semestre do curso de Tecnólogo em Análise e Desenvolvimento de Sistemas (TADS) do Instituto Federal de Mato Grosso do Sul (IFMS), para a disciplina de Estruturas de Dados.

---
## Objetivo
Implementar uma lista simplesmente encadeada utilizando Programação Orientada a Objetos (POO) em Python.

A estrutura permite armazenar elementos de forma dinâmica, conectando cada elemento a um nó subsequente, formando uma cadeia de nós.

## Sobre 
O código conta com funções que trazem lógica para:
* `insert_beginning`: inserir um nó no começo da lista; 
* `insert_end`: inserir um nó ao final da lista;
* `remove`: remove um nó da lista;
* `search`: realiza busca de um elemento na lista;
* `print_list`: imprime lista no terminal;
* `get_size`: devolve o tamanho da lista;
* `is_empty`: verifica se a lista está vazia.

## Como testar
As funções podem ser chamadas diretamente no código, passando os parâmetros necessários.

Exemplo de uso: 
```
list.insert_beginning(12) # insere número 12 no começo da lista 
list.insert_end(20) # insere número 20 ao fim da lista 
list.remove(12) # remove o número 12 da lista

list.print_list() # imprime a lista

list.search(15) # busca o número 15 da lista - retorna False
list.get_size() # devolve o tamanho da lista - retorna 1
list.is_empty() # verifica se a lista esta vazia - retorna False 
```
## Como executar 
Para executar o programa, utilize o terminal na pasta do projeto: 
```
python lista_simplesmente_encadeada.py
```
