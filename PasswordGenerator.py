import os
import random
import tkinter as tk
from tkinter import messagebox, filedialog

symbols = ['!', '@', "#", '$', '%', '&']
numbers = [str(i) for i in range(10)]
alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]
options = [symbols, numbers, alphabet]

folder_path = None  # Global variable to store file path

def select_folder_location():
    """Allow the user to select a folder to save the passwords file."""
    global folder_path
    folder_path = filedialog.askdirectory(
        title="Select Folder Location"
    )

def generate_passwords():
    try:
        global folder_path
        if not folder_path:
            messagebox.showwarning("No File Selected", "Please select a file location first.")
            return
        
        # Get the number of passwords from the user
        number_of_passwords = int(entry_number.get())
        password_names = entry_purposes.get().split(" ")  # space-separated purposes
        length_of_password = int(entry_length.get())

        # Ensure the password length is at least 5
        if length_of_password < 5:
            messagebox.showerror("Error", "Password length must be at least 5 characters.")
            return
        
        if len(password_names) != number_of_passwords:
            raise ValueError("Number of purposes must match the number of passwords.")
        
        passwords = []
        for _ in range(number_of_passwords):
            password = []
            for _ in range(length_of_password):
                current = random.choice(options)
                if current == alphabet:
                    if random.randint(0, 1) == 0:
                        password.extend(random.choice(current).upper())
                    else:
                        password.extend(random.choice(current))
                else:
                    password.extend(random.choice(current))
            
            random.shuffle(password)
            passwords.append(''.join(password))


        filename = os.path.join(folder_path, "passwords.txt")
        # Write passwords to the selected file
        with open(filename, 'a') as file:
            for i in range(number_of_passwords):
                file.write(password_names[i] + ": " + passwords[i] + '\n')
        
        # Display the passwords in the Text widget
        text_display.delete('1.0', tk.END)  # Clear existing content
        for i in range(number_of_passwords):
            text_display.insert(tk.END, f"{password_names[i]}: {passwords[i]}\n")
        
    except ValueError as e:
        messagebox.showerror("Error", f"Invalid input: {e}")
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong: {e}")

def clear_inputs():
    """Clear all input fields."""
    entry_number.delete(0, tk.END)  # Clear the number input
    entry_purposes.delete(0, tk.END)  # Clear the purposes input
    entry_length.delete(0, tk.END)  # clear the length input
    text_display.delete('1.0', tk.END)  # Clear the password display

# Create the GUI
root = tk.Tk()
root.title("Password Generator")
root.geometry("600x400")

# Create input for number of passwords
label_number = tk.Label(root, text="How many passwords?")
label_number.pack()
entry_number = tk.Entry(root)
entry_number.pack()

# Create input for password purposes
label_purposes = tk.Label(root, text="Enter purposes (space separated):")
label_purposes.pack()
entry_purposes = tk.Entry(root)
entry_purposes.pack()

# Create input for number of passwords
label_length = tk.Label(root, text="Length of password?")
label_length.pack()
entry_length = tk.Entry(root)
entry_length.pack()

# Create a button to generate passwords
button_generate = tk.Button(root, text="Generate Passwords", command=generate_passwords)
button_generate.pack()

# Button to select file location
button_file_location = tk.Button(root, text="Select File Location", command=select_folder_location)
button_file_location.pack()

# Button to clear inputs
button_clear = tk.Button(root, text="Clear Input", command=clear_inputs)
button_clear.pack()

# Text widget to display the passwords
label_display = tk.Label(root, text="Generated Passwords:")
label_display.pack()
text_display = tk.Text(root, wrap=tk.WORD, height=10, width=50)
text_display.pack()

# Run the GUI
root.mainloop()