# implement of recursive function to calculate factorial number in python 
def facctorial(n):
  #checking the number
  # is 1 or 0 then
  # return 1
  # otherwise return 
  # factorial 
  if (n==1 or n==0):


    return 1
    
  else :
    return(n * factorial(n-1))
    # Driver code
num =5;
print ("number:",num)
print("factorial:",factorial(num))
    


