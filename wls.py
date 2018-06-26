#!/usr/bin/python
import os, sys

###################################################################
###################################################################
####                                                           ####
####  createDomain Auxiliary Tool: Oracle WebLogic Server 12c  ####
####                                                           ####
###################################################################
###################################################################


# WLS Configuration
JDK_HOME    = '/ofmlv/jdk1.8.0_121'
ORACLE_HOME = '/uclick/mw/hjkim/wls12212'
WLS_HOME    = ORACLE_HOME + '/wlserver'
WLS_VER     = '12.2.1.2.0'
DOMAIN_NAME = 'wlsDom12212'
DOMAIN_HOME = '/uclick/mw/hjkim/domains'
LOG_HOME    = '/uclick/mw/hjkim/logs'

# Node Environment
HOST_NAME  = 'uclick'
START_MODE     = "prod"
#START_MODE     = "dev"

# Admin Server Configuration
ADMIN_SERVER   = 'AdminServer'
ADMIN_ADDRESS  = '192.168.0.106'
ADMIN_PORT     = '7200'
ADMIN_USER     = 'weblogic'
ADMIN_PASSWORD = 'weblogic1'

# Managed Server 1 Configuration
MG1_SERVER     = 'M1'
MG1_ADDRESS    = '192.168.0.106'
MG1_PORT       = '7203'


##############################################
##############################################
####                                      ####
####  If you create more Managed Servers  ####
####  Copy and Paste lines 50 to 53.      ####
####  And Go to line 232 and edit.        ####
####                                      ####
##############################################
##############################################

# Managed Server 2 Configuration
MG2_SERVER     = ''
#MG2_ADDRESS    = '192.168.0.106'
#MG2_PORT       = '7204'


print('#################################')
print('#### HELLO Create WLS Domain ####')
print('#################################')
print('')
print('')
print('# Check your WLS Domain Configuration')
print('ORACLE HOME : ' + ORACLE_HOME)
print('DOMAIN HOME : ' + DOMAIN_HOME + '/' + DOMAIN_NAME)
print('LOG HOME    : '    + LOG_HOME + '/' + DOMAIN_NAME)
print('')
print('# Admin Server Configuration')
print('ADMIN SERVER  : ' + ADMIN_SERVER)
print('ADMIN ADDRESS : ' + ADMIN_ADDRESS + ':' + ADMIN_PORT)
print('')
print('# Managed Server Configuration')
print('MANAGED SERVER         : ' + MG1_SERVER)
print('MANAGED SERVER ADDRESS : ' + MG1_ADDRESS + ':' + MG1_PORT)
if MG2_SERVER == '':
    print('')
else:
    print('MANAGED SERVER : ' + MG2_SERVER)
    print('ADMIN ADDRESS  : ' + MG2_ADDRESS + ':' + MG2_PORT)
    print('')


#########################################
#########################################
####                                 ####
####  Don't modify under this line!  ####
####                                 ####
#########################################
#########################################


# Read Template
selectTemplate('Basic WebLogic Server Domain',WLS_VER)
loadTemplates()
#readTemplate(WLS_HOME+'/common/templates/wls/wls.jar')

# Admin Server Name
cd('/Servers/AdminServer')
set('Name',ADMIN_SERVER )
cd('/Servers/'+ADMIN_SERVER)

# Admin Server ADDRESS & PORT
set('ListenAddress',ADMIN_ADDRESS)
set('ListenPort'   ,int(ADMIN_PORT))

# Admin Server SSL
cd('/Server/'+ADMIN_SERVER)
create(ADMIN_SERVER,'SSL')
cd('SSL/'+ADMIN_SERVER)
set('Enabled'                    , 'False')
set('HostNameVerificationIgnored', 'True')

# Admin Server Diagnostics Off
cd('/Server/' + ADMIN_SERVER)
create(ADMIN_SERVER,'ServerDiagnosticConfig')
cd('/Server/' + ADMIN_SERVER + '/ServerDiagnosticConfig/' + ADMIN_SERVER)
set('WldfDiagnosticVolume','Off')

