# def custom_len(string):
#     count = 0 
#     for element in string:
#         count +=1
#     return count

# print(custom_len([1,7,3]))

# def custom_sum(imput):
#     count = 0 
#     for element in imput:
#         count += element
#     return count

# print(custom_sum([1,7,3]))

# def custom_min(imput):
    
#     lowest_number = imput[0]
#     for element in imput:
#         if element < lowest_number:
#             lowest_number = element
            
#     return lowest_number

# print(custom_min([6,1,2]))


# def custom_max(imput):
    
#     biggest_number = imput[0]
#     for element in imput:
#         if element > biggest_number:
#             biggest_number = element
            
#     return biggest_number

# print(custom_max([6,7,9]))


def custom_sorted(input, reverse=False):
    # Rozlišení mezi řetězcem a seznamem
    if isinstance(input, str):
        is_string = True
        input = list(input)  # Převod řetězce na seznam znaků pro řazení
    else:
        is_string = False

    for i in range(len(input)):
        for j in range(i+1, len(input)):
            if (not reverse and input[i] > input[j]) or (reverse and input[i] < input[j]):
                input[i], input[j] = input[j], input[i]

    if is_string:
        input = ''.join(input)  # Spojení seznamu znaků zpět do řetězce

    return input

# Testování funkce
print(custom_sorted("Hello", True))  # Pro seznam



# def custom_reversed(imput):
#     reversed_list = imput [::-1]
#     return reversed_list

# print(custom_reversed("Hello"))


