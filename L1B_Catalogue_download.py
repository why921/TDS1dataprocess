from ftplib import FTP
import os


#########################################
###############L1B_Catalogue#############
#########################################


Year='2018'
Month='12'
Day='01'
Product='H12'


destdir='E:\GNSSR_DATA\TDS-1\L1B_Catalogue\\'+Year+'-'+Month+'\\'+Day+'\\'+Product
directory = '/Data/L1B_Catalogue/'+Year+'-'+Month+'/'+Day+'/'+Product

if not os.path.isdir(destdir):
	os.makedirs(destdir)

#Registration：http://merrbys.co.uk/data-access/registration
userName = ''
passWord = ''

ftpdir = 'ftp.merrbys.co.uk'


#Connect and log in to the FTP
print('Logging in')

ftp = FTP(ftpdir)
ftp.login(user=userName, passwd = passWord) 

# Change to the directory where the files are on the FTP
print('Changing to '+ directory)
ftp.cwd(directory)
# Get a list of the files in the FTP directory
files = ftp.nlst()
#files = files[1:2]
print(files)

os.chdir(destdir)


for file in files:
    print('Downloading...' + file)
    print(ftp.size(file))
    ftp.retrbinary('RETR ' + file, open(file, 'wb').write)

ftp.quit()



