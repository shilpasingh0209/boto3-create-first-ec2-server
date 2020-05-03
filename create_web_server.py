import boto3
import time

def create_web_server():

    REGION = 'us-east-1' # region to launch instance.
    AMI = 'ami-0de53d8956e8dcf80'  # ami_id for linux instance in us-east-1 
    INSTANCE_TYPE = 't2.micro' # instance type to launch.

    #  script to install Apache and run index.html on the web server
    init_script =  """#!/bin/bash
    sudo yum update -y
    sudo yum install -y httpd
    sudo service httpd start
    echo "<html><h1>Hello World!</h1></html>" > test
    cat test > /var/www/html/index.html
    """

    # boto3 AWS ec2 resource to create connection with AWS
    EC2 = boto3.resource('ec2', region_name=REGION)

    # Create New VPC
    vpc = EC2.create_vpc(
        CidrBlock='10.0.0.0/26'
    )
    vpc.wait_until_available()

    # Create internet gateway
    ig = EC2.create_internet_gateway()
    vpc.attach_internet_gateway(InternetGatewayId=ig.id)

    # Create routing table
    route_table = vpc.create_route_table()
    route = route_table.create_route(
        DestinationCidrBlock='0.0.0.0/0',
        GatewayId=ig.id
    )

    # Create subnet
    subnet = EC2.create_subnet(
        CidrBlock='10.0.0.0/28',
        VpcId=vpc.id
    )
    
    # Associate routing table with subnet
    route_table.associate_with_subnet(SubnetId=subnet.id)

    # Create security group
    mysg = EC2.create_security_group(GroupName="testgroup",Description='testme',VpcId=vpc.id)
    mysg.authorize_ingress(IpProtocol="tcp",CidrIp="0.0.0.0/0",FromPort=80,ToPort=80)

    # Create EC2 Instance
    response = boto3.resource('ec2',region_name=REGION)
    instance = response.create_instances(
        ImageId=AMI,
        InstanceType=INSTANCE_TYPE,
        MinCount=1, 
        MaxCount=1,
        NetworkInterfaces=[{'SubnetId': subnet.id, 'DeviceIndex': 0, 'AssociatePublicIpAddress': True, 'Groups': [mysg.group_id]}],
        UserData=init_script
    )
    
    print("\n")
    print("Please wait while AWS is launching your instance..........")
    time.sleep(20)
    print("Hold on! This might take a minute......")
    time.sleep(30)

    # Fetch public IP address from the instance
    ip_address = boto3.client('ec2',region_name=REGION)
    instance_details = ip_address.describe_instances(
        InstanceIds=[
            instance[0].id
        ]
    )

    public_ip_address = instance_details['Reservations'][0]['Instances'][0]['PublicIpAddress'] #Public IP Address
    print("Your instance is launched successfully in US East (N. Virginia) region. Your public IP is " + public_ip_address)

create_web_server()