# PythonWebscraping
Project is reagading finding the number of cases of COvid19 for a given year.
"# final-project-IndraPhani" 
## Project to find the different metrics regarding the top five countires covid data.
## Installation instructin for the Users and prerequsites
1. Check for existing installation
Open a non administrative PowerShell and run the following command:
python --version
If that gives you an error, try running
python3 --version
2. Installing Python
Download the installer from https://www.python.org/downloads/ (at the time of writing this document version 3.11.2).  Run the installer, but carefully read each screen.
The first screen screen with have an option to “Add python.exe to PATH”. Make sure to check that box then select “Install Now”.
3. Installing Windows Terminal
From https://github.com/microsoft/terminal/releases download the installer from the latest release.  Specifically, you want the one that has an extension of msixbundle (not .zip) and is for your version of Windows (either 10 or 11).  At the writing of this document, the file name for Windows 10 is Microsoft.WindowsTerminal_Win10_1.16.10261.0_8wekyb3d8bbwe.msixbundle
 
Run the installer; all default options should be fine.
Configuring Windows Terminal
We will use Windows Terminal to make it easy for us to open a PowerShell with the virtual environment activated.  Open your newly installed Windows Terminal.  We are going to configure the terminal to have a profile for our Virtual Environment.  In the upper bar, click the little down arrow
 
Select the “Settings” option (note, you can also open the settings window with the keyboard shortcut “Ctrl+,”
 
In the settings window, scroll down in the left pane until you see + Add a new profile, and select that option. We are going to choose to Duplicate the PowerShell profile
 
Change the Name of the profile by clicking the name field and typing a descriptive Name (notice that it starts as “Windows PowerShell (copy)”
Open the Command line argument.  Leave the powershell command, but add a space and
-NoExit -File %userprofile%\big-data-venv\Scripts\activate.ps1
To the end.  The entire command should now be:
%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe -NoExit -File %userprofile%\big-data-venv\Scripts\activate.ps1
If you had to use a different folder name when creating the virtual environment, replace big-data-venv with that folder name. Save your settings.

4. We will install packages using the pip command.  In the virtual environment run the following command
pip install jupyterlab
If this fails because of a broken prerequisite, try installing an older version of jupyterlab:
pip install jupyterlab==3.5.3
