import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror, showwarning, showinfo
import os
import configparser
import shutil
from rich.console import Console
from rich import print

roaming_path = f"C:\\Users\\{os.getlogin()}\\AppData\\Roaming"
local_path = f"C:\\Users\\{os.getlogin()}\\AppData\\Local"
locallow_path = f"C:\\Users\\{os.getlogin()}\\AppData\\LocalLow"
documents_path = f"C:\\Users\\{os.getlogin()}\\Documents"
steam_path = "C:\\Program Files (x86)\\Steam"
users_path = f"C:\\Users\\{os.getlogin()}"

gameCounter = 0
games_saves_paths = []
check_vars = []

def first_run():
	if os.path.exists("config.ini"):
		pass
	else:
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
				'valheim_path': ''
				}
		}

		with open('config.ini', 'w') as configfile:
				for section, values in config_data.items():
						configfile.write(f'[{section}]\n')
						for key, value in values.items():
								configfile.write(f'{key} = {value}\n')
						configfile.write('\n')
	if os.path.exists(".\Archivated"):
		pass
	else:
		os.mkdir(".\Archivated")

first_run()

configg = configparser.ConfigParser()
configg.read("config.ini")

# lang = configg["SETTINGS"]["lang"]
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
		if config.get('GAME PATHS', self.cfg_name) == '' or not os.path.exists(config.get('GAME PATHS', self.cfg_name)):
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
										cb = ttk.Checkbutton(right_frame, text=self.name, variable=tosave_val)
										cb.pack(anchor=W)
										print(tosave_val, end=' ')
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
									cb = ttk.Checkbutton(right_frame, text=self.name, variable=tosave_val)
									cb.pack(anchor=W)
									print(tosave_val, end=' ')
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
									cb = ttk.Checkbutton(right_frame, text=self.name, variable=tosave_val)
									cb.pack(anchor=W)
									print(tosave_val, end=' ')
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
								cb = ttk.Checkbutton(right_frame, text=self.name, variable=tosave_val)
								cb.pack(anchor=W)
								print(tosave_val, end=' ')
								check_vars.append(tosave_val)
				
								config.set('GAME PATHS', self.cfg_name, os.path.join(root, dirname))
								with open('config.ini', 'w') as configfile:
									config.write(configfile)
								break
		else:
			gameCounter += 1
			games_saves_paths.append(config.get('GAME PATHS', self.cfg_name))
			games_list.insert(0, f"{self.name} - {config.get('GAME PATHS', self.cfg_name)}")

			tosave_val = IntVar()
			tosave_val.set(0)
			cb = ttk.Checkbutton(right_frame, text=self.name, variable=tosave_val)
			cb.pack(anchor=W)
			check_vars.append(tosave_val)

			print(f"[bold white]{gameCounter}. [bold blue]{self.name}[bold white][italic] In:", f"{config.get('GAME PATHS', self.cfg_name)}")




def find_games():
	startfind_btn.config(state=DISABLED)
	
	print("\n=== Finding game saves paths... ===")
	# -------------- GAMES --------------
	
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
	# deadcells = game("Dead Cells", "DeadCells", appdata_path, "deadcells_path")
	# deadcells.find_game()
	#
	# -------------- GAMES --------------

def copy_and_archive():
		print(value_inside.get(), " - ", options_list[2])
		
		if all(i.get() == 0 for i in check_vars):
				showerror(title="SaveFinder&Archiver", message="No files selected!")
				return

		selected_option = value_inside.get()

		if selected_option == options_list[1]:  # Archive to individual archives
				for i in range(len(games_saves_paths)):
						if check_vars[i].get() == 1:
								destination = os.path.join(".\\Archivated", os.path.basename(games_saves_paths[i]))
								shutil.copytree(games_saves_paths[i], destination, dirs_exist_ok=True)
								shutil.make_archive(destination, 'zip', destination)
								shutil.rmtree(destination)

				showinfo(title="SaveFinder&Archiver", message="Files successfully archived!")

		elif selected_option == options_list[2]:  # Archive all to one archive
				selected_paths = [games_saves_paths[i] for i in range(len(games_saves_paths)) if check_vars[i].get() == 1]
				if selected_paths:
						archive_destination = ".\\Archivated\\All saves"
						for path in selected_paths:
								shutil.copytree(path, os.path.join(archive_destination, os.path.basename(path)), dirs_exist_ok=True)
						
						shutil.make_archive(archive_destination, 'zip', archive_destination)
						shutil.rmtree(archive_destination)

						showinfo(title="SaveFinder&Archiver", message="Files successfully archived to one archive!")

		elif selected_option == options_list[3]:  # Copy to individual folders
				for i in range(len(games_saves_paths)):
						if check_vars[i].get() == 1:
								destination = os.path.join(".\\Archivated", os.path.basename(games_saves_paths[i]))
								shutil.copytree(games_saves_paths[i], destination, dirs_exist_ok=True)

				showinfo(title="SaveFinder&Archiver", message="Files successfully copied!")

		elif selected_option == options_list[4]:  # Copy all to one folder
				archive_destination = ".\\Archivated\\All saves"
				os.makedirs(archive_destination, exist_ok=True)  # Ensure the directory exists

				for i in range(len(games_saves_paths)):
						if check_vars[i].get() == 1:
								shutil.copytree(games_saves_paths[i], os.path.join(archive_destination, os.path.basename(games_saves_paths[i])), dirs_exist_ok=True)

				showinfo(title="SaveFinder&Archiver", message="Files successfully copied to one folder!")


