import pymysql
from dotenv import load_dotenv
import os
import boto3
import sqlfluff
import json

load_dotenv()

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
        host =  os.getenv("DATABASE_RDS_EP"),
        port = 3306,
        user = os.getenv("DATABASE_RDS_USR"),
        password = os.getenv("DATABASE_RDS_PSD"),
        database = 'mysql'
    )

    cursor = connection.cursor()

    return cursor

resp = check_user_authentication(demo_json)
print(resp)