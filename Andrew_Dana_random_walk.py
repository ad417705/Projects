''' This program is an ABM and will be used to track the movement of a random autonomous 
agent in a 2-D grid and a fixed grid size of 15x15. The way the agent moves will be randomly generated.
The agent will take 100 randomly generated moves
Author: [Andrew Dana]
'''

import random
random.seed(43543)

grid = [[0 for _ in range(15)] for _ in range(15)]

grid[6][6] = 1


c = 100
i,j = 6,6

agent_path = [(6,6)]


while c > 0:
    randomNum = random.randint(1,20)
    c -= 1
    if randomNum >=1 and randomNum <= 5:
        if i - 1 >=0:
            i = i-1
            grid[i][j] += 1

    if randomNum >=6 and randomNum <= 10:
        if i + 1 <= 14:
            i += 1
            grid[i][j] +=1
    
    if randomNum >= 11 and randomNum <= 15:
        if j - 1 > 0:
            j = j - 1
            grid[i][j] += 1
    
    if randomNum >= 16 and randomNum <=20:
        if j -1 <= 14:
            j += 1
            grid[i][j] += 1
    agent_path.append((i,j))


def print_grid(list):
    for i in range(15):
        print(grid[i])

print_grid(grid)

final_position = agent_path[-1]

distance = abs(final_position[0] - 6) + abs(final_position[1] - 6)

print(f'Agent\'s final position: {final_position}')
print(f'Distance from starting point: {distance}')