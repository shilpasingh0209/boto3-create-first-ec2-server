
# Introduction
This script will run on any AWS account to launch a web server running 'Hello World' html page. This script is created using Boto, the Amazon Web Services (AWS) SDK for Python. It will create a new VPC, subnet, internet gateway, routing table and an EC2 instance to launch the web server running via Apache. 

## Getting Started
Python, boto3 and awscli should be installed in the local machine to run the script. An AWS account is required to launch the web server on cloud.

### Prerequisites
* Python 3.7.1
* pip
* Boto3
* Amazon Web Service account
* AWS CLI

### Installing

* Install python, follow these links for 	
	* [Windows](https://www.ics.uci.edu/~pattis/common/handouts/pythoneclipsejava/python.html)
	* [Mac](https://gist.github.com/patriciogonzalezvivo/77da993b14a48753efda)
	* [Linux](https://docs.aws.amazon.com/cli/latest/userguide/install-linux-python.html)

* Install pip by running `$ python get-pip.py`

* Install Boto module by running `$ pip install boto3`

* Install AWS CLI by running `$ pip install awscli`

* Find your Access Key and Secret Access Key on AWS:
	* Log in to your AWS Management Console.
	* Click on your user name at the top right of the page.
	* Click on the Security Credentials link from the drop-down menu.
	* Find the Access Credentials section, and copy the latest Access Key ID.
	* Click on the Show link in the same row, and copy the Secret Access Key.

* Run `$ aws configure` and pass following information:

    aws_access_key_id = your access key
    
	aws_secret_access_key = your secret access key
	
    region = us-east-1
	
    output foramt = json


## Running the script
Run `$ python create_web_server.py` command from the file location

## Built With
* [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
* [Python](https://www.python.org/)
* [AWS CLI](https://aws.amazon.com/cli/)
* [Apache](https://httpd.apache.org/)

## Author
Shilpa Singh


```python

```
