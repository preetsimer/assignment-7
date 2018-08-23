#question 1
my_dict = dict()
n=int(input("Enter size of dictionary "))
for i in range(1,n+1):
    key = input("Enter the key: ")
    value = input("Enter the value: ")
    my_dict[key] = value
print(my_dict)    

#question 2
dict1={}
dict2={}
n=int(input("Enter number of students: "))
s=int(input("Enter number of subject: "))
for i in range(1,n+1):
    dict2={}
    name = input("Enter name: ")
    for j in range(1,s+1):
              sub=input("Enter subject name: ")
              marks=int(input("Enter marks: "))
              dict2[sub]=marks
    dict1[name]=dict2
print(dict1)
student=input("Enter the name of student to see marks: ")
print(dict1[student])
