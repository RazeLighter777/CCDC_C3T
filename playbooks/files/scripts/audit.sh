echo 'Crontab list:'
echo '----------------'
for user in $(cut -f1 -d: /etc/passwd); do crontab -u $user -l; done
echo 'List of users:'
echo '----------------'
awk -F: '($2 != "") {print $1}' /etc/shadow
echo 'All authorized keys:'
echo '----------------'
find /home -name authorized_keys -exec cat {} \;
echo 'All running services (systemctl):'
echo '----------------'
systemctl list-units --type=service --state=running