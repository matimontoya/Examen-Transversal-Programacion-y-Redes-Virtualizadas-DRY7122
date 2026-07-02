
def evaluar_vlan():
    print("\n--- ANALIZADOR DE RANGOS DE VLAN (Cisco Architecture) ---")
    
    try:
        vlan_id = int(input("[?] Ingrese el número de VLAN a evaluar: "))
        
        if vlan_id == 1:
            print(f"[*] VLAN {vlan_id}: Corresponde a la VLAN predeterminada (Default Rango Normal).")
        elif vlan_id >= 2 and vlan_id <= 1001:
            print(f"[+] VLAN {vlan_id}: Pertenece al Rango NORMAL (Uso común en redes LAN).")
        elif vlan_id >= 1002 and vlan_id <= 1005:
            print(f"[*] VLAN {vlan_id}: Reservada por Cisco para tecnologías heredadas (Token Ring/FDDI).")
        elif vlan_id >= 1006 and vlan_id <= 4094:
            print(f"[+] VLAN {vlan_id}: Pertenece al Rango EXTENDIDO (Uso en proveedores de servicios/MetroEthernet).")
        else:
            print(f"[-] Código {vlan_id} INCORRECTO: El ID de VLAN debe estar en el rango de 1 a 4094.")
            
    except ValueError:
        print("[-] Error crítico: Debe ingresar exclusivamente un valor numérico entero.")
    print("---------------------------------------------------------\n")

if __name__ == "__main__":
    evaluar_vlan()