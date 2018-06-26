#!/usr/bin/python
import os, sys

###############################################################
###############################################################
####                                                       ####
####  createDomain Auxiliary Tool: Oracle HTTP Server 12c  ####
####                                                       ####
###############################################################
###############################################################

# OHS Configuration
ORACLE_HOME = '/uclick/mw/hjkim/ohs12212'
WLS_HOME    = ORACLE_HOME + '/wlserver'
OHS_HOME    = ORACLE_HOME + '/ohs'
DOMAIN_HOME ='/uclick/mw/hjkim/domains'
DOMAIN_NAME ='ohsDom12212'

# OHS Node Manager Account
NODE_USERNAME = 'ohs'
NODE_PASSWORD = 'welcome1'
NODE_PORT     = '5556'

# OHS INSTANCE Configuration
SYSTEM_COMPONENT     = 'ohs1'
ADMIN_HOST           = 'uclick'
ADMIN_PORT           = '8888'
LISTEN_ADDRES        = 'uclick'
LISTEN_PORT          = '7722'
SSL_LISTEN_PORT      = '5443'
OHS_MACHINE          = 'localmachine'

print('#################################')
print('#### HELLO Create OHS Domain ####')
print('#################################')
print('')
print('')
print('# Check your OHS Domain Configuration')
print('ORACLE HOME : ' + ORACLE_HOME)
print('DOMAIN HOME : ' + DOMAIN_HOME + '/' + DOMAIN_NAME)
print('')
print('# Check your Node Manager Configuration')
print("# Don't forget Node Manager Password!!")
print('USERNAME : ' + NODE_USERNAME)
print('PASSWORD : ' + NODE_PASSWORD)
print('')
print('# OHS Domain Configuration')
print('COMPONENT NAME : ' + SYSTEM_COMPONENT)
print('ADMIN ADDRESS  : ' + ADMIN_HOST + ':' + ADMIN_PORT)
print('LISTEN ADDRESS : ' + LISTEN_ADDRES + ':' + LISTEN_PORT)
print('')


# Read Oracle HTTP Server Standalone Template
print('Reading OHS Domain Template.')
selectTemplate('Oracle HTTP Server (Standalone)','12.2.1.2.0')
loadTemplates()
print('')

#########################################
#########################################
####                                 ####
####  Don't modify under this line!  ####
####                                 ####
#########################################
#########################################

## readTemplate will be disuse.
#readTemplate(WLS_HOME + '/common/templates/wls/base_standalone.jar')
#addTemplate(OHS_HOME + '/common/templates/wls/ohs_standalone_template.jar')

# Configuration Nodemanager
print('Composing OHS Domain Configuration')
cd('/')
create(DOMAIN_NAME,'SecurityConfiguration')
cd('SecurityConfiguration/' + DOMAIN_NAME)
set('NodeManagerUsername',NODE_USERNAME)
set('NodeManagerPasswordEncrypted',NODE_PASSWORD)


setOption('NodeManagerType','PerDomainNodeManager')
cd('/Machines/localmachine/NodeManager/localmachine')
cmo.setListenPort(int(NODE_PORT))

# Create OHS Component
cd('/SystemComponent/ohs1')
cmo.setName(SYSTEM_COMPONENT)
cd('/OHS/' + SYSTEM_COMPONENT)

# OHS Component
cmo.setAdminHost(ADMIN_HOST)
cmo.setAdminPort(ADMIN_PORT)
cmo.setListenAddress(LISTEN_ADDRES)
cmo.setListenPort(LISTEN_PORT)
cmo.setSSLListenPort(SSL_LISTEN_PORT)

print('Now Creating OHS Domain!')
print('Please wait a moment.')
writeDomain(DOMAIN_HOME + '/' + DOMAIN_NAME)
print('Success! Bye')
closeTemplate()
exit()