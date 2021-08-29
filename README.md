# Automated-mail-for-health-checks
This repo will contain scripts for automating sending mail for failed health check of system
Here health check means check for cpu usage, free disk, and free memory, etc.
there will be threshold for all types of data, and if actual data exceeds the threshold,
an email wil be sent to the administrator to check for the error.

To check if the health_checks.py script works correctly we can either use a test script file or manually run 'stress' tool to stress the use of resources and execute the script.
guidelines on using stress tool:
$sudo apt install stress #to install the tool if not available
$stress --cpu 8 #calling the tool using a good number of cpus to fully load the cpu resources

To make the health_checks.py execute regularly such as services do we need to setup a cron job which would execute the script after a specified period of time.
To set a user cron job:
$crontab -e
enter appropriate choice then set the absolute path for health_checks.py script and save the file.
