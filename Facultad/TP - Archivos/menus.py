from msvcrt import getwch

def principal() -> str:
    while (True):
        print(
            f"##########################################################\n"
            f"#      _             _     _                             #\n"
            f"#     / \   _ __ ___| |__ (_)_   _____  ___              #\n"
            f"#    / _ \ | '__/ __| '_ \| \ \ / / _ \/ __|             #\n"
            f"#   / ___ \| | | (__| | | | |\ V / (_) \__ \             #\n"
            f"#  /_/   \_\_|  \___|_| |_|_| \_/ \___/|___/             #\n"
            f"#                                Menu Principal          #\n"
            f"#                                                        #\n"
            f"#    ~ (1) Crear Archivo de Texto                        #\n"
            f"#    ~ (2) Ver Directorio                                #\n"
            f"#                                                        #\n"
            f"#                                                        #\n"
            f"#    ~ (9) Salir                                         #\n"
            f"#                                                        #\n"
            f"##########################################################\n"
        )
        opc = getwch()
        
        if( (opc == "1") or (opc == "2") or (opc == "9") ):
            
            return opc
    
        
