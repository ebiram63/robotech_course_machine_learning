import re
def solve(arr):
    array = arr
    arr_splited_by_equal = array.split("=")
    #print(arr_splited_by_equal)
    
    arr_splited_by_plus = arr_splited_by_equal[0].split("+")
    number_one = arr_splited_by_plus[0].strip()
    number_two = arr_splited_by_plus[1].strip()
    number_three = arr_splited_by_equal[1].strip()
    #print(number_one, number_two, number_three)
    pattern = '#'
    match_one = (re.search(pattern, number_one))   
    match_two = (re.search(pattern, number_two)) 
    match_three = (re.search(pattern, number_three)) 
    if(match_one):
        real_number = int(number_three) - int(number_two)
        position = match_one.start()
        if(position == 0):
            new_replace = number_one.replace("#" , "")
            if((re.search(new_replace, str(real_number)))):
                match_number= (re.search(new_replace, str(real_number)))
                start_index = match_number.start()
            else:
                return("-1")
            start_index = match_number.start()
            new_real_number = str(real_number)[:start_index] + str(new_replace)
            #print(new_real_number)
            #print(real_number)
            if(new_real_number == str(real_number)):
                 return(f"{real_number} + {number_two} = {number_three}")
            else:
                return("-1")
        new_replace = number_one.replace("#" , "")
        if(int(new_replace) + int(number_two) == int(number_three)):
            return(f"{real_number} + {number_two} = {number_three}")
        new_string = number_one.replace("#",str(real_number)[position])
        #print(new_string)
        if re.match(str(new_string), str(real_number)):
            return(f"{real_number} + {number_two} = {number_three}")
        else:
            return("-1")
    if(match_two):
        real_number = int(number_three) - int(number_one)
        position = match_two.start()
        if(position == 0):
            new_replace = number_two.replace("#" , "")
            len_number_one = len(new_replace)
            #print(len_number_one)
            if((re.search(new_replace, str(real_number)))):
                match_number= (re.search(new_replace, str(real_number)))
                #print(match_number)
                start_index = match_number.start()
            else:
                return("-1")
            start_index = match_number.start()
            new_real_number = str(real_number)[:start_index+1] + str(new_replace)
            #print(new_real_number)
            #print(real_number)
            if(new_real_number == str(real_number)):
                 return(f"{number_one} + {real_number} = {number_three}")
            else:
                return("-1")
        else:
            position = match_two.start()
            sliced_number_two = number_two.split('#')
            if any(x in sliced_number_two[0] for x in str(real_number)) and str(real_number).endswith(sliced_number_two[1]):
                return(f"{number_one} + {real_number} = {number_three}")
        new_replace = number_two.replace("#" , "")
        if(int(number_one) + int(new_replace) == int(number_three)):
            return(f"{number_one} + {real_number} = {number_three}")
        new_string = number_two.replace("#",str(real_number)[position])
        #print(new_string)
        if re.match(str(new_string), str(real_number)):
            return(f"{number_one} + {real_number} = {number_three}")
        else:
            return("-1")
    if(match_three):
        real_number = int(number_one) + int(number_two)
        #print(real_number)
        position = match_three.start()
        if(position == 0):
            if number_three == '#':
              return(f"{number_one} + {number_two} = {real_number}")  
            new_replace = number_three.replace("#" , "")
            if((re.search(new_replace, str(real_number)))):
                match_number= (re.search(new_replace, str(real_number)))
                start_index = match_number.start()
            else:
                return("-1")
            start_index = match_number.start()
            new_real_number = str(real_number)[:start_index+1] + str(new_replace)
            #print(new_real_number)
            #print(real_number)
            if(new_real_number == str(real_number)):
                 return(f"{number_one} + {number_two} = {real_number}")
            else:
                return("-1")
            print(match_number)
        new_replace = number_three.replace("#" , "")
        if(int(number_one) + int(number_two) == int(new_replace)):
            return(f"{number_one} + {number_two} = {real_number}")
        new_string = number_three.replace("#",str(real_number)[position])
        print(new_string)
        print(real_number)
        if re.match(str(new_string), str(real_number)):
            return(f"{number_one} +  {number_two}  =  {real_number}")
        else:
            return("-1")
            
print(solve("1003 + 35#7 = 35353300"))