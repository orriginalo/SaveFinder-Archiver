import os
import configparser
import shutil
from rich.console import Console
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

class game():
	def __init__(self, name, folder_name, where_search_path, cfg_name, file_in: str = None, exception_in_path: str = None, second_folder_name: str = None, folder_in_path: str = None):
		self.folder_name = folder_name
		self.second_folder_name = second_folder_name
		self.path = where_search_path
		self.cfg_name = cfg_name
		self.name = name
		self.file_in = file_in
		self.exception_in_path = exception_in_path
		self.folder_in_path = folder_in_path	

	def game_found(self, root, dirname):
		global gameCounter
		gameCounter += 1
		print(f"[bold white]{gameCounter}. [bold blue]{self.name} detected![bold white][italic] In:", f"{os.path.join(root, dirname)}")
		games_saves_paths.append(os.path.join(root, dirname))
		config.set('GAME PATHS', self.cfg_name, os.path.join(root, dirname))
		with open('config.ini', 'w') as configfile:
			config.write(configfile)

	def find_game(self):
		global gameCounter
		if (config.get('GAME PATHS', self.cfg_name) == '' or (not os.path.exists(config.get('GAME PATHS', self.cfg_name)))):
			for root, dirs, files in os.walk(self.path):
				for dirname in dirs:
					if dirname == self.folder_name or dirname == self.second_folder_name:
						if self.folder_in_path != None:
							if self.file_in != None: # Если file_in не None
								if self.exception_in_path != None: # Если exception_in_path не None
									if any(file == self.file_in for file in os.listdir(os.path.join(root, dirname))): # if file_in == "steam.exe"
										if self.exception_in_path not in os.path.join(root, dirname):
											if self.folder_in_path in os.path.join(root, dirname):
												self.game_found(root, dirname)
												break 
								else:
									if any(file == self.file_in for file in os.listdir(os.path.join(root, dirname))): # if file_in == "steam.exe"
										if self.folder_in_path in os.path.join(root, dirname):
											self.game_found(root, dirname)
											break 
							else:
								if self.exception_in_path != None:
									if self.exception_in_path not in os.path.join(root, dirname):
										if self.folder_in_path in os.path.join(root, dirname):
											self.game_found(root, dirname)
											break 
								else:
									if self.folder_in_path in os.path.join(root, dirname):
										self.game_found(root, dirname)
										break
						else:
							if self.file_in != None: # Если file_in не None
								if self.exception_in_path != None: # Если exception_in_path не None
									if any(file == self.file_in for file in os.listdir(os.path.join(root, dirname))): # if file_in == "steam.exe"
										if self.exception_in_path not in os.path.join(root, dirname):
											self.game_found(root, dirname)
											break 
								else:
									if any(file == self.file_in for file in os.listdir(os.path.join(root, dirname))): # if file_in == "steam.exe"
										self.game_found(root, dirname)
										break 
							else:
								if self.exception_in_path != None:
									if self.exception_in_path not in os.path.join(root, dirname):
										self.game_found(root, dirname)
										break 
								else:
									self.game_found(root, dirname)
									break
		else:
			if config.get("GAME PATHS", self.cfg_name) != '' and os.path.exists(config.get("GAME PATHS", self.cfg_name)):
				gameCounter += 1
				games_saves_paths.append(config.get('GAME PATHS', self.cfg_name))

				print(f"[bold white]{gameCounter}. [bold blue]{self.name}[bold white][italic] In:", f"{config.get('GAME PATHS', self.cfg_name)}")


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
		'FOLDERS WITH GAMES': {
			'folder_1': '',
			'folder_2': '',
			'folder_3': '',
			'folder_4': '',
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
				'warframe_path': '',
				'drg_path': '',
				'drg_survivor_path': '',
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


def copy_and_archive(source:str, destination:str):
	current_datetime = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
	
	shutil.copytree(source, destination, dirs_exist_ok=True)
	shutil.make_archive(destination, 'zip', destination)
	shutil.rmtree(destination)

def get_save_saves():
	print("\n")
	saveSaves: list = []
	saveNumbers: list = list(input("Enter the numbers you want to save: ").split())

	saveNumbers = [int(el) for el in saveNumbers if isinstance(el, str) and el.isdigit()]

	while (0 in saveNumbers) or (len(saveNumbers) != len(set(saveNumbers))) or (max(saveNumbers) > len(games_saves_paths)):
		print("[bold red]Incorrect numbers")
		saveNumbers = list(input("Enter the numbers you want to save: ").split())
		saveNumbers = [int(el) for el in saveNumbers if isinstance(el, str) and el.isdigit()]

	for el in saveNumbers: # Получаем пути до сохранений игр по номерам
		saveSaves.append(games_saves_paths[int(el)-1])
	print("----------------------[bold white]\nTo save: ")
	for el in saveSaves:
		print(os.path.basename(el))
	print("----------------------")
	def get_answer():
		answer = str(Console().input("\nEnter [[green]y[/green]/[red]n[/red]]: "))
		match(answer.lower()):
			case "y" | "yes":
				print("\n")
				for el_path in saveSaves:
					print(f"[bold green]Copying and archiving {os.path.basename(el_path)}...", end= "")
					copy_and_archive(el_path, ".\\Archivated\\" + os.path.basename(el_path))
					print(f"[bold green] DONE!")
				print("\nCopying and archiving files is complete!")
			case "n" | "no":
				exit()
			case _:
				print("[bold red]Invalid input") 
				get_answer()
	get_answer()
	
	return saveSaves

def find_games():
 
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
 
	dont_starve_together = game("Don't Starve Together", "DoNotStarveTogether", documents_path, "dont_starve_together_path", exception_in_path="Agreements")
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
 
	warframe = game("Warframe", "Warframe", local_path, "warframe_path")
	warframe.find_game()

	drg_survivor = game("Deep Rock Gamactic: Survivor", "DRG_Survivor", locallow_path, "drg_survivor_path")
	drg_survivor.find_game()

	end = perf_counter()
 
	time = end - start
 
	print(f"\n=== Found {gameCounter} game saves paths in {time:.2f} seconds ===\n")
	# -------------- GAMES --------------
 
def main():
	first_run()
 
	configg = configparser.ConfigParser()
	configg.read("config.ini")

	# lang = configg["SETTINGS"]["lang"]
	global config
	config = configg
	
	find_games()
 
	get_save_saves()
	


if __name__ == "__main__":
	main()