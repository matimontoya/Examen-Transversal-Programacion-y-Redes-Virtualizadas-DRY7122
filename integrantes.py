# integrantes.py
# Script para listar los integrantes oficiales del grupo - Examen Transversal DRY7122

def mostrar_integrantes():
    # Estructura de datos tipo lista indexada con los datos del grupo
    grupo_dry7122 = [
        "Matias Montoya",
        "Maximiliano Arratia"
    ]
    
    print("\n========================================================")
    print("  INTEGRANTES EXAMEN TRANSVERSAL - ASIGNATURA DRY7122   ")
    print("========================================================")
    
    # Bucle iterativo for para recorrer la lista de strings
    for alumno in grupo_dry7122:
        print(f" Alumno: {alumno}")
        
    print("========================================================\n")

if __name__ == "__main__":
    mostrar_integrantes()