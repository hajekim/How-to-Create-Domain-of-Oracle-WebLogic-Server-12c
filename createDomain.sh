#!/bin/sh

#####################################################
#####################################################
####                                             ####
####  Oracle Fustion Middleware 12c              ####
####  createDomain Auxiliary Tool                ####
####                                             ####
#####################################################
#####################################################

## Insert your ORACLE_HOME
ORACLE_HOME="/uclick/mw/hjkim/wls12212"


#########################################
#########################################
####                                 ####
####  Don't modify under this line!  ####
####                                 ####
#########################################
#########################################

CREATE_PY=$1

# CREATE_PY Null Check
if [ ${CREATE_PY} ];
# None Null
then
    # If Insert Help
    if [ -f ${CREATE_PY} ];
    then
    echo ''
    echo ''
    echo '#######################################'
    echo '#######################################'
    echo '####                               ####'
    echo '####  createDomain Auxiliary Tool  ####'
    echo '####                               ####'
    echo '#######################################'
    echo '#######################################'
    echo ''
    echo ''
    # Print ORACLE_HOME
    echo 'ORACLE HOME :' ${ORACLE_HOME}
    echo ''
    echo 'Starting Domain Shell with WLST'
    ${ORACLE_HOME}/oracle_common/common/bin/wlst.sh ${CREATE_PY}    

    else
    echo ''
    echo 'Error Occurred!'
    echo 'FILE Not Found Exception: ' ${CREATE_PY} ' not found'
    echo 'Check File Exists!'
    echo ''
    echo '  How to use it?'
    echo ''
    echo '  ./createDomain.sh "Python File Path"'
    echo '  Example: ./createDomain.sh /install/ofm/wls.py'
    echo ''
    fi

else
echo ''
echo 'Error Occurred!'
echo 'Not Input Value Exception: No File Path'
echo 'Insert PY File Path'
echo ''
echo '  How to use it?'
echo ''
echo '  ./createDomain.sh "Python File Path"'
echo '  Example: ./createDomain.sh /install/ofm/wls.py'
echo ''
fi