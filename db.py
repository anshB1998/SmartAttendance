import pymysql

def insertIntoDB(name):
  # Open database connection
  db = pymysql.connect("localhost","root","test","smartattendance" )

  # prepare a cursor object using cursor() method
  cursor = db.cursor()

  # Prepare SQL query to INSERT a record into the database.
  sql = "INSERT INTO attendance(student_name) VALUES ('"+ name +"')"

  try:
    # Execute the SQL command
    cursor.execute(sql)
    print("Inserting "+str(name)+" into db")
    # Commit your changes in the database
    db.commit()
  except:
    # Rollback in case there is any error
    db.rollback()


  # disconnect from server
  db.close()