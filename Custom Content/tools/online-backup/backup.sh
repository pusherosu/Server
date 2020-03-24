#!/bin/bash
#-- user-defined variables
username=
password=
databasename=
#-- Begin
d=`date +%Y-%m-%d-%H-%M-%S`
n="eqemu-backup-"
echo "Dumping database"
mysqldump --user=$username --password=$password $databasename > $n$d.sql
echo "Compressing"
tar -czvf $n$d.tar.gz $n$d.sql
echo "Uploading file to cloud storage"
~/upload-backup.py -f $n$d.tar.gz
echo "Cleaning up..."
rm $n$d.sql
rm $n$d.tar.gz
echo "Backup complete!"
#-- End
