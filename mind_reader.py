import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Function to center the window on the screen
def center_window(window, width=300, height=150):
    # Get screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    
    # Calculate position x and y coordinates
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    
    # Set the window's geometry
    window.geometry(f'{width}x{height}+{x}+{y}')

# Function to simulate mind reading with a delay
def read_mind():
    # Get the number entered by the user
    number = entry.get()

    try:
        number = str(int(number))
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number between 1 and 100")
        return
    
    # Ensure the number is between 1 and 10
    if not 1 <= int(number) <= 100:
        messagebox.showerror("Error", "Please enter a number between 1 and 100")
        return
    
    # List of mysterious messages to display, one for each second
    messages = [
        "Tapping into hidden brainwaves...",
        "Decrypting your subconscious thoughts...",
        "Interpreting neural signals...",
        "Analyzing mental patterns...",
        "Unlocking your inner secrets..."
    ]
    
    # Function to update the progress bar and message
    def update_progress(step=0):
        if step < len(messages):
            # Update the label and progress bar value
            popup_label.config(text=messages[step])
            progress_bar['value'] = (step + 1) * 20  # Each step increases 20%
            
            # Schedule the next update in 1 second
            popup.after(1000, update_progress, step + 1)
        else:
            # After all messages are displayed, reveal the number
            popup_label.config(text="Mind read successfully!")
            progress_bar['value'] = 100  # Complete the progress bar
            popup.after(1000, lambda: [popup.destroy(), reveal_number()])

    # Function to show the final result
    def reveal_number():
        messagebox.showinfo("Mind Reader", f"You're thinking of the number {number}!")
    
    # Create a popup window for the mind reading simulation
    popup = tk.Toplevel(root)
    popup.title("Mind Reader")
    
    # Center the popup window
    center_window(popup, 350, 150)
    
    # Label for displaying mysterious messages
    popup_label = tk.Label(popup, text="Starting mind reading...", font=("Helvetica", 12))
    popup_label.pack(pady=10)
    
    # Progress bar for loading simulation
    progress_bar = ttk.Progressbar(popup, orient="horizontal", length=300, mode="determinate")
    progress_bar.pack(pady=10)
    progress_bar['value'] = 0  # Start the progress bar at 0

    # Start updating the progress after the popup is ready
    update_progress()

# Create the main window
root = tk.Tk()
root.title("Mind Reader")

# Center the main window
center_window(root, 350, 200)

# Label for instructions
label = tk.Label(root, text="Enter a number between 1 and 100", font=("Helvetica", 12))
label.pack(pady=10)

# Entry widget for user input
entry = tk.Entry(root, font=("Helvetica", 14), justify='center')
entry.pack(pady=10)

# Button to trigger mind reading
button = tk.Button(root, text="Read My Mind", font=("Helvetica", 14), command=read_mind)
button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
