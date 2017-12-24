import os
from termcolor import colored
import time

print(colored('''


 _______  _______  _______  __    _  __   __  _______  __   __
|       ||       ||       ||  |  | ||  | |  ||  _    ||  |_|  |
|   _   ||    _  ||    ___||   |_| ||  |_|  || |_|   ||       |
|  | |  ||   |_| ||   |___ |       ||       ||       ||       |
|  |_|  ||    ___||    ___||  _    ||       ||  _   |  |     |
|       ||   |    |   |___ | | |   | |     | | |_|   ||   _   |
|_______||___|    |_______||_|  |__|  |___|  |_______||__| |__|
 _______  _______  _______  __   __  _______
|       ||       ||       ||  | |  ||       |
|  _____||    ___||_     _||  | |  ||    _  |
| |_____ |   |___   |   |  |  |_|  ||   |_| |
|_____  ||    ___|  |   |  |       ||    ___|
 _____| ||   |___   |   |  |       ||   |
|_______||_______|  |___|  |_______||___|



A Script to Automate the Deployment of OpenVBX Phone Servers


By the Technology Action Project
https://techaction.io

-----------------------------------------------------------------
''', 'yellow', attrs=['bold']))



print('\n')
print(colored('[*] Updating System, Installing PHP 5.6 and Other Dependencies', 'yellow', attrs=['bold']))
print('\n')
os.system('sudo apt update && sudo apt upgrade -y')
os.system('''sudo apt-get purge `dpkg -l | grep php| awk '{print $2}' |tr "\n" " "`''')
os.system('sudo apt-get install software-properties-common')
os.system('sudo add-apt-repository ppa:ondrej/php')
os.system('sudo apt-get update')
os.system('sudo apt-get install php5.6')
os.system('sudo apt-get install mysql-server apache2 libapache2-mod-php5.6 php5.6-mysql php5.6-curl sendmail')

print('\n')
print(colored('[*] Creating Databases', 'yellow', attrs=['bold']))
print('\n')
dbpass = input(colored('Password for OpenVBX database: ', 'green'))
print('\n')
print(colored('[*] Remember username and password for database to use during post installation setup', 'red', attrs=['bold']))
print('\n')
print(colored('[*] Setting Up Database...', 'yellow', attrs=['bold']))
print('\n')
mysql_cmd = 'echo "CREATE DATABASE OpenVBX; GRANT ALL PRIVILEGES ON OpenVBX.* TO ' + user + '@localhost IDENTIFIED BY ' + dbpass + '; FLUSH PRIVILEGES" | sudo mysql -p'
os.system('sudo ' + mysql_cmd)
print('\n')

print(colored('[*] Clearing Webroot and Installing OpenVBX', 'yellow', attrs=['bold']))
print('\n')
os.system('sudo rm -rf /var/www/html/*')
os.system('git clone https://github.com/techaction/OpenVBX.git')
os.system('sudo cp -r OpenVBX/* /var/www/html')
os.system('sudo chmod 777 -Rf /var/www/html/OpenVBX/config')
os.system('sudo chmod 777 -Rf /var/www/html/OpenVBX/audio-uploads')
print('\n')
print(colored('[*] Restarting Apache Server', 'yellow', attrs=['bold']))
print('\n')
os.system('sudo service apache2 restart')
print('\n')
print(colored('[+] Installation Complete!', 'yellow', attrs=['bold']))
