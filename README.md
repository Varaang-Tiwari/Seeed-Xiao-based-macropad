# Seeed-Xiao-based-macropad
I've wanted a USB-C based macropad for a cheaper price than what any of the other pro micro USB C baords sp I've made this for the seeed xiao. It was a challenge as by using circuit python after uploading circuit python and the required libraries there was only 7Kb of memory left.


Steps:-
After getiing the Xiao on boot mode you can delete all the files on the drive named "arduino" (during boot mode the Xiao is detected as a normal drive on the computer, this is normal) and then drag the Circuit python (.uf2) file on the Xiao, It will reboot then the name of the drive would change to "circuitpy".
You can now delete all the files on the "circuitpy" drive apart from the .uf2 file and the lib folder. Now copy over the "adafruit_hid" to the lib folder, add the main.py on the main page of the drive. Your macropad should work now, If it doesnt then just reset the board once and then it should work.
