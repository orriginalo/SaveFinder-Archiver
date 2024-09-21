import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror, showwarning, showinfo
from tkinter import filedialog
import os
import configparser
import json
import shutil
import zipfile
from rich import print
from time import perf_counter
from datetime import datetime


roaming_path = f"C:\\Users\\{os.getlogin()}\\AppData\\Roaming"
local_path = f"C:\\Users\\{os.getlogin()}\\AppData\\Local"
locallow_path = f"C:\\Users\\{os.getlogin()}\\AppData\\LocalLow"
documents_path = f"C:\\Users\\{os.getlogin()}\\Documents"
steam_path = "C:\\Program Files (x86)\\Steam"
users_path = f"C:\\Users\\{os.getlogin()}"

gameCounter = 0
games_saves_paths = []
check_vars = []
global scan_new_var


def first_run():
	if os.path.exists("config.ini"):
		pass
	else:
		scan_new_var.set(1)
		with open('config.ini', 'w') as configfile:
				config_data = {
		'BASE PATHS': {
				'steam_path_1': '',
				'steam_path_2': '',
				'steam_path_3': '',
				'steam_path_4': ''
		},
		'SETTINGS': {
				'lang': 'en'
		},
		'GAME PATHS': {
				'terraria_path': '',
				'geometrydash_path': '',
				'stormworks_path': '',
				'zomboid_path': '',
				'deadcells_path': '',
				'ftl_path': '',
				'rimworld_path': '',
				'stardew_path': '',
				'mgs_path': '',
				'mgr_path': '',
				'satisfactory_path': '',
				'cult_of_the_lamb_path': '',
				'valheim_path': '',
				'doom_eternal_path': '',
				'doom_2016_path': '',
				'operator_911_path': '',
				'skylines1_path': '',
				'skylines2_path': '',
				'dying_light_path': '',
				'snowrunner_path': '',
				'the_forest_path': '',
				'the_long_dark_path': '',
				'disco_elysium_path': '',
				'scrap_mechanic_path': '',
				'dont_starve_together_path': '',
				'ets_2_path': '',
				'skyrim_path': '',
				'fs_19_path': '',
				'fs_17_path': '',
				'fs_22_path': '',
				'fallout4_path': '',
				}
		}
		with open('config.ini', 'w') as configfile:
				for section, values in config_data.items():
						configfile.write(f'[{section}]\n')
						for key, value in values.items():
								configfile.write(f'{key} = {value}\n')
						configfile.write('\n')
	if os.path.exists(f".\\Archivated"):
		pass
	else:
		os.mkdir(f".\\Archivated")
	
	configg = configparser.ConfigParser()
	configg.read("config.ini")
	global config
	config = configg

