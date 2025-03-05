""" 
Author: Alysha Marin
Date: 03/02/2025 
Assignment: Quick Notes! Final Project 

A program that allows the user to write out and save notes directly to their device. 
It also allows users to delete their notes. 
The app will allow the user to title and has basic functions, like a exit and start button. 

"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog, simpledialog, PhotoImage

class NoteTakingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quick Notes!")
        self.root.geometry("800x600")
        self.root.configure(background='white')
        
        # start Screen (initial screen displayed when the app is launched)
        self.start_frame = tk.Frame(self.root, bg='white')
        self.start_frame.pack(expand=True, fill='both')

        # label displaying welcome message
        tk.Label(self.start_frame, text="Welcome to Quick Notes!", font=("Arial", 18, "bold"), bg='white').pack(pady=20)

        # loads and displays application logo
        self.app_logo = PhotoImage(file="applogo.png")
        app_logo_label = tk.Label(self.start_frame, image=self.app_logo, text="[Quick Notes Logo]")
        app_logo_label.pack()

        # creates button frame for Start and Exit buttons
        button_frame = tk.Frame(self.start_frame, bg='white')
        button_frame.pack(pady=10)

        # starts and Exit buttons under the same frame
        start_button = tk.Button(button_frame, text="Start", font=("Arial", 14), command=self.show_main_screen)
        start_button.pack(side='left', padx=10)

        exit_button = tk.Button(button_frame, text="Exit", font=("Arial", 14), command=self.exit_app, bg='#5cb6f9')
        exit_button.pack(side='left', padx=10)
    
    def show_main_screen(self):
        # switches to the main note-taking screen from the start screen
        self.start_frame.pack_forget()
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(expand=True, fill='both')

        # loads and displays application logo for the main screen
        self.app_logo2 = PhotoImage(file="applogo2.png")
        app_logo2_label = tk.Label(self.main_frame, image=self.app_logo2, text="[Quick Notes Logo 2]")
        app_logo2_label.pack()

        # notebook widget (tabbed system for managing notes)
        self.notebook = ttk.Notebook(self.main_frame)
        self.notebook.pack(expand=True, fill='both')
        
        # button frame for note actions 
        button_frame = tk.Frame(self.main_frame)
        button_frame.pack(fill='x', pady=10)

        # button for each action 
        tk.Button(button_frame, text="New Note", command=self.add_note).pack(side='left', padx=5)
        tk.Button(button_frame, text="Delete Note", command=self.delete_note).pack(side='left', padx=5)
        tk.Button(button_frame, text="Edit Title", command=self.edit_title).pack(side='left', padx=5)
        tk.Button(button_frame, text="Save Note", command=self.save_note).pack(side='left', padx=5)
        tk.Button(button_frame, text="Back", command=self.show_start_screen).pack(side='left', padx=5)
        
        self.add_note()  # starts with one note by default
    
    def show_start_screen(self):
        # returns to the start screen
        self.main_frame.pack_forget()
        self.start_frame.pack(expand=True, fill='both')

    # function responsible for adding new note
    def add_note(self):
        # adds a new note tab in the notebook
        frame = ttk.Frame(self.notebook)
        
        # creates a Text widget for note content
        text_area = tk.Text(frame, wrap='word')
        text_area.pack(expand=True, fill='both', padx=5, pady=5)

        # adds the note to the notebook and select it
        self.notebook.add(frame, text="New Note")
        self.notebook.select(frame)

    # function responsible for deletion note
    def delete_note(self):
        # deletes the currently selected note tab
        current_tab = self.notebook.index(self.notebook.select())
        if current_tab >= 0:
            self.notebook.forget(current_tab)  # removes the tab
        else:
            # shows warning if no note is selected
            messagebox.showwarning("Warning", "No note selected to delete")

    # function responsible for editing title of note
    def edit_title(self):
        # edits the title of the currently selected note tab
        current_tab = self.notebook.select()
        if not current_tab:
            messagebox.showwarning("Warning", "No note selected to rename")
            return
        
        # prompts user to enter a new title for the note
        new_title = simpledialog.askstring("Edit Title", "Enter new title:")
        if new_title and new_title.strip():  # validates input to ensure it's not empty
            self.notebook.tab(current_tab, text=new_title.strip())
        else:
            messagebox.showwarning("Warning", "Title cannot be empty")

    # function that is responsible for saving notes
    def save_note(self):
        # saves the currently selected note content to a file
        current_tab = self.notebook.select()
        if not current_tab:
            messagebox.showwarning("Warning", "No note selected to save")
            return
        
        # gets the text area from the current note tab
        frame = self.notebook.nametowidget(current_tab)
        text_area = frame.winfo_children()[0]
        content = text_area.get("1.0", tk.END).strip()  # gets the note content

        # validates if the note is not empty before saving
        if not content:
            messagebox.showwarning("Warning", "Cannot save an empty note")
            return
        
        # opens file dialog to save the note
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            try:
                # saves content to the selected file
                with open(file_path, "w", encoding="utf-8") as file:
                    file.write(content)
                messagebox.showinfo("Success", "Note saved successfully!")
            except Exception as e:
                # shows error if saving fails
                messagebox.showerror("Error", f"An error occurred while saving: {e}")
    # function for exiting application
    def exit_app(self):
        # exits the application when the Exit button is clicked
        self.root.quit()

if __name__ == "__main__":
    # creates the main Tkinter window and run the app
    root = tk.Tk()
    app = NoteTakingApp(root)
    root.mainloop()