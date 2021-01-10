# Autor: Samuel Silva
# Date: 8/1/2021
# App: Investent manager
# Version: 0.0
 
 
MENU = """
	 ----------------
	       MENU
	 -----------------

	 1 -- Deposit
	 2 -- Extract
	 3 -- Calculate
	 4 -- View Balance

	 -----------------"""

def get_Menu(menu = MENU): 

	print(menu)

	return action_Menu(int(input()))


def action_Menu(action : int):

	if action == 1:
		pass
	elif action == 2:
		pass
	elif action == 3:
		print(percentage_increase(50, 1.5))
	else: 
		pass




get_Menu()