class game():
	def __init__(self, name, folder_name, where_search_path, cfg_name, file_in: str = None, exception_in_path: str = None, second_folder_name: str = None):
		self.folder_name = folder_name
		self.second_folder_name = second_folder_name
		self.path = where_search_path
		self.cfg_name = cfg_name
		self.name = name
		self.file_in = file_in
		self.exception_in_path = exception_in_path
		
	def find_game(self):
		global gameCounter
		if scan_new_var.get() == 1 and (config.get('GAME PATHS', self.cfg_name) == '' or (not os.path.exists(config.get('GAME PATHS', self.cfg_name)))):
			for root, dirs, files in os.walk(self.path):
				for dirname in dirs:
					if dirname == self.folder_name or dirname == self.second_folder_name:
						if self.file_in != None:
							if self.exception_in_path != None:
								if any(file == self.file_in for file in os.listdir(os.path.join(root, dirname))): # if file_in == "steam.exe"
									if self.exception_in_path not in os.path.join(root, dirname):
										gameCounter += 1
										print(f"[bold white]{gameCounter}. [bold blue]{self.name} detected![bold white][italic] In:", f"{os.path.join(root, dirname)}")
										games_list.insert(0, f"{self.name} - {os.path.join(root, dirname)}")
										games_saves_paths.append(os.path.join(root, dirname))
					
										tosave_val = IntVar()
										tosave_val.set(0)
										cb = ttk.Checkbutton(cb_frame, text=self.name, variable=tosave_val, takefocus=0)
										cb.pack(anchor=W)
										check_vars.append(tosave_val)
					
										config.set('GAME PATHS', self.cfg_name, os.path.join(root, dirname))
										with open('config.ini', 'w') as configfile:
											config.write(configfile)
										break 
							else:
								if any(file == self.file_in for file in os.listdir(os.path.join(root, dirname))): # if file_in == "steam.exe"
									gameCounter += 1
									print(f"[bold white]{gameCounter}. [bold blue]{self.name} detected![bold white][italic] In:", f"{os.path.join(root, dirname)}")
									games_list.insert(0, f"{self.name} - {os.path.join(root, dirname)}")
									games_saves_paths.append(os.path.join(root, dirname))
				 
									tosave_val = IntVar()
									tosave_val.set(0)
									cb = ttk.Checkbutton(cb_frame, text=self.name, variable=tosave_val, takefocus=0)
									cb.pack(anchor=W)
									check_vars.append(tosave_val)
				 
									config.set('GAME PATHS', self.cfg_name, os.path.join(root, dirname))
									with open('config.ini', 'w') as configfile:
										config.write(configfile)
									break 
						else:
							if self.exception_in_path != None:
								if self.exception_in_path not in os.path.join(root, dirname):
									gameCounter += 1
									print(f"[bold white]{gameCounter}. [bold blue]{self.name} detected![bold white][italic] In:", f"{os.path.join(root, dirname)}")
									games_list.insert(0, f"{self.name} - {os.path.join(root, dirname)}")
									games_saves_paths.append(os.path.join(root, dirname))
				 
									tosave_val = IntVar()
									tosave_val.set(0)
									cb = ttk.Checkbutton(cb_frame, text=self.name, variable=tosave_val, takefocus=0)
									cb.pack(anchor=W)
									check_vars.append(tosave_val)
				 
									config.set('GAME PATHS', self.cfg_name, os.path.join(root, dirname))
									with open('config.ini', 'w') as configfile:
										config.write(configfile)
									break 
							else:
								gameCounter += 1
								print(f"[bold white]{gameCounter}. [bold blue]{self.name} detected![bold white][italic] In:", f"{os.path.join(root, dirname)}")
								games_list.insert(0, f"{self.name} - {os.path.join(root, dirname)}")
								games_saves_paths.append(os.path.join(root, dirname))
				
								tosave_val = IntVar()
								tosave_val.set(0)
								cb = ttk.Checkbutton(cb_frame, text=self.name, variable=tosave_val, takefocus=0)
								cb.pack(anchor=W)
								check_vars.append(tosave_val)
				
								config.set('GAME PATHS', self.cfg_name, os.path.join(root, dirname))
								with open('config.ini', 'w') as configfile:
									config.write(configfile)
								break
		else:
			if config.get("GAME PATHS", self.cfg_name) != '' and os.path.exists(config.get("GAME PATHS", self.cfg_name)):
				gameCounter += 1
				games_saves_paths.append(config.get('GAME PATHS', self.cfg_name))
				games_list.insert(0, f"{self.name} - {config.get('GAME PATHS', self.cfg_name)}")

				tosave_val = IntVar()
				tosave_val.set(0)
				cb = ttk.Checkbutton(cb_frame, text=self.name, variable=tosave_val, takefocus=0)
				cb.pack(anchor=W)
				check_vars.append(tosave_val)

				print(f"[bold white]{gameCounter}. [bold blue]{self.name}[bold white][italic] In:", f"{config.get('GAME PATHS', self.cfg_name)}")


def create_saves_json(json_path):
	saves = {}
	username = os.getlogin()  # Получение имени пользователя
	for path in selected_paths:
		gamename = os.path.basename(path)
		saves[gamename] = {"path": path, "username": username}
	
	with open(json_path, 'w', encoding='utf-8') as f:
		json.dump(saves, f, ensure_ascii=False, indent=4)