# Admin Server Server Log
cd('/Server/'+ADMIN_SERVER)
create(ADMIN_SERVER,'Log')
cd('/Server/' + ADMIN_SERVER + '/Log/' + ADMIN_SERVER)
set('FileName'    ,LOG_HOME + '/' + DOMAIN_NAME + '/' + ADMIN_SERVER + '/wls/' + ADMIN_SERVER + '_%yyyy%_%MM%_%dd%.log')
set('FileCount'   ,30)
set('FileMinSize'  , 5000)
set('RotationTime' ,'23:59')
set('RotationType','byTime')
set('RotateLogOnStartup',false)
set('FileTimeSpan',24)
set('LoggerSeverity','Info')
set('LogFileSeverity','Info')
set('StdoutSeverity','Info')
set('DomainLogBroadcastSeverity','Off')

# Admin Server Access Log
cd('/Server/' + ADMIN_SERVER)
create(ADMIN_SERVER,'WebServer')
cd('/Server/' + ADMIN_SERVER + '/WebServer/' + ADMIN_SERVER)
create(ADMIN_SERVER,'WebServerLog')
cd('/Server/' + ADMIN_SERVER + '/WebServer/' + ADMIN_SERVER + '/WebServerLog/' + ADMIN_SERVER)
set("LoggingEnabled", true)
set('FileName'    ,LOG_HOME + '/' + DOMAIN_NAME + '/' + ADMIN_SERVER + '/wls/' + 'access_%yyyy%_%MM%_%dd%.log')
set('FileCount'   ,30)
set('FileMinSize'  , 5000)
set('RotationTime' ,'23:59')
set('RotationType','byTime')
set('LogFileFormat','extended')
set('ElfFields','date time cs-method cs-uri sc-status time-taken')
set('RotateLogOnStartup',false)
set('FileTimeSpan',24)

# Admin Server End


## WLS Domain Account
cd('/')
cd('Security/base_domain/User/weblogic')

set('Name',ADMIN_USER)
cmo.setPassword(ADMIN_PASSWORD)

# WLS Domain Options
setOption('ServerStartMode',START_MODE)
setOption('JavaHome',JDK_HOME)
setOption('OverwriteDomain', 'true')

# Create WLS Domain
print('Now Creating WLS Domain!')
print('Please wait a moment.')
writeDomain(DOMAIN_HOME + '/' + DOMAIN_NAME)
closeTemplate()
#exit()


##################################################################################
##################################################################################
####                                                                          ####
####  From this line, It is beggining that Create Managed Server in Offline.  ####
####                                                                          ####
##################################################################################
##################################################################################

# Read Domain
print('# Load WLS Domain')
readDomain(DOMAIN_HOME + '/' + DOMAIN_NAME)

# Creating Managed Server 1
cd('/')
create(MG1_SERVER, 'Server')
cd('Server/' + MG1_SERVER)
set('ListenAddress',MG1_ADDRESS)
set('ListenPort',int(MG1_PORT))

# Managed Server 1 Diagnostics Off
cd('/Server/' + MG1_SERVER)
create(MG1_SERVER,'ServerDiagnosticConfig')
cd('/Server/' + MG1_SERVER + '/ServerDiagnosticConfig/' + MG1_SERVER)
set('WldfDiagnosticVolume','Off')

# Managed Server 1 Server Log
cd('/Server/'+MG1_SERVER)
create(MG1_SERVER,'Log')
cd('/Server/' + MG1_SERVER + '/Log/' + MG1_SERVER)
set('FileName'    ,LOG_HOME + '/' + DOMAIN_NAME + '/' + MG1_SERVER + '/wls/' + MG1_SERVER + '_%yyyy%_%MM%_%dd%.log')
set('FileCount'   ,30)
set('FileMinSize'  , 5000)
set('RotationTime' ,'23:59')
set('RotationType','byTime')
set('RotateLogOnStartup',false)
set('FileTimeSpan',24)
set('LoggerSeverity','Info')
set('LogFileSeverity','Info')
set('StdoutSeverity','Info')
set('DomainLogBroadcastSeverity','Off')

# Managed Server 1 Access Log
cd('/Server/' + MG1_SERVER)
create(MG1_SERVER,'WebServer')
cd('/Server/' + MG1_SERVER + '/WebServer/' + MG1_SERVER)
create(MG1_SERVER,'WebServerLog')
cd('/Server/' + MG1_SERVER + '/WebServer/' + MG1_SERVER + '/WebServerLog/' + MG1_SERVER)
set("LoggingEnabled", true)
set('FileName'    ,LOG_HOME + '/' + DOMAIN_NAME + '/' + MG1_SERVER + '/wls/' + 'access_%yyyy%_%MM%_%dd%.log')
set('FileCount'   ,30)
set('FileMinSize'  , 5000)
set('RotationTime' ,'23:59')
set('RotationType','byTime')
set('LogFileFormat','extended')
set('ElfFields','date time cs-method cs-uri sc-status time-taken')
set('RotateLogOnStartup',false)
set('FileTimeSpan',24)


###############################################
###############################################
####                                       ####
####  Allow modification under this line!  ####
####  Remove the '#' of lines.             ####
####  If you want more Servers,            ####
####  Copy and Paste lines 244 to 288.     ####
####                                       ####
###############################################
###############################################


## Creating Managed Server 2
#cd('/')
#create(MG1_SERVER, 'Server')
#cd('Server/' + MG1_SERVER)
#set('ListenAddress',MG1_ADDRESS)
#set('ListenPort',int(MG1_PORT))

## Managed Server 2 Diagnostics Off
#cd('/Server/' + MG2_SERVER)
#create(MG2_SERVER,'ServerDiagnosticConfig')
#cd('/Server/' + MG2_SERVER + '/ServerDiagnosticConfig/' + MG2_SERVER)
#set('WldfDiagnosticVolume','Off')

## Managed Server 2 Server Log
#cd('/Server/'+MG1_SERVER)
#create(MG1_SERVER,'Log')
#cd('/Server/' + MG1_SERVER + '/Log/' + MG1_SERVER)
#set('FileName'    ,LOG_HOME + '/' + DOMAIN_NAME + '/' + MG1_SERVER + '/wls/' + MG1_SERVER + '_%yyyy%_%MM%_%dd%.log')
#set('FileCount'   ,30)
#set('FileMinSize'  , 5000)
#set('RotationTime' ,'23:59')
#set('RotationType','byTime')
#set('RotateLogOnStartup',false)
#set('FileTimeSpan',24)
#set('LoggerSeverity','Info')
#set('LogFileSeverity','Info')
#set('StdoutSeverity','Info')
#set('DomainLogBroadcastSeverity','Off')
#
## Managed Server 2 Access Log
#cd('/Server/' + MG1_SERVER)
#create(MG1_SERVER,'WebServer')
#cd('/Server/' + MG1_SERVER + '/WebServer/' + MG1_SERVER)
#create(MG1_SERVER,'WebServerLog')
#cd('/Server/' + MG1_SERVER + '/WebServer/' + MG1_SERVER + '/WebServerLog/' + MG1_SERVER)
#set("LoggingEnabled", true)
#set('FileName'    ,LOG_HOME + '/' + DOMAIN_NAME + '/' + MG1_SERVER + '/wls/' + 'access_%yyyy%_%MM%_%dd%.log')
#set('FileCount'   ,30)
#set('FileMinSize'  , 5000)
#set('RotationTime' ,'23:59')
#set('RotationType','byTime')
#set('LogFileFormat','extended')
#set('ElfFields','date time cs-method cs-uri sc-status time-taken')
#set('RotateLogOnStartup',false)
#set('FileTimeSpan',24)

print('Now Creating Managed Server!')
print('Please wait a moment.')
updateDomain()

print('Success! Bye')
closeDomain()
exit()