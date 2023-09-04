# Veeam_test

The 'result.png' photo is a screenshot of my execution result, source is the source folder, and backup is the backup folder, and log.text is the output log. sync_folders.py is my code.


A summary of the steps in this code:

1.Parse command-line arguments to get source folder path, replica folder path, sync interval, and log file path.  

2.Enter an infinite loop to continuously perform the synchronization process at specified intervals.  

3.Inside the loop, the sync_folders function is called to:  

  -Retrieve lists of files in the source and replica folders.  
  
  -Identify files to be copied from source to replica and files to be deleted from replica.  
  
  -Copy the required files from source to replica and log the copying operations.  
  
  -Delete the required files from replica and log the deletion operations.  
  
4.The log function is used to log the synchronization operations to a specified log file and display them on the console.  

5.Finally, the if __name__ == "__main__": block ensures that the code only runs when the script is executed directly and not when it's imported as a module.  

In summary, this code sets up a folder synchronization program that periodically synchronizes the contents of two folders, logs the operations, and can be configured through command-line arguments.
