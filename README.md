# Remote Python Pop-Up

This is a script that lets you remotely trigger a pop-up by just running a script from a usb-stick.
Use it to prank your friends or colleagues

## Requirements:

- Receiving PC with Python3 installed (Windows, MacOs)
- Sending PC with Python3 installed
- USB-stick or something else to transfer files
- Both computers on the same network

## How to use it:
You put your desired receiver file on the USB-stick, put it in the receiver PC and run it by double clicking(on windows) or running it in a terminal. Wait a few seconds and a sender.py file will appear after it finishes (ca 5 seconds). Take the USB-stick out of the receiving pc and put it into the Sending PC. open the sender.py file in your editor of choice to change the message or just run it to send the message: CRITICAL ERROR: YOUR FILES ARE BEING DELETED .

the script automatically finds out the ip adress and puts it in the sender.py file so you just have to run it

Notes:
- make sure to eject the usb when using a mac i found it didnt work without ejecting
- i havent tried mac to mac communication i only tried mac to windows messages
