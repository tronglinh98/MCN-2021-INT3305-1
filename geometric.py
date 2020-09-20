import math

def prob(n, p):
  return p**n

def infoMeasure(n, p):
  i = prob(n, p)
  return -math.log(i, 2)

def sumProb(N, p):
  '''
  Khi p = 1/2 thì sumProb theo công thức sẽ bằng 
  p/(1-p) khi N tiến đến vô cùng 
  => sumProb = (1/2) / (1-1/2) = 1
  '''

  sum = 0.0
  for i in range(1, N+1):
    sum += prob(i, p)
  return sum

def approxEntropy(N, p):
  sum = 0.0
  for i in range(1, N+1):
    sum += infoMeasure(i, p)
  return sum / N
  
help(sumProb)

  