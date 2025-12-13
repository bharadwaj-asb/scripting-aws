import boto3

svc = boto3.client('iam')

def iam():
    return svc.list_users()
    

if __name__=="__init__":
    print(iam())