def find_games():
	startfind_btn.config(state=DISABLED)
	select_all_btn.config(state=NORMAL)	
	startarchive_btn.config(state=NORMAL)
 
	print("\n=== Finding game saves paths... ===")
	# -------------- GAMES --------------
	
	start = perf_counter()	
 
	stormworks = game("Stormworks","Stormworks", roaming_path, "stormworks_path")
	stormworks.find_game()
 
	terraria = game("Terraria", "Terraria", documents_path, "terraria_path")
	terraria.find_game()
	
	geometrydash = game("Geometry Dash", "GeometryDash", local_path, "geometrydash_path")
	geometrydash.find_game()
 
	zomboid = game("Project Zomboid", "Zomboid", users_path, "zomboid_path")
	zomboid.find_game()
 
	ftl = game("FTL: Faster Than Light", "FasterThanLight", documents_path, "ftl_path")
	ftl.find_game()
 
	rimworld = game("RimWorld", "RimWorld", locallow_path, "rimworld_path", exception_in_path="Temp", second_folder_name="RimWorld by Ludeon Studios")
	rimworld.find_game()
	
	stardew = game("Stardew Valley", "StardewValley", roaming_path, "stardew_path")
	stardew.find_game()
	
	mgr = game("MGR", "MGR", documents_path, "mgr_path")
	mgr.find_game()
 
	satisfactory = game("Satisfactory", "FactoryGame", local_path, "satisfactory_path")
	satisfactory.find_game()
	
	mgs = game("Metal Gear Solid","287700", documents_path, "mgs_path")
	mgs.find_game()
 
	cult_of_the_lamb = game("Cult Of The Lamb", "Cult Of The Lamb", locallow_path, "cult_of_the_lamb_path")
	cult_of_the_lamb.find_game()
 
	valheim = game("Valheim", "Valheim", locallow_path, "valheim_path")
	valheim.find_game()
 
 
	doom_eternal = game("Doom Eternal", "DOOMEternal", users_path, "doom_eternal_path")
	doom_eternal.find_game()
	
	doom_2016 = game("Doom 2016", "DOOM", users_path, "doom_2016_path", exception_in_path="AppData")
	doom_2016.find_game()
 
	operator_911 = game("911 Operator", "911 Operator", locallow_path, "operator_911_path")
	operator_911.find_game()
 
	skylines1 = game("Cities: Skylines", "Cities_Skylines", local_path, "skylines1_path")
	skylines1.find_game()
 
	skylines2 = game("Cities: Skylines 2", "Cities Skylines II", locallow_path, "skylines2_path")	
	skylines2.find_game()
 
	dying_light = game("Dying Light", "DyingLight", documents_path, "dying_light_path")
	dying_light.find_game()
 
	snowrunner = game("Snowrunner", "SnowRunner", documents_path, "snowrunner_path")
	snowrunner.find_game()
 
	the_forest = game("The Forest", "TheForest", locallow_path, "the_forest_path")
	the_forest.find_game()
 
	the_long_dark = game("The Long Dark", "TheLongDark", local_path, "the_long_dark_path")
	the_long_dark.find_game()
 
	disco_elysium = game("Disco Elysium", "Disco Elysium", locallow_path, "disco_elysium_path")
	disco_elysium.find_game()
 
	scrap_mechanic = game("Scrap Mechanic", "Scrap Mechanic", roaming_path, "scrap_mechanic_path")
	scrap_mechanic.find_game()
 
	dont_starve_together = game("Don't Starve Together", "DoNotStarveTogether", documents_path, "dont_starve_together_path")
	dont_starve_together.find_game()
 
	ets_2 = game("Euro Truck Simulator 2", "Euro Truck Simulator 2", documents_path, "ets_2_path")
	ets_2.find_game()
 
	skyrim = game("Skyrim", "Skyrim", documents_path, "skyrim_path")
	skyrim.find_game()
 
	fs_19 = game("Farming Simulator 19", "FarmingSimulator2019", documents_path, "fs_19_path")
	fs_19.find_game()
 
	fs_17 = game("Farming Simulator 17", "FarmingSimulator2017", documents_path, "fs_17_path")
	fs_17.find_game()
	
	fs_22 = game("Farming Simulator 22", "FarmingSimulator2022", documents_path, "fs_22_path")
	fs_22.find_game()
 
	fallout4 = game("Fallout 4", "Fallout4", documents_path, "fallout4_path")
	fallout4.find_game()
 
 
	end = perf_counter()
 
	time = end - start
 
	print(f"\n=== Found {gameCounter} game saves paths in {time:.2f} seconds ===\n")
	# deadcells = game("Dead Cells", "DeadCells", appdata_path, "deadcells_path")
	# deadcells.find_game()
	#
	# -------------- GAMES --------------

selected_all = False
def select_all():
	global select_all
	
	if select_all == True:
		for i in check_vars:
			i.set(0)
		select_all = False
	else:
		for i in check_vars:
			i.set(1)
			print(i.get())
		select_all = True
def copy_and_archive(): # Функция для копирования и архивации
		if all(i.get() == 0 for i in check_vars):
				showerror(title="SaveFinder&Archiver", message="No files selected!")
				return

		current_datetime = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
	
	
		global selected_paths
		selected_paths = [games_saves_paths[i] for i in range(len(games_saves_paths)) if check_vars[i].get() == 1]
	
		if type_var.get() == "archive":
				if selected_paths:
						archive_destination = f".\\Archivated\\temp.savefind-{current_datetime}"
						for path in selected_paths:
								shutil.copytree(path, os.path.join(archive_destination, os.path.basename(path)), dirs_exist_ok=True)
						
						create_saves_json(f".\\Archivated\\temp.savefind-{current_datetime}\\savepaths.json")

						shutil.make_archive(archive_destination.replace("temp.", ""), 'zip', archive_destination)
						shutil.rmtree(archive_destination)
						showinfo(title="SaveFinder&Archiver", message="Files successfully archived to one archive!")

		elif type_var.get() == "copy":
				archive_destination = f".\\Archivated\\savefind-{current_datetime}"
				os.makedirs(archive_destination, exist_ok=True)  # Ensure the directory exists
				
				for i in range(len(games_saves_paths)):
						if check_vars[i].get() == 1:
								shutil.copytree(games_saves_paths[i], os.path.join(archive_destination, os.path.basename(games_saves_paths[i])), dirs_exist_ok=True)
				
				create_saves_json(f".\\Archivated\\savefind-{current_datetime}\\savepaths.json")

				showinfo(title="SaveFinder&Archiver", message="Files successfully copied to one folder!")
		print("SHOOO: ", selected_paths)




placer_window = None

