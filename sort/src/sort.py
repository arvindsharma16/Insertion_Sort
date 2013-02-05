'''
Created on 2013. 2. 5.

@author: changhan.ryu
'''

def sort(list):
    if len(list) == 0: 
        return list()
    elif len(list) == 1:
        return list
    else:
        for i in range(len(list)) :
            j = i - 1
            while j >= 0 :
                if list[j+1] < list[j]:
                    temp = list[j+1]
                    list[j+1] =  list[j]
                    list[j] = temp
                j = j - 1
            i = i + 1
        return list 
        
            
            
            
a = [7,3,1,2,4,6]
print(sort(a))       