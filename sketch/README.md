# Sketch

Sketch is a Python module you can use to draw images with code.

![sketch examples](.data/sketch_examples.jpg)


---

## Self Setup Instructions

You will need to install Python and Pygame before using the sketch module.

### Install Python
1. Click on this link to go to the Python downloads page: https://www.python.org/downloads/
2. Press the orange button to download the latest version of Python for your operating sytem.
3. Once the file has downloaded, open it and follow the instructions. When it asks you whether you want to install `pip`, make sure to tick this box!

### Install Pygame
4. Open the `Terminal` application (Mac/Linux) or `Command Prompt` (Windows).
5. Copy and paste this command into the terminal: `python3 -m pip install -U pygame --user` and then press the `return` key on your keyboard.
6. If all has gone well, you should be able to copy and paste the following command into your terminal: `python3 -m pygame.examples.aliens`. After pressing the `return` key again, a small window should appear, allowing you to play a game of `Aliens`.

### Install the Sketch module
7. Finally, open the following page in your web browser: https://github.com/ddrous/ks3-project
8. Click on the green button marked `code` and then select `Download ZIP` to download the ZIP file.
9. On Mac, double-click the file. On Windows, right click the file, select `extract all` and then follow the instructions.
10. You should be able to find the sketch folder within this folder.

### Alternatively

If you can't install the above locally, an alternative option is to use replit.com:
1. Create an account on https://replit.com
2. Follow this link: https://replit.com/@PaoloM/PythonSketch
3. Press the blue "Use Template" button in the top right


## Instructions for Network Environments

Schools with network environments require special instructions since the ones above install PyGame to the local appdata, and often, students' appdata clears after every log out. So follow the steps below.

1) Install the version of Python you require and reboot after

2) Go to PyGame's PyPI to get the ".WHL" file. https://pypi.org/project/pygame/#files
(Make sure that you download the correct version file to match the version of Python you have)

3) Once downloaded, move it to a network drive and then make a batch file of the lines below for example:
```bash
cd C:\Program Files\Python310\include
pip install "T:\Pygame\pygame-2.1.2-cp310-cp310-win_amd64.whl" --force-reinstall
```
First, specify the python directory and the includes folder as this is where it will pickup that PyGame is installed. Secondly, install the whl file. Now this should be complete and pygame should be installed. You can then run their test commands to make sure that it is working.

4) Run the code (a window should appear with the Japanese flag).


---

## Getting Started

Read the `cheat-sheet.md` file - it tells you how to use the `sketch` module. 

Either follow the lessons in the `worksheets` folder, or just freestyle!


---

## School Setup Instructions

1. Install Python on the students' lab machines (version 3.x). https://www.python.org/downloads/
2. This should include the IDLE IDE if the machines don't already have an editor like VSCode.
3. Install Pygame for the chosen version of Python. `python3 -m pip install -U pygame --user`
4. Clone this repository (https://github.com/ddrous/ks3-project) into a shared folder that the students have access to.

To test that setup was successful, please check that students are able to:
1. Copy the ks3-project folder into their own personal directory.
2. Open the example.py file with an IDE (e.g. IDLE).
