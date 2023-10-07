# Function to calculate the sum of variable arguments
def sum_of_args(*args):
    # Print the arguments received
    print(args)
    result = 0
    
    # Loop through each argument in args
    for x in args:
        result += x
    
    # Print the result
    return print(result)

# Call the function with arguments 2, 5, and 9
sum_of_args(2, 5, 9)