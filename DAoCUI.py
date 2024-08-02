# import json
import os
import shutil
import sys
# import tkinter as tk
from tkinter import ttk
# from tkinter import filedialog
from tkinter import messagebox
from tkinter import font
import webbrowser
import tkinter as tk


# from PIL import ImageTk, Image

class App:
    def __init__(self, master):
        self.master = master
        master.title("DAoC UI Duplicator")
        master.geometry("360x240")
        master.resizable(0, 0)
        self.center_window()

        base_font = font.Font(size=11)

        # Grid layout
        master.columnconfigure((0, 1), weight=1)  # Allow columns to expand to fill available space

        # Insert image (Experimental)
        # image_path = r"C:\Users\<user>\1688677692.png"  # Replace with the path to your image file
        # image = Image.open(image_path)
        # image = image.resize((75, 67))  # Resize the image if needed
        # photo = ImageTk.PhotoImage(image)

        # Add label for dropdown 1 description
        file_label = tk.Label(master, text="Select existing Character:", font=base_font)
        file_label.grid(row=0, column=0, padx=5, pady=5, sticky='w')

        self.ui_files = self.find_ini_files()
        if not self.ui_files:
            messagebox.showerror("Check folder ▼ ▼ ▼",
                                 "No .ini files found. Please move to: \n\n<DRIVE>:\\Users\\<USER>\\AppData\\Roaming\\Electronic Arts\\Dark Age of Camelot\\LotM\n\n and try again.")
            master.destroy()
            return

        self.selected_file = tk.StringVar()

        self.file_dropdown = ttk.OptionMenu(master, self.selected_file, "", *self.ui_files)
        self.selected_file.set(self.ui_files[0])

        self.file_dropdown.grid(row=0, column=1, padx=5, pady=5, sticky='we')

        # Add label for dropdown 2 description
        ywain_label = tk.Label(master, text="Select Ywain server:", font=base_font)
        ywain_label.grid(row=1, column=0, padx=5, pady=5, sticky='w')

        self.ywain_options = [("Ywain1", "-41"), ("Ywain2", "-49"), ("Ywain3", "-50"), ("Ywain4", "-51"),
                              ("Ywain5", "-52"), ("Ywain6", "-53"), ("Ywain7", "-54"), ("Ywain8", "-55"),
                              ("Ywain9", "-56"), ("Ywain10", "-57")]

        self.selected_ywain = tk.StringVar()
        self.ywain_dropdown = ttk.OptionMenu(master, self.selected_ywain, "",
                                             *[name for name, num in self.ywain_options])
        self.selected_ywain.set(self.ywain_options[0][0])
        self.ywain_dropdown.grid(row=1, column=1, padx=5, pady=5, sticky='we')

        self.filename_label = tk.Label(master, text="New Character name:", font=base_font)
        self.filename_label.grid(row=2, column=0, padx=5, pady=5, sticky='w')

        self.filename_entry = tk.Entry(master, font=base_font)
        self.filename_entry.grid(row=2, column=1, padx=5, pady=5, sticky='we')

        self.copy_button = tk.Button(master, text="Copy UI to new Char", command=self.copy_ui, font=base_font)
        self.copy_button.grid(row=3, column=1, padx=5, pady=5, sticky='we')

        label = tk.Label(root, text="")
        label.grid(row=4, column=1, padx=5, pady=5, sticky='e')

        self.cancel_button = tk.Button(master, text="Quit", command=self.cancel_program, font=base_font)
        self.cancel_button.grid(row=5, column=1, padx=5, pady=5, sticky='e')

        self.download = tk.Button(master, text="Git Release Download", command=self.download, font=base_font)
        self.download.grid(row=3, column=0, padx=5, pady=5, sticky='w')

        label = tk.Label(master, text="", font=("Arial", 8, "bold"), fg="blue")
        label.grid(row=5, column=1, sticky='w', padx=0, pady=5)

        # label = tk.Label(master, image=photo)
        # label.grid(row=5, column=0, padx=5, pady=5, sticky='w')

        # self.reddid_post = tk.Button(master, text="User Guide", command=self.reddid_post, font=base_font)
        # self.reddid_post.grid(row=4, column=0, padx=5, pady=5, sticky='w')

        # Add version label here
        ispy_label = tk.Label(master, text="v1.1.0", font=("Arial", 8, "bold"), fg="blue")
        ispy_label.grid(row=6, column=1, sticky='e', padx=0, pady=5)

        ispy_label.bind("<Button-1>", self.open_link)

    def center_window(self):
        self.master.update_idletasks()
        width = self.master.winfo_width()
        height = self.master.winfo_height()
        x = (self.master.winfo_screenwidth() // 2) - (width // 2)
        y = (self.master.winfo_screenheight() // 3) - (height // 2)
        self.master.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def open_link(self, event):
        url = "https://www.reddit.com/user/ISPY4ever"
        webbrowser.open(url)

    def reddid_post(self):
        pass
        url = "https://www.reddit.com/r/daoc/comments/11dadu7/i_made_an_app_to_duplicate_uis_to_newly_created/"
        webbrowser.open(url)

    def download(self):
        url = "https://github.com/df8819/DAoC_UI_Duplicator/releases"
        webbrowser.open(url)

    def find_ini_files(self):
        script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))
        ini_files = []
        for file in os.listdir(script_directory):
            if file.endswith(".ini"):
                ini_files.append(file)
        return ini_files

    def copy_ui(self):
        script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))
        source_file = os.path.join(script_directory, self.selected_file.get())
        ywain_number = [num for name, num in self.ywain_options if name == self.selected_ywain.get()][0]
        dest_file = os.path.join(script_directory, self.filename_entry.get() + ywain_number + ".ini")
        shutil.copy2(source_file, dest_file)
        messagebox.showinfo("Copy Paste Rename App", f"UI successfully copied to {dest_file}")

    def cancel_program(self):
        self.master.destroy()


root = tk.Tk()
app = App(root)
# app.check_ini_files()  # Check for .ini files before running the app
root.mainloop()
