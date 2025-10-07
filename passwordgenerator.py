import tkinter as tk
from tkinter import messagebox
import random

# Characters allowed in password
CHARACTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#_"

# Function to generate password
def generate_password():
    length = int(length_entry.get())
    return "".join(random.choice(CHARACTERS) for _ in range(length))

# Handle password generation with up to 3 tries
def start_generation():
    global tries
    if tries < 3:
        pwd = generate_password()
        password_var.set(pwd if show_password.get() else "*" * len(pwd))
        tries += 1

        # Ask user if satisfied
        if messagebox.askyesno("Password Check", "Are you satisfied with this password?"):
            messagebox.showinfo("Success", "Password saved successfully!")
            root.quit()
    else:
        messagebox.showwarning("Limit Reached", "You have used all 3 attempts.")
        root.quit()

# Toggle show/hide password
def toggle_password():
    if show_password.get():
        password_var.set(current_password)  # show
    else:
        password_var.set("*" * len(current_password))  # hide

# Store current password separately for hiding/unhiding
def update_password_var(*args):
    global current_password
    current_password = password_var.get().replace("*", "")
    
# ---------------- GUI ----------------
root = tk.Tk()
root.title("Password Generator 🔒")
root.configure(bg="navy")
root.geometry("500x400")

tries = 0
current_password = ""
password_var = tk.StringVar()
password_var.trace("w", update_password_var)
show_password = tk.BooleanVar(value=True)

# Heading
heading = tk.Label(root, text="Password Generator 🔒", 
                   font=("Arial", 18, "bold"), fg="white", bg="navy")
heading.pack(pady=15)

# Length input
length_label = tk.Label(root, text="Enter Password Length:", 
                        font=("Arial", 12, "bold"), fg="white", bg="navy")
length_label.pack()
length_entry = tk.Entry(root, font=("Arial", 12))
length_entry.pack(pady=5)

# Password box
password_box = tk.Entry(root, textvariable=password_var, 
                        font=("Arial", 14, "bold"), fg="black", bg="white", justify="center")
password_box.pack(pady=20, ipadx=20, ipady=5)

# Show/Hide checkbox
toggle_btn = tk.Checkbutton(root, text="Show Password", variable=show_password,
                            onvalue=True, offvalue=False, command=lambda: password_var.set(current_password if show_password.get() else "*"*len(current_password)),
                            font=("Arial", 10, "bold"), fg="white", bg="navy", selectcolor="navy")
toggle_btn.pack()

# Generate button
generate_btn = tk.Button(root, text="Generate Password", 
                         command=start_generation,
                         font=("Arial", 12, "bold"), bg="white", fg="black")
generate_btn.pack(pady=20)

root.mainloop()