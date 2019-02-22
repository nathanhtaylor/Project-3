#x = [0,1,2]

# def function():
#     x[0] = 100
#     print('function:', x)
#     return

def main():
    #global x
    x = [0,1,2]
    x[0] = 99
    print('main:', x )
    return


main()

print(x)
