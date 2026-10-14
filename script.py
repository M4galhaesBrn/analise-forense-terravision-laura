def carregar_camada_satelite(lista_altitudes):
    for altitude in lista_altitudes:
        if altitude > 10000:
           print(f"Altitude: {altitude} m")
           print("Baixa resolução: mosaico geral da Terra, com visão ampla das regiões vulcânicas.")

        elif altitude >= 1000:
             print(f"Altitude: {altitude} m")
             print("Média resolução: mosaico regional de vulcões e formações geológicas.")

        else:
             print(f"Altitude: {altitude} m")
             print("Alta resolução: detalhes de crateras, cones vulcânicos e estruturas geológicas.")


altitudes = [15000, 8000, 3000, 900, 500]
carregar_camada_satelite(altitudes)
