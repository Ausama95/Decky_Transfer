import paramiko
import tkinter as tk
from tkinter import filedialog
import os

class FileTransferGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Decky Transfer")  # Change the program title
        self.root.geometry("300x400")  # Set the window size
        
        # Create a menu bar
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)
        
        # Create a "File" menu with an "Exit" option
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Exit", command=self.root.quit)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        
        # Create a "Help" menu with "Instructions" and "About" options
        self.help_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.help_menu.add_command(label="Instructions", command=self.show_instructions)
        self.help_menu.add_command(label="About", command=self.show_about)
        self.menu_bar.add_cascade(label="Help", menu=self.help_menu)

        # Create a frame to hold all the elements
        self.main_frame = tk.Frame(root)
        self.main_frame.pack(pady=20)
        
        self.hostname_label = tk.Label(self.main_frame, text="Linux System IP:")
        self.hostname_label.pack(anchor="w")
        self.hostname_entry = tk.Entry(self.main_frame)
        self.hostname_entry.pack(fill="x", pady=5)
        
        self.username_label = tk.Label(self.main_frame, text="Username:")
        self.username_label.pack(anchor="w")
        self.username_entry = tk.Entry(self.main_frame)
        self.username_entry.pack(fill="x", pady=5)
        
        self.password_label = tk.Label(self.main_frame, text="Password:")
        self.password_label.pack(anchor="w")
        self.password_entry = tk.Entry(self.main_frame, show="*")
        self.password_entry.pack(fill="x", pady=5)
        
        self.local_file_label = tk.Label(self.main_frame, text="Local File:")
        self.local_file_label.pack(anchor="w")
        self.local_file_button = tk.Button(self.main_frame, text="Select File", command=self.browse_local_file)
        self.local_file_button.pack(fill="x", pady=5)
        
        self.remote_file_label = tk.Label(self.main_frame, text="Remote Path:")
        self.remote_file_label.pack(anchor="w")
        self.remote_file_entry = tk.Entry(self.main_frame)
        self.remote_file_entry.pack(fill="x", pady=5)
        
        self.transfer_button = tk.Button(self.main_frame, text="Transfer File", command=self.transfer_files)
        self.transfer_button.pack(fill="x", pady=10)
        
        self.error_label = tk.Label(self.main_frame, text="", fg="red")
        self.error_label.pack()

    def browse_local_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.local_file_button.config(text="File Selected")
            self.local_file_path = file_path

    def transfer_files(self):
        hostname = self.hostname_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()
        local_file_path = self.local_file_path
        remote_path = self.remote_file_entry.get()  # Get the remote path from the entry

        # Check if any required field is empty
        if not hostname or not username or not password or not local_file_path or not remote_path:
            self.error_label.config(text="Please fill in all required fields.", fg="red")
            return

        try:
            client = paramiko.SSHClient()
            client.load_system_host_keys()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(hostname, port=22, username=username, password=password)
            print("Connected successfully!")

            sftp = client.open_sftp()

            # Extract the filename from the local file path
            local_filename = os.path.basename(local_file_path)

            # Combine the remote path with the extracted filename
            remote_file_path = os.path.join(remote_path, local_filename)

            sftp.put(local_file_path, remote_file_path)
            print("File transferred successfully!")

            sftp.close()
            client.close()

            self.error_label.config(text="File transferred successfully!", fg="green")  # Update the label color

        except Exception as e:
            print(f"Error: {e}")
            print("Full Traceback:")
            import traceback
            traceback.print_exc()
            self.error_label.config(text=f"Error: {e}", fg="red")
    
    def show_instructions(self):
        instructions_text = """
        Instructions:
        1. Enter the System IP (e.g., 192.168.1.100), Username, and Password.
        2. Click 'Select File' to choose a local file.
        3. Enter the Remote Path where you want to transfer the file (e.g., /home/username/).
        4. Click 'Transfer File' to initiate the transfer.
        """
        # Adjust width and height to fit the content
        instructions_window = tk.Toplevel(self.root)
        instructions_window.title("Instructions")
        instructions_text_widget = tk.Label(instructions_window, text=instructions_text, padx=10, pady=10, anchor="w", justify="left")
        instructions_text_widget.pack()

    def show_about(self):
        about_text = "Decky Transfer\nVersion 1.0\n\nCreated by Ausama95\n\nGitHub Profile: https://github.com/Ausama95"
        tk.messagebox.showinfo("About", about_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = FileTransferGUI(root)
    root.mainloop()
