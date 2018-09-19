import pyautogui as ms
import time
for i in range(2):
		time.sleep(4)
		ms.moveTo(308, 271)
		ms.moveRel(0, 75)  # move mouse 10 pixels down
		ms.dragTo(1142, 325)
		ms.dragRel(0, 75)  # drag mouse 10 pixels down
	

	


#print(ms.position())
