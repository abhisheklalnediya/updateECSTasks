# Update ECS Tasks

A python script to update the running ECS tasks one by one.
It will wait for each task to update, so that there will be no down time.

You can call this script after pusing your new docker with the same last tag.



## Update the global vars before running the script.

AWS_ACCESS_KEY_ID = None;#####
AWS_SECRET_ACCESS_KEY = None;####
REGION_NAME = "eu-central-1"

CLUSTER =  None # cluseter name
SERVICES = [] 