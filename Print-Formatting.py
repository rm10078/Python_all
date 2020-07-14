name='Elizabeth'
age=18
mark=96.6
#using .format index
print("My name is {0} and I am {1} years old and my score is {2}".format(name,age,mark))
#using f-string
print(f"My name is {name} and I am {age} years old and my score is {mark}")


#working with field width and precision
num=500/49
print(num)
print("The value of num is:{0:8.6f}".format(num))
print(f"The value of num is:{num:{8}.{6}}")