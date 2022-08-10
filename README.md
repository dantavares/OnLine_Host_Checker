# OnLine Host Checker
Python script that checks if your host is online based on its service port, and send in your Telegram if the service is online or offline.

## Requirements
- python3
- nmap

## Usage
Edit "bot_file.yml" and supply your Telegram Bot Token and ChatID
Example:
```
botok:  '5476678767:AAFDFW43dp9L4oWYQuZRzXfFDKs11aOD8v5'
chatid: '-1001691246687'
```

Edit "esc_file.yml" and insert your hosts to check and service port. Always follow the above format!
Example:
```
- - Google
  - google.com
  - 443
  - 0
- - Yahoo
  - yahoo.com
  - 443
  - 0
```
The Format
```
- - Service Name
  - host
  - host port (ssh= 22, https: 443, ftp: 21 etc)
  - OffLine Flag (0 if Online, 1 if Offline)
```

Offline flag is aways "0" and the scritp changes if got offline and back online.

### Executing
```
python3 ckonline -T <TIME> -v <Verbose On> -h <HELP!> --notelegram <Disable Telegram MSG> 
```
#### Parameters
-T <TIME>
Time defined by nmap to wait a host response, default is T3, can be:
```
T0 = Insane
T1 = Agressive
T2 = Gentle
T3 = Default
```
Example:
