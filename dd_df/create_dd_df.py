import pandas as pd
from getsig import getsig
from scipy.interpolate import interp1d
from scipy.signal import medfilt

def create_dd_df(shotnr=30554, tBegin=1.0, tEnd=6.5, dt=0.1,
                 dne_data=['DNE','neDdel_2',17,'sfp',21],
                 ouput_file=None):
    """Returns a pandas dataframe"""
    times = np.arange(tBegin, tEnd+dt, dt)
    
    beta = getsig(shotnr, 'TOT', 'beta_N')
    wmhd = getsig(shotnr, 'TOT', 'Wmhd')
    taue = getsig(shotnr, 'TOT', 'tau_tot')
    h98 = getsig(shotnr, 'TTH', 'H/L-facs')
    h98y2_index = 7
    
    nev_shotfile = 'DNE'
    nev_signal = 'neDdel_2'
    nev_channel = 17
    nev_experiment = 'sfp'
    medfilt_pts = 21

    #Divertor Spectroscpy data
    nev_shotfile = dne_data[0]
    nev_signal = dne_data[1]
    nev_channel = int(dne_data[2])
    nev_experiment = dne_data[3]
    medfilt_pts = int(dne_data[4])

    dne = getsig(shotnr, nev_shotfile, nev_signal, exper=nev_experiment)
    
    #Interpolations
    interp_beta = interp1d(beta.time, beta.data)
    beta_df_entry = interp_beta(times)

    interp_wmhd = interp1d(wmhd.time, wmhd.data)
    wmhd_df_entry = interp_wmhd(times)

    interp_taue = interp1d(taue.time, taue.data)
    taue_df_entry = interp_taue(times)

    interp_h98 = interp1d(h98.time, h98.data[:,h98y2_index])
    h98_df_entry = interp_h98(times)

    interp_nev = interp1d(dne.time, medfilt(dne.data[:, nev_channel], medfilt_pts))
    nev_df_entry = interp_nev(times)
    
    dict_df = {'time':times, 'nev':nev_df_entry, 'h98y2':h98_df_entry, 'taue':taue_df_entry, 'beta':beta_df_entry, 'wmhd':wmhd_df_entry}
    ddf = pd.DataFrame(data=dict_df)
    df = ddf[['time','nev','beta','taue','h98y2','wmhd']]
    
    #if output_file is not None:
    #    writer = pd.ExcelWriter(output_file)
    #    df.to_excel(writer,'Sheet1')
    
    return df
