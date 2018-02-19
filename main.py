from hell_triangle import *

def main():
    print "Welcome Hell Triangle"
    print "Format input data Ex: [[6],[3,5],[9,7,1],[4,6,8,4]]"
    triangle = input("Input: ")
    hell =  HellTriangle(triangle)
    print hell.get_max()

if __name__ == "__main__":
    main()
