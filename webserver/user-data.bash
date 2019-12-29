#!/bin/bash

# AWS EC2 User Data
# After creating and starting the EC2 instance, this script is run.

# Install httpd (Linux 2 version)
yum update -y
yum install -y httpd.x86_64
systemctl start httpd.service
systemctl enable httpd.service

# Output a test website.
echo "Hello World from $(hostname -f)" > /var/www/html/index.html
