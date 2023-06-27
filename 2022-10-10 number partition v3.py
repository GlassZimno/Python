# Glass Zimny
# 11/10/2022

# if (primes[0]*i[0] + primes[1]*i[1] + ... + primes[j]*i[j]) == n-1:
#   value = primes[0]**i[0] * primes[1]**i[1] * ... * primes[j]**i[j]
def enum(n):
  if n<3:
    return [n]
  # Find all prime numbers smaller than n
  # Check each prime against all others so that
  # f(n) = i*prime 
  # f(n) * numOfPrimes
  # value *= prime**1
  # output.append(value)
  primes = [2]
  o=[]
  for i in range(3,n+1):
    prime=1
    for j in primes:
      if i%j==0:
        prime=0
    if prime:
      primes.append(i)

  i=[]
  for j in primes:
    i.append(0)
  front = len(i-1)
  iSum = 0
  while 1:
    for j in range(len(primes)):
      iSum += primes[j]*i[j]
    if iSum == n-1:
      product = 1
      for j in range(len(primes)):
        product *= primes[j]**i[j]
    elif iSum < n-1:
      
      
  print(iSum)
        
def prod(n):
  o = enum(n)
  o = list(set(o))
  length = len(o)
  o.sort()
  print(n,o)
  if length % 2 == 1:
    med = o[length//2]
  else:
    med = (o[(length-1)//2]+o[length//2])/2
  return "Range: "+str(o[-1]-o[0])+" Average: "+"{:0.2f}".format(sum(o)/len(o))+" Median: "+"{:0.2f}".format(med)

while 1:
  enum(int(input()))


