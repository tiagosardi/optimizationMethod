#utilizaremos um metodo de eliminacao de intervalos, reduzindo 
# a distancia entre a e b ao redor do minimo local. O metodo se
#chama Golden Section Search Method
#
import math
def golden_search(f,a,b,tol=1e-6):
  
  gr = (1 + math.sqrt(5))/2 #razao aurea


  c = b - (b-a)/gr
  d = a + (b-a)/gr

  while abs(b-a) > tol:
    if f(c) > f(d):
      a = c
    else:
      b = d
      
    c = b - (b-a)/gr
    d = a + (b-a)/gr

  return (b+a)/2