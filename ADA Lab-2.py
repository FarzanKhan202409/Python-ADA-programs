def mergeSort(array):  								#START OF MERGE SORT FUNCTION
	if len(array) > 1:
		r = len(array)//2      				 		#Length divided by 2
		L = array[:r]          						        #LAST
		M = array[r:]        				  		        #front
		mergeSort(L)
		mergeSort(M)
		i = j = k = 0
		while i < len(L) and j < len(M): 
			if L[i] < M[j]: 							#COMPARING
				array[k] = L[i]  	
				i += 1
			else:
				array[k] = M[j]
				j += 1
			k += 1
		while i < len(L):                      					 #LAST ELEMENT
			array[k] = L[i]
			i += 1
			k += 1
		while j < len(M):						                   	#LAST ELEMENT
			array[k] = M[j]	
			j += 1
			k += 1
array = []                    
n = int(input('Enter size of the list:\n'))      				#ARRAY INPUT
print("Enter the numbers:")
for i in range(n): 
	temp = int(input()) 
	array.append(temp) 
mergeSort(array)	
print("Sorted array is: ")     					 		#PRINTING ARRAY
print(array)
