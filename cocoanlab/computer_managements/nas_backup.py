# Python 3.9.6

# 2024.04.16 - Jihoon Han
# This is the code to make a secondary backup of the data stored on the NAS to the DAS Cluster.
# For "nas_path", enter the location where the volume of the NAS you want to back up is mounted. 
# For "das_path", enter the location where the volume of the DAS you want to save is mounted. 
# 
# This code executes the rsync command for each of the subfolders of project and data.
# The output of the rsync command is created in a location called "rsync_history" inside das_path.

from glob import glob
from datetime import datetime
import os

# main function
if __name__ == "__main__":
    nas_path = '/Volumes/cocoanlab02' # CNIR NAS 11 mount path
    das_path = '/Volumes/DAS_Cluster02' # DAS Cluster mount path

    # Make rsync output directory
    # get a date of today
    today_date = str(datetime.now()).split(' ')[0]
    # path to save output of rsync
    rsync_history_path = os.path.join(das_path, 'rsync_history', today_date)
    # create a rsync output path when it doesn't exist
    if not os.path.exists(rsync_history_path):
        os.makedirs(os.path.join(rsync_history_path, 'data'))
        os.makedirs(os.path.join(rsync_history_path, 'projects'))
    
    # get all path to be back-up
    _path2backup_projects = glob(os.path.join(nas_path, 'projects/*')) # project dir
    _path2backup_data = glob(os.path.join(nas_path, 'data/*')) # data dir
    path2backup = _path2backup_projects + _path2backup_data 

    # excute NAS to DAS for each of project and data.
    for src_path in path2backup:
        # get names of directories
        dir_name, proj_name = src_path.split('/')[-2:]
        dst_path = os.path.join(das_path, dir_name)
        # output history file
        rsync_output_fname = os.path.join(rsync_history_path, f'{dir_name}/{proj_name}.out')

        # rsync command line
        rsync_command = f'nohup rsync -aurvPtl --delete {src_path} {dst_path} > {rsync_output_fname} &'
        _ = os.system(rsync_command) # excute
        print(rsync_command) # print it to check.