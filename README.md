# optimizationMethod

## Metodo de otimização para funções objetivo que possuam várias restrições de igualdade e desigualdade


![Badge](https://img.shields.io/badge/Colab-F9AB00?style=for-the-badge&logo=googlecolab&color=525252)


<!--ts-->
   * [Sobre](#Sobre)
   * [Métodos com 1 variável](#Problemas)
   * [Métodos com várias variáveis](#Vetores)
<!--te-->
# Sobre
Trata-se de algoritmos de busca do mínimo local de uma função.

# Status
<h4 align="center"> 
	🚧 Em construção 🚧
</h4>

### Features

- [x] Métodos de busca do mínimo local para 1 variável
- [x] Métodos de busca do mínimo local com N variáveis
- [x] Aplicação

# Definições básicas

## Função unimodal
uma função \displaystyle{f(x)} é unimodal se, para algum valor \displaystyle{m}, ela cresce monotonamente para \displaystyle{x} \leq{m} e decresce monotonamente para \displaystyle{x} \geq {m}. Nesse caso, o valor máximo de \displaystyle{f(x)} é \displaystyle{f(m)} e não existe nenhum outro máximo local.

# Problemas com 1 variável e sem restrições

## Método Bracketing	
Dentro de um intervalo [a b] da função, este método começará a percorrer a função unimodal $\displaystyle{f(m)}$ a partir de $\displaystyle{a}$ em um passo $\displaystyle{p}$ enquanto $\displaystyle{f(m)}$ descresce na função. Então, ao notar que o coeficiente angular mudou, o percurso inverte utilizando um passo menor, a fim de convergir com o mínimo local da função. O método funciona apenas para função unimodal.

### Vantagem
Simples de implementar

### Desvantagem
A taxa de acerto depende do passo.

Se tiver mais de um mínimo, ele vai encontrar algum mínimo, mas nao o melhor.

### Algoritmo

**Inicialização**

* ponto a
* Função f
* passo s
* multiplicador m

**Passo 1**

* Definir b = a+s
* Calcular f(a) e f(b)
* Definir c= b+s

**Passo 2**

* Se f(a)>=f(b), então enquanto f(c)< f(b) atualize:
  * b=c
  * f(b)
  * c = c+s*m
  * f(c)
  
  E ao sair do laço, retorne a e c

* Se f(a)< f(b), então enquanto f(c)< f(a) atualize:
  * a=c
  * f(a)=f(c)
  * s = s*m
  * c=c-s
  * f(c)
  
  E ao sair do laço, retorne c e b

## Golden Section Search
O método elimina intervalos que não sejam possíveis conter o mínimo local até que seja reduzida a distância entre o intervalo e assuma um valor aproximado para o mínimo local. O método também funciona apenas para função unimodal.

![alt text](https://github.com/tiagosardi/optimizationMethod/blob/main/images/goldenSection.jpg)

### Vantagem

* Simples de implementar
* A função não precisa ser contínua
* Garante a convergência

### Desvantagem

* Só garante um mínimo local
* Se baseia na existência de um intervalo inicial pré-definido

### Algoritmo

**Inicialização**

* Entra com a função
* Determina um intervalo [a,b]
* Determina uma tolerância

**Passo 1**

* Determina dois pontos intermediários c e d tal que: 
   
  * c = b + (b-a)/gr 
  * d = b - (b-a)/gr

  Sendo gr a razão áurea.

**Passo 2**

Avalia f(c) e f(d)

* Se f(c) > f(d), então determine novos a,c,d,b. Repare que o valor de c é calculado com a razão áurea:

  * a = d
  * d = c
  * c = a + (b-a)/gr
   
* Se f(c) < f(d), entao determine novos a,c,d,b. Repare que o valor de d é calculado com razão áurea:

  *  b=c
  *  c=d
  *  d= b - (b-a)/gr

  
**Passo 3**

Se b-a < tolerância, então o extremo local possível é retornado no atual (a+b)/2 e a iteração para, caso contrário, volta ao passo 2

## Aproximação Quadrática
Assumindo que a função seja quadrática, o método usa o teorema de fermat para encontrar o mínimo local, derivando a função em primeira ordem e igualando a zero. E a partir do cálculo do sistema linear, é possível descobrir o coeficiente angular, de forma que se possa chegar ao mínimo local. 

# Vetores

# Descida do Gradiente
Método para busca do mínimo local, aplicando a inversa do gradiente da função f. Aplicado para resolução de problemas com várias variáveis. É um método indireto porque não usa o valor f(x) diretamente.

# Força Bruta
Usado para problemas com várias variáveis, podendo o problema ser inteiro.
Ele vai permutar entre todos os valores.

Um exemplo de uso é com Caixeiro Viajante

# Algoritmo Guloso

O algoritmo guloso com densidade encontra o valor ótimo do problema da mochila com valores binários