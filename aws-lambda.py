# Required AWS Lambda JSON response
# {
#     "isBase64Encoded": true|false,
#     "statusCode": httpStatusCode,
#     "headers": { "headerName": "headerValue", ... },
#     "body": "..."
# }
import sys
import json
import psycopg2 as p
from psycopg2 import Error

def connect():
    conn = p.connect(
	    user = 'postgres',
	  	password = 'postgres',
	  	host = 'order-mgmt.cm8jgfxv846i.us-east-2.rds.amazonaws.com',
	  	port = '5432',
	  	database = 'postgres'
	)
    return conn

def retrieve_vendors():
    try:
      conn = connect()
      cursor = conn.cursor()
      cursor.execute("select row_to_json(vendors) from (select * from om_vendor) as vendors")
      result = cursor.fetchall()
      print("Retrieved all of the vendors")

      vendors = []
      for vendor in result:
          vendors.append(vendor)

    except p.Error as error:
      print("A database exception was thrown: {}".format(error))
    except:
      print("An unknow exception was thrown: {}".format(sys.exc_info()[1]))
    finally:
      if conn:
        cursor.close()
        conn.close()

    return vendors

def lambda_handler(event, context):
    print(event)
    method = event["httpMethod"]
    message = "Hello!  I received a " + method + " request."

    vendors = retrieve_vendors()

    return {
        "statusCode": 200,
        "body": json.dumps(vendors)
    }

def main():
    vendors = retrieve_vendors()
    print(vendors)

main()