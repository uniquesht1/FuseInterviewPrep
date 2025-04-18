# list comprehension
nums = [1, 2, 3, 4, 5,6,7,8,9,10]
my_list = [n for n in nums if n % 2 == 0]
print (my_list)

# dict comprehension

name= ['Bruce', 'Clark', 'Peter']
heros = ['Batman', 'Superman', 'Spiderman']
my_dict = {name: heros for name, heros in zip(name, heros)}
print (my_dict)

# lambda
nums = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, nums))
print(squared)