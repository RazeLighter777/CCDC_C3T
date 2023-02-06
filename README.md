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
2. Edit the files in inventory.yaml, playbooks/ and playbooks/files to include the correct information. **This is important because some of the playbooks could break the systems or scoring checks if the information is incorrect!**

    - Check fail2ban jail.local and make sure ignoreip is set to the correct subnets for scoring checker and LAN!.
    - Check firewall.yml and make sure the correct ports are selected for any services running on docker swarm.
    - Make sure the hosts are under the correct group in inventory.yaml to prevent misconfiguration.

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
    - [x] Installs the C3T custom banner on the hosts.
    - [x] Locks the authorized_keys file on the hosts with chattr +i.
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
    - [x] Sets passwordless sudo for the ansible user
    - [x] Sets password for ansible user and root and removes passwords from all other users
    - [x] Marks /etc/shadow as immutable, preventing password changes
- audit.yml
    - [x] Runs an audit script and fetches the results to playbooks/fetch  
- network.yml
    - [x] Configures the hosts to use the C3T DNS servers specified in the inventory.yaml
- honeypot.yml
    - [ ] Installs and configures the honeypot on the hosts.
- firewall.yml
    - [x] Installs ufw on all hosts.
    - [x] Disables firewalld on RHEL hosts.
    - [x] Configures ufw on all hosts to allow SSH.
    - [x] Enables group-based firewall rules on all hosts. Relies on the group names in inventory.yaml.
- os_hardening.yml
    - [x] Runs scripts to harden the hosts from github.com/dev-sec/ansible-os-hardening
# Suggested run order
1. audit.yml
2. network.yml
3. os_hardening.yml
4. packages.yml
5. ssh.yml
6. mac.yml
7. fail2ban.yml
8. sudo.yml
9. honeypot.yml
9. firewall.yml