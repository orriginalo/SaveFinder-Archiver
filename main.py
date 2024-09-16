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
										games_saves_paths.append(os.path.join(root, dirname))
										config.set('GAME PATHS', self.cfg_name, os.path.join(root, dirname))
										with open('config.ini', 'w') as configfile:
											config.write(configfile)
										break 
							else:
								if any(file == self.file_in for file in os.listdir(os.path.join(root, dirname))): # if file_in == "steam.exe"
									gameCounter += 1
									print(f"[bold white]{gameCounter}. [bold blue]{self.name} detected![bold white][italic] In:", f"{os.path.join(root, dirname)}")
									games_saves_paths.append(os.path.join(root, dirname))
									config.set('GAME PATHS', self.cfg_name, os.path.join(root, dirname))
									with open('config.ini', 'w') as configfile:
										config.write(configfile)
									break 
						else:
							if self.exception_in_path != None:
								if self.exception_in_path not in os.path.join(root, dirname):
									gameCounter += 1
									print(f"[bold white]{gameCounter}. [bold blue]{self.name} detected![bold white][italic] In:", f"{os.path.join(root, dirname)}")
									games_saves_paths.append(os.path.join(root, dirname))
									config.set('GAME PATHS', self.cfg_name, os.path.join(root, dirname))
									with open('config.ini', 'w') as configfile:
										config.write(configfile)
									break 
							else:
								gameCounter += 1
								print(f"[bold white]{gameCounter}. [bold blue]{self.name} detected![bold white][italic] In:", f"{os.path.join(root, dirname)}")
								games_saves_paths.append(os.path.join(root, dirname))
								config.set('GAME PATHS', self.cfg_name, os.path.join(root, dirname))
								with open('config.ini', 'w') as configfile:
									config.write(configfile)
								break
		else:
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
				'satisfactory_path': ''
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


def copy_and_archive(source:str, destination:str):
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
 
	# mgs = game("MGS", "MGS", appdata_path, "mgs_path")
	# mgs.find_game()
 
	# deadcells = game("Dead Cells", "DeadCells", appdata_path, "deadcells_path")
	# deadcells.find_game()
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