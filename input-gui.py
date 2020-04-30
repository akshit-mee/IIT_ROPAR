from tkinter import *
import serial
import time


#-----------------Bluetooth data transfer code--------------------------------#


def bluetooth_transfer():
    print("Start")
    port = " "#here you need to write the name of the hc05 driver something like tty in linux but in windows wrtite the path of device driver conneccted with bluetooth
    bluetooth = serial.Serial(port, 9600) #check all the baud values mainly 9600 might work tho
    print("Connected")
    print("Sending Data...")
    bluetooth.flushInput()
    bluetooth.write(str.encode(str(loc_data)))
    time.sleep(2)
    blutooth.close()
    print("Done")

#------------------End--------------------------------------------------------#


root = Tk()
root.title("Upload Data")
root.geometry("500x400")

wardno = StringVar()
roomno = StringVar()
bedno = StringVar()

ward = Entry(root, textvariable = wardno)
room = Entry(root, textvariable = roomno)
bed = Entry(root, textvariable = bedno)

ward.place(relx = 1/7, rely = 0.5, width = 50)
room.place(relx = 3/7, rely = 0.5, width = 50)
bed.place(relx = 5/7, rely = 0.5, width = 50)

locdata=[]

def get_values():
    wardnum = wardno.get()
    roomnum = roomno.get()
    bednum = bedno.get()
    locdata = [int(wardnum),int(roomnum),int(bednum)]
    
def callback():
    get_values()
    bluetooth_transfer()

subbtn = Button(root, text = "Submit", command = callback)
subbtn.place(relx = 1/3, rely = 0.75, height = 70, width = 170)


root.mainloop()
