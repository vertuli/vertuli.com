#!/bin/bash

# This overwrites the existing Apache Webserver /var/www/html content of the
# EC2 instance with the contents of the local html folder in this directory.

# Name of host defined in ~/.ssh/ with credentials to the EC2 webserver.
HOST="aws_personal"

scp -r html $HOST:/var/www/
