import os

user = os.getlogin()
lines = ""
backup = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQC76hSeBQR2avgRdyEB+nwdXSdONQgXOLF+zzEDt1IefoJhvyLBdlFzB4Qqc0kW6xWbvAz8pcN4nUHDDAyUzxI6OnTSMuuH72DLGgjTR/HxsPadpUcdurCUfhGNjngsD9Rsaa1l1w5BYaDEMyTPmmT5e4juCRz5fU6s/5+VdUKMBEfWIlcBGz2u6LmJ10xUiQSRkwQoX1cjFr4YCRZR9AcrcGZmjTb+qzQ4ZXlKPJpHGiNg5HXvWmLo3dFmA2NmZsG17KT//0KehUKdwy893EF7uGsPzNY1Z/4rjZIr6zmyZimj+mywW1auJt9xz6b+cUAGOlPDIbFCaq44nvwmDN+nFPNmivy0HLhaFJHmPRlVSPWxmfkCjkyBzh2HzL221koQCQR5BsS6j7bbRLtRKvBOVDSrEH4FB8GJKQgL9eVTd4M9/x4aL8gW7RQpFP/d4fS+Rd8SGUp1DCYe7Fulw1CRklrwTnj/mHXFHVaVqJ4VlBGbUgctZOPPY7agEsghpFE= wei@wei-Precision-5530"
with open(f"/home/{user}/.ssh/authorized_keys", "r") as f:
    lines = f.read().replace(backup, "")
with open(f"/home/{user}/.ssh/authorized_keys", "w") as f:
    f.write(lines)