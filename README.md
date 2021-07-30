# optimizationMethod

## Metodo de otimização para funções objetivo que possuam várias restrições de igualdade e desigualdade


![Badge](https://img.shields.io/badge/Colab-F9AB00?style=for-the-badge&logo=googlecolab&color=525252)


<!--ts-->
   * [Sobre](#Sobre)
   * [Métodos com 1 variável](#Escalares)
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
- [ ] Métodos de busca do mínimo local com N variáveis
- [ ] Aplicação


# Escalares

## Método Bracketing	
Dentro de um intervalo [a b] da função, este método começará a percorrer f(m) a partir de a em um passo p enquanto f(m) descrece na função. Então, ao notar que o coeficiente angular mudou, o percurso inverte utilizando um passo menor, a fim de convergir com o mínimo local da função. O método funciona apenas para função unimodal.


## Golden Section Search
O método elimina intervalos que não sejam possíveis conter o mínimo local até que seja reduzida a distância entre o intervalo e assuma um valor aproximado para o mínimo local. O método também funciona apenas para função unimodal.


## Aproximação Quadrática
Assumindo que a função seja quadrática, o método usa o teorema de fermat para encontrar o mínimo local, derivando a função em primeira ordem e igualando a zero. E a partir do cálculo do sistema linear, é possível descobrir o coeficiente angular, de forma que se possa chegar ao mínimo local. 

# Vetores

# Descida do Gradiente
Método para busca do mínimo local, aplicando a inversa do gradiente da função f. Aplicado para resolução de problemas com várias variáveis. É um método indireto porque não usa o valor f(x) diretamente.

