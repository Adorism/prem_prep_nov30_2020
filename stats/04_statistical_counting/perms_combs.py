five_toys = ['red truck', 'pog', 'fidget spinner', 'tamagotchi', 'gi joe']

'''
You have 5 toys in a bag. You pull them out one at a time and 
you don't put them back in. In how many different orders
can you pull out these 5 toys?

5! = 120

['red truck', 'pog', 'fidget spinner', 'tamagotchi', 'gi joe']
['red truck', 'pog', 'fidget spinner', 'gi joe', 'tamagotchi']
['red truck', 'pog', 'gi joe', 'fidget spinner', 'tamagotchi']
...

'''

def factorial(num):
    prod = 1
    for n in range(2, num+1):
        prod *= n
    return prod

# print(factorial(-1))


'''
You have 10 students and you are conducting a science fair where 
4 students will win 1st, 2nd, 3rd, 4th. 
How many different arrangements of those 4 winners is possible?

code the perms(n, k) function, then answer this question ^

g h i j
g h j i
g i j h
...
'''
def perms(n, k):
    return int(factorial(n) / factorial(n-k))



def perms(n, k):
    perm = 1
    for num in range(n, n-k, -1):
        perm *= num
    return perm

# print(perms(10, 4)) # 5040


# print(perms(10000, 400)) # will have precision error with less optimized version



'''
Permutation Intuition

Five pets and 5 pet bets. What are all the ways 
that you can arrange those 5 pets in 5 beds?
'''

base_5 = ['bat', 'cat', 'frog', 'eel', 'hamster']

animals_counting = []

