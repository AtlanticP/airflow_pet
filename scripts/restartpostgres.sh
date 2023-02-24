# /bin/bash
echo $SUDO_PASSWORD | sudo -S systemctl restart postgresql
