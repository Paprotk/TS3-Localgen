import tkinter as tk
from tkinter import scrolledtext, simpledialog, messagebox, filedialog
import os
import subprocess
from base64 import b64decode
small_icon_data = "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"
text_content = ""
save_directory = ""
folder_path = ""  # Initialize folder_path to keep track of the latest directory
open_folder_button = None  # Variable to hold the reference to the "Open Folder" button
has_generated = False  # Flag to track if localized files have been generated

# Function to calculate the FNV-1 64-bit hash
def fnv1_64(data):
    # FNV offset basis for 64-bit
    FNV_OFFSET_BASIS = 0xcbf29ce484222325
    # FNV prime for 64-bit
    FNV_64_PRIME = 0x100000001b3
    
    # Initialize the hash value
    hash_value = FNV_OFFSET_BASIS
    
    # Process each byte of the input data
    for byte in data:
        hash_value = (hash_value * FNV_64_PRIME) & 0xffffffffffffffff
        hash_value ^= byte
    
    return hash_value

# Function to load the content of the selected text file into the text area
def load_text():
    global text_content
    global open_folder_button
    global has_generated
    
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        try:
            with open(file_path, 'r') as file:
                text_content = file.read()  # Save the content to the global variable
                text_area.delete(1.0, tk.END)  # Clear existing text
                text_area.insert(tk.END, text_content)  # Insert the text from the file
                save_button.config(state=tk.NORMAL)  # Enable the save button
                has_generated = False  # Reset the generation flag
                
                # Hide the "Open Folder" button if it exists
                if open_folder_button:
                    open_folder_button.grid_forget()
                    
        except Exception as e:
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, f"Failed to open file: {e}")
            save_button.config(state=tk.DISABLED)  # Disable the save button

# Function to save the hashed files based on predefined patterns
def save_hash():
    global save_directory
    global folder_path
    global open_folder_button
    global has_generated

    if has_generated:
        messagebox.showinfo("Info", "Localized files have already been generated. Please open a new base strings file to generate files again.")
        return

    name = simpledialog.askstring("", "Enter something unique for your mod.\nSomething with your name and the mod's name in it is a good choice. ")
    root.iconphoto(False, small_icon)
    if name:
        # Create a lowercase version of the name for hashing
        name_lower = name.lower()
        
        # Calculate the FNV-1 64-bit hash
        name_bytes = name_lower.encode('utf-8')
        hash_value = fnv1_64(name_bytes)
        hash_value_hex = f"{hash_value:016X}"

        # Ask where to save the files (folder name)
        save_directory = filedialog.askdirectory(title="Select Directory to Save Files")
        if save_directory:
            # Create a directory with the name provided by the user
            folder_path = os.path.join(save_directory, name)
            folder_path = os.path.normpath(folder_path)  # Normalize the path
            os.makedirs(folder_path, exist_ok=True)
            
            # List of filename patterns
            patterns = [
                "S3_220557DA_00000000_16(hash)_(HashedName)Strings_THA_TH%%+STBL.txt",
                "S3_220557DA_00000000_15(hash)_(HashedName)Strings_SWE_SE%%+STBL.txt",
                "S3_220557DA_00000000_14(hash)_(HashedName)Strings_SPA_MX%%+STBL.txt",
                "S3_220557DA_00000000_13(hash)_(HashedName)Strings_SPA_ES%%+STBL.txt",
                "S3_220557DA_00000000_12(hash)_(HashedName)Strings_RUS_RU%%+STBL.txt",
                "S3_220557DA_00000000_11(hash)_(HashedName)Strings_POR_BR%%+STBL.txt",
                "S3_220557DA_00000000_10(hash)_(HashedName)Strings_POR_PT%%+STBL.txt",
                "S3_220557DA_00000000_09(hash)_(HashedName)Strings_EL_GR%%+STBL.txt",
                "S3_220557DA_00000000_08(hash)_(HashedName)Strings_GER_DE%%+STBL.txt",
                "S3_220557DA_00000000_07(hash)_(HashedName)Strings_FRE_FR%%+STBL.txt",
                "S3_220557DA_00000000_06(hash)_(HashedName)Strings_FIN_FI%%+STBL.txt",
                "S3_220557DA_00000000_05(hash)_(HashedName)Strings_DUT_NL%%+STBL.txt",
                "S3_220557DA_00000000_04(hash)_(HashedName)Strings_DAN_DK%%+STBL.txt",
                "S3_220557DA_00000000_03(hash)_(HashedName)Strings_CZE_CZ%%+STBL.txt",
                "S3_220557DA_00000000_02(hash)_(HashedName)Strings_TAI_CN%%+STBL.txt",
                "S3_220557DA_00000000_01(hash)_(HashedName)Strings_CHI_CN%%+STBL.txt",
                "S3_220557DA_00000000_0F(hash)_(HashedName)Strings_POL_PL%%+STBL.txt",
                "S3_220557DA_00000000_0E(hash)_(HashedName)Strings_NOR_NO%%+STBL.txt",
                "S3_220557DA_00000000_0D(hash)_(HashedName)Strings_KOR_KR%%+STBL.txt",
                "S3_220557DA_00000000_0C(hash)_(HashedName)Strings_JPN_JN%%+STBL.txt",
                "S3_220557DA_00000000_0B(hash)_(HashedName)Strings_ITA_IT%%+STBL.txt",
                "S3_220557DA_00000000_0A(hash)_(HashedName)Strings_HUN_HU%%+STBL.txt",
                "S3_220557DA_00000000_00(hash)_(HashedName)Strings_ENG_US%%+STBL.txt"
            ]

            for pattern in patterns:
                # Replace placeholders in the pattern
                file_name = pattern.replace("(hash)", hash_value_hex).replace("(HashedName)", name)
                file_path = os.path.join(folder_path, file_name)
                file_path = os.path.normpath(file_path)  # Normalize the file path

                try:
                    # Write content to the file
                    with open(file_path, 'w') as file:
                        file.write(text_content)
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to save file: {file_path}\nError: {e}")

            def open_folder():
                if os.name == 'nt':
                    os.startfile(folder_path)
                elif os.name == 'posix':
                    subprocess.run(['xdg-open', folder_path], check=True)

            messagebox.showinfo(
                "Success",
                f"Files saved in:\n{folder_path}\n\nClick 'Open Folder' to view the files."
            )

            if open_folder_button is None:
                open_folder_button = tk.Button(frame_buttons, text="Open Folder", command=open_folder)
                open_folder_button.grid(row=0, column=2, padx=10, pady=10, sticky="ew")
            else:
                open_folder_button.grid(row=0, column=2, padx=10, pady=10, sticky="ew")  # Show the button if it's already created

            save_button.config(state=tk.DISABLED)
            has_generated = True

# Create the main window
root = tk.Tk()
root.title("Localgen")

small_icon = tk.PhotoImage(data=b64decode(small_icon_data))
root.iconphoto(False, small_icon)

# Add a scrollable text area
text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=20)
text_area.pack(padx=10, pady=10)

# Create a frame to hold buttons and keep their positions consistent
frame_buttons = tk.Frame(root)
frame_buttons.pack(padx=10, pady=10, fill=tk.X)

# Add button to open and load text file
open_button = tk.Button(frame_buttons, text="Open base strings file", command=load_text)
open_button.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

# Add button to save hash values and generate files
save_button = tk.Button(frame_buttons, text="Generate localized files", command=save_hash, state=tk.DISABLED)
save_button.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

# Run the main loop
root.mainloop()
