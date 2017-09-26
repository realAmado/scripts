import ipaddress
import csv
import sys
import subprocess
cmd='rm -f vpc.out;aws --profile tiaa-brokerage-api ec2 describe-vpcs --region us-east-1 --query "Vpcs[*].[VpcId,CidrBlock]" --output=text >> vpc.out'
refresh=subprocess.Popen(cmd, shell=True, stdout = subprocess.PIPE)
#print refresh.returncode
cidr_arg = sys.argv[1]
cidr_check = cidr_arg.decode('unicode_escape')
v0 = ipaddress.ip_network(cidr_check)
with open('vpc.out','r') as f:
	reader = csv.reader(f, delimiter='\t')
	for row in reader:
           vpcid = row[0]			
           cidr = row[1]	
	   cidr_decode = cidr.decode('unicode_escape')	
           cidr_exist = ipaddress.ip_network(cidr_decode) 		
	   if v0.overlaps(cidr_exist): 	
		print v0, "overlaps", cidr, "on", vpcid
