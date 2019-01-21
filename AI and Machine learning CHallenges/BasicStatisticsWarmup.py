# Enter your code here. Read input from STDIN. Print output to STDOUT
#Ongoing ....
def func_median(N,tab):
  if(N%2 == 1):
    return tab[N//2]
  else:
    return (tab[int(N/2)]+tab[int(N/2)-1])/2

def func_mean(N,tab):
  count = 0
  for i in range(N):
    count += tab[i]
  return round(count/N,1)

def func_mode(N,tab):
  higher_occ_val = 0
  occ = 0
  for k in range(N):
    occ = tab.count(tab[k])
    if( occ > higher_occ_val): 
      higher_occ_val = occ
  return higher_occ_val

"{{f_list_all_subject.display}}"

if __name__ == '__main__':
  #read Data
  N = int(input())
  tab_entry = list(map(int,input().split()))
  print(func_mean(N,tab_entry))
  print(func_median(N,tab_entry))
  print(func_mode(N,tab_entry))
