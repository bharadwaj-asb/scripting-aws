import boto3

def iam():
    svc = boto3.client("iam")
    response = svc.list_users()
    for user in response["Users"]:
        print(user["UserName"])

if __name__ == "__main__":
    iam()
