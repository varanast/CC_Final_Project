import os 
import mysql.connector 

dir_path = os.path.dirname(os.path.realpath(__file__)) 

# config = { 
#   'host':'cc-final-server.mysql.database.azure.com', 
#   'user':'rekhasqlserver@cc-final-server',
#   'password':'Rekha@123',
#   'database':'ccfinaldb', 
#   'port': 3306, 
#   'ssl_ca': os.path.join(dir_path, 'ssl', 'BaltimoreCyberTrustRoot.crt.pem'), 
#   'ssl_verify_cert': 'true', 
#   'connect_timeout':50 
# } 
 
config = { 
  'host':'ccmysqlserver.mysql.database.azure.com', 
  'user':'mysql@ccmysqlserver', 
  'password':'Rupa@123', 
  'database':'cc_project', 
  'port':3306, 
  'client_flags': [mysql.connector.ClientFlag.SSL], 
 'ssl_ca': os.path.join(dir_path, 'ssl','BaltimoreCyberTrustRoot.crt.pem'), 
  'ssl_verify_cert': 'true', 
  'connect_timeout':50 
} 


conn = mysql.connector.connect(**config)
print(conn)
cur = conn.cursor()
cur.execute('SELECT * FROM users')
user = cur.fetchone()
print(user)


# import pyodbc 

# cnxn = pyodbc.connect(
#     "Driver={ODBC Driver 17 for SQL Server};"
#     "Server=tcp:cc-final-server.database.windows.net,1433;"
#     "Database=ccfinaldb;"
#     "Uid=cc-final-server;"
#     "Pwd=cloud@123;"
#     "Encrypt=yes;"
#     "TrustServerCertificate=no;"
#     "Connection Timeout=30;")

# cursor = cnxn.cursor()
# print(cursor)
# cursor.execute("select * from users")
# row = cursor.fetchone()
# while row:
#     print(str(row[0]) + " " + str(row[1]))
#     row = cursor.fetchone()
