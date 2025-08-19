# Error Handling Lab 🧪
# Asks the user for a filename and handles errors if the file cannot be read.

def error_handling_lab():
    filename = input("Enter the filename you want to read: ")

    try:
        with open(filename, "r") as file:
            content = file.read()
            print("\n📄 File Content:")
            print(content)
    except FileNotFoundError:
        print(f"❌ Error: '{filename}' not found. Please check the filename and try again.")
    except PermissionError:
        print(f"Error: You don't have permission to read '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    error_handling_lab()
