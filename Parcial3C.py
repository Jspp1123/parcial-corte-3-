def inicializar_grupo(equipos):
    """Crea la estructura inicial para los equipos del grupo."""
    tabla = {}
    for equipo in equipos:
        tabla[equipo] = {
            "PJ": 0,  
            "PG": 0,  
            "PE": 0,  
            "PP": 0,  
            "GF": 0,  
            "GC": 0,  
            "DG": 0,  
            "PTS": 0  
        }
    return tabla

def registrar_partido(tabla, equipo1, goles1, equipo2, goles2):
    """Registra el resultado de un partido y actualiza las estadísticas."""
    if equipo1 not in tabla or equipo2 not in tabla:
        print("Error: Uno o ambos equipos no pertenecen a este grupo.")
        return

    
    tabla[equipo1]["PJ"] += 1
    tabla[equipo2]["PJ"] += 1
    
    tabla[equipo1]["GF"] += goles1
    tabla[equipo1]["GC"] += goles2
    tabla[equipo2]["GF"] += goles2
    tabla[equipo2]["GC"] += goles1

    
    if goles1 > goles2:
        tabla[equipo1]["PG"] += 1
        tabla[equipo1]["PTS"] += 3
        tabla[equipo2]["PP"] += 1
    elif goles2 > goles1:
        tabla[equipo2]["PG"] += 1
        tabla[equipo2]["PTS"] += 3
        tabla[equipo1]["PP"] += 1
    else:
        tabla[equipo1]["PE"] += 1
        tabla[equipo1]["PTS"] += 1
        tabla[equipo2]["PE"] += 1
        tabla[equipo2]["PTS"] += 1

    
    tabla[equipo1]["DG"] = tabla[equipo1]["GF"] - tabla[equipo1]["GC"]
    tabla[equipo2]["DG"] = tabla[equipo2]["GF"] - tabla[equipo2]["GC"]

def mostrar_tabla(tabla):
    """Ordena y muestra la tabla de posiciones en la consola."""
    
    tabla_ordenada = sorted(
        tabla.items(), 
        key=lambda x: (x[1]["PTS"], x[1]["DG"]), 
        reverse=True
    )

    print("\n" + "="*55)
    print(f"{'POS':<4}{'EQUIPO':<15}{'PJ':<4}{'PG':<4}{'PE':<4}{'PP':<4}{'GF':<4}{'GC':<4}{'DG':<4}{'PTS':<4}")
    print("="*55)
    
    for i, (equipo, stats) in enumerate(tabla_ordenada, 1):
        print(f"{i:<4}{equipo:<15}{stats['PJ']:<4}{stats['PG']:<4}{stats['PE']:<4}{stats['PP']:<4}{stats['GF']:<4}{stats['GC']:<4}{stats['DG']:<+4}{stats['PTS']:<4}")
    print("="*55 + "\n")


if __name__ == "__main__":
    
    equipos_grupo = ["Colombia", "Alemania", "Japón", "Senegal"]
    grupo_h = inicializar_grupo(equipos_grupo)

   
    registrar_partido(grupo_h, "Colombia", 2, "Japón", 1)
    registrar_partido(grupo_h, "Alemania", 1, "Senegal", 1)

    
    registrar_partido(grupo_h, "Colombia", 3, "Senegal", 0)
    registrar_partido(grupo_h, "Alemania", 2, "Japón", 2)

   
    print("TABLA DE POSICIONES EN CURSO:")
    mostrar_tabla(grupo_h)