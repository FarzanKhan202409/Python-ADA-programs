class Solution:  
    def solution(self, list1):  
        list1.sort()  #sort the given list
        for i in range(1, len(list1)):         #use for loop to check the two consecutive elements to find out if they are duplicates  
            for j in range(0, i):  
                if list1[i] == list1[i-1]:     #Check Duplicate Element after Sorting
                    return 'true'  
            return 'false'  
  
obj = Solution()                 
list1 = [1, 2, 3, 1]  
print(obj.solution(list1)) 
