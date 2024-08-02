import os
import shutil
import sys
import tkinter as tk
from tkinter import ttk, messagebox, font, filedialog
import webbrowser


class App:
    def __init__(self, master):
        self.master = master
        master.title("DAoC UI Duplicator")
        master.geometry("400x300")
        master.resizable(0, 0)
        self.center_window()

        base_font = font.Font(size=11)

        # Grid layout
        master.columnconfigure((0, 1), weight=1)

        # UI Elements
        self.create_widgets(base_font)

        # Ini files
        self.ini_directory = ""
        self.ui_files = []

    def create_widgets(self, base_font):
        # Directory selection
        dir_label = tk.Label(self.master, text="Select .ini files directory:", font=base_font)
        dir_label.grid(row=0, column=0, padx=5, pady=5, sticky='w')

        self.dir_button = tk.Button(self.master, text="Browse", command=self.browse_directory, font=base_font)
        self.dir_button.grid(row=0, column=1, padx=5, pady=5, sticky='we')

        # Existing Character
        file_label = tk.Label(self.master, text="Select existing Character:", font=base_font)
        file_label.grid(row=1, column=0, padx=5, pady=5, sticky='w')

        self.selected_file = tk.StringVar()
        self.file_dropdown = ttk.OptionMenu(self.master, self.selected_file, "")
        self.file_dropdown.grid(row=1, column=1, padx=5, pady=5, sticky='we')

        # Ywain server
        ywain_label = tk.Label(self.master, text="Select Ywain server:", font=base_font)
        ywain_label.grid(row=2, column=0, padx=5, pady=5, sticky='w')

        self.ywain_options = [("Ywain1", "-41"), ("Ywain2", "-49"), ("Ywain3", "-50"), ("Ywain4", "-51"),
                              ("Ywain5", "-52"), ("Ywain6", "-53"), ("Ywain7", "-54"), ("Ywain8", "-55"),
                              ("Ywain9", "-56"), ("Ywain10", "-57")]

        self.selected_ywain = tk.StringVar()
        self.ywain_dropdown = ttk.OptionMenu(self.master, self.selected_ywain, "",
                                             *[name for name, num in self.ywain_options])
        self.ywain_dropdown.grid(row=2, column=1, padx=5, pady=5, sticky='we')

        # New Character Name
        filename_label = tk.Label(self.master, text="New Character name:", font=base_font)
        filename_label.grid(row=3, column=0, padx=5, pady=5, sticky='w')

        self.filename_entry = tk.Entry(self.master, font=base_font)
        self.filename_entry.grid(row=3, column=1, padx=5, pady=5, sticky='we')

        # Buttons
        self.copy_button = tk.Button(self.master, text="Copy UI to new Char", command=self.copy_ui, font=base_font)
        self.copy_button.grid(row=4, column=1, padx=5, pady=5, sticky='we')

        self.cancel_button = tk.Button(self.master, text="Quit", command=self.cancel_program, font=base_font)
        self.cancel_button.grid(row=5, column=1, padx=5, pady=5, sticky='e')

        self.download_button = tk.Button(self.master, text="Git Release Download", command=self.download,
                                         font=base_font)
        self.download_button.grid(row=4, column=0, padx=5, pady=5, sticky='w')

        # Version Label
        version_label = tk.Label(self.master, text="v1.2.0", font=("Arial", 8, "bold"), fg="blue")
        version_label.grid(row=6, column=1, sticky='e', padx=0, pady=5)
        version_label.bind("<Button-1>", self.open_link)

    def browse_directory(self):
        self.ini_directory = filedialog.askdirectory()
        if self.ini_directory:
            self.ui_files = self.find_ini_files()
            self.update_file_dropdown()

    def update_file_dropdown(self):
        menu = self.file_dropdown["menu"]
        menu.delete(0, "end")
        for file in self.ui_files:
            menu.add_command(label=file, command=lambda value=file: self.selected_file.set(value))
        if self.ui_files:
            self.selected_file.set(self.ui_files[0])
        else:
            messagebox.showerror("No .ini files found", "No .ini files found in the selected directory.")

    def find_ini_files(self):
        ini_files = [file for file in os.listdir(self.ini_directory) if file.endswith(".ini")]
        return ini_files

    def copy_ui(self):
        if not self.ini_directory:
            messagebox.showerror("Directory not selected", "Please select the directory containing .ini files.")
            return
        source_file = os.path.join(self.ini_directory, self.selected_file.get())
        ywain_number = [num for name, num in self.ywain_options if name == self.selected_ywain.get()][0]
        dest_file = os.path.join(self.ini_directory, self.filename_entry.get() + ywain_number + ".ini")
        shutil.copy2(source_file, dest_file)
        messagebox.showinfo("Copy Paste Rename App", f"UI successfully copied to {dest_file}")

    def cancel_program(self):
        self.master.destroy()

    def center_window(self):
        self.master.update_idletasks()
        width = self.master.winfo_width()
        height = self.master.winfo_height()
        x = (self.master.winfo_screenwidth() // 2) - (width // 2)
        y = (self.master.winfo_screenheight() // 3) - (height // 2)
        self.master.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def open_link(self, event):
        url = "https://www.reddit.com/r/daoc/comments/11dadu7/i_made_an_app_to_duplicate_uis_to_newly_created/"
        webbrowser.open(url)

    def download(self):
        url = "https://github.com/df8819/DAoC_UI_Duplicator/releases"
        webbrowser.open(url)


root = tk.Tk()
app = App(root)
root.mainloop()
