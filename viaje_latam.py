import requests
import urllib.parse

# Reemplaza con tu clave de Graphhopper
key = "17102e5e-af0a-4ddd-a86f-c7934e192837"
geocode_url = "https://graphhopper.com/api/1/geocode?"
route_url = "https://graphhopper.com/api/1/route?"

def obtener_coordenadas(ciudad):
    url = geocode_url + urllib.parse.urlencode({"q": ciudad, "limit": "1", "key": key})
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        json_data = respuesta.json()
        if "hits" in json_data and len(json_data["hits"]) > 0:
            # Aquí está la corrección: agregar ["point"]
            lat = json_data["hits"][0]["point"]["lat"]
            lng = json_data["hits"][0]["point"]["lng"]
            return f"{lat},{lng}"
    return None

while True:
    print("\n--- Planificador de Viajes (Graphhopper) ---")
    origen = input("Ingrese la Ciudad de Origen (o presione 's' para salir): ")
    if origen.lower() == 's':
        print("Saliendo del programa...")
        break
        
    destino = input("Ingrese la Ciudad de Destino (o presione 's' para salir): ")
    if destino.lower() == 's':
        print("Saliendo del programa...")
        break
    
    print("\nTipos de medio de transporte:")
    print("1. Automóvil")
    print("2. Caminando")
    print("3. Bicicleta")
    transporte_opcion = input("Elija el medio de transporte a utilizar (1/2/3): ")
    
    vehicle = "car"
    if transporte_opcion == "2":
        vehicle = "foot"
    elif transporte_opcion == "3":
        vehicle = "bike"

    # Obtener coordenadas de ambas ciudades
    coord_origen = obtener_coordenadas(origen)
    coord_destino = obtener_coordenadas(destino)

    if not coord_origen or not coord_destino:
        print("\n[ERROR] No se pudieron encontrar las coordenadas de una o ambas ciudades. Revisa los nombres.\n")
        continue

    # Construir URL de ruta asegurando que el idioma sea español
    url_ruta = f"{route_url}point={coord_origen}&point={coord_destino}&vehicle={vehicle}&locale=es&key={key}"
    
    try:
        respuesta_ruta = requests.get(url_ruta)
        
        if respuesta_ruta.status_code != 200:
            print(f"\n[ERROR] Falló la conexión. Código HTTP: {respuesta_ruta.status_code}")
            print(f"Mensaje del servidor: {respuesta_ruta.text}")
            print("Revisa tu API Key de Graphhopper.\n")
            continue

        json_ruta = respuesta_ruta.json()
        
        if "paths" in json_ruta:
            ruta = json_ruta["paths"][0]
            
            kilometros = ruta["distance"] / 1000
            millas = kilometros / 1.60934
            
            milisegundos = ruta["time"]
            segundos = int((milisegundos / 1000) % 60)
            minutos = int((milisegundos / (1000 * 60)) % 60)
            horas = int((milisegundos / (1000 * 60 * 60)))
            duracion_formateada = f"{horas:02d}:{minutos:02d}:{segundos:02d}"
            
            print("\n=============================================")
            print("RESUMEN DEL VIAJE")
            print("=============================================")
            print(f"Duración del viaje : {duracion_formateada}")
            print(f"Distancia en millas: {millas:.2f} mi")
            print(f"Distancia en km    : {kilometros:.2f} km")
            
            print("\nNarrativa del viaje:")
            for instruccion in ruta["instructions"]:
                distancia_tramo = instruccion['distance'] / 1000
                print(f"- {instruccion['text']} ({distancia_tramo:.2f} km)")
            print("=============================================\n")
        else:
            print("\nNo se encontró una ruta disponible para el medio de transporte seleccionado entre estas ciudades.\n")
            
    except Exception as e:
        print(f"\nOcurrió un error en la ejecución: {e}\n")