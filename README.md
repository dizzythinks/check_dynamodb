check_dynamodb
==============

A simple Nagios plugin for monitoring size of DynamoDB tablesa

requirements
============

boto==2.34.0

usage
=====

	usage: check_dynamodb.py [-h] -r R -t T -w W -c C
	
	DynaamoDB Table Nagios Check
	
	optional arguments:
  	-h, --help  show this help message and exit
  	-r R        region
  	-t T        table name
  	-w W        warn threshold for size in MB
  	-c C        crit threshold for size in MB


aws credentials
===============

The plugin assumes that you're either running this on an EC2 instance that has "Describe" permissions in DynamoDB through an instance-profile role. Or that you've set your environments for the AWS access key and secret.
