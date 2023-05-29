# Import the boto3 library, which is the official AWS SDK for Python, and allows us to interact with AWS services.

import boto3

# Create an ECR client object for accessing the Amazon ECR service.

ecr_client = boto3.client('ecr')

# Specify the name of the ECR repository.

repository_name = "my-cloud-native-repo"

# Create a new ECR repository with the specified name.

response = ecr_client.create_repository(repositoryName=repository_name)

# Extract the repository URI from the response.

repository_uri = response['repository']['repositoryUri']

# Print the repository URI to the console.

print(repository_uri)