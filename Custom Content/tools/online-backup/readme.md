**Consists of 2 files:**

backup.sh

upload-backup.py

**example schedule via crontab:**

0 4 * * * ~/backup.sh >> ~/cron.log 2>&1

This will run the backup script every day at 4 am. For more schedling options, check out https://crontab.guru/
