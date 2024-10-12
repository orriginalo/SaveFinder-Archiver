[English readme](https://github.com/orriginalo/SaveFinder-Archiver/blob/main/README.md) • [Русский readme](https://github.com/orriginalo/SaveFinder-Archiver/blob/main/README.ru.md)

#### Это приложение для копирования и архивации сохранений и настроек в некоторых играх.

## Функции :
### Консольное и GUI :
- Поиск и обнаружение путей к игровым сохранениям
- Копирование и архивация сохранений в zip архив
### GUI :
- Архивация в один архив
- Копирование в одну папку
- Восстановление сохранений из созданного файла

## 1. Установка
```python
pip install -r requirements.txt
```
## 2. Использование
- **Консольное:**
1) Запустите файл **main.py** с помощью python3
2) Ожидайте окончания сканирования файлов
3) После этого, укажите нужные игры
4) Подтвердите свой выбор
5) Ожидайте окончания архивации.
- **GUI:**
1) Запустите файл **main_gui.py**
2) Если это первый запуск, то включите чекбокс **'Scan for new saves'**.
3) Нажмите на кнопку **'Start finding'**
4) Выберите нужные чекбоксы
5) Выберите копирование или архивацию
6) Нажмите на кнопку **'Start'** (файлы скопируются в папку Archivated которая появится при первом запуске в директории с программой)
- **SavePlacer**:
	- Нажмите на кнопку **'SavePlacer'** сверху основного окна и нажмите **'Open'**.
	- Выберите **'Archive'** или **'Folder'** в зависимости от того в каком виде у вас созданный SaveFinder файл.
	- Укажите путь до этого файла.
	- Нажмите кнопку **'Start'**
	
 Если вы хотите чтобы программа искала не только в C:/Users (по умолчанию), то нажмите кнопку **'Other paths'** сверху программы, затем кнопку **'Add'**. И нажатием на кнопку *Select* укажите путь где лежат ваши игры. Пока есть только 4 варианта, думаю, что больше и не нужно.
### Этапы :
1) Добавить возможность выбирать другую папку куда будут бэкапится файлы
2) Добавлять поддержку большего количества игр.
---
' * ' - В других директориях *(Other paths)*
#### Поддерживаемые игры:
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
- Overcooked 1, 2
- Dead Cells *
- Doom 3 *
#### Игры на очереди:
- Risk of rain 2 *
- Cyberpunk 2077 *
- Subnautica *
- FarCry 4 *
- FarCry 5 *
- Ultrakill *
- Watch Dogs 2 *
- Devil May Cry 5 *
- Minecraft