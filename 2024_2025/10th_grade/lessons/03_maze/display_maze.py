def display_maze(maze):
    for line in maze:
        print("|", end="")
        for item in line:
            print(" " if item == 0 else "*", end="")
            
        print("|")


my_maze = [
    [ 0, 1, 0, 0, 0, 0 ],
    [ 0, 1, 1, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 1 ],
    [ 1, 1, 1, 0, 0, 0 ],
    [ 0, 0, 0, 0, 1, 1 ],
    [ 0, 1, 1, 0, 0, 0 ]
]

display_maze(my_maze)



