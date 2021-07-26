#assumindo que a funcao eh unimodal no intervalo [a,b]
#o objetivo serah encontrar o extremo local da funcao, seja
# ela monotomicamente crescente para x<=m e decrescente para x>=m

#definindo o intervalo a partir do metodo bracket
import math

def bracket(a,f,passo=0.001,mult=2):
  bracket = [a]

  b = a + passo
  bracket = [a,b]

  fa = f(a)
  fb = f(b)

  if fa >= fb :
  
    c = b + passo
    fc = f(c)

    while fc < fb:
      b = c
      fb = fc
      passo = passo*mult
      c = c + passo
      fc = f(c)

      bracket = [a,c]

  else :
    c = a - passo
    fc = f(c)
    while fc < fa:
      a = c
      fa = fc
      passo = passo*mult
      c = c - passo
      fc = f(c)

      bracket = [c,b] 

  return bracket
funcao = lambda x: x**2
b = bracket(-2, funcao)
print(b)