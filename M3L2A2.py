#cube of cube using function and arguments
def cube_of_cube(num):
    if num < 0:
        return "Please enter a positive number"
    else:
        cube = num ** 3
        cube_of_cube = cube ** 3
        return cube_of_cube