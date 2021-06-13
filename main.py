import mis_funciones, mis_clases
from getpass import getpass

#Variables globales
bandera = 0
opcion = 0


#Carga de usuarios desde txt
usuarios = mis_funciones.cargar_archivo('usuarios')

#Diccionario del inventario
inventario = {
    'nombre_tienda' : "Tienda Simón Escazú",
    'sede': "Escazú",
    'departamentos': {
        'damas': {
            'nombre': "Damas",
            'productos': []
        },
        'caballeros': {
            'nombre': "Caballeros",
            'productos': []
        },
        'kids': {
            'nombre': "Niños",
            'productos': []
        }

    }
}

#PARA TEST ONLY
nuevo_producto = {
        'Codigo': 24568,
        'Nombre': 'i5 10500K 4.5Ghz',
        'Precio_Unitario': 10.0,
        'Cantidad': 10
    }
nuevo_producto2 = {
        'Codigo': 65842,
        'Nombre': 'Razer Nari Ultimate',
        'Precio_Unitario': 110000.0,
        'Cantidad': 6
    }
inventario['departamentos']['caballeros']['productos'].append(nuevo_producto)
inventario['departamentos']['caballeros']['productos'].append(nuevo_producto2)

#Presentacion de portada
mis_funciones.limpiar_consola()
print(mis_funciones.get_logo())
print(mis_funciones.get_portada())
respuesta = input(f"{mis_clases.consolaColor.AMARILLO}Presione cualquier tecla para continuar con el inicio de sesión...{mis_clases.consolaColor.NORMAL}")

while bandera == 0:      
    mis_funciones.limpiar_consola()    
    print("\n")
    print(mis_funciones.get_logo())

    #Login    
    print(mis_funciones.get_login()) 
    
    nombre_usuario = input(f"{mis_clases.consolaColor.VERDE}Usuario: {mis_clases.consolaColor.NORMAL}")
    password = getpass(f"{mis_clases.consolaColor.VERDE}Contraseña: {mis_clases.consolaColor.NORMAL}")    

    usuario_actual = mis_funciones.encontrar_usuario(usuarios, nombre_usuario, password)

    mis_funciones.limpiar_consola()  
    if usuario_actual == None:              
        print(f"{mis_clases.consolaColor.ROJO}¡Usuario y contraseña inválida!{mis_clases.consolaColor.NORMAL}") 
        respuesta = input(f"{mis_clases.consolaColor.AMARILLO}Presione cualquier tecla para salir...{mis_clases.consolaColor.NORMAL}")  
        break     
    else:   
        #Sistema de inventario    
        print(f"{mis_clases.consolaColor.AMARILLO}Bienvenido al sistema de inventarios de tienda Simón, {usuario_actual['full_name']} es un placer atenderle{mis_clases.consolaColor.NORMAL}")        
        respuesta = input(f"{mis_clases.consolaColor.AMARILLO}¿Desea ingresar al sistema de inventarios?(Si/No) {mis_clases.consolaColor.NORMAL}\n")

        if respuesta.lower().strip() == 'si':
            while bandera == 0:
                mis_funciones.limpiar_consola()
                print(mis_funciones.get_departamento())
                
                opcion = mis_funciones.opcion_menu(4)
                
                if opcion == 1:
                    bandera = mis_funciones.menu_por_departamento(usuario_actual, inventario['departamentos']['damas']) 
                elif opcion == 2:
                    bandera = mis_funciones.menu_por_departamento(usuario_actual,inventario['departamentos']['caballeros'])
                elif opcion == 3:
                    bandera = mis_funciones.menu_por_departamento(usuario_actual,inventario['departamentos']['kids'])                                        
                else:
                    break
                            
    break

mis_funciones.limpiar_consola()
print(mis_funciones.get_gracias())
print(mis_funciones.get_portada())




