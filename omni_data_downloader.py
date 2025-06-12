#! usr/bin/env python3
import pyspedas
from pyspedas import tplot
import pytplot
import pandas as pd

#Coded by José Ángel López, lightning2901 on github
# or you may reach me on discipulosde



# This is where the dates are introduced along with a delta_t of the
# data retrieving, we can select 1 min or 5 min changing the number on datatype
# There are many variables of data availables, so if you want to add them
#you may want to un-comment the code below to see them all
#data_dict = pyspedas.projects.omni.data(trange=['2023-11-5', '2023-11-6'], 
#                                        datatype='5min', 
#                                        notplot=True)

#print(data_dict.keys())
print('Welcome! To start downloading data please type as yyyy-mm-dd the start and finish dates you want to download data, it is also posible in YYYY-MM-DD/hh:mm:ss ')
start = print(input('initial Date: '))
final = print(input('initial Date: '))
pyspedas.projects.omni.data(
    trange=[start, end],  # cambia el rango si deseas más días
    datatype='1min',
    varnames=['F', 'flow_speed'],
    notplot=False, time_clip=True
)

#  datos de magnitud del campo magnético (F) y velocidad del flujo flow_speed
# data of magnitude of magnetic field (F) and flux speed
f_data = pytplot.get_data('F')
flow_data = pytplot.get_data('flow_speed')

# Convertir a DataFrame
df = pd.DataFrame({
    'Time': pd.to_datetime(f_data.times, unit='s', origin='unix'),
    'IMF_nT': f_data.y,
    'FlowSpeed_kms': flow_data.y
})

# Guardar a CSV
save_name = print("Write the name you want to save the file, don't forget to add .csv ")
df.to_csv(save_name, index=False)
