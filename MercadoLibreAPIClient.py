#!/usr/bin/python3
import requests
import json
import mysql.connector

publications_url = "https://api.mercadolibre.com/sites/MLU/search?q=autos&offset="
offset = 0

while offset < 1000:
    offset = offset + 50
    url = publications_url + str(offset)
    r = requests.get(url)
    if r.status_code == 200:
        data = r.json()
        data_results = data["results"]
        for result in data_results:
            car_condition = result["condition"]
            publication_link = result["permalink"]
            publication_title = result["title"]
            car_price = result["price"]
            car_price_currency = result["currency_id"]
            car_attributes = result["attributes"]
            publication_thumbnail = result["thumbnail"]
            try:
              ubication = result["seller_address"]["state"]["name"]
            except TypeError:
              ubication = "NA"
            for attribute in car_attributes:
                attribute_id = attribute["id"]
                attribute_value = attribute["value_name"]
                if attribute_id == "ITEM_CONDITION":
                    car_condition2 = attribute_value
                elif attribute_id == "BRAND":
                    car_brand = attribute_value
                elif attribute_id == "DOORS":
                    car_doors = attribute_value
                elif attribute_id == "FUEL_TYPE":
                    car_fuel_type = attribute_value
                elif attribute_id == "KILOMETERS":
                    car_kilometers = attribute_value
                elif attribute_id == "MODEL":
                    car_model = attribute_value
                elif attribute_id == "VEHICLE_YEAR":
                    car_year = attribute_value
                elif attribute_id == "TRIM":
                    car_version = attribute_value
                elif attribute_id == "TRANSMISSION":
                    car_transmission = attribute_value
            mydb = mysql.connector.connect(host="localhost",user="idatos",password="idatos",database="IDATOS")
            mycursor = mydb.cursor()
            sql = "INSERT INTO vehiculo (condicion,precio,moneda,marca,modelo,version,ubicacion,year,tipo_combustible,transmision,kilometraje,cant_puertas,url_imagen,url_publiation,publication_title, source ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            val = (car_condition, car_price, car_price_currency, car_brand, car_model, car_version, ubication, car_year, car_fuel_type, car_transmission, car_kilometers, car_doors, publication_thumbnail, publication_link, publication_title, 'MercadoLibre')
            mycursor.execute(sql, val)
            mydb.commit()
            print(mycursor.rowcount, "record inserted.")
    else:
        print(r)
        print("Error")
