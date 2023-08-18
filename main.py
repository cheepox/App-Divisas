import requests

def main():
    url = "https://api.bluelytics.com.ar/v2/latest"

    try:
        response = requests.get(url)
        response.raise_for_status()

        json_data = response.json()

        # Acceder al valor del correo electrónico
        Moneda= "DOLAR BLUE"
        valor_promedio = json_data['blue']['value_avg']
        valor_venta = json_data['blue']['value_sell']
        valor_compra = json_data['blue']['value_buy']
        print(f"Moneda : {Moneda}\n\tValor De Venta :{valor_venta}\n\tValor de Compra : {valor_compra}\n\t VALOR PROMEDIO : {valor_promedio}")

    except requests.exceptions.RequestException as e:
        print("Error al realizar la solicitud:", e)

def segunda():
    url2 = "https://api.bluelytics.com.ar/v2/evolution.json"
    try:
        response2 = requests.get(url2)
        response2.raise_for_status()

        json_data2 = response2.json()

        # Acceder al valor del correo electrónico
        datos = {}
        blue_data_list = [data_dict for data_dict in json_data2 if data_dict["source"] == "Blue"]

        for blue_data in blue_data_list:
            date = blue_data["date"]
            value_sell = blue_data["value_sell"]
            value_buy = blue_data["value_buy"]
            if date not in datos:
                datos[date] = []
            datos[date].append({'VALOR VENTA' :value_sell,'VALOR COMPRA':value_buy})
        testeo = "2023-08-17"
        testeo2 = datos.get(testeo,[])
        print(f"{testeo2}\n")
        print()
        for valores in testeo2:
            precio_venta_dia = valores['VALOR VENTA']
            precio_compra_dia = valores['VALOR COMPRA']
        print(f"PRECIO VENTA {precio_venta_dia}\nPRECIO COMPRA {precio_compra_dia}")


        

    except requests.exceptions.RequestException as e:
        print("Error al realizar la solicitud:", e)

#main()
segunda()
