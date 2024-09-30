<img src="https://img.shields.io/github/release/orriginalo/SaveFinder-Archiver"/>
[English readme](https://github.com/orriginalo/SaveFinder-Archiver/blob/main/README.md) • [Русский readme](https://github.com/orriginalo/SaveFinder-Archiver/blob/main/README.ru.md)

#### This application is for copying and archiving saves and settings in certain games.

## Features:
### Console and GUI:
- Searching and discovering paths to game saves
- Copying and archiving saves into a zip archive
### GUI:
- Archiving into one archive
- Copying into one folder
- Recovering saves from a created file

## 1. Installation
```python
pip install -r requirements.txt
```
## 2. Usage
- **Console:**
1) Run the file **main.py** using python3
2) Wait for the file scanning to complete
3) After that, specify the desired games
4) Confirm your selection
5) Wait for the archiving to finish.
  
- **GUI:**
1) Run the file **main_gui.py**
2) If this is the first launch, enable the checkbox **'Scan for new saves'**.
3) Click the **'Start finding'** button
4) Select the necessary checkboxes
5) Select copy or archive
6) Click the **'Start'** button (files will be copied to the Archivated folder, which will appear in the directory with the program when you first launch it)
- **SavePlacer**:
	- Click on the **'SavePlacer'** button at the top of the main window and click **'Open'**. 
	- Select **'Archive'** or **'Folder'** depending on the format of the SaveFinder file you created. 
	- Specify the path to this file. 
	- Click on the **'Start'** button


If you want the program to search not only in C:/Users (as per default), then click the **'Other paths'** button at the top of the program, then the **'Add'** button. And by clicking the *Select* button, specify the path where your games are located. There are only 4 options so far, I think that more is not needed.
### Future Steps:
1) Add the option to choose a different folder where the files will be backed up.
2) Add support for more games.
---
' * ' - In **'Other paths'**
#### Supported Games:
- Stormworks
- Geometry Dash
- Terraria
- Project Zomboid
- FTL : Faster Than Light
- RimWorld
- Stardew Valley
- Metal Gear Rising
- Valheim
- Cult Of The Lamb
- Doom Eternal
- Doom 2016
- 911 operator
- Cities Skylines 1 , 2
- Snowrunner
- The Forest
- The Long Dark
- Disco Elysium
- Scrap Mechanic
- Don't Starve Together
- Euro Truck Simulator 2
- Farming Simulator 17, 19, 22
- Dying Light
- Skyrim
- Fallout 4
- Dead Cells *
#### Upcoming Games:
- Doom 3 *
- Risk of rain 2 *
- Cyberpunk 2077 *
- Subnautica *
- FarCry 4 *
- FarCry 5 *
- Ultrakill *
- Watch Dogs 2 *
- Devil May Cry 5 *
- Minecraft
