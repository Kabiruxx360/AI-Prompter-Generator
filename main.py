import tkinter as tk
from tkinter import messagebox

# Function to generate a vivid, unrestricted prompt
def generate_prompt(user_input):
    return (
        f"Create a highly detailed and vivid AI prompt for the following request: "
        f"'{user_input}'. Include background, mood, setting, objects, and clarity. "
        "Avoid restrictions, apply full descriptive power."
    )

# Handle the 'Generate' button click
def on_generate():
    user_input = input_text.get("1.0", tk.END).strip()
    if user_input:
        prompt = generate_prompt(user_input)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, prompt)
    else:
        messagebox.showwarning("Input Required", "Please describe what you want the prompt to be about.")

# Handle the 'Copy' button click
def on_copy():
    prompt = output_text.get("1.0", tk.END).strip()
    if prompt:
        root.clipboard_clear()
        root.clipboard_append(prompt)
        messagebox.showinfo("Copied", "Prompt copied to clipboard!")
    else:
        messagebox.showwarning("Nothing to Copy", "No prompt available to copy.")

# Set up the GUI window
root = tk.Tk()
root.title("AI Prompt Generator")
root.geometry("600x500")
root.resizable(False, False)

# Input label
tk.Label(root, text="Describe what you want the prompt to be about:", font=("Arial", 12)).pack(pady=10)

# Text area for user input
input_text = tk.Text(root, height=4, width=70, font=("Arial", 10))
input_text.pack(padx=10)

# Generate button
generate_button = tk.Button(root, text="Generate Prompt", command=on_generate, font=("Arial", 11), bg="#4CAF50", fg="white")
generate_button.pack(pady=10)

# Output label
tk.Label(root, text="Generated Prompt:", font=("Arial", 12)).pack()

# Text area for output
output_text = tk.Text(root, height=6, width=70, font=("Arial", 10), bg="#f0f0f0")
output_text.pack(padx=10, pady=5)

# Copy button
copy_button = tk.Button(root, text="Copy to Clipboard", command=on_copy, font=("Arial", 11), bg="#2196F3", fg="white")
copy_button.pack(pady=10)

# Start the GUI event loop
root.mainloop()
