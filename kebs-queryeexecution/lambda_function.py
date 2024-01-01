import pymysql
from dotenv import load_dotenv
import os
import boto3
import sqlfluff
import json

# load_dotenv()


demo_json = [
    {
        "Associate-ID": "901224",
        "Email": "brohidh@kaartech.com",
        "Query": "INSERT INTO `m_gl_tax_account` ( `gl_code`, `gl_name`, `gl_description`, `gl_type`, `created_on`, `created_by`, `changed_on`, `changed_by`, `is_active`) VALUES ( NULL, 'TDS - Rent - Coy - 194I - P&M Or Equipment', 'TDS - Rent - Coy - 194I - P&M Or Equipment', 'less', '2023-12-28 11:06:50', NULL, '2023-12-28 11:06:50', NULL, 1); \nALTER TABLE t_c4c_opportunity MODIFY COLUMN rfp_date DATE; \nSELECT * FROM congruent.t_notification WHERE recipient_id_1 = \"532c63bb-c654-4181-9a3e-867a941be474\";",
        "DatabaseName": "stelliumdev",
        "Environment": "Development",
        "Team": "KTern",
        "QueryType": "Update",
        "Reason": "test",
        "TableName" : 'm_employee_master'
    }
]



def lambda_handler(event, context):
    # Print the entire event received by the Lambda function
   #  print("Received event:", json.dumps(event))
    
    
   # If the event contains a 'body', print its content
   if 'body' in event:
        json_body = json.loads(event['body'])
      #   print("Received body:", json.dumps(body))
    
    # Your logic goes here...
   user_details = json.dumps(json_body)
   response = check_user_authentication(user_details)

    # Return a response (optional)
   # response = {
   #      'statusCode': 200,
   #      'body': json.dumps(json_body)
   #  }
   return response  


def get_query_from_file(json_data):

    email = json_data[0]["Email"]
    split_email = email.split('@')
    username = split_email[0]
    query = json_data[0]["Query"]
    queries = query.split('\n')
    comment = json_data[0]["Reason"]
    database_name = json_data[0]["DatabaseName"]

    bucket_name = 'kebs-queryexecution'  # Replace with your bucket name
    file_path = f'changelogs/{database_name}/changelog.sql'  # S3 file path

    # Prepare the content to insert into S3
    content = f"\n--changeset {username} labels:{comment} \n"
    content += f"--comment: {comment}\n"
    content += '\n'.join(queries) + '\n'
    print(content)


    s3 = boto3.client(
        's3',
        aws_access_key_id= os.environ('AWS_ACCESS_KEY'),
        aws_secret_access_key= os.environ('AWS_SECRET_KEY')
        )

    try:
            # Retrieve existing content from S3 file
            response = s3.get_object(
                Bucket=bucket_name,
                Key=file_path
            )
            existing_content = response['Body'].read().decode('utf-8')

            # Append new content to the existing content
            updated_content = existing_content + '\n' + content

            # Upload updated content back to S3 bucket
            s3.put_object(
                Bucket=bucket_name,
                Key=file_path,
                Body=updated_content
            )

            return "Inserted Successfully"
        
    except s3.exceptions.NoSuchKey:
            # If the file doesn't exist, create a new file with the content
            s3.put_object(
                Bucket=bucket_name,
                Key=file_path,
                Body=content
            )
            return "Inserted Successfully"


def lint_violoations_check(queries):

    queries_string = "\n".join(queries)
    result = sqlfluff.lint(queries_string)
    violation_result = []
    if result:
        for violation in result:
            violation_result.append(violation)
        # total_errors = len(result)
        return violation_result
    else:
        return "No Violation"

def check_user_authentication(user_detail_json):

    email = user_detail_json[0]["Email"]
    split_email = email.split('@')
    username = split_email[0]
    # print(username)
    database_name = user_detail_json[0]["DatabaseName"]
    QueryType = user_detail_json[0]["QueryType"]
    TableName = user_detail_json[0]["TableName"]
    query = user_detail_json[0]["Query"]
    queries = query.split('\n')

    connection = pymysql.connect(
        host =  os.environ("DATABASE_RDS_EP"),
        port = 3306,
        user = os.environ("DATABASE_RDS_USR"),
        password = os.environ("DATABASE_RDS_PSD"),
        database = 'mysql'
    )

    cursor = connection.cursor()

    database_priv = f"SELECT Db, {QueryType}_priv FROM db WHERE USER = '{username}' and (Db = '{database_name}' and {QueryType}_priv = 'Y') "
    table_priv = f"SELECT Db, Table_name, Table_priv FROM tables_priv WHERE USER = '{username}' and  Db = '{database_name}'"

    cursor.execute(database_priv)

    database_priv_result = cursor.fetchall()
    print(database_priv_result)

    cursor.execute(table_priv)

    table_priv_result = cursor.fetchall()

    cursor.close()

    connection.close()

    lint_violoations_result = lint_violoations_check(queries)

    if len(database_priv_result) == 0 and len(table_priv_result) == 0:

        return "User has no access privileges. Kindly Raise the access request."
    
    elif len(table_priv_result) != 0:
        table_found = False  # Initialize a flag to track if the table was found

        for db, table, permissions in table_priv_result:
            if database_name == db and table == TableName:
                table_found = True  # Set the flag to True indicating the table was found
                user_permissions = permissions.split(',')
                if QueryType in user_permissions:
                    response = get_query_from_file(user_detail_json)
                    return lint_violoations_result, response

        # If the loop completes without finding a match, check the flag
        if not table_found:
            response =  f"The {username} does not have {QueryType} access for table {TableName}."
            return lint_violoations_result, response

    # If no table privilege results were found
    return f"No table privileges found for {username} or the database."

    # else:
    #     print("executing else")
    #     response = get_query_from_file(demo_json)
    #     return response 

# response = check_user_authentication(demo_json)
# print(response)