def create_placer_window():
	global placer_window
	def select_folder():
		entry.delete(0, tk.END)
		# Открываем диалог выбора папки
		if filetype_var.get() == "folder":
			folder_path = filedialog.askdirectory()
			if folder_path:  # Проверяем, что путь не пустой
					entry.insert(0, folder_path)  # Вставляем выбранный путь
		elif filetype_var.get() == "archive":
			folder_path = filedialog.askopenfilename()
			if folder_path:  # Проверяем, что путь не пустой
					entry.insert(0, folder_path)  # Вставляем выбранный путь
	def place_saves():
		if os.path.isfile(entry.get()) or os.path.isdir(entry.get()):
			if zipfile.is_zipfile(entry.get()):
				shutil.unpack_archive(entry.get(), entry.get().replace(".zip", ""))
				with open(os.path.join(entry.get().replace(".zip", ""), "savepaths.json"), 'r', encoding='utf-8') as f:
					data = json.load(f)
					for save in data.values():
						path = save["path"]
						username = save["username"]
						game_name = os.path.basename(path)
						path = path.replace(username, os.getlogin()).replace(game_name, "")
						print(f"{entry.get().replace(".zip", "")}/{game_name}")
						shutil.copytree(f"{entry.get().replace(".zip", "")}/{game_name}", path+game_name, dirs_exist_ok=True)
				shutil.rmtree(entry.get().replace('.zip', ''))
		
			if os.path.isdir(entry.get()):
				with open(os.path.join(entry.get(), "savepaths.json"), 'r', encoding='utf-8') as f:
					data = json.load(f)
					for save in data.values():
						path = save["path"]
						username = save["username"]
						game_name = os.path.basename(path)
						path = path.replace(username, os.getlogin()).replace(game_name, "")
						print(f"{entry.get()}/{game_name}")
						shutil.copytree(f"{entry.get()}/{game_name}", path+game_name, dirs_exist_ok=True)
			showinfo(title="SavePlacer", message="Files successfully placed!")
		else:
			showerror(title="SavePlacer", message="Invalid path!")
	def is_valid_path(newval):
		path = newval
		# Проверяем, является ли путь папкой
		if os.path.isdir(path):
				# Проверяем наличие файла savepaths.json в папке
				if 'savepaths.json' in os.listdir(path):
						start_place_btn.config(state=NORMAL)
						error_lb.config(foreground="green")
						errmsg.set("Путь действителен")
						return True

		# Проверяем, является ли путь zip-архивом
		if zipfile.is_zipfile(path):
				# Проверяем, содержит ли имя файла 'savefind-'
				if 'savefind-' in os.path.basename(path):
						start_place_btn.config(state=NORMAL)
						error_lb.config(foreground="green")
						errmsg.set("Путь действителен")
						return True
		
		start_place_btn.config(state=DISABLED)
		error_lb.config(foreground="red")
		errmsg.set("Путь недействителен")
		return False
	 
	if placer_window is None or not placer_window.winfo_exists():
		placer_window = Toplevel(main_w)
		placer_window.title("SavePlacer")
		placer_window.geometry("300x170")

		placer_header = Label(placer_window, text="SavePlacer", font=("JetBrains Mono", 14))
		placer_header.pack(side=TOP)
	
		separator = ttk.Separator(placer_window, orient="horizontal")
		separator.pack(fill=X, padx=10, pady=5)
		
		radio_frame = ttk.Frame(placer_window, borderwidth=0)
		radio_frame.pack(after=separator, padx=0, pady=0)

		global sel_folder_rb
		filetype_var = StringVar()
		sel_folder_rb = ttk.Radiobutton(radio_frame, text="Folder", variable=filetype_var, value="folder", takefocus=0)
		sel_folder_rb.pack(side=LEFT)

		global sel_archive_rb
		sel_archive_rb = ttk.Radiobutton(radio_frame, text="Archive", variable=filetype_var, value="archive", takefocus=0)
		sel_archive_rb.pack(side=LEFT, padx=10)
		filetype_var.set("archive")
	
		fileask_frame = ttk.Frame(placer_window)
		fileask_frame.pack(anchor=NW, fill=X, padx=4)

		entry = ttk.Entry(fileask_frame, width=30, validate="key", validatecommand=(placer_window.register(is_valid_path), "%P"))
		entry.pack(side=tk.LEFT, fill=tk.X, padx=[5,0], pady=3, expand=True)
	
		# Создаем кнопку
		global button
		button = ttk.Button(fileask_frame, text="Select", takefocus=0, command=select_folder)
		button.pack(side=tk.LEFT, padx=[3,5], pady=3)

		errmsg = StringVar()
		error_lb = ttk.Label(placer_window, foreground="red", textvariable=errmsg)
		error_lb.pack(anchor=NW, padx=[5,0])

		global start_place_btn
		start_place_btn = ttk.Button(placer_window, text="Start", takefocus=0, state=DISABLED, command=place_saves)
		start_place_btn.pack(side=TOP, padx=10, pady=10)

		def change_lang():
			if config.get('SETTINGS', 'lang') == 'en':
				sel_folder_rb.config(text="Folder")
				sel_archive_rb.config(text="Archive")
				button.config(text="Select")
				start_place_btn.config(text="Start")
    
			if config.get('SETTINGS', 'lang') == 'ru':
				sel_folder_rb.config(text="Папка")
				sel_archive_rb.config(text="Архив")
				button.config(text="Выбрать")
				start_place_btn.config(text="Запуск")
		change_lang()
	else:
			# Если окно уже открыто, просто передаем ему фокус
			placer_window.focus()

def change_language(lang):
	global options_list
	config.set('SETTINGS', 'lang', f'{lang}')
	print(config.get('SETTINGS', 'lang'))
	if lang == 'en':
		header.config(text="SaveFinder")
		# select_type_lb.config(text="Select archive\ntype:")
		startfind_btn.config(text="Start finding")
		startarchive_btn.config(text="Start")
		found_games_lb.config(text="Found games:")
		select_all_btn.config(text="Select all")
		scan_new_cb.config(text="Scan for new saves")
		archive_rb.config(text="Archive")
		copy_rb.config(text="Copy")
  
		# sel_folder_rb.config(text="Folder")
		# sel_archive_rb.config(text="Archive")
		# button.config(text="Select")
		# start_place_btn.config(text="Start")
	elif lang == 'ru':
		header.config(text="SaveFinder")
		# select_type_lb.config(text="Выберите тип\nархивирования:")
		startfind_btn.config(text="Начать поиск")
		startarchive_btn.config(text="Запустить")
		found_games_lb.config(text="Найденные игры:")
		select_all_btn.config(text="Выбрать все")
		scan_new_cb.config(text="Искать новые сохранения")
		archive_rb.config(text="Архив")
		copy_rb.config(text="Копия")
  
		# sel_folder_rb.config(text="Папка")
		# sel_archive_rb.config(text="Архив")
		# button.config(text="Выбрать")
		# start_place_btn.config(text="Запуск")
	config.set('SETTINGS', 'lang', f'{lang}')


main_w = Tk()
main_w.title("SaveFinder & Archiver")
# main_w.iconbitmap(default="icon.ico")
main_w.geometry("610x600")

menu_panel = tk.Menu(main_w)
main_w.config(menu=menu_panel)

language_menu = tk.Menu(menu_panel, tearoff=0)
lang_cas = menu_panel.add_cascade(label="Language", menu=language_menu)

language_menu.add_command(label="English", command= lambda:change_language('en'))
language_menu.add_command(label="Русский", command= lambda:change_language('ru'))


placer_menu = tk.Menu(menu_panel, tearoff=0)
placer_cas = menu_panel.add_cascade(label="SavePlacer", menu=placer_menu)

placer_menu.add_command(label="Open", command= create_placer_window)


header = Label(main_w, text="SaveFinder", font=("JetBrains Mono", 30))
header.pack()

separator = ttk.Separator(main_w, orient="horizontal")
separator.pack(fill=X, padx=10, pady=10)

startfindbtn_style = ttk.Style()
startfindbtn_style.configure('startfind.TButton', font=("JetBrains Mono", 15))
startfind_btn = ttk.Button(main_w, text="Start finding",style='startfind.TButton',takefocus=0, command=find_games)
startfind_btn.pack(ipadx=5, ipady=5)

scan_new_var = IntVar()
scan_new_cb = ttk.Checkbutton(main_w, text="Check new gamesaves", variable=scan_new_var, takefocus=0)
scan_new_cb.pack()

left_frame = Frame(main_w) # Левая часть
left_frame.pack(side=LEFT, padx=10, pady=10, fill=BOTH)

found_games_lb = Label(left_frame, text="Found games: ", font=("JetBrains Mono", 15))
found_games_lb.pack()

games_list = Listbox(left_frame, font=("JetBrains Mono", 10), width=50) # Список найденных игр с путями
games_list.pack(expand=1, fill=BOTH)

scrollbar = ttk.Scrollbar(left_frame, orient=HORIZONTAL) # Скроллбар для games_list
scrollbar.pack(side=BOTTOM, fill=X)
games_list.config(xscrollcommand=scrollbar.set)
scrollbar.config(command=games_list.xview)

right_frame = Frame(main_w) # Правая часть
right_frame.pack(side=RIGHT, padx=10, pady=10, fill=Y)

style = ttk.Style()
style.configure('TButton', font=('JetBrains Mono', 10))

startarchive_btn = ttk.Button(right_frame, text="Start", style='TButton',state=DISABLED,takefocus=0 ,command=copy_and_archive)
startarchive_btn.pack(fill=X, anchor=W,)

radio_frame = ttk.Frame(borderwidth=0)
radio_frame.pack(after=startarchive_btn, padx=0, pady=0)

type_var = StringVar()
copy_rb = ttk.Radiobutton(radio_frame, text="Copy", variable=type_var, value="copy", takefocus=0)
copy_rb.pack(side=LEFT)

archive_rb = ttk.Radiobutton(radio_frame, text="Archive", variable=type_var, value="archive", takefocus=0)
archive_rb.pack(side=LEFT, padx=10)
type_var.set("archive")
 
select_all_btn = ttk.Button(right_frame, text="Select all", style='TButton',state=DISABLED,takefocus=0 ,command=select_all)
select_all_btn.pack(fill=X)

cb_frame = ttk.Frame(borderwidth=2, relief=SOLID, padding=[7,7], width=157)
cb_frame.pack(anchor=NW, fill=X, after=select_all_btn, padx=0, pady=5)
	

first_run()
change_language(str(config.get('SETTINGS', 'lang')))

main_w.mainloop()
