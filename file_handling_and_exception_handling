def read_and_modify_file():
    try:
        # Ask the user for the input filename
        input_filename = input("Enter the name of the file to read: ")

        # Try to open and read the file
        with open(input_filename, 'r') as infile:
            content = infile.read()

        # Modify the content (convert to uppercase)
        modified_content = content.upper()

        # Create output filename
        output_filename = f"modified_{input_filename}"

        # Write the modified content to a new file
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)

        print(f"Modified content written to '{output_filename}' successfully.")

    except FileNotFoundError:
        print(f" X - Error: File '{input_filename}' not found.")
    except IOError as e:
        print(f"X - Error: I/O error occurred: {e}")
    except Exception as e:
        print(f"X - Error: An unexpected error occurred: {e}")


# Run the function
read_and_modify_file()
