a_input = input('Enter the numbers seperated by comma:')
a_list = a_input.split(',')


def even_list_finder(a:list) -> list[int]:
    output_list=[]
    for num in a:
        if int(num) % 2 == 0:
            output_list.append(int(num))
    
    return output_list


print(even_list_finder(a_list))
print('asha')

