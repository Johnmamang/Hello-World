def copy_file(input_file, output_file):
    with open(input_file, 'r') as f_in:
        with open(output_file, 'w') as f_out:
            content = f_in.read()
            f_out.write(content)
    print(f"Contents of {input_file} copied to {output_file}.")

# example usage
input_file = input("Enter the name of the input file: ")
output_file = input("Enter the name of the output file: ")
copy_file(input_file, output_file)
