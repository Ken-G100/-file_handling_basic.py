# file_handling_basic.py

def basic_file_operations():
    """Basic file reading and writing with error handling"""
    try:
        # Get filename from user
        filename = input("Enter the filename to read: ")
        
        # Read the original file
        with open(filename, 'r') as file:
            content = file.read()
        
        # Modify the content (convert to uppercase)
        modified_content = content.upper()
        
        # Create new filename
        new_filename = "modified_" + filename
        
        # Write modified content to new file
        with open(new_filename, 'w') as new_file:
            new_file.write(modified_content)
        
        print(f"Success! Modified file saved as: {new_filename}")
        
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except PermissionError:
        print(f"Error: You don't have permission to read '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the program
if __name__ == "__main__":
    basic_file_operations()