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
echo 'All bound ports:'
echo '----------------'
netstat -tulpn
echo 'Sudoers file:'
echo '----------------'
cat /etc/sudoers
echo 'Wheel, admin, docker, and sudo groups (users are effectively root):'
echo '----------------'
grep -E 'wheel|admin|docker|sudo' /etc/group
echo 'All files with SUID/SGID bit set:'
echo '----------------'
find /bin -perm -u=s -o -perm -g=s -type f 2>/dev/null
find /usr/bin -perm -u=s -o -perm -g=s -type f 2>/dev/null
find /usr/local/bin -perm -u=s -o -perm -g=s -type f 2>/dev/null
find /sbin -perm -u=s -o -perm -g=s -type f 2>/dev/null
find /usr/sbin -perm -u=s -o -perm -g=s -type f 2>/dev/null
find /usr/local/sbin -perm -u=s -o -perm -g=s -type f 2>/dev/null
echo 'Installed games:'
echo '----------------'
dpkg -l | grep game
echo 'Unauthorized media files:'
echo '----------------'
find /home -name '*.mp3' -o -name '*.mp4' -o -name '*.avi' -o -name '*.mov' -o -name '*.flv' -o -name '*.wmv' -o -name '*.mkv' -o -name '*.mpg' -o -name '*.mpeg' -o -name '*.m4v' -o -name '*.ogg' -o -name '*.wav' -o -name '*.flac' -o -name '*.wma' -o -name '*.m4a' -o -name '*.aac' -o -name '*.jpg' -o -name '*.jpeg' -o -name '*.png' -o -name '*.gif' -o -name '*.bmp' -o -name '*.tiff' -o -name '*.tif' -o -name '*.svg' -o -name '*.psd' -o -name '*.ai' -o -name '*.eps' -o -name '*.indd' -o -name '*.raw' -o -name '*.cr2' -o -name '*.nef' -o -name '*.orf' -o -name '*.sr2' -o -name '*.srf' -o -name '*.arw' -o -name '*.dng' -o -name '*.webp' -o -name '*.3fr' -o -name '*.cine' -o -name '*.crw' -o -name '*.dcr' -o -name '*.k25' -o -name '*.kdc' -o -name '*.mdc' -o -name '*.mef' -o -name '*.mos' -o -name '*.mrw' -o -name '*.nrw' -o -name '*.pef' -o -name '*.ptx' -o -name '*.pxn' -o -name '*.r3d' -o -name '*.raf' -o -name '*.rw2' -o -name '*.rwl' -o -name '*.rwz' -o -name '*.srw' -o -name '*.x3f' -o -name '*.pdf' -o -name '*.doc' -o -name '*.docx' -o -name '*.xls' -o -name '*.xlsx' -o -name '*.ppt' -o -name '*.pptx' 
echo 'Locally installed executables:'
echo '----------------'

