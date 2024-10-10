def khayam_list(n_rows):
    previous_row = [1, 1]
    print([1])
    for _ in range(n_rows-1):
        rows = [1, 1]
        print(previous_row)
        for j in range(1, len(previous_row)):
            rows.insert(j, previous_row[j] + previous_row[j-1])
        
        previous_row = rows 
    
khayam_list(5)