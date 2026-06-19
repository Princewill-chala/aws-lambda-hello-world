def lambda_handler(event, context):
    """
    AWS Lambda Hello World Function

    This function demonstrates a basic Lambda invocation.
    It prints a message to CloudWatch Logs and returns
    a successful HTTP-style response.
    """

    print("Hello from AWS Lambda!")

    return {
        "statusCode": 200,
        "body": "Hello from AS Lambda"
    }