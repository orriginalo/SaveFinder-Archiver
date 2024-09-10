import os
import shutil
import zipfile
import configparser
from rich import print
from rich.console import Console
import string
from ctypes import windll
import time

config: any

steam_path: str
doc_path: str
appdata_path: str



gameCounter = 0
games_saves_paths = []

def first_run():
	if os.path.exists("config.ini"):
		pass
	else:
		with open('config.ini', 'w') as configfile:
				config_data = {
		'BASE PATHS': {
				'steam_path': '',
    		'steam_path_1': '',
				'steam_path_2': '',
				'steam_path_3': '',
				'steam_path_4': '',
				'documents_path': '',
				'appdata_path': ''
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

def get_drives():
		drives = []
		bitmask = windll.kernel32.GetLogicalDrives()
		for letter in str(string).upper():
				if bitmask & 1:
						drives.append(letter)
				bitmask >>= 1
		drives.pop(0)
		return drives

def print_detected(game:str, root:str, dirname:str):
	global gameCounter
	gameCounter += 1
	if game == "Project Zomboid":
		print(f"[bold white]{gameCounter}. [bold blue]{game} detected![bold white][italic] In:", fR"[italic]C:\Users\{os.getlogin()}\Zomboid")
		games_saves_paths.append(fR"C:\Users\{os.getlogin()}\Zomboid")
	else:
		print(f"[bold white]{gameCounter}. [bold blue]{game} detected![bold white][italic] In:", f" [italic]{os.path.join(root, dirname)} ")
		games_saves_paths.append(os.path.join(root, dirname))
 
def print_from_cfg(game:str, path_name:str):
	global gameCounter
	gameCounter += 1
	path = config.get('GAME PATHS', path_name)
	print(f"[bold white]{gameCounter}. [bold blue]{game}")
	games_saves_paths.append(path)

def copy_and_archive(source:str, destination:str):
	shutil.copytree(source, destination, dirs_exist_ok=True)
	shutil.make_archive(destination, 'zip', destination)
	shutil.rmtree(destination)

def find_def_paths():
	print("\n=== Finding base paths... ===")
	if config.get('BASE PATHS', 'steam_path') != '' and config.get('BASE PATHS', 'documents_path') != '' and config.get('BASE PATHS', 'appdata_path') != '':
		print("[bold green]Extracting base paths from cfg...")
		return config.get('BASE PATHS', 'steam_path'), config.get('BASE PATHS', 'documents_path'), config.get('BASE PATHS', 'appdata_path')
	else:
		for dirpath, dirnames, filenames in os.walk("C:\\"):
			for dirname in dirnames:
				if dirname == "Steam" and any(file == "steam.exe" for file in os.listdir(os.path.join(dirpath, dirname))):
					steam_path = os.path.join(dirpath, dirname)
					config.set('BASE PATHS', 'steam_path', steam_path)
					print(f"[bold green]Steam folder detected![bold white][italic] In:", f"[italic]{os.path.join(dirpath, dirname)}")
				if dirname == "Documents" and os.path.join(dirpath, dirname) == f"C:\\Users\\{os.getlogin()}\\Documents":
					doc_path = os.path.join(dirpath, dirname)
					config.set('BASE PATHS', 'documents_path', doc_path)
					print(f"[bold green]Documents folder detected![bold white][italic] In:", f"[italic]{os.path.join(dirpath, dirname)}")
				if dirname == "AppData" and os.path.join(dirpath, dirname) == f"C:\\Users\\{os.getlogin()}\\AppData":
					appdata_path = os.path.join(dirpath, dirname)
					config.set('BASE PATHS', 'appdata_path', appdata_path)
					print(f"[bold green]AppData folder detected![bold white][italic] In:", f"[italic]{os.path.join(dirpath, dirname)}")
		
		global steam_path_1 , steam_path_2, steam_path_3, steam_path_4
		
		steam_count = 0
		print("[bold]Finding other Steams on other drives...")
		for disk in get_drives():
			if os.path.exists(f"{disk}:\\SteamLibrary"):
				steam_count += 1
				match steam_count:
					case 1:
						steam_path_1 = f"{disk}:\\SteamLibrary"
					case 2:
						steam_path_2 = f"{disk}:\\SteamLibrary"
					case 3:
						steam_path_3 = f"{disk}:\\SteamLibrary"
					case 4:
						steam_path_4 = f"{disk}:\\SteamLibrary"
				print(f"[bold green]Steam folder {steam_count} detected![bold white][italic] In:", f"[italic]{f'{disk}:\\SteamLibrary'}")
				config.set('BASE PATHS', f'steam_path_{steam_count}', f'{disk}:\\SteamLibrary')
			
			
			# for dirpath, dirnames, filenames in os.walk(f"{disk}:\\"):
			# 	for dirname in dirnames:
			# 		if dirname == "SteamLibrary" and any(file == "steam.dll" for file in os.listdir(os.path.join(dirpath, dirname))):
			# 			steam_count += 1
			# 			match steam_count:
			# 				case 1:
			# 					steam_path_1 = os.path.join(dirpath, dirname)
			# 				case 2:
			# 					steam_path_2 = os.path.join(dirpath, dirname)
			# 				case 3:
			# 					steam_path_3 = os.path.join(dirpath, dirname)
			# 				case 4:
			# 					steam_path_4 = os.path.join(dirpath, dirname)
			# 			print(f"[bold green]Steam folder {steam_count} detected![bold white][italic] In:", f"[italic]{os.path.join(dirpath, dirname)}")
			# 			config.set('BASE PATHS', f'steam_path_{steam_count}', os.path.join(dirpath, dirname))
			# 			break
			# 	else:
			# 		continue
			# 	break
					
		with open('config.ini', 'w') as configfile:
			config.write(configfile)
				
				
	print("=== [bold green]Done![/bold green] ===\n")
	
	return steam_path, doc_path, appdata_path


def check_def_paths(steam_path, doc_path, appdata_path):
	
	#TODO : Добавить поддержку :
	# 1. Minecraft
	
	print("--- Finding [bold white]GAMES SAVES [/bold white]paths... ---")
	
	if config.get('GAME PATHS', 'deadcells_path') == '':
		for root, dirs, files in os.walk(steam_path): # Поиск в директории Steam -------------------
			for dirname in dirs:
					match(dirname):
						case "588650": # Код игры в Steam
							print_detected("DeadCells", root, dirname)
							config.set('GAME PATHS', 'deadcells_path', os.path.join(root,dirname))
	else:
		print_from_cfg("DeadCells", "deadcells_path")
							
	if config.get('GAME PATHS', 'terraria_path') == '':
		for root, dirs, files in os.walk(doc_path): # Поиск в директории документы -------------------
			for dirname in dirs:
					match(dirname):
						case "Terraria":
							print_detected("Terraria", root, dirname)
							config.set('GAME PATHS', 'terraria_path', os.path.join(root,dirname))
	else:
		print_from_cfg("Terraria", "terraria_path")
		
	if config.get('GAME PATHS', 'stormworks_path') == '' or config.get('GAME PATHS', 'geometrydash_path') == '' or config.get('GAME PATHS', 'ftl_path') == '' or config.get('GAME PATHS', 'rimworld_path') == '' or config.get('GAME PATHS', 'stardew_path') == '':
		for root, dirs, files in os.walk(appdata_path): # Поиск в директории AppData -------------------
			for dirname in dirs:
					match(dirname):
						
						case "Stormworks":
							print_detected("Stormworks", root, dirname)
							config.set('GAME PATHS', 'stormworks_path', os.path.join(root,dirname))
							
						case "GeometryDash":
							print_detected(r"Geometry Dash", root, dirname)
							config.set('GAME PATHS', 'geometrydash_path', os.path.join(root,dirname))
			 
						case "FasterThanLight":
							print_detected(r"FTL: Faster Than Light", root, dirname)
							config.set('GAME PATHS', 'ftl_path', os.path.join(root,dirname))

						case "RimWorld" | "RimWorld by Ludeon Studios":
							if "Temp" not in os.path.join(root,dirname):
								print_detected("RimWorld", root, dirname)
								config.set('GAME PATHS', 'rimworld_path', os.path.join(root,dirname))
        
						case "StardewValley":
							print_detected("Stardew Valley", root, dirname)
							config.set('GAME PATHS', 'stardew_path', os.path.join(root,dirname))
	else:
		# print("[bold blue]Extracting gamesaves paths from cfg...[/bold blue]\n")
		print_from_cfg("Stormworks", "stormworks_path")
		print_from_cfg("Geometry Dash", "geometrydash_path")
		print_from_cfg("FTL: Faster Than Light", "ftl_path")
		print_from_cfg("RimWorld", "rimworld_path")
	
	if config.get("GAME PATHS", "zomboid_path") == '':
		if os.path.exists(f"C:\\Users\\{os.getlogin()}\\Zomboid"):
				print_detected("Project Zomboid", root, dirname)
				config.set('GAME PATHS', 'zomboid_path', f"C:\\Users\\{os.getlogin()}\\Zomboid")
	else:
		print_from_cfg("Project Zomboid", "zomboid_path")
	if games_saves_paths == []:
		print("[bold red]Gamesaves paths not found")
		input("Press Enter to exit...")
		exit()
	with open('config.ini', 'w') as configfile:
			config.write(configfile)
	
def get_save_saves():
	print("\n")
	saveSaves: list = []
	saveNumbers: list = list(input("Введите числа которые вы хотите сохранить: ").split())

	saveNumbers = [int(el) for el in saveNumbers if isinstance(el, str) and el.isdigit()]

	while (0 in saveNumbers) or (len(saveNumbers) != len(set(saveNumbers))) or (max(saveNumbers) > len(games_saves_paths)):
		print("[bold red]Некорректные числа")
		saveNumbers = list(input("Введите числа которые вы хотите сохранить: ").split())
		saveNumbers = [int(el) for el in saveNumbers if isinstance(el, str) and el.isdigit()]

	for el in saveNumbers: # Получаем пути до сохранений игр по номерам
		saveSaves.append(games_saves_paths[int(el)-1])
	print("----------------------[bold white]\nК сохранению: ")
	for el in saveSaves:
		print(os.path.basename(el))
	print("----------------------")
	def answerr():
		answer = str(Console().input("\nВведите [[green]y[/green]/[red]n[/red]]: "))
		match(answer.lower()):
			case "y" | "yes":
				print("\n")
				for el_path in saveSaves:
					print(f"[bold green]Копирование и архивация {os.path.basename(el_path)}...", end= "")
					copy_and_archive(el_path, ".\\Archivated\\" + os.path.basename(el_path) + ".zip")
					print(f"[bold green] DONE!")
				print("\nКопирование и архивация файлов завершена!")
			case "n" | "no":
				exit() # Выход
			case _:
				print("[bold red]Некорректный ввод") 
				answerr()
	answerr()
	
	return saveSaves



def main():
	first_run()
 
	configg = configparser.ConfigParser()
	configg.read("config.ini")

	lang = configg["SETTINGS"]["lang"]
	global config
	config = configg
	steam_path, doc_path, appdata_path = find_def_paths()
	
	check_def_paths(steam_path, doc_path, appdata_path)
	
	get_save_saves()

	input("Нажмите Enter для выхода...")

if __name__ == "__main__":
	main()