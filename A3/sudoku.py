
# provided function - do NOT remove or change
def load_puzzle(filename):
    ''' Reads a sudoku puzzle from the text file 'filename' in the current directory. 
        Returns a list of lists of integers that represents the game.
            load_puzzle(filename:str) -> str[str[int]]
        Empty cells in the game are denoted by 0s in the file (and the output list)
    '''
    puzzle = [] 
    with open(filename, "r") as f:
        for line in f:
            puzzle.append( [int(val) for val in line.split(",")] )
    return puzzle




#------------------------------------------------------------------#
#------------------------------------------------------------------#


# your functions go here!
def puzzle_to_string(puzzle:list):
    vis = ""                                            #Vis string is just short for vistualization string
    rowcount = 0
    for row in puzzle:
        rowcount+=1
        if rowcount%3==1:
            vis = vis + "-------+-------+-------\n"
        for index in range(len(row)):
            nindex = index + 1
            if row[index] == 0:                        # If the value is a zero insted of adding zero to the string it adds a bank space
                vis = vis + " " + " "
            else:
                vis = vis + " " + str(row[index])      #Adds the value to the string
            if nindex == len(row):
                vis = vis + "\n"                        #If its the end of the row it adds a new line char so it goes to the next line
                break
            if nindex%3==0:
                vis = vis + " " + "|"                   #Adds a line inbetween every 3 char numbers
    return vis[23:]

def check_puzzle(puzzle:list):                      # General function that just calls on all the check functions
    invalid_rows = check_rows(puzzle)
    invalid_columns = check_columns(puzzle)
    invalid_subgrids = check_subgrids(puzzle)
    return invalid_rows , invalid_columns , invalid_subgrids

def check_rows(puzzle:list):
    invalid_rows = []
    values =[1,2,3,4,5,6,7,8,9]
    rowcount = 0
    zero_count = 0
    for row in puzzle:                                             #goes through every element in the puzzle list of lists, which is a row
        rowcount+=1
        values =[1,2,3,4,5,6,7,8,9]
        for index_in_row in row:                                   #goes throught the individual element in the selected row
            if index_in_row == 0:                                   
                zero_count+=1
#                if zero_count > 8:
#                    invalid_rows.append(rowcount)
            elif index_in_row in values:                           #if the value is in the list values(1-9) remove that values so esencially when we loop around if the value is not in the list that means that it already appeared in the row or is not valid
                values.remove(index_in_row)
            else:
                invalid_rows.append(rowcount)
    return invalid_rows 

def check_columns(puzzle:list):
    invalid_columns = []
    values = [1,2,3,4,5,6,7,8,9]
    column = 0
    zero_count = 0
    for colcount in values:
        values = [1,2,3,4,5,6,7,8,9]
        for row in puzzle:
            if row[column] == 0:
                zero_count+=1
#                if zero_count > 8:
#                    invalid_columns.append(colcount)
            elif row[column] in values:   # Goes through every row and at the specific coloum value , if and else statment also does the same things  as the one in row with the list
                values.remove(row[column])
            else:
                invalid_columns.append(colcount)
        column+=1                                      # At the end of for loop after going through every row at a specific index value it goes to the next column aka next index value to search for in list
    return invalid_columns

def check_subgrids(puzzle:list):
    invalid_subgrids = []
    zero_count = 0
    values=[1,2,3,4,5,6,7,8,9]
    row_1 = puzzle[:3]          #Splits up list of list with the first 3 Llist that are used for the first 3 sub grids
    row_4 = puzzle[3:6]         #Next list that are for the next 3 sub grids
    row_7 = puzzle[6:9]         #Final 3 sub grids with the 3 rows that are used
