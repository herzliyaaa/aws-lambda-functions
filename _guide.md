## GUIDE

### Creating a Lambda Function: A Step-by-Step Guide

1. Navigate to the Lambda Console

* Log in to your AWS Management Console.
* Go to the Lambda service.

2. Create a New Function

* Click on "Create function".
* Choose "Author from scratch".

3. Basic Information

* Function name: Give your function a descriptive name (e.g., my_python_function).
* Runtime: Select Python 3.12 or a compatible version.
* Architecture: Leave it as x86_64 for now.

4. Permissions
* Existing Role: If you have a suitable role with necessary permissions, select it.
* Create a New Role: If you don't have an existing role, click "Create a new role".
* Role name: Give it a descriptive name (e.g., lambda_execution_role).
* Trust relationship: Select Lambda as the service that can assume this role.
* Permissions: Attach the required policies. For most functions, the AWSLambdaBasicExecutionRole policy is sufficient. However, if your function needs to access other AWS services, add the corresponding policies.

5. Create Function
Click "Create function".

### Adding a Trigger and Configuring Your Lambda Function

### Adding an EventBridge Trigger
* Navigate to your Lambda function: In the Lambda console, select the function you created.

* Add trigger: Click the "Add trigger" button.

* Select EventBridge: Choose "EventBridge" as the trigger type.

* Create a rule: Click "Create rule".

Configure the rule:
* Name: Give your rule a descriptive name (e.g., "MyFunctionTrigger").

* Description: Add an optional description for the rule.

* Rule type: Select "Schedule expression" for a scheduled trigger.

* Schedule expression: Define the schedule for your function. 

    For example:

            rate(1 day): Runs every day.
            cron(0 17 ? * MON-FRI): Runs at 5 PM every weekday.

* Targets: Ensure your Lambda function is selected as the target.
* Save: Click "Save" to create the rule and trigger.

### Writing Your Lambda Function Code

* Open the function code editor: In the Lambda console, click the "Code" tab.

* Write your Python code: Replace the default code with your desired logic.

* Include necessary configurations: Add your instance_id, region_name, s3_bucket_name, and other required configurations as variables or environment variables.

### Testing Your Function

* Choose a test event: Select a test event template or create a custom one.

* Configure test event: Provide any necessary input parameters for your function.

* Test: Click "Test" to execute your function.