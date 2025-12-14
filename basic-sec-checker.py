import boto3

iamsvc = boto3.client("iam") # Creating client for using IAM methods

def iam():
    response = iamsvc.list_users() # Returns list of users in a dict 
    return response


def mfaCheck(userList):
    response = []
    for value in userList: # For each value in the dict
        mfaStatus = iamsvc.list_mfa_devices(UserName=value['UserName'])  # Getting the dict associated with UserName
        if mfaStatus['MFADevices'] != []:
            print(f'MFA is enabled for {value['UserName']}')
        else:
            print(f'MFA is not enabled for {value['UserName']}')
    # Yet to be paginated for larger response    

def securityGroupChecker():
    sgsvc = boto3.client("ec2") # Creating client for using EC2 methods
    response = sgsvc.describe_security_groups()
    sg_ids, risky_rules = [],[]
    risky_ports = [22,3389]
    for i in response['SecurityGroups']: # Adding all security group IDs to a list
        sg_ids.append(i['GroupId'])
    for group in sg_ids: # Iterating the list of SG IDs using SG ID
        response_rules = sgsvc.describe_security_group_rules(
            Filters=[{'Name':'group-id','Values': [group]}])
        for sgr in response_rules['SecurityGroupRules']: # Iterating each rule within each Security group 
            if not sgr['IsEgress'] and sgr['FromPort'] in risky_ports and sgr['CidrIpv4'] and sgr['CidrIpv4']=='0.0.0.0/0': 
                risky_rules.append(sgr['GroupId'])
    print(f'Security groups with risky ports open are {risky_rules}')     # Printing the final security groups with risky ports open in inbound rules


if __name__ == "__main__":
    userList = iam() # Function to get the IAM users list.
    mfaCheck(userList['Users']) # Sending only the value associated with Users key.
    securityGroupChecker()

