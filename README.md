# stem-python-ev3dev2
Installation guide and educational samples


## PuTTY
https://the.earth.li/~sgtatham/putty/latest/w64/putty-64bit-0.73-installer.msi

## Connecting
Connect with USB.

Wait until EV3 defined as NDIS device in computer network settings.

Share primary connection to EV3 connection. It would recieve IP like 192.168.*.*

Connect with PuTTY or some other SSH client.

## Share EV3 
Download ngrok for Linux (ARM).

`wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.zip`

Install it with official instruction. 

https://dashboard.ngrok.com/get-started

Start ngrok

`./ngrok tcp 22`

Now can conntect from any device with SSH using provided IP and port like

`0.tcp.ngrok.io:10050`

## To install
man
htop
