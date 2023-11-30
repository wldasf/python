while True:
    num_one = input("Number one: ")
    if num_one == 'q':
        break
    num_two = input("Number two: ")
    if num_two == 'q':
        break
    try:
        print(int(num_one) + int(num_two))
    except ValueError:
        print("One of the inputs is not a number.")