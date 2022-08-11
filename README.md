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

Offline flag is aways "0" and the scritp changes if is offline and back online.

### Executing
```
python3 ckonline.py -T <TIME> -v <Verbose On> -h <HELP!> --notelegram <Disable Telegram MSG> -t <Tries>
```
#### Parameters

##### -T <TIME> - Time defined by nmap to wait a host response, default is T3, can be:
```
T0 = Insane
T1 = Agressive
T2 = Gentle
T3 = Default
```
Example:
```
python3 ckonline.py -T T1
```
##### -v Verbose On - Aways tell you if the hosts is online or offline. By default, the scrit only send notification if the status changes.
##### --notelegram - Do not send telegram msg, only stout
##### -t Tries - Number of tries before send offline message. Default 1 try
Example tries 2 times:
```
python3 ckonline.py -t 2
```

## Pratical Usage
Example 1 Crontab:
```
*/20 * * * * python3 /home/admin/ckonline/ckonline.py >> /tmp/ckonline_log.txt
```
This example, scritp on folder "/home/admin/ckonline" check every 20 minutes and send stdout on logfile

Example 2 on a php file:
```
<?php
    echo '<!DOCTYPE html> <html> <head> <meta name="viewport" content="width=device-width, initial-scale=1.0"> </head> <body>';
    echo "<pre>".shell_exec("python3 /home/admin/ckonline/ckonline.py --notelegram -v 2>&1")."<pre>";
?>
```
This example lists the state and all hosts and shows it through a web page (apache server). Don't forget to give write permissions (user www-data) to the file 'esc_file.yml'.
