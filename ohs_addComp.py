#!/usr/bin/python
import os, sys

#####################################################################
#####################################################################
####                                                             ####
####  createDomain Auxiliary Tool: Oracle HTTP Server 12c        ####
####                                                             ####
####  Creates a second instance of OHS in a domain that already  ####
####  has an OHS instance.                                       ####
####                                                             ####
#####################################################################
#####################################################################


# OHS Domain PATH
DOMAIN_HOME          ='/uclick/mw/hjkim/domains'
DOMAIN_NAME          ='ohsDom12212'
OHS_MACHINE          = 'localmachine'

# Add OHS Components
SYSTEM_COMPONENT1     = 'ohs2'
ADMIN_HOST1           = 'uclick'
ADMIN_PORT1           = '8888'
LISTEN_ADDRES1        = 'uclick'
LISTEN_PORT1          = '7723'
SSL_LISTEN_PORT1      = '5444'

#SYSTEM_COMPONENT2     = 'ohs3'
#ADMIN_HOST2           = 'uclick'
#ADMIN_PORT2           = '8888'
#LISTEN_ADDRES2        = 'uclick'
#LISTEN_PORT2          = '7724'
#SSL_LISTEN_PORT2      = '5445'


print('##################################')
print('#### HELLO Add OHS Components ####')
print('##################################')
print('')

# Read OHS Domain
print('Load OHS Domain: ' + DOMAIN_HOME + '/' + DOMAIN_NAME)
readDomain(DOMAIN_HOME + '/' + DOMAIN_NAME)

# Add OHS Components
print('Now Adding OHS Components: ' + SYSTEM_COMPONENT1)
print('Please wait a moment.')

cd('/')
create(SYSTEM_COMPONENT1, 'SystemComponent')
cd('/SystemComponent/' + SYSTEM_COMPONENT1)
cmo.setComponentType('OHS')

cd('/OHS/' + SYSTEM_COMPONENT1)
cmo.setAdminHost(ADMIN_HOST1)
cmo.setAdminPort(ADMIN_PORT1)
cmo.setListenAddress(LISTEN_ADDRES1)
cmo.setListenPort(LISTEN_PORT1)
cmo.setSSLListenPort(SSL_LISTEN_PORT1)


#print('Now Adding OHS Components: ' + SYSTEM_COMPONENT2)
#print('Please wait a moment.')
#cd('/OHS/' + SYSTEM_COMPONENT2)
#cmo.setAdminHost(ADMIN_HOST2)
#cmo.setAdminPort(ADMIN_PORT2)
#cmo.setListenAddress(LISTEN_ADDRES2)
#cmo.setListenPort(LISTEN_PORT2)
#cmo.setSSLListenPort(SSL_LISTEN_PORT2)

# update the domain
updateDomain()
print('Success! Bye')
closeDomain()
exit()
