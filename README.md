## File Organizer

A simple and efficient file organization tool that automatically sorts files in a directory based on their extensions. 
It helps keep folders clean and structured by grouping files into categories such as documents, media, code, and more.

Features                                                                                                          
Scans a selected directory for files                                                                                                      
Automatically sorts files based on extension                                                                                                      
Organizes files into categorized folders such as:                                                                                                      
Documents (.txt, .pdf, .docx, etc.)                                                                                                      
Media (.mp4, .mp3, .jpg, .png, etc.)                                                                                                      
Code files (.py, .html, etc.)                                                                                                      
Creates folders automatically if they don’t exist                                                                                                      
Simple and lightweight script with minimal setup                                                                                                      
How It Works

The script iterates through all files in a given directory, checks each file’s extension, and moves it into the appropriate category folder. 
If the destination folder does not exist, it is created automatically.

Installation

Clone the repository:                                                                  
git clone https://github.com/your-username/file-organizer.git                                                                  

Navigate into the project folder:                                                                  
cd file-organizer                                                                  

Ensure you have Python installed (if it is a Python script):
python --version                                                                  
Usage                                                                  

Run the script and specify the folder you want to organize:
python organizer.py /path/to/your/folder                                                                  

Or, if no argument is required, simply:                                                                  

python organizer.py                                                                  
Example Structure After Running                                                                  
Downloads/                                                                  
│
├── Documents/                                                                  
│   ├── notes.txt                                                                  
│   ├── report.pdf                                                                  
│                                                                  
├── Media/                                                                  
│   ├── video.mp4                                                                  
│   ├── image.jpg                                                                  
│                                                                  
├── Code/                                                                  
    ├── script.py                                                                  
    ├── app.js                                                                  
 

Future Improvements:
Add GUI support                                                                   
Allow custom category rules via config file                                                                  
Add undo/rollback functionality                                                                  
Support recursive folder organization   

License:                                                           
This project is open-source.

