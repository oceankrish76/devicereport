import mysql.connector

for x in myresult:
  print(x)

class Report:
  def __init__(self, id, device_id, location, date_created):
    self.id = id
    self.device_id = device_id
    self.location = location
    self.nadate_createdme = date_created
    self.db = mysql.connector.connect(
      host="localhost",
      user="yourusername",
      password="yourpassword",
      database="mydatabase"
    )
  def connect(self):

    cursor = db.cursor()
    cursor.execute("SELECT * FROM customers")
    result = cursor.fetchall()

  def get_devices(self):

    pass