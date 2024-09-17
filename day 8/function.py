#please write a program for me where the program asks which file to input, the to create that file then to enter that file content then asks which file to delete and the delete that file 
 
 
 import os

# Function to create a file and write content to it
def create_file():
    file_name = input("Enter the name of the file to create (with extension): ")
    
    # Open the file in write mode and create it
    with open(file_name, 'w') as file:
        content = input("Enter the content you want to write to the file: ")
        file.write(content)
    
    print(f"File '{file_name}' created and content written.")

# Function to delete a file
def delete_file():
    file_name = input("Enter the name of the file to delete (with extension): ")
    
    # Check if file exists before attempting to delete
    if os.path.exists(file_name):
        os.remove(file_name)
        print(f"File '{file_name}' has been deleted.")
    else:
        print(f"File '{file_name}' does not exist.")

# Main program
while True:
    print("\n1. Create a file")
    print("2. Delete a file")
    print("3. Exit")
    
    choice = input("\nChoose an option: ")
    
    
    if choice == '1':
        create_file()
    elif choice == '2':
        delete_file()
    elif choice == '3':
        print("Exiting the program...")
        break
    else:
        print("Invalid choice! Please select 1, 2, or 3.")