import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='db-learn.gec.io',
                             user='gco_test',
                             password='go_apple!',
                             db='teacher',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO `TblUsers` (`name`, `password`) VALUES (%s, %s)"
        cursor.execute(sql, ('newbie', 'very-secret'))

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `user_id`, `password` FROM `TblUsers` WHERE `name`=%s"
        cursor.execute(sql, ('Santa',))
        result = cursor.fetchone()
        print(result)
finally:
    connection.close()