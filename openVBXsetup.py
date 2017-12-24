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
print(colored('[*] Creating Non-Root User', 'yellow', attrs=['bold']))
print('\n')
user = input(colored('Name of new non-root user: ', 'green'))
print('\n')
os.system('sudo useradd -m ' + user )
os.system('sudo passwd ' + user)
os.system('sudo usermod -a -G sudo ' + user)
print('\n')
print(colored('[*] User Created and Added To Sudo', 'yellow', attrs=['bold']))

print('\n')
print(colored('[*] Updating System, Installing PHP 5.6 and Other Dependencies', 'yellow', attrs=['bold']))
print('\n')
os.system('su ' + user + ' -c "sudo apt update && sudo apt upgrade -y"')
os.system('su ' + user + ''' -c "sudo apt-get purge `dpkg -l | grep php| awk '{print $2}' |tr "\n" " "`''')
os.system('su ' + user + ' -c "sudo apt-get install software-properties-common"')
os.system('su ' + user + ' -c "sudo add-apt-repository ppa:ondrej/php"')
os.system('su ' + user + ' -c "sudo apt-get update"')
os.system('su ' + user + ' -c "sudo apt-get install php5.6"')
os.system('su ' + user + ' -c "sudo apt-get install mysql-server apache2 libapache2-mod-php5.6 php5.6-mysql php5.6-curl sendmail"')

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
os.system('su ' + user + ' -c "' + mysql_cmd + '"')
print('\n')

print(colored('[*] Clearing Webroot and Installing OpenVBX', 'yellow', attrs=['bold']))
print('\n')
os.system('su ' + user + ' -c "sudo rm -rf /var/www/html/*"')
os.system('su ' + user + ' -c "git clone https://github.com/techaction/OpenVBX.git"')
os.system('su ' + user + ' -c "sudo cp -r OpenVBX/* /var/www/html"')
os.system('su ' + user + ' -c "sudo chmod 777 -Rf /var/www/html/OpenVBX/config"')
os.system('su ' + user + ' -c "sudo chmod 777 -Rf /var/www/html/OpenVBX/audio-uploads"')
print('\n')
print(colored('[*] Restarting Apache Server', 'yellow', attrs=['bold']))
print('\n')
os.system('su ' + user + ' -c "sudo service apache2 restart"')
print('\n')
print(colored('[+] Installation Complete!', 'yellow', attrs=['bold']))
