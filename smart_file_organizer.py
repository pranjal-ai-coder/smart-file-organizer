import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

# --- Logic: Safe Organize ---
def organize_files():
    folder_path = filedialog.askdirectory()
    if not folder_path:
        return
    
    extensions = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif'],
        'Documents': ['.pdf', '.docx', '.txt', '.xlsx'],
        'Videos': ['.mp4', '.mkv', '.mov'],
        'Programs': ['.exe', '.msi', '.py']
    }

    for filename in os.listdir(folder_path):
        if os.path.isdir(os.path.join(folder_path, filename)):
            continue

        file_ext = os.path.splitext(filename)[1].lower()
        for folder, exts in extensions.items():
            if file_ext in exts:
                dest_folder = os.path.join(folder_path, folder)
                os.makedirs(dest_folder, exist_ok=True)
                
                src = os.path.join(folder_path, filename)
                dest = os.path.join(dest_folder, filename)
                
                # Collision handling: Safe renaming
                if os.path.exists(dest):
                    base, ext = os.path.splitext(filename)
                    dest = os.path.join(dest_folder, f"{base}_copy{ext}")
                
                try:
                    shutil.move(src, dest)
                except Exception as e:
                    print(f"Error moving {filename}: {e}")
    
    messagebox.showinfo('all files organize successfully')

# --- GUI: Dark Theme & Neon Green Border ---
root = tk.Tk()
root.title('SMART FILE ORGANIZER')
root.geometry('350x200')
root.configure(bg='#000000') # Deep Black Background

# Green Border Effect using a Frame
border_frame = tk.Frame(root, bg='#39FF14', padx=2, pady=2) # Neon Green Border Color
border_frame.pack(padx=20, pady=20, expand=True, fill='both')

inner_frame = tk.Frame(border_frame, bg='#121212') # Dark Grey Inner
inner_frame.pack(expand=True, fill='both')

# UI Elements
title_lbl = tk.Label(inner_frame, text='MART FILE ORGANIZER', font=('Consolas', 16, 'bold'), bg='#121212', fg='#39FF14')
title_lbl.pack(pady=20)

organize_btn = tk.Button(
    inner_frame, 
    text='START SCAN & ORGANIZE', 
    command=organize_files, 
    bg='#121212', 
    fg='#39FF14', 
    font=('Consolas', 10, 'bold'),
    activebackground='#39FF14',
    activeforeground='#000000',
    relief='flat',
    borderwidth=1
)
# Border around button
organize_btn.pack(pady=10, padx=20)

root.mainloop()
