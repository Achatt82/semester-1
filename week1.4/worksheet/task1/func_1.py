
def func_1(lst_value): 
    ''' 
    write your docstring to explain the function 

    This function declares a variable sum initialsed with the value 0. A new variable is declared called num_of_value that 
    is initialised with the value of the length of the parameter variable lst_value. the function then iterates over lst_value, 
    where during each iteration, the current value is added to the variable sum. The function then returns the value of the sum 
    divided by the number of values.
    ''' 

    sum = 0 
    num_of_value = len(lst_value) 
    for value in lst_value: 
        sum = sum + value # This wasnt indented but I am assuming it was supposed to be otherwise the loop would be redundant.
    return sum/num_of_value 