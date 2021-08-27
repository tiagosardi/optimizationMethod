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
uma função $\displaystyle{f(x)}$ é unimodal se, para algum valor $\displaystyle{m}$, ela cresce monotonamente para $\displaystyle {x}$ $\leq{m}$ e decresce monotonamente para $\displaystyle {x}$ $\geq {m}$. Nesse caso, o valor máximo de $\displaystyle {f(x)}$ é $\displaystyle{f(m)}$ e não existe nenhum outro máximo local.

# Problemas com 1 variável e sem restrições

## Método Bracketing	
Dentro de um intervalo [a b] da função, este método começará a percorrer a função unimodal $\displaystyle{f(m)}$ a partir de $\displaystyle{a}$ em um passo $\displaystyle{p}$ enquanto $\displaystyle{f(m)}$ descresce na função. Então, ao notar que o coeficiente angular mudou, o percurso inverte utilizando um passo menor, a fim de convergir com o mínimo local da função. O método funciona apenas para função unimodal.

### Vantagem
Simples de implementar

### Desvantagem
A taxa de acerto depende do passo.

Se tiver mais de um mínimo, ele vai encontrar algum mínimo, mas nao o melhor


## Golden Section Search
O método elimina intervalos que não sejam possíveis conter o mínimo local até que seja reduzida a distância entre o intervalo e assuma um valor aproximado para o mínimo local. O método também funciona apenas para função unimodal.

![alt text](http://url/to/img.png)


## Aproximação Quadrática
Assumindo que a função seja quadrática, o método usa o teorema de fermat para encontrar o mínimo local, derivando a função em primeira ordem e igualando a zero. E a partir do cálculo do sistema linear, é possível descobrir o coeficiente angular, de forma que se possa chegar ao mínimo local. 

# Vetores

# Descida do Gradiente
Método para busca do mínimo local, aplicando a inversa do gradiente da função f. Aplicado para resolução de problemas com várias variáveis. É um método indireto porque não usa o valor f(x) diretamente.

