import boto3

AWS_ACCESS_KEY_ID = None;#####
AWS_SECRET_ACCESS_KEY = None;####
REGION_NAME = "eu-central-1"

CLUSTER =  None # cluseter name
SERVICES = [] # services to update

client = boto3.client('ecs', region_name=REGION_NAME, aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
waiter = client.get_waiter('services_stable')

for service in SERVICES:
	print "Updating Service: " + service
	tasks = client.list_tasks(cluster=CLUSTER, serviceName=service).get('taskArns',[])
	print "\tTasks to update \t:" , len(tasks)
	print "\tUpdating tasks "
	for task in tasks:
		print "\t - ", task 
		client.stop_task(cluster=CLUSTER, task=task)
		waiter.wait(cluster=CLUSTER, services=client.list_services(cluster=CLUSTER).get('serviceArns',[]))