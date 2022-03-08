# Python Driver Code

def solve(s: str) -> chr:
  # l = len(s)
  sec_count=0
  count=0
  
  for i in range(l):
    
    cur_count=1
    for j in range(i+1,l):
      if (s[i]=!s[j]):
          break
          cur_count+=1
          
          if cur_count > count :
          sec_count = count
          count = cur_count
  return sec_count

# The following snippet reads the input in the required format. 
# Just complete the solve function above. 

T = int(input())
for i in range(T):
  test_case = input()
  answer = solve(test_case)
  print(answer)
