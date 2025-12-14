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


if __name__ == "__main__":
    userList = iam() # Function to get the IAM users list.
    mfaCheck(userList['Users']) # Sending only the value associated with Users key.

