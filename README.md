## :space_invader: About

This code generates a colorful ASCII art representation of a tree and animates it in the terminal. Here is a summary of the code:

1. Import necessary modules: time, random, and shutil.
2. Define a function named `get_random_color_code()` that returns a random ANSI escape sequence for a color.
3. Define a function named `print_tree(rows, leaf_char='^', trunk_char='| |', light_char='@')` that prints the tree.
4. Get the terminal width using `shutil.get_terminal_size().columns`.
5. Iterate through the specified number of `rows`.
6. Calculate the number of spaces to add before each row.
7. Create a string of leaves for the current row.
8. Iterate through each leaf and randomly add colored lights or regular leaves to the row.
9. Print the row with the proper spacing and colors.
10. Print the trunk using the specified trunk character.
11. Define a `main()` function.
12. Set the number of rows for the tree.
13. Enter an infinite while loop.
14. Print empty lines to clear the terminal.
15. Call `print_tree(rows)` to print the tree.
16. Pause execution for 0.5 seconds using `time.sleep(0.5)`.
17. Clear the terminal screen using the ANSI escape sequence "\033[H\033[J".
18. Run the `main()` function if the script is executed directly.

## :wrench: Requirements

The following Python libraries are required:

- time
- random
- shutil


## :runner:  Usage

, run the following command in the terminal: 
 
python .\tree.py

## :raising_hand: Contribution

All contributions are welcome! Please open an issue or submit a pull request.