#    print(row_1)
#    print(row_4)
#    print(row_7)
    for subgrid in values:                                      #For loop that goes through each sub grid, When programe gets to individual values it check it the same ways by eliminating from the values list, and the values list get re initialized with the 1-9 values after each subgrid has been gon through
        values=[1,2,3,4,5,6,7,8,9]
        if subgrid == 1 or subgrid == 2 or subgrid == 3:       
            for row in row_1:                                  #Stars with the first list out of the 3 list that are used for sub grids 1 to 3
                if subgrid == 1:
                    check_value = row[:3]                       #Takes the first 3 values of the given list and makes the first sub grid 
                    for index in check_value:
                        if index == 0:
                            zero_count+=1
                        elif index in values:
                            values.remove(index)
                        else:
                            invalid_subgrids.append(subgrid)
                elif subgrid == 2:
                    check_value = row[3:6]                      #Takes the next 3 values of the given list to make sub grid 2 given the 3 list rows
                    for index in check_value:
                        if index == 0:
                            zero_count+=1
                        elif index in values:
                            values.remove(index)
                        else:
                            invalid_subgrids.append(subgrid)
                elif subgrid == 3:
                    check_value = row[6:9]                     #Takes the final 3 values in the list of the given list to make the subgrid 3 given the 3 list rows
                    for index in check_value:
                        if index == 0:
                            zero_count+=1
                        elif index in values:
                            values.remove(index)
                        else:
                            invalid_subgrids.append(subgrid)
        elif subgrid == 4 or subgrid == 5 or subgrid == 6:      #The exact same steps are take fro the rest of the subgrids 4,5,6,7,8,9 as seen above the only part of the code that is different is the subgrid values
            for row in row_4:
                if subgrid == 4:
                    check_value = row[:3]
                    for index in check_value:
                        if index == 0:
                            zero_count+=1
                        elif index in values:
                            values.remove(index)
                        else:
                            invalid_subgrids.append(subgrid)
                elif subgrid == 5:
                    check_value = row[3:6]
                    for index in check_value:
                        if index == 0:
                            zero_count+=1
                        elif index in values:
                            values.remove(index)
                        else:
                            invalid_subgrids.append(subgrid)
                elif subgrid == 6:
                    check_value = row[6:9]
                    for index in check_value:
                        if index == 0:
                            zero_count+=1
                        elif index in values:
                            values.remove(index)
                        else:
                            invalid_subgrids.append(subgrid)
        elif subgrid == 7 or subgrid == 8 or subgrid == 9:
            for row in row_7:
                if subgrid == 7:
                    check_value = row[:3]
                    for index in check_value:
                        if index == 0:
                            zero_count+=1
                        elif index in values:
                            values.remove(index)
                        else:
                            invalid_subgrids.append(subgrid)
                elif subgrid == 8:
                    check_value = row[3:6]
                    for index in check_value:
                        if index == 0:
                            zero_count+=1
                        elif index in values:
                            values.remove(index)
                        else:
                            invalid_subgrids.append(subgrid)
                elif subgrid == 9:
                    check_value = row[6:9]
                    for index in check_value:
                        if index == 0:
                            zero_count+=1
                        elif index in values:
                            values.remove(index)
                        else:
                            invalid_subgrids.append(subgrid)
    return invalid_subgrids

def puzzle_move(move:str,puzzle:list):  #Function takes in the given move entered by the user
    row = int(move[:1])
    column = int(move[2:3])
    digit = int(move[4:])
    puzzle[row][column] = digit
    valid_subgrid = check_subgrids(puzzle)
    valid_row = check_rows(puzzle)
    valid_column = check_columns(puzzle)
    if not valid_subgrid and not valid_row and not valid_column:      #If the returned list from the check_subgrid or check_rows or check_column function has anything in it that means that the enter values by the user is invalid
        return puzzle
    else:
        puzzle[row][column] = 0             #It will revert the changes it made by setting the entered digit back to zero and return false which will be used to display the incorrect message to the user
        return False

def check_end_game(final_puzzle:list):                  #Function calles the original puzzle stored as puzzle1.csv and comapred it to given puzzle if they are the same it is completed and returne true else it is not completed and returns false
    original_puzzle =load_puzzle("puzzle1.csv")
    if original_puzzle == final_puzzle:
        return True
    else:
        return False





                





#------------------------------------------------------------------#
#------------------------------------------------------------------#




# Your "program" is driven by the main method
# Modify as needed to test your functions
def main():
    puzzle = load_puzzle('puzzle1.csv')
    print(puzzle)
    visualization = puzzle_to_string(puzzle)
    print(visualization)
    valid = check_puzzle(puzzle)
    print(valid)




# Guard for main function - do NOT remove or change
if __name__ == "__main__":
    main()