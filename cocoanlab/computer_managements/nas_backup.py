# Python 3.9.6

# 2024.04.16 - Jihoon Han
# This script creates a secondary backup of data stored on the NAS (Network Attached Storage) to the DAS (Direct Attached Storage) Cluster.
# 
# Instructions:
# - For "nas_path", enter the location where the NAS volume you want to back up is mounted.
# - For "das_path", enter the location where the DAS volume where you want to save the backup is mounted.
#
# This script executes the rsync command for each subfolder of "projects" and "data".
# The output of the rsync command is saved in a directory called "rsync_history" inside das_path.
#
# ---
# 2024.06.05 - Updated rsync options, and added tar+cp transfer scripts, but  not in use.

from glob import glob  # Import glob module for finding file paths matching a specified pattern
from datetime import datetime  # Import datetime module to work with date and time
import os  # Import os module for interacting with the operating system

# main function
if __name__ == "__main__":
    nas_path = '/Volumes/cocoanlab02'  # Path where the NAS volume is mounted
    das_path = '/Volumes/DAS_Cluster02'  # Path where the DAS cluster volume is mounted

    # Create rsync output directory
    # Get today's date as a string in the format 'YYYY-MM-DD'
    today_date = str(datetime.now()).split(' ')[0]
    # Path to save the output of rsync
    rsync_history_path = os.path.join(das_path, 'rsync_history', today_date)
    # Create the rsync output path if it doesn't exist
    if not os.path.exists(rsync_history_path):
        os.makedirs(os.path.join(rsync_history_path, 'data'))  # Create 'data' directory
        os.makedirs(os.path.join(rsync_history_path, 'projects'))  # Create 'projects' directory
    
    # Get all paths to be backed up
    _path2backup_projects = glob(os.path.join(nas_path, 'projects/*'))  # Get all subfolders in the 'projects' directory
    _path2backup_data = glob(os.path.join(nas_path, 'data/*'))  # Get all subfolders in the 'data' directory
    path2backup = _path2backup_projects + _path2backup_data  # Combine both lists of paths

    # Execute NAS to DAS backup for each project and data folder
    for src_path in path2backup:
        # Extract the directory names
        dir_name, proj_name = src_path.split('/')[-2:]
        # Destination path on the DAS
        dst_path = os.path.join(das_path, dir_name)
        # Output history file path for the rsync command
        rsync_output_fname = os.path.join(rsync_history_path, f'{dir_name}/{proj_name}.out')

        # Construct the rsync command
        rsync_command = f'nohup rsync -rpuihv --progress --partial --append --append-verify --size-only --delete -og {src_path} {dst_path} > {rsync_output_fname} &'
        # rsync_command = f'nohup sh -c "tar cvf - {src_path} | (cd {dst_path} ; tar xvf -)" > {rsync_output_fname} &'  # Alternative command using tar, currently not in use
        _ = os.system(rsync_command)  # Execute the rsync command
        print(rsync_command)  # Print the rsync command to the console for verification
