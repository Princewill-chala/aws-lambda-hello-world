# AWS Lambda Hello World
![AWS Lambda Banner](Lambda/lambda-banner.png)

## Project Overview

This project demonstrates the deployment of a basic AWS Lambda function using the AWS Management Console.

The function was written in Python and tested directly from the Lambda console. CloudWatch Logs were used to monitor execution and verify successful invocation.

---

# Objectives

- Learn AWS Lambda fundamentals
- Create a serverless function
- Deploy Python code
- Test the function
- Monitor execution using CloudWatch Logs

---

# Services Used

- AWS Lambda
- Amazon CloudWatch
- Python 3.x

---

# Project Workflow

User

↓

AWS Lambda

↓

Execute Python Function

↓

CloudWatch Logs

---

# Step 1 - Create Lambda Function

Created a Lambda function named:

HelloLambda

Screenshot:

![Create Function](Lambda/Create_function.jpeg)

---

# Step 2 - Hello World Function

The default code was replaced with a simple Hello World Lambda function.

![Lambda Function](Lambda/helloworld_function.jpeg)

Example code:

```python
def lambda_handler(event, context):

    print("Hello from AWS Lambda")

    return {
        "statusCode":200,
        "body":"Hello from AWS Lambda"
    }
```

---

# Step 3 - Test Event

A test event was created inside the Lambda console to invoke the function.

![Test Event](Lambda/test_event.jpeg)

---

# Step 4 - Monitor Execution

The Monitor tab was used to observe function execution metrics.

![Monitor](Lambda/monitor_event.jpeg)

---

# Step 5 - CloudWatch Logs

CloudWatch Logs confirmed that the Lambda function executed successfully.

![CloudWatch Logs](screenshots/log_event.jpeg)

---

# Skills Demonstrated

- AWS Lambda
- Serverless Computing
- Python
- CloudWatch Monitoring
- Event Testing
- AWS Console Navigation

---

# Learning Outcome

This project introduced the basics of serverless computing using AWS Lambda.

I learned how to:

- Create Lambda functions
- Deploy Python code
- Invoke functions manually
- Monitor executions
- View CloudWatch Logs

---

# Author

Elochukwu Princewill

Aspiring Cloud & Cybersecurity Engineer