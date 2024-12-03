def display_maze(maze):
    for line in maze:
        print("|", end="")
        for item in line:
            print(" " if item == 0 else "*", end="")
            
        print("|")

def check_solution(solution, maze): # return boolean
    # XXX implement this
    return False 


my_maze = [
    [ 0, 1, 0, 0, 0, 0 ],
    [ 0, 1, 1, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 1 ],
    [ 1, 1, 1, 0, 0, 0 ],
    [ 0, 0, 0, 0, 1, 1 ],
    [ 0, 1, 1, 0, 0, 0 ]
]

display_maze(my_maze)

solution = [(0,0), (0,1), (0,2), (1,2), (2,2), (3,2), (3,3), (3,4), (3,5),
            (4,5), (5,5)]
print("The solution is", "good" if check_solution(solution, my_maze) else "bad")



