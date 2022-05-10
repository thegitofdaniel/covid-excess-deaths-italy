# import packages
import csv
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def reduce_df(df
              ,cols=['MM','T_15','T_16','T_17','T_18','T_19','T_20']
             ):
    sup = df[cols]
    sup = sup.groupby(cols[0]).sum()
    sup.columns = [2015,2016,2017,2018,2019,2020]
    sup = sup/1000
    return sup

def plot_lines(df):
    
    # build image
    sns.set_style('darkgrid')
    fig, ax = plt.subplots(1,1,figsize=(16, 8))

    # series
    for c in [2015,2016,2017,2018,2019,2020]:
        sns.lineplot(x=df.index-1,y=df[c],label=c)
        plt.annotate(c,(df.index[0]-1,df[c].tolist()[0]),fontsize=12,fontweight='bold')

    # graph elements    
    ax.set_title('Total Deaths in Italy by Month',fontsize=16,fontweight='bold')
    ax.set_ylabel("deaths ('000)",fontsize=16)
    ax.set_xlabel('',fontsize=16)
    ax.legend(loc='lower left',ncol=2)
    plt.yticks(fontsize=12)
    plt.xticks(ticks=[0,1,2],labels=['January','February','March'],rotation=0,fontsize=16)
    
    #ax.set_ylim(40,80)
    
    # show
    plt.show()
    
def plot_bars(df
              ,annotate=True
              ,gr=1
             ):

    # build image
    sns.set_style('darkgrid')
    ax = df.plot(kind="bar",figsize=(16, 8))

    if annotate:
        # february -> just a line
        plt.bar(x=1.207,
                y=df.loc[2,2020]*.99,
                height=0.1,
                width=0.0825,
                fc=(0,0,0,0),
                edgecolor='black',
                linewidth=2)
        
        # march
        plt.bar(x=2.207,
                y=df.loc[3,2020]-13.710*gr,
                height=13.710*gr,
                width=0.0825,
                fc=(0,0,0,0),
                edgecolor='black',
                linewidth=2)

        plt.text(x=2.19,
                 y=df.loc[3,2020]-10*gr,
                 s='CV-19',
                 rotation=90,
                 fontsize=16,
                 c='white')

    for i in range(3):
        plt.text(i-0.230,2,s='2015',rotation=90,fontsize=16,c='white')
        plt.text(i-0.145,2,s='2016',rotation=90,fontsize=16,c='white')
        plt.text(i-0.060,2,s='2017',rotation=90,fontsize=16,c='white')
        plt.text(i+0.025,2,s='2018',rotation=90,fontsize=16,c='white')
        plt.text(i+0.110,2,s='2019',rotation=90,fontsize=16,c='white')
        plt.text(i+0.195,2,s='2020',rotation=90,fontsize=16,c='white')

    # graph elements    
    #plt.xticks(df.index,fontsize=12)
    plt.yticks(fontsize=12)
    plt.xticks(ticks=[0,1,2],labels=['January','February','March'],rotation=0,fontsize=16)
    ax.set_title('Total Deaths in Italy by Month (6866 Comuni)',fontsize=16,fontweight='bold')
    ax.set_ylabel("deaths ('000)",fontsize=16)
    ax.set_xlabel('',fontsize=16)
    ax.get_legend().remove()
    #ax.set_ylim(0,80)

    # show
    plt.show()