def change_language(lang):
	global options_list
	if lang == 'en':
		header.config(text="SaveFinder")
		select_type_lb.config(text="Select archive\ntype:")
		startfind_btn.config(text="Start finding")
		startarchive_btn.config(text="Start archiving")
		found_games_lb.config(text="Found games:")
		lang_cas.config(label="Language")
		# TODO: Make a translation for options_list
		# options_list = [
		# "",
		# "Archive to individual archives",
		# "Archive all to one archive",
		# "Copy to individual folders",
		# "Copy all to one folder"
		# 		]
	elif lang == 'ru':
		header.config(text="SaveFinder")
		select_type_lb.config(text="Выберите тип\nархивирования:")
		startfind_btn.config(text="Начать поиск")
		startarchive_btn.config(text="Начать архивирование")
		found_games_lb.config(text="Найденные игры:")
		lang_cas.config(label="Язык")
		# options_list = [
		# "",
		# "Архивировать в отдельные архивы",
		# "Архивировать все в один архив",
		# "Скопировать в отдельные папки",
		# "Скопировать все в одну папку"
		# 		]

main_w = Tk()
main_w.title("SaveFinder & Archiver")
# main_w.iconbitmap(default="icon.ico")
main_w.geometry("650x600")

menu_panel = tk.Menu(main_w)
main_w.config(menu=menu_panel)

language_menu = tk.Menu(menu_panel, tearoff=0)
lang_cas = menu_panel.add_cascade(label="Language", menu=language_menu)

language_menu.add_command(label="English", command=lambda: change_language('en'))
language_menu.add_command(label="Русский", command=lambda: change_language('ru'))

header = Label(main_w, text="SaveFinder", font=("JetBrains Mono", 30))
header.pack()

separator = ttk.Separator(main_w, orient="horizontal")
separator.pack(fill=X, padx=10, pady=10)

startfind_btn = Button(main_w, text="Start finding", font=("JetBrains Mono", 15), command=find_games)
startfind_btn.pack()

left_frame = Frame(main_w)
left_frame.pack(side=LEFT, padx=10, pady=10, fill=BOTH)

found_games_lb = Label(left_frame, text="Found games: ", font=("JetBrains Mono", 15))
found_games_lb.pack()

games_list = Listbox(left_frame, font=("JetBrains Mono", 10), width=50)
games_list.pack(expand=1, fill=BOTH)

scrollbar = ttk.Scrollbar(left_frame, orient=HORIZONTAL)
scrollbar.pack(side=BOTTOM, fill=X)
games_list.config(xscrollcommand=scrollbar.set)
scrollbar.config(command=games_list.xview)

right_frame = Frame(main_w)
right_frame.pack(side=RIGHT, padx=10, pady=10, fill=Y)

select_type_lb = Label(right_frame, text="Select archive\ntype:", font=("JetBrains Mono", 15))
select_type_lb.pack(anchor=W)

options_list = [
	"",
	"Archive to individual archives",
	"Archive all to one archive",
	"Copy to individual folders",
	"Copy all to one folder"
				]

value_inside = StringVar()
value_inside.set(options_list[1])

question_menu = ttk.OptionMenu(right_frame, value_inside, *options_list) 
question_menu.pack(fill=X, anchor=W) 

startarchive_btn = Button(right_frame, text="Start archiving", font=("JetBrains Mono", 10), command=copy_and_archive)
startarchive_btn.pack(fill=X, anchor=W)

main_w.mainloop()