import sudoku


# Your "program" is driven by the main method
def main():
    print("Welcome to Matei's Sudoku Game")
    while True:                                                            #While loop to repeat until user enters the appropriate puzzle file
        try:
            filename = input("Please enter in your sudoku puzzle file:")
            puzzle = sudoku.load_puzzle(filename)                           #puzzle1.csv is the valid file name for the complete puzzle , InCpuzzle1.csv is the puzzle that should be displayed to play
            break
        except:
            print("Not a valid puzzle file name")
    
    visualization = sudoku.puzzle_to_string(puzzle)
    print("Current grid:" + visualization)
#    valid = sudoku.check_puzzle(puzzle)
#    print(valid)
#    print(puzzle)
    numbers_entered = 0
    invalid_numbers = 0
    while True:                                                             #While loop setup to catch if the user would like to quit the game, if "quit" is enter program breaks out of while loop
        move = input("Enter move row/col/digit (quit to exit)")
        if move.lower() == "quit":
            if sudoku.check_end_game(puzzle) == True:                          #CHecks if the ended puzzle is the same as the final puzzle and determines if the puzzle is completed
                print("Puzzle is completed")
            else:
                print("Puzzle is NOT completed")
            print("Thanks for playing, Bye")
            print("You entered " + str(numbers_entered) + " numbers in total")
            print("You entered " + str(invalid_numbers) + " invalid numbers")
            break
        else:
            newgrid = sudoku.puzzle_move(move,puzzle)                           #Gives the move which is the entered string from the user with the current puzzle to the puzzle_move to be changed and checked if it is a valid move( the puzzle_move function returns either the changed puzzle or false if the move is invalid)
            numbers_entered+=1
            if sudoku.check_end_game(puzzle) == True:                          #CHecks if the ended puzzle is the same as the final puzzle and determines if the puzzle is completed, this time at the end of every move
                visualization = sudoku.puzzle_to_string(newgrid)
                print(visualization)
                print("Puzzle is completed")
                print("Thanks for playing, Bye")
                print("You entered " + str(numbers_entered) + " numbers in total")
                print("You entered " + str(invalid_numbers) + " invalid numbers")
                break
            if newgrid == False:                                            #If the returned values is false then the move was invalid
                print("That is invalid")
                invalid_numbers+=1
            else:
                visualization = sudoku.puzzle_to_string(newgrid)            #Sends the new changed grid to be printed out by puzzle_to_string_function
                print(visualization)





# Guard for main function - do NOT remove or change
if __name__ == "__main__":
    main()