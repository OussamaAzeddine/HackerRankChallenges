# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import sqrt
from statistics import mean

if __name__ == '__main__':
  physics = [15,12,8,8,7,7,7,6,5,3]
  history = [10,25,17,11,13,17,20,13,9,15]

  m_phy = mean(physics)
  m_his = mean(history)
  N = len(physics)
  nominateur = 0
  denom_p = 0
  denom_h = 0
  for k in range(N):
    nominateur += (physics[k]-m_phy)*(history[k]-m_his)
    denom_p += (physics[k]-m_phy)**2
    denom_h += (history[k]-m_his)**2
  denom_p = sqrt(denom_p)
  denom_h = sqrt(denom_h)
  denom = denom_h*denom_p
  print(str(round(nominateur/denom,3)))
