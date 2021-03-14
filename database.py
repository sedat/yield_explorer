import mysql.connector
db = mysql.connector.connect(host='localhost',
                             user='root',
                             passwd='root',
                             auth_plugin='mysql_native_password',
                             db="yield_db")
cursor = db.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS yield_history ( id INT NOT NULL AUTO_INCREMENT, pool VARCHAR(50) NOT NULL, token_amount FLOAT NOT NULL, token_price FLOAT NOT NULL, deposit FLOAT NOT NULL, yield FLOAT NOT NULL, date datetime NOT NULL DEFAULT CURRENT_TIMESTAMP, PRIMARY KEY ( id ) )')
cursor.execute('CREATE TABLE IF NOT EXISTS lp_yield_history ( id INT NOT NULL AUTO_INCREMENT, pool VARCHAR(50) NOT NULL, first_token_amount FLOAT NOT NULL, second_token_amount FLOAT NOT NULL, first_token_price FLOAT NOT NULL, second_token_price FLOAT NOT NULL, deposit FLOAT NOT NULL, yield FLOAT NOT NULL, date datetime NOT NULL DEFAULT CURRENT_TIMESTAMP, PRIMARY KEY ( id ) )')
