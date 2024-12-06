from mysql.connector import MySQLConnection, Error

# Connect to the database
#mydbProyectoCleaver = MySQLConnection(
    #host="bdbkdmoqb7hpy245kzg4-mysql.services.clever-cloud.com",
    #user="usbpsjyeeg8faqcs",
    #password="Sm12X6iYojG3GwccIwh5",
    #database="bdbkdmoqb7hpy245kzg4",
    #port=3306
#)
#cursorCleaver = mydbProyectoCleaver.cursor()

mydbProyectoLocal = MySQLConnection(
    host="localhost",
    user="root",
    password="",
    database="ti360",
    port=3306
)
cursorLocal = mydbProyectoLocal.cursor()