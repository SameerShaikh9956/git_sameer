#Q1.write a program to print the prime numbers between 1 and 100 using loop.
#Ans: 
'''for j in range(0,100+ 1):
    if j > 1:
        for i in range (2,j):
            if (j % i) == 0:
                break
        else:
           print(j)'''
      
#Q2.Given a list of int , write a function that returns the product of all odd number in the using a loop.
#Ans:
'''list1=[1,2,3,4,5,6,7,8,9,10]
for i in list1:
    if i%2==0:
        print("even")
    else:
        print("odd")'''
    
#Q3. write a python function that taes a list and removes all duplicates using a loop (without using set()).
#Ans:
'''list1=[1,2,3,4,5,6,7,8,9,10,2,4,6,7]
list1=set(list1)
for i in list1:
  if i==i:
    print(list1)
print(type(list1))'''

    


#Q4.implement a function to find the the second largest number in a list using a loop.
#Ans :
'''list1=[1,2,3,4,5,6,7,8,9]
first_largest= second_largest=float('-inf')

for num in list1:
    if num>first_largest:
        second_largest=first_largest
        first_largest=num
    elif num>second_largest and num<first_largest:
        third_largest=second_largest
        second_largest=num
print(f'The third_highest value is {second_largest}')'''

#Q5.write a function that reverse a string without using slicing , only using loop.
#Ans:
'''list2=["hii","hello","how","what"]
 
end=0
for _ in list2:
    end+=1
    end-=1
    for j in range(end//2+1):
        list2[j],list2[end-1]=list2[end-1],list2[j]
    print(list2)'''
    
#Q6.Write a python program that prints the fibonacci sequence up to n terms using loop.
#Ans:
'''n=10
a,b=0,1
c=a+b
print(a)
print(b)
for i in range(10): 
        c=b
        b=a
        a=c+b
        print(a)'''
    
#Q7.Write a python function to rotate a list element to the right using a loop.
'''l1=[1,3,2,5,6]
k=2
end=
for _ in l1:
    end+=1
    end-+1
    for k in range (end//2+1):
        l1[k],l1[end-1]=l1[end-1],l1[k]
print(l1)'''

#Q8.implement a function to fatten a nested list using loops.
'''list1_list=[[1,2,3],[4,5]]
list2_list=[i for i in list1_list for i in i]
print(list2_list)'''

#Q9.Write a program that prints all the elements of a list and their corresponding frequencies using loop.
'''
'''
  
#Q10.write a program that calculate tha camulative sum of a list using a loop.
'''
'''

#Q11.Write a program to shift every element of a list to the left by one position, and the first element moves to the last,using loop.
'''list2=[1,2,3,4,5,6,7,8,9,10]
 
end=0
for _ in list2:
    end+=1
    end-=1
    for j in range(end//2+1):
        list2[j],list2[end-1]=list2[end-1],list2[j]
    print(list2)'''
    
#Q12.write a program to find the common element between two list using loop.
# set.intersection(set2)
'''list1=[1,2,3,4,5,6,7,8]
list2=[9,10,2,11,12,3,13,4]
for i in list1:
    if i in list2:
        print(i)'''

#Q13.write a program to check if two string are anagram or not.
'''str1="no"
str2="on"
for i in str1:
    if i in str2:
        print("it is anagram")
    else:
        print("not anagram")'''

# Q14.write a program that finds the intersection of two sets using loop.
'''set1={1,2,3,4,5,6,7,8}
set2={9,10,2,11,12,3,13,4}
for i in set1:
    if i in set2:
        print(i)'''
       
#Q15.implement a function to transfer a matrix using loops.

'''matrix=[
    [1,2,3],
    [3,4,5],
    [6,7,8]]
for i in matrix:
      if i in matrix:
        print(matrix)'''

#Q16.write a python program to chacks if a list is sorted in ascending order using loop.
'''list1=[1,2,3,4,5]
for i in list1:
    if i+1>i:
        print("the list is sorted with ascending order.")
    else:
        print("the list is sorted with descending order. ")'''
  
#Q17.write a function that takes a list integer and returns the longest contiguose subsequence of increacing numbers using loop.
'''list1=[1,2,3,4,5,6,1,2,4,8,7,9,10]
for i in list1:
    if i-1>i:
        print()'''

#Q18.write a python program that prints the pascals tringle up to n rows using loops.
'''
'''

#Q19.implement a function that counts the number of vowels in a string using loop.
'''str1="apple"
vowels="a","e","i","o","u"
for i in str1:
    if i in vowels:
        print("vowels")
    else:
        print("not vovels")
'''
#Q20.write a function to merge two dictionary by adding values for common keys using loops.
'''dic1={"a":19,"b":20,"c":23}
dic2={"a":18,"b":22,"c":11}
dic3={}
for i in dic2: 
    if i in dic1:
       dic3[i]=dic2[i]+dic1[i]
print(dic3)'''

#Q21.write a python program to find the union of two lists without using set(),used loops.
'''
'''
 
 #Q22.implement a function that takes a list of int and return that list with all element incremented by 1 using loop.
'''list1=[1,2,3,4,5,6,7,8,9,10]
for i in range(len(list1)):
    list1[i]+=1
    print(list1)'''

#Q23.write a python function that takes two lists and returns a new list with element at odd position from the first list and elements at even position from the second list.
       
'''l1=[12,1,4,23,45]  
l2=[1,2,3,4,5,6]
for i in l1:
    if i%2==0:
        print(f'in {l1}even:{i}')
    if i%2!=0:
        print(f'in {l1}odd:{i}')
        
for j in l2:
    if j%2==0:
        print(f'in {l2} is even:{j}')
    if j%2!=0:
        print(f'in {l2} is odd:{j}')'''
        
#Q24.write a python program to check if a tuple is a palidrome using loop.  
'''tup1=1,2
tup2=3,2,1
for i in tup1:
    if i in tup2:
        print("it is palindrome")
    else:
        print("not palindrome")'''
        
#Q25. implement a function that reverse the element in a dic (i.e, swaps keys and values ) using loop.
dic1={"name":"priti","middle name":"subhash","surnam":"tarmale"}
end=0
for _ in dic1:
    end=+1
    end-=1
    for j in dic1:
        dic1[j],dic1[end+1]=dic1[end+1],dic1[j]
        print(dic1)
    



      


    
#Q26. write a python function that takes a string and prints a possible substring of the string using loop.


#Q27.write a python program that counts the number of digit,letters,and spl char in a string using loops.

#Q28.implement a fun that checks whether two lists are cyclic rotation of each other using lops.
#Q29.write a program to check if a element in a list are unique using loop.
#Q30.write a program to find non repeating char in a string.
#Q31.implement a fun that sorta ist using the bubble sort algorithm.
#Q32write a program that prints a possibe combination of the element of a using loop: