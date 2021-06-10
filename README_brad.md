# Brad's Notes

### Paths
* Chia.exe location: `C:\Users\b\AppData\Local\chia-blockchain\app-1.1.7\resources\app.asar.unpacked\daemon`
* Python location: `C:\Users\b\AppData\Local\Programs\Python\Python39\`
* Config: 
* Debug: 

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

## Set logs to INFO

## View logs
```
cat "C:\Users\b\.chia\mainnet\log\debug.log" | grep 192.168.86.28
```

## Run the GUI
```
cd ~/chia-blockchain/chia-blockchain-gui
npm run electron &
```

## PSChiaPlotter
* [PSChiaPlotter](https://github.com/MrPig91/PSChiaPlotter)
* [YouTube Video](https://www.youtube.com/watch?v=txUmNYhTfD4)
```
Get-ChiaPlottingStatistics
```
### Executiy Policy Error
```
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope CurrentUser
```
### Usage
```
# List all
Get-ChiaPlottingStatistic | sort Time_Started -Descending

# Get recent plots
Get-ChiaPlottingStatistic | sort Time_Started -Descending | select -First 20

# Get Plot average
Get-ChiaPlottingStatistic | measure -Average -Property phase_1_sec
# Convert seconds to minutes
[seconds] / 60
```
