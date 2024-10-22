# Problema 1
# Caso 1

import pandas as pd

df_airbnb = pd.read_csv('./data/airbnb.csv')

filtro = (df_airbnb['reviews'] > 10) & (df_airbnb['overall_satisfaction'] > 4)
df_filtrado = df_airbnb[filtro]

df_ordenado = df_filtrado.sort_values(by=['overall_satisfaction', 'reviews'], ascending=[False, False])

alojamientos_para_alicia = df_ordenado.head(3)

print(alojamientos_para_alicia)

# Caso 2

import pandas as pd

df_airbnb = pd.read_csv('./data/airbnb.csv')

ids = [97503, 90387]
df_roberto_clara = df_airbnb[df_airbnb['room_id'].isin(ids)]

df_roberto_clara.to_excel('roberto.xls', index=False)

print(df_roberto_clara)

# Caso 3

import pandas as pd

df_airbnb = pd.read_csv('./data/airbnb.csv')

filtro_presupuesto = df_airbnb[df_airbnb['price'] <= 50]

shared_rooms = filtro_presupuesto[filtro_presupuesto['room_type'] == 'Shared room']

shared_rooms_ordenadas = shared_rooms.sort_values(by='overall_satisfaction', ascending=False)

if len(shared_rooms_ordenadas) < 10:
    faltan = 10 - len(shared_rooms_ordenadas)

    otras_propiedades = filtro_presupuesto[filtro_presupuesto['room_type'] != 'Shared room']
    otras_propiedades_ordenadas = otras_propiedades.sort_values(by='price', ascending=True).head(faltan)

    resultado = pd.concat([shared_rooms_ordenadas, otras_propiedades_ordenadas])
else:
    resultado = shared_rooms_ordenadas.head(10)

print(resultado)

# Problema 2
# Caso 1



