# poor man's host agent

A inventory script to collect hardware information of the current local host to TXT file.
Works on MS Windows semi-automatically and offline.
Intended to build up a initial hosts hardware inventory for your CMDB, without deploying software agents to every machine

## Build

Create a standalone portable .EXE file with
```
cd 'C:\Users\myself\AppData\Roaming\Python\Python39\Scripts\dist'
.\pyinstaller.exe --onefile 'C:\Users\myself\workspace\localhost inventory\main.py'
```
Copy resulting main.exe to your USB-Drive and optionally to be invoked at USB mount, copy the `autorun.inf` to the disk as well.

Feel free to fork and adapt to your own requirements to buildup a first machine repository of your organisation!

