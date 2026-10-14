def carregar_camada_satelite(lista_altitudes):
    for altitude in lista_altitudes:
        if altitude > 10000:
           print(f"Altitude: {altitude} m")
           print("Baixa resolução: visão geral das regiões vulcânicas.")

        elif altitude >= 1000:
             print(f"Altitude: {altitude} m")
             print("Média resolução: vulcões e formações geológicas da região.")

        else:
             print(f"Altitude: {altitude} m")
             print("Alta resolução: detalhes de crateras e formações geológicas.")


altitudes = [15000, 8000, 3000, 900, 500]
carregar_camada_satelite(altitudes)
