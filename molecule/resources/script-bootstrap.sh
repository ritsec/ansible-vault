#!/bin/bash
# Figure out the default username of the template
USER=$(grep 1000 /etc/passwd | sed 's/:/ /g' | awk '{ print $1 }')
NEWUSER=deploy-user
usermod -l ${NEWUSER} ${USER}
groupmod -n ${NEWUSER} ${USER}
usermod -md /home/${NEWUSER} ${NEWUSER}
sed -i "s/${USER}/${NEWUSER}/g" /etc/sudoers.d/90-cloud-init-users
shutdown -r 0