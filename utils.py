import pandas as pd

def get_dfsettimanale_from_df(df_t, column, target):
    '''
    
    Parameters
    ----------
        - df_t:       pandas.DataFrame with DateTimeIndex
        - column:     first dataframe columns for group by
        - target:     column for sum
    returns
    -------
    pandas.DataFrame with DateTimeIndex
    
    '''
    columns = list(df_t[column].unique())
    i = 0
    for c in columns:

        df_f = df_t[df_t[column]==c].resample('W')[[target]].sum().fillna(0)
        df_f[column]=c
        if i == 0:
            df_settimanale = df_f.copy()
            i=1
        else:
            df_settimanale = df_settimanale.append(df_f)

    return df_settimanale
