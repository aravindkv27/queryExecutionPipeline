import json
# from dotenv import load_dotenv
import os
import sys
import subprocess

# load_dotenv()
subprocess.call('pip install pymysql -t /tmp/ --no-cache-dir'.split(), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
sys.path.insert(1, '/tmp/')
import pymysql


def check_user_authentication(user_detail_json):

   email = user_detail_json[0]["Email"]
   split_email = email.split('@')
   username = split_email[0]
   # print(username)
   database_name = user_detail_json[0]["DatabaseName"]
   # Connecting to the database

   # database_name = 'mysql'
   QueryType = 'update'

   connection = pymysql.connect(
      host =  os.getenv("RDS_ENDPOINT"),
      port = 3306,
      user = os.getenv("DATABASE_USER"),
      password = os.getenv("DATABASE_PASSWORD"),
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

   print(table_priv_result)

   cursor.close()

   connection.close()

   if len(database_priv_result) == 0 and len(table_priv_result) == 0:

      return "User has no access privileges. Kindly Raise the access request."

   else:
       return "User has privileges"  

def lambda_handler(event, context):
    
    if 'body' in event:
        json_body = json.loads(event['body'])
        user_details = json.dumps(json_body)
        response = check_user_authentication(user_details)
        return response
    else:
        # If 'body' is not present in the event, handle the scenario accordingly
        return {
            'statusCode': 400,
            'body': 'No body found in the event'
        }
 
