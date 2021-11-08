
import math
from numpy import *
from time import time

random.seed(20000)
t0=time()

S0=100.0;K=105.0;T=1.0;r=0.05;sigma=0.2
M=50;dt=T/M;I=250000

S=S0*exp(cumsum((r-0.5*sigma**2)*dt+sigma*math.sqrt(dt)*random.standard_normal((M+1,I)),axis=0))

S[0]=S0

C0=math.exp(-r*T)*sum(maximum(S[-1]-K,0))/I

tnp2=time()-t0;
print C0
print tnp2

