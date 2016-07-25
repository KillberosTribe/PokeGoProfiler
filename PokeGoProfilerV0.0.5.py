import win32api
import win32com.client
import win32gui
import time
import StringIO

print("Credits to Stefan2142. Edited by KillberosTribe")
print("For PokeGoBot V0.0.5")
print("")
print("")
run = raw_input("Create profile or run profile? (create/run): ")
run = run.lower()

while run != "run":
        print("Creating profile")
        filename = raw_input("Enter profile name: ")
        filename = filename + '.txt'
        print("Looks like: C:\Users\Stefan\Documents\GO.Bot.v0-0-4\GO Bot.exe")
        location = raw_input("Enter the location of the file: ")
        username = raw_input("Enter username: ")
        password = raw_input("Enter password: ")
        latitude = raw_input("Enter latitude: ")
        longitude = raw_input("Enter longitude: ")
        altitude = raw_input("Enter altitude (default is 10): ")
        evolve = raw_input("Enable auto-evolve? (y/n): ")
        duplicate = raw_input("Enable transfer duplicates? (y/n): ")
        evolve = evolve.lower()
        duplicate = duplicate.lower()
        location = 'cmd /K "' + location + '"'

        filez = open(filename, 'w')
        filez.write(location + '\n')
        filez.write(username + '\n')
        filez.write(password + '\n')
        filez.write(latitude + '\n')
        filez.write(longitude + '\n')
        filez.write(altitude + '\n')
        filez.write(evolve + '\n')
        filez.write(duplicate + '\n')
        filez.close()
        
        print("profile created...")
        print("")
        print("")
        run = raw_input("Create profile or run profile? (create/run): ")
        run = run.lower()

if run == "run":
        what = raw_input("Enter profile name (CASE SENSITIVE): ")
        what = what + '.txt'
        filez = open(what, 'r')
        profile = filez.readlines()
        filez.close()

        location = profile[0].rstrip('\n')
        username = profile[1].rstrip('\n')
        password = profile[2].rstrip('\n')
        latitude = profile[3].rstrip('\n')
        longitude = profile[4].rstrip('\n')
        altitude = profile[5].rstrip('\n')
        evolve = profile[6].rstrip('\n')
        duplicate = profile[7].rstrip('\n')

	shell = win32com.client.Dispatch("WScript.Shell")
	shell.Run(location)

	win32api.Sleep(100)
	
	win32api.Sleep(4000)
	hwnd= win32gui.FindWindow(0,'GO Bot v0.0.5 (BETA)')


	win32gui.SetForegroundWindow(hwnd)
	shell.SendKeys("{TAB}")
	win32api.Sleep(300)
	shell.SendKeys("{RIGHT}")
	win32api.Sleep(300)
	shell.SendKeys("{TAB}")
	win32api.Sleep(300)
        shell.SendKeys("^a")
	win32api.Sleep(300)
	shell.SendKeys("{BACKSPACE}")
	win32api.Sleep(300)
	shell.SendKeys(str(username))
	win32api.Sleep(300)
	shell.SendKeys("{TAB}")
	win32api.Sleep(300)
	shell.SendKeys("^a")
	win32api.Sleep(300)
	shell.SendKeys("{BACKSPACE}")
	win32api.Sleep(300)
	shell.SendKeys(str(password))
	win32api.Sleep(300)
	shell.SendKeys("{TAB}")
	win32api.Sleep(300)
	shell.SendKeys("^a")
	win32api.Sleep(300)
	shell.SendKeys("{BACKSPACE}")
	win32api.Sleep(300)
	shell.SendKeys(str(latitude))
	win32api.Sleep(300)
	shell.SendKeys("{TAB}")
	win32api.Sleep(300)
	shell.SendKeys("^a")
	win32api.Sleep(300)
	shell.SendKeys("{BACKSPACE}")
	win32api.Sleep(300)
	shell.SendKeys(str(longitude))
	win32api.Sleep(300)
	shell.SendKeys("{TAB}")
	win32api.Sleep(300)
	shell.SendKeys("^a")
	win32api.Sleep(300)
	shell.SendKeys("{BACKSPACE}")
	win32api.Sleep(300)
	shell.SendKeys(str(altitude))
	win32api.Sleep(300)
	shell.SendKeys("{TAB}")
	win32api.Sleep(300)
	shell.SendKeys("{TAB}")
	win32api.Sleep(300)
	shell.SendKeys("{TAB}")
	win32api.Sleep(300)
	shell.SendKeys("{TAB}")
	win32api.Sleep(300)
	if evolve == 'y':
                shell.SendKeys("{SPACE}")
                win32api.Sleep(300)
                shell.SendKeys("{TAB}")
                win32api.Sleep(300)
        else:
                shell.SendKeys("{TAB}")
                win32api.Sleep(300)
        if duplicate == 'n':
                shell.SendKeys("{SPACE}")
                win32api.Sleep(300)
                shell.SendKeys("{TAB}")
                win32api.Sleep(300)
        else:
                shell.SendKeys("{TAB}")
                win32api.Sleep(300)
                
	
	
	win32api.Sleep(2000)
	shell.SendKeys("{TAB}{TAB}{TAB}")
	shell.SendKeys("{LEFT}")
	shell.SendKeys("{TAB}")


	shell.SendKeys("{ENTER}") #Start Go BOt

        win32api.Sleep(4000) #Wait for cmd to switch back to and close (milliseconds)
	shell.SendKeys("exit {ENTER}") #Send Exit command
