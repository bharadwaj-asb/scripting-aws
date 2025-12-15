import boto3
from datetime import date

def main():
    client = boto3.client('iam')
    iam_users = client.list_users()
    for value in iam_users['Users']: # For each value in the dict
        response = client.list_access_keys(UserName=value['UserName'])
        akmd = response['AccessKeyMetadata'] 
        for akid in akmd: # Iterating through each dict of metadata about each IAM user
            duration = date.today() - akid['CreateDate'].date() # Converts to same format for difference and stores in timedelta var
            if  duration.days > 90: 
                print(f'Access keys of {akid['UserName']} are older than 90 days.')
            else:
                print(f'Access keys of {akid['UserName']} are rotated within last 90 days.')



if __name__ == '__main__':
    main()