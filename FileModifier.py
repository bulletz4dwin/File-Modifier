import os
import time
import tkinter as tk
from tkinter import ttk, messagebox

def rename_files():
    folder_path = folder_path_entry.get()
    new_prefix = new_prefix_entry.get()
    new_extension = new_extension_entry.get()

    if not os.path.isdir(folder_path):
        messagebox.showerror("Error", "Invalid folder path.")
        return

    message_label.config(text="Made By rizzshiii on GitHub.")
    root.update()
    time.sleep(3) 
    message_label.config(text="Renaming files...")

    files = os.listdir(folder_path)
    i = 1

    for file_name in files:
        if os.path.isfile(os.path.join(folder_path, file_name)):
            old_name, old_extension = os.path.splitext(file_name)

         
            new_name = new_prefix + str(i) if not new_prefix == "" else old_name

           
            new_extension_with_dot = new_extension if new_extension else old_extension

            new_name_with_extension = f"{new_name}{new_extension_with_dot}"

            os.rename(os.path.join(folder_path, file_name), os.path.join(folder_path, new_name_with_extension))
            i += 1

    messagebox.showinfo("Success", "Files renamed successfully.")

root = tk.Tk()
root.title("File Renamer by rizzshiii")


window_width = 600  
window_height = 300  
root.geometry(f"{window_width}x{window_height}")


root.configure(background="white")


style = ttk.Style()
style.theme_use("clam")  


main_frame = ttk.Frame(root)
main_frame.pack(padx=20, pady=20, expand=True, fill="both")

folder_label = tk.Label(main_frame, text="Enter the folder path:")
folder_label.grid(row=0, column=0, sticky="w")

folder_path_entry = tk.Entry(main_frame)
folder_path_entry.grid(row=0, column=1, sticky="we")

prefix_label = tk.Label(main_frame, text="Enter the new prefix:")
prefix_label.grid(row=1, column=0, sticky="w")

new_prefix_entry = tk.Entry(main_frame)
new_prefix_entry.grid(row=1, column=1, sticky="we")

extension_label = tk.Label(main_frame, text="Enter the new extension:")
extension_label.grid(row=2, column=0, sticky="w")

new_extension_entry = tk.Entry(main_frame)
new_extension_entry.grid(row=2, column=1, sticky="we")

start_button = tk.Button(main_frame, text="Start", command=rename_files)
start_button.grid(row=3, column=0, columnspan=2, sticky="we", pady=(10, 0)) 

message_label = tk.Label(root, text="")
message_label.pack(side="bottom", anchor="w", padx=20, pady=(0, 20))

root.mainloop()
