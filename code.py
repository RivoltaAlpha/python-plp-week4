# Step 1: Read the file
try:
    with open('Tiff.txt', 'r') as file:
        data = file.read()
except FileNotFoundError:
    print("Error: 'Tiff.txt' not found.")
    data = ""
except Exception as e:
    print("An error occurred while reading 'Tiff.txt':", e)
    data = ""

# Step 2: Write the modified file
if data:  # Only write if data was successfully read
    modified_data = data.upper()  # Example modification: Convert to uppercase
    try:
        with open('modified_filename.txt', 'w') as file:
            file.write(modified_data)
        print("Modified file written successfully.")
    except Exception as e:
        print("An error occurred while writing the modified file:", e)

# Step 3: Ask for a filename and handle errors
filename = input("Enter a filename: ")
try:
    with open(filename, 'r') as file:
        user_file_data = file.read()
    print("File read successfully. Content:")
    print(user_file_data)
except FileNotFoundError:
    print(f"Error: '{filename}' not found.")
except PermissionError:
    print(f"Error: Permission denied for '{filename}'.")
except Exception as e:
    print("An error occurred while reading the file:", e)