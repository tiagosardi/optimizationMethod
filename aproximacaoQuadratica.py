#metodo para aproximacao quadratica
#assumindo que a funcao seja quadratica

#a partir do teorema de fermat, podemos encontrar o minimo
#derivando em primeira ordem a funcao e igualando a zero.
#Entao descobriremos o coeficiente angular do ponto resolvendo
# o sistema linear

"""
f(x)= p1 + p2x + p3x^2

f'(x) = p2+2*p3x

p2+2*p3x = 0

minimo da primeira aproximacao:
x*= -p2/2*p3

sistema linear:
fa = p1 + ap2
fb = p1 +bp2

avaliando x* com a funcao, podemos inferir onde o minimo nao estah e eliminaremos
parte da funcao.

forma fechada, onde a<b<c:
x* = 1/2 *((fa(b^2+c^2) + fb (c^2+a^2) + fc (a^2 + b^2))/ (fa (b-c) + fb(c-a) + fc(a-b)))

"""

def quadratic_fit_search(f,a,b,tol=1e-6):
  """ encontra o minimo para funcao de 1 variavel
    
    Args: 
      f: funcao objetivo
      [a b]: intervalo inicial
      tol: tolerancia para o ponto de minimo
  """

  c = b
  b = (c-a)/2

  fa = f(a)
  fb = f(b)
  fc = f(c)

  while abs(c-a) < tol:
    x = 0.5*(fa*(b**2-c**2)+fb*(c**2-a**2)+fc*(a**2-b**2))/(fa*(b-c) +fb*(c-a) +fc*(a-b))
    fx = f(x)
    print(x)
    if x > b:
      if fx > fb:
        c = x
        fc = fx
      else: 
        a = b
        fa = fb
        b = x
        fb = fx
    else:
      if fx > fb:
        a = x
        fa = fx
      else:
        c = b
        fc = fb
        b = x
        fb = fx

  return (a+c)/2