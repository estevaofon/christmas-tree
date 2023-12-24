import time
import random
import shutil  # Import the shutil module for terminal width

def get_random_color_code():
    # ANSI escape codes for 8 basic colors
    colors = [
        "\033[31m",  # Red
        "\033[32m",  # Green
        "\033[33m",  # Yellow
        "\033[34m",  # Blue
        "\033[35m",  # Magenta
        "\033[36m",  # Cyan
        "\033[91m",  # Light red
        "\033[94m",  # Light blue
    ]
    return random.choice(colors)

def print_tree(rows, leaf_char='^', trunk_char='| |', light_char='@'):
    terminal_width = shutil.get_terminal_size().columns

    for i in range(rows):
        spaces = " " * ((terminal_width - 1) // 2 - i)
        leaves = leaf_char * (2 * i + 1)

        # Add lights randomly within the entire row
        row_with_lights = []
        for leaf in leaves:
            if random.random() < 0.2:
                row_with_lights.append(get_random_color_code() + light_char + "\033[0m")
            else:
                row_with_lights.append("\033[32m" + leaf + "\033[0m")

        print(f"{spaces}{''.join(row_with_lights)}")

    # Trunk
    trunk_spaces = " " * ((terminal_width - 1) // 2 - 1)
    for _ in range(2):
        print(trunk_spaces + trunk_char)

def main():
    
    rows = 30  # Adjust the number of rows to make the tree bigger
    terminal_size = shutil.get_terminal_size()
    terminal_height = terminal_size.lines
    while True:
        print("\n"*((terminal_height - rows) // 3))
        print_tree(rows)
        time.sleep(0.5)
        # Clear the terminal screen after each iteration
        print("\033[H\033[J", end='', flush=True)

if __name__ == "__main__":
    main()