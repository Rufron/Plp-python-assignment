


## 🖋️ file_read_write.py

# File Read & Write Challenge 🖋️
# Reads a file and writes a modified version to a new file.

def file_read_write():
    try:
        # Read the input file
        with open("input.txt", "r") as infile:
            content = infile.read()

        # Modify content (example: convert to uppercase)
        modified_content = content.upper()

        # Write to output file
        with open("output.txt", "w") as outfile:
            outfile.write(modified_content)

        print("✅ File successfully read and written to output.txt")

    except FileNotFoundError:
        print("❌ Error: input.txt was not found. Please create it first.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")


if __name__ == "__main__":
    file_read_write()
