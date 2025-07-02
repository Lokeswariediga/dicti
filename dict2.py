# 1. Delete a list of keys from a dictionary 
# sample_dict = {"name": "Kelly","age": 25, "salary": 8000, "city": "New york"} 
sample_dict={"name": "Kelly","age": 25, "salary": 8000, "city": "New york"} 
res=["name","salary"]
for res in res:
   sample_dict.pop(res)
print(sample_dict)
# output:
# {'age': 25, 'city': 'New york'}


# 2. Count the frequency of each character in a given string using a dictionary.
L="priyanka"
res={}
for x in L:
    if x not in res:
        res[x]=1
else:
    res[x]+=1
    print(res)
#     output:
    # {'p': 1, 'r': 1, 'i': 1, 'y': 1, 'a': 2, 'n': 1, 'k': 1}


# 3. Swap keys and values in a dictionary.
P={"ammu":21,"priya":15,"priyanka":22}
res={}
for a,b in P.items():
    res[b]=a
    print(res)
#     output:
#     {21: 'ammu', 15: 'priya', 22: 'priyanka'}

# 4. Write a program to sum all the values in a dictionary. 
A={"a":101,"b":50,"c":69,"d":79,"e":37}
sum=0
for x in A:
    sum+=A[x]
print(sum)
# # output:
# 336


# 5. Create a nested dictionary for student details (name, roll, marks).
L={"student1":{'name':"ammu",'roll':201,'marks':250},
   "student5":{'name':"priya",'roll':206,'marks':550}}
print(L)
# output:
# {'student1': {'name': 'ammu', 'roll': 201, 'marks': 250}, 'student5': {'name': 'priya', 'roll': 206, 'marks': 550}}


# 6. Convert a dictionary to a list of tuples.
L={"L":15,"M":17,"N":19,"X":21,"Y":23,"O":25}
for x in L.items():
    print(x)
#     output:
#     ('L', 15)
# ('M', 17)
# ('N', 19)
# ('X', 21)
# ('Y', 23)
# ('O', 25)


# 7. Write a program to store names as keys and their lengths as values. 
S=["python","developer","stack","java","c++"]
res={}
for x in S:
    res[x]=len(x)
    print(res)
#     output:
#     {'python': 6, 'developer': 9, 'stack': 5, 'java': 4, 'c++': 3}


# 8. Create a dictionary for numbers 1 to 5, where the value is "even" if the number is even, and 
# "odd" if the number is odd 
M={'odd':1,'even':2,'odd':3,'even':4,'odd':5}
L={}
for i in range (1,6):
    if i%2==0:
        L[i]="even"
else:
       L[i]="odd"
print(L)
# output:
# {2: 'even', 4: 'even', 5: 'odd'}


# 9. Create Reverse Word Dictionary 
# Given list of words: 
# words = ["cat", "dog", "bat"] 
# Create a dictionary with words as keys and their reversed strings as values 
words = ["cat", "dog", "bat"] 
L={}
for x in words:
    res=""
    for i in x:
        res=i+res
    L[x]=res 
print(L)   
# output:
# {'cat': 'tac', 'dog': 'god', 'bat': 'tab'}