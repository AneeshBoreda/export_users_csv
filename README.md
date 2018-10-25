# RedLock user export 

Version: *1.0*
Author: *Eddie Beuerlein*

### Summary
This script will create a csv file that contains information of all your active servers. Including server group name, server hostname, server os type, server
os version, ec2 instance id and list of softwares on the server.

### Requirements and Dependencies

1. Python 2.7.10 or newer

2. OpenSSL 1.0.2 or newer

### Configuration

1. Navigate to *export_users_csv/config/configs.yml*

2. Fill out your RedLock username, password, and customer name - if you are the only customer in your account then leave this blank.

### Run

```
python runner.py

```
