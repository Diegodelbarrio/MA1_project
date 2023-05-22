import pandas as pd
import os 
import matplotlib.pyplot as plt

folder_path = '/Users/diegodelbarrio/Desktop/Documentos_ETSII/MII/Bruface/1º Cuatri/Project in Electromechanical engineering /MA1_project_code/NASA_dataset/_csv/B0005'
metadata_file = '/Users/diegodelbarrio/Desktop/Documentos_ETSII/MII/Bruface/1º Cuatri/Project in Electromechanical engineering /MA1_project_code/NASA_dataset/metadata.csv'
charge_type = ['charge', 'discharge']
battery_name = ["B0005", "B0006", "B0007"]
ruta_plots = "/Users/diegodelbarrio/Desktop/Documentos_ETSII/MII/Bruface/1º Cuatri/Project in Electromechanical engineering /MA1_project_code/Plots/"

# get a list of csv files in the folder
csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]
#sort the cvs files 
csv_files.sort()
#create a dataFrame of the metadata file 
meta_df = pd.read_csv(metadata_file)

df_charge_B0005_metadata = meta_df[(meta_df["type"]== charge_type[0]) & (meta_df["battery_id"]==battery_name[0])]

df_charge_B0006_metadata = meta_df[(meta_df["type"]== charge_type[0]) & (meta_df["battery_id"]==battery_name[1])]

df_charge_B0007_metadata = meta_df[(meta_df["type"]== charge_type[0]) & (meta_df["battery_id"]==battery_name[2])]

#print(df_charge_B0005.head())

filename_0005_list = df_charge_B0005_metadata["filename"].to_list()
filename_0006_list = df_charge_B0006_metadata["filename"].to_list()
filename_0007_list = df_charge_B0007_metadata["filename"].to_list()

################ Charge: time-current ##############

fig, ax = plt.subplots()

for filename in filename_0005_list: 

    df = pd.read_csv(folder_path + "/" + filename)
    
    ax.plot(df["Time"], df["Current_measured"], alpha = 0.7)
     
ax.set_xlabel('Time')
ax.set_ylabel('Current Measured')
ax.set_title('CC-CV')
ax.set_ylim(0, 1.6)

plt.show() 

fig.savefig(ruta_plots + "charge_time_current_all_cicles.png", bbox_inches='tight', dpi=300)



################ Charge: time-voltage ##############

fig, ax = plt.subplots()

for filename in filename_0005_list: 

    df = pd.read_csv(folder_path + "/" + filename)
    
    ax.plot(df["Time"], df["Voltage_measured"], alpha = 0.7)
    plt.show()
     
ax.set_xlabel('Time')
ax.set_ylabel('Voltage Measured')
ax.set_title('CC-CV')
#ax.set_ylim(3, 4.3)


fig.savefig(ruta_plots + "charge_time_voltage_all_cicles.png", bbox_inches='tight', dpi=300)


################ Discharge: time-current ##############

fig, ax = plt.subplots()

for filename in filename_0005_list: 

    df = pd.read_csv(folder_path + "/" + filename)
    
    ax.plot(df["Time"], df["Voltage_measured"], alpha = 0.7)
    plt.show()
     
ax.set_xlabel('Time')
ax.set_ylabel('Voltage Measured')
ax.set_title('CC-CV')
#ax.set_ylim(3, 4.3)


fig.savefig(ruta_plots + "charge_time_voltage_all_cicles.png", bbox_inches='tight', dpi=300)



