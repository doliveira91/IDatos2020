#!/usr/bin/python3
import requests
import json
import mysql.connector

car_condition = "usado"
publication_link = "https://www.gallito.com.uy/suzuki-celerio-2015-27600-km-unico-dueno-sin-choques-18675701"
publication_title = "Suzuki Celerio 2015 - 27600 Km -unico Dueno - Sin Choques"
car_price = "10000"
car_price_currency = "USD"
publication_thumbnail = "https://imagenes.gallito.com/images/fotosavi/201129211555670.jpg"
ubication = "Montevideo"
car_brand = "Suzuki"
car_doors = 5
car_fuel_type = "Nafta" 
car_kilometers = "27600 km"
car_model = "Celerio" 
car_year = "2015" 
car_version = "NA" 
car_transmission = "Manual"

mydb = mysql.connector.connect(host="localhost",user="idatos",password="idatos",database="IDATOS")
mycursor = mydb.cursor()
sql = "INSERT INTO vehiculo (condicion,precio,moneda,marca,modelo,version,ubicacion,year,tipo_combustible,transmision,kilometraje,cant_puertas,url_imagen,url_publiation,publication_title, source ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
val = (car_condition, car_price, car_price_currency, car_brand, car_model, car_version, ubication, car_year, car_fuel_type, car_transmission, car_kilometers, car_doors, publication_thumbnail, publication_link, publication_title, 'GallitoLuis')
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")
