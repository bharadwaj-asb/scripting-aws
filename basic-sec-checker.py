import boto3

svc = boto3.client("iam")
def iam():
    response = svc.list_users()
    #print(response)
    return response
    #for user in response["Users"]:
     #   print(user["UserName"])
def mfaCheck(userList):
    response = []
    for value in userList:
        mfaStatus = svc.list_mfa_devices(UserName=value['UserName'])
        if mfaStatus['MFADevices'] != []:
            print(f'MFA is enabled for {value['UserName']}')
        else:
            print(f'MFA is not enabled for {value['UserName']}')
        

if __name__ == "__main__":
    userList = iam()
    mfaCheck(userList['Users'])
