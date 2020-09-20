import math

def giaithua(n):
  if n == 0:
    return 1
  else:
    return n * giaithua(n - 1)
    
def prob(n, p, N):
  tohop = giaithua(N) / (giaithua(n) * giaithua(N-n))
  return tohop * p ** N

def infoMeasure(n, p, N):
  i = prob(n, p, N)
  return -math.log(i, 2)

def sumProb(N, p):
  sum = 0.0
  for i in range(1, N+1):
    sum += prob(i, p)
  return sum

def approxEntropy(N, p):
  sum = 0.0
  for i in range(1, N+1):
    sum += infoMeasure(i, p, N)
  return sum / N  