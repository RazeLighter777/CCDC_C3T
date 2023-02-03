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
    - [ ] Locks the authorized_keys file on the hosts.