# scripting-aws

This repository contains the Python scripts that can be used to perform basic security checks in AWS. Uses boto3 SDK in Python to make the API calls.

## Current checks:
  - IAM: Identifies which IAM users have MFA enabled and disabled. Checks if access keys associated with each IAM user are rotated in last 90 days.
  - Security Groups: Identifies which security groups have inbound ports 22 (SSH) and 3389 (RDP) open from any source (0.0.0.0/0).
  - S3: Identifies default encryption settings and public access settings for S3 buckets.

## Purpose
Built to demonstrate hands-on cloud security automation and security-as-code practices.
