# Python 3.9.6, test at OSX

# 2024.06.12 - Jihoon Han
# This script creates a secondary backup of data stored on the NAS (Network Attached Storage) to the DAS (Direct Attached Storage) Cluster.
# 
# Instructions:
# - For "nas_path", enter the location where the NAS volume you want to back up is mounted.
# - For "das_path", enter the location where the DAS volume where you want to save the backup is mounted.
#
# This script executes the rsync command for each subfolder of "projects" and "data".
# The output of the rsync command is saved in a directory called "rsync_history" inside das_path.

from glob import glob  # Import glob module for finding file paths matching a specified pattern
from datetime import datetime  # Import datetime module to work with date and time
import os  # Import os module for interacting with the operating system

# main function
if __name__ == "__main__":
    nas_path = '/path/to/nas'  # Path where the NAS volume is mounted
    das_path = '/path/to/das'  # Path where the DAS cluster volume is mounted
    rsync_password = 'password' # NAS rsync account password for DAS-Cluster01
    rsync_port = 123456 # NAS rsync service port
    nas_ip = '127.0.0.1' # NAS source IP 
    nas_id = 'myidgood'

    data2backup_names = [path.split('/')[-1] for path in glob(os.path.join(das_path, 'data/*'))]
    proj2backup_namse = [path.split('/')[-1] for path in glob(os.path.join(das_path, 'projects/*'))]

    _path2backup_data = [os.path.join(nas_path, 'data', dname) for dname in data2backup_names] # Get all subfolders in the 'data' directory
    _path2backup_proj = [os.path.join(nas_path, 'projects', dname) for dname in proj2backup_namse] # Get all subfolders in the 'projects' directory
    path2backup = _path2backup_proj + _path2backup_data  # Combine both lists of paths 

    # Execute NAS to DAS backup for each project and data folder
    for src_path in path2backup:
        # Extract the directory names
        dir_name, proj_name = src_path.split('/')[-2:]
        # Destination path on the DAS
        dst_path = os.path.join(das_path, dir_name)

        # Construct the rsync command
        rsync_command = f'nohup rsync -rpuihv --rsh="/opt/homebrew/bin/sshpass -p {rsync_password} ssh -o StrictHostKeyChecking=no -p {rsync_port}" --partial --append --append-verify --size-only --delete -og {nas_id}@{nas_ip}:{src_path} {dst_path} 1>/dev/null 2>&1 &'
        _ = os.system(rsync_command)  # Execute the rsync command
        print(rsync_command)  # Print the rsync command to the console for verification
