#  Write a function that returns all the permutation of the given string of length 3.

def generatePermutation(string,start,end):  
    current = 0;  
    #Prints the permutations  
    if(start == end-1):  
        print(string);  
    else:   
        for current in range(start,end):  
    
            x = list(string);  
            temp = x[start];  
            x[start] = x[current];  
            x[current] = temp;  
  
      
  
            generatePermutation("".join(x),start+1,end);  
           
            temp = x[start];  
            x[start] = x[current];  
            x[current] = temp;  
  
str = "ABC"  
n = len(str);  
print("All the permutations of the string are: ");  
generatePermutation(str,0,n);
