# Brad's Notes
### Useful Links
* [Raspberry Pi as Harvester](https://medium.com/geekculture/how-to-use-your-raspberry-pi-as-a-chia-harvester-66440c17d318).
* [Farming on multiple systems](https://www.youtube.com/watch?v=QpgXr3aeU5g)

## SSH - Windows to Linux
1. Install SSH on Linux machine
```
sudo apt install openssh-server
```
2. From Windows machine, using PowerShell enter
```
ssh [username]@[computer-name-or-ip-address]

# Example
ssh bharvest@192.168.86.28
```

## Start Harvester
Use the `-r` flag to restart the harvester service.
```
cd ~/chia-blockchain
. ./activate
chia start harvester
```

## Add Plot Directory
```
chia plots add -d [path-to-plot-directory]

# Example
chia plots add -d /media/bharvest/Chia1
```

## Run the GUI
```
cd ~/chia-blockchain/chia-blockchain-gui
npm run electron &
```

