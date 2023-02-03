# C3T NECCDL REGIONALS SCRIPTS
This directory contains scripts related to NECCDL 2023 regionals. 

# Requirements
- Python
- Ansible

# Configuration
1. Edit the `inventory.yml` file to include the hostname of the hosts you want to configure.
You can add additional hosts by adding a new entry under the appropriate `hosts` in the `inventory.yml` file.
Make sure all hosts added to the inventory are added to your .ssh/config file.

The syntax for the ~/.ssh/config file is as follows:
```
Host <hostname (must match inventory.yml)>
    HostName <ip address>
    User <username>
    IdentityFile <path to private key  (Eg. ~/.ssh/practice_key)>
```
2. Edit the `group_vars/all.yml` file to include the appropriate values for the variables. See the comments in the file for more information.

3. To run an invividual playbook, run the following command:
```
ansible-playbook -i inventory.yaml <playbook name>
```
# Playbooks
- packages.yml
    - [x] Installs some QoL packages on the hosts.
    - [x] Updates the hosts using apt or yum.
- ssh.yml
    - [x] Configures SSH on the hosts to disallow root login.
    - [ ] Installs the C3T backup key on the hosts.
    - [x] Locks the authorized_keys file on the hosts with chattr +i.
- auditd.yml
    - [x] Installs auditd on the hosts.
    - [x] Configures auditd on the hosts to log all events.
    - [ ] Enables auditd on the hosts. (Doesn't work on RHEL hosts . . . )
- mac.yml
    - [x] Enabled SELinux on RHEL hosts.
    - [x] Enables AppArmor on Ubuntu hosts.
- fail2ban.yml
    - [x] Installs fail2ban on the hosts.
    - [x] Configures fail2ban on the hosts to ban hosts that fail to login 3 times.
- sudo.yml
    - [x] Changes default sudo timeout to 30s
    - [x] Removes root password
    - [x] Adds immutable flag to sudoers file