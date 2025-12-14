import boto3

client = boto3.client('s3')

def check_encryption():
    buckets = client.list_buckets()
    for bucket in buckets['Buckets']: # Iterating each bucket
        bucket_name = bucket['Name']
        try:
            encryption = client.get_bucket_encryption(Bucket=bucket_name)
            rules = encryption['ServerSideEncryptionConfiguration']['Rules']
            for rule in rules: # Iterating each rule
                sse_algorithm = rule['ApplyServerSideEncryptionByDefault']['SSEAlgorithm']
                print(f"Bucket: {bucket_name}, Encryption: {sse_algorithm}")
        except client.exceptions.ClientError as e: # Handling case where no encryption is configured
            if e.response['Error']['Code'] == 'ServerSideEncryptionConfigurationNotFoundError':
                print(f"Bucket: {bucket_name} has no encryption configured.")
            else:
                print(f"Error checking bucket {bucket_name}: {e}")


def check_public_access():
    buckets = client.list_buckets()
    for bucket in buckets['Buckets']: # Iterating each bucket
        bucket_name = bucket['Name']
        try:
            response = client.get_public_access_block(Bucket= bucket_name)
            public = response['BlockPublicAcls'] and response['BlockPublicPolicy'] and response['RestrictPublicBuckets'] # Checking public access settings
            if not public:
                print(f"Bucket: {bucket_name} is publicly accessible.")
            else:
                print(f"Bucket: {bucket_name} is not publicly accessible.")
        except client.exceptions.ClientError as e: # Handling case where no public access block is configured
            print(f"Error checking bucket {bucket_name}: {e}")

if __name__ == "__main__":
    check_encryption() # This function checks all S3 buckets in the AWS account for server-side encryption configuration.
    check_public_access() # This function checks all S3 buckets in the AWS account for public access settings.