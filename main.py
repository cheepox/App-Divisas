import requests
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def Valor_RT():
    url = "https://api.bluelytics.com.ar/v2/latest"

    try:
        response = requests.get(url)
        response.raise_for_status()

        json_data = response.json()

        # Acceder al valor de las variables
        Moneda= "DOLAR BLUE"
        valor_promedio = json_data['blue']['value_avg']
        valor_venta = json_data['blue']['value_sell']
        valor_compra = json_data['blue']['value_buy']
        print(f"Moneda : {Moneda}\n\tValor De Venta :{valor_venta}\n\tValor de Compra : {valor_compra}\n\t VALOR PROMEDIO : {valor_promedio}")

    except requests.exceptions.RequestException as e:
        print("Error al realizar la solicitud:", e)

def Historia():
    url2 = "https://api.bluelytics.com.ar/v2/evolution.json"
    try:
        response2 = requests.get(url2)
        response2.raise_for_status()

        json_data2 = response2.json()

        # Acceder al valor de los datos
        datos = {}
        blue_data_list = [data_dict for data_dict in json_data2 if data_dict["source"] == "Blue"]

        for blue_data in blue_data_list:
            date = blue_data["date"]
            value_sell = blue_data["value_sell"]
            value_buy = blue_data["value_buy"]
            if date not in datos:
                datos[date] = []
            datos[date].append({'VALOR VENTA' :value_sell,'VALOR COMPRA':value_buy})
        fecha = "2023-08-18"
        valor_dia = datos.get(fecha,[])
        #PASAR DEL DICCIONARIO A VARIABLES LOS VALORES DE VENTA Y COMPRA
        for valores in valor_dia:
            precio_venta_dia = valores['VALOR VENTA']
            precio_compra_dia = valores['VALOR COMPRA']
        print(f"PRECIO VENTA {precio_venta_dia}\nPRECIO COMPRA {precio_compra_dia}")


        

    except requests.exceptions.RequestException as e:
        print("Error al realizar la solicitud:", e)


def Grafico(dias_atras):
    url2 = "https://api.bluelytics.com.ar/v2/evolution.json"
    try:
        response2 = requests.get(url2)
        response2.raise_for_status()

        json_data2 = response2.json()

        # Calcular la fecha límite
        fecha_limite = datetime.now() - timedelta(days=dias_atras)
        fecha_limite_str = fecha_limite.strftime('%Y-%m-%d')

        # Filtrar los datos para incluir solo las fechas dentro del rango deseado
        datos = {}
        blue_data_list = [data_dict for data_dict in json_data2 if data_dict["source"] == "Blue"]
        for blue_data in blue_data_list:
            date = blue_data["date"]
            if date >= fecha_limite_str:
                value_sell = blue_data["value_sell"]
                value_buy = blue_data["value_buy"]
                if date not in datos:
                    datos[date] = []
                datos[date].append({'VALOR VENTA' :value_sell,'VALOR COMPRA':value_buy})

        # Preparar los datos para los gráficos
        fechas = list(datos.keys())
        precios_venta = [data[0]['VALOR VENTA'] for data in datos.values()]
        precios_compra = [data[0]['VALOR COMPRA'] for data in datos.values()]

        # Invertir el orden de las listas para mostrar de izquierda a derecha
        fechas.reverse()
        precios_venta.reverse()
        precios_compra.reverse()

        # Crear la figura con subplots
        fig, axs = plt.subplots(1, 2, figsize=(12, 6))  # 1 fila, 2 columnas

        # Generar el gráfico de Precio de Venta en el primer subplot
        axs[0].plot(fechas, precios_venta, marker='o', color='b')
        axs[0].set_title(f'Evolución del Precio de Venta (Blue) en los últimos {dias_atras} días')
        axs[0].set_xlabel('Fecha')
        axs[0].set_ylabel('Precio de Venta')
        axs[0].grid(True)

        # Generar el gráfico de Valor de Compra en el segundo subplot
        axs[1].plot(fechas, precios_compra, marker='o', color='r')
        axs[1].set_title(f'Evolución del Valor de Compra (Blue) en los últimos {dias_atras} días')
        axs[1].set_xlabel('Fecha')
        axs[1].set_ylabel('Valor de Compra')
        axs[1].grid(True)

        plt.tight_layout()

        # Mostrar los gráficos en la misma ventana
        plt.show()  

    except requests.exceptions.RequestException as e:
        print("Error al realizar la solicitud:", e)

Valor_RT()
#Historia()
Grafico(dias_atras = int(input("Ingrese cuantos dias atras quiere ir :")))