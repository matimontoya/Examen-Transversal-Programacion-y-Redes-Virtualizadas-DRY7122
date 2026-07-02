from netmiko import ConnectHandler

# Datos del router
router = {
    'device_type': 'cisco_ios',
    'host': '192.168.48.131',
    'username': 'cisco',
    'password': 'cisco123!',
}

# Comandos de configuración para EIGRP Nombrado (AS 100)
eigrp_config = [
    'router eigrp MATIAS-AR',
    'address-family ipv4 unicast autonomous-system 100',
    'af-interface default',
    'passive-interface',
    'exit-af-interface',
    'no af-interface GigabitEthernet1',
    'exit-address-family',
    'router eigrp MATIAS-AR',
    'address-family ipv6 unicast autonomous-system 100',
    'topology base',
    'exit-af-topology',
    'af-interface default',
    'passive-interface',
    'exit-af-interface',
    'no af-interface GigabitEthernet1',
    'exit-address-family'
]

try:
    # Conexión al dispositivo
    with ConnectHandler(**router) as net_connect:
        print(f"--- Conectado a {net_connect.host} ---")
        
        # 1. Configuración de EIGRP Nombrado
        print("\nConfigurando EIGRP Nombrado...")
        output = net_connect.send_config_set(eigrp_config)
        print(output)
        
        # Mostrar resultado específico de EIGRP
        eigrp_check = net_connect.send_command("show running-config | section eigrp")
        print("\n--- Resultado EIGRP ---")
        print(eigrp_check)
        
        # 2. Información de IP y estado de interfaces
        ip_info = net_connect.send_command("show ip interface brief")
        print("\n--- Estado de Interfaces IP ---")
        print(ip_info)
        
        # 3. Running-config completo
        run_config = net_connect.send_command("show running-config")
        print("\n--- Running Config Obtenido ---")
        # Mostramos solo las primeras líneas para no saturar el chat
        print("\n".join(run_config.splitlines()[:20])) 
        
        # 4. Show version
        version_info = net_connect.send_command("show version")
        print("\n--- Información de Versión ---")
        print(version_info[:500]) # Mostramos solo el encabezado

except Exception as e:
    print(f"Error en la automatización: {e}")