# slack_notify
Send slack notification on system startup or shutdown

Add your own web hook URL to the script.

Place the script in /etc/init.d/ as slack_notify or similar.

Creat symbolic links in the various /etc/rcx.d/ folders with the S99 or K01 prefix depending upon startup or shutdown.

You can test the script by issuing the /etc/init.d/slack_notify start or stop commands.
