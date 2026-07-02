from ncclient import manager
import sys

# Credenciales y host
host = "192.168.48.131"
port = 830
user = "cisco"
password = "cisco123!"

# XML para cambiar el hostname y crear la Loopback 11
netconf_config = """
<config>
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
    <hostname>Router-Montoya-Arratia</hostname>
    <interface>
      <Loopback>
        <name>11</name>
        <ip>
          <address>
            <primary>
              <address>11.11.11.11</address>
              <mask>255.255.255.255</mask>
            </primary>
          </address>
        </ip>
      </Loopback>
    </interface>
  </native>
</config>
"""

try:
    # Conexión SSH mediante NETCONF
    with manager.connect(host=host, port=port, username=user, password=password, 
                         hostkey_verify=False, device_params={'name': 'iosxe'}) as m:
        
        print(f"Conectado exitosamente a {host} mediante NETCONF/SSH.")
        
        # Aplicar configuración
        m.edit_config(target="running", config=netconf_config)
        print("Configuración aplicada: Hostname cambiado y Loopback 11 creada.")

except Exception as e:
    print(f"Error al conectar o configurar: {e}")