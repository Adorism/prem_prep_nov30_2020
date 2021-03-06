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

for an1 in base_5:
    for an2 in base_5:
        for an3 in base_5:
            for an4 in base_5:
                for an5 in base_5:
                    animals_counting.append([an1, an2, an3, an4, an5])

# for an_number in animals_counting:
#     print(an_number)

animal_perms = []

for an_number in animals_counting:
    perm = True

    for an in an_number:
        if an_number.count(an) > 1:
            perm = False
            break

    if perm:
        animal_perms.append(an_number)

# for an_number in animal_perms:
#     print(an_number)



'''
Combination
nCk = n! / ((n-k)! * k!)
'''

def combs(n, k):
    return int(factorial(n) / ((factorial(n-k) * factorial(k))))


def combs(n, k):
    perm = 1
    for num in range(n, n-k, -1):
        perm *= num
    return int(perm / factorial(k))

# print(combs(10, 5))



'''
Combs Intuition

Out of a traveling team of 11 futsol players, only 5 can be on the 
court at any given time. What are all the possible combinations
of 5 player teams?
'''

# an expensive counting approach

num_combs = combs(11, 5)
# print(num_combs)

def futsol_team_combs():
    eleven_nums = range(1, 11+1)

    # build our base 5 counting
    base_11 = []

    for i in eleven_nums:
        for j in eleven_nums:
            for k in eleven_nums:
                for l in eleven_nums:
                    for m in eleven_nums:
                        base_11.append([i,j,k,l,m])

    # for num in base_11:
    #     print(num)

    permutations = []

    for five in base_11:
        if len(list(set(five))) == 5:
            permutations.append(five)

    # for perm in permutations:
    #     print(perm)

    combinations = []

    for five in permutations:
        sorted_five = sorted(five)

        if sorted_five not in combinations:
            combinations.append(sorted_five)

    return combinations

# for five in futsol_team_combs():
#     print(five)



# an expensive sampling approach

'''
We can sample 5 players from our list of 11,
can build combinations until we reach combs(11, 5)
'''

from random import choice

def futsol_combs_samp(team_size=11, num_players=5):
    player_combs = []

    player_range = range(1, team_size+1)

    while len(player_combs) < combs(team_size, num_players):
        player_comb = []

        while len(player_comb) < num_players:
            player_num = choice(player_range)

            if player_num not in player_comb:
                player_comb.append(player_num)
        
        player_comb = sorted(player_comb)

        if player_comb not in player_combs:
            print(player_comb)
            player_combs.append(player_comb)

    return player_combs


team_size = 11
num_players = 5


print(len(futsol_combs_samp(team_size, num_players)))
print(combs(team_size, num_players))