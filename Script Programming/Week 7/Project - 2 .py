"""Project 2"""
def main():
    # User input
    filename = input("Enter filename: ")
    try:
        with open(filename) as file:
            # Read lines into a list
            lines = file.readlines()
    except FileNotFoundError:
        print("File not found.")
        return

    num_lines = len(lines)

    while True:
        # Print lines in file
        print(f"The file contains {num_lines} lines.")

        # User input for line number
        line_num = input("Enter a line number (0 to quit): ")

        try:
            line_num = int(line_num)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if line_num == 0:
            print("Exiting program.")
            break
        elif line_num < 1 or line_num > num_lines:
            print("Invalid line number. Please enter a number between 1 and", num_lines)
            continue

        # Print line number
        print(lines[line_num - 1])

if __name__ == '__main__':
    main()
