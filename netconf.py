from ncclient import manager


router = {
    "host": "192.168.56.106",
    "port": 830,
    "username": "cisco",
    "password": "cisco123!",
    "hostkey_verify": False
}


with manager.connect(**router) as m:

    print("Conectado al CSR1000v")


    config = """
    <config>
      <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">

        <hostname>MaxArratia-MatiasMontoya</hostname>


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


    respuesta = m.edit_config(
        target="running",
        config=config
    )


    print("Configuración enviada correctamente")
    print(respuesta)
