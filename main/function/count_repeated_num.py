# wpa to display the number repeated in a sequence

def count_repeated_values():
    user_input = input("Enter values separated by commas: ")
    values = user_input.split(',')
    Num = {}

    for value in values:
        if value in Num:
           Num [value] += 1
        else:
            Num[value] = 0

    for value, count in Num.items():
        print(f"The value '{value}' is repeated {count} times.")
        
count_repeated_values()

