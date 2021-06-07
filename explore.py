# acquire
from env import host, user, password
from pydataset import data
import seaborn as sns
import matplotlib.pyplot as plt

# turn off pink warning boxes
import warnings
warnings.filterwarnings("ignore")

from sklearn.model_selection import train_test_split



def plot_variable_pairs(df, target):
    columns = df[list(df.select_dtypes(exclude='O').columns)].drop(columns=target)
    
    for col in columns:
        
        sns.lmplot(x=col, y=target, data=df,  line_kws={'color': 'red'})
        plt.show()
    

    
def months_to_years(df):
    '''
    This function will take the tenure months and transform them to full years
    '''
    df['tenure_years'] = (df.tenure/12).astype(int)
    return df



def plot_categorical_and_continuous_vars(df, categorical_var, continuous_var):
    '''
    returning the train dataframe with all columns which will hold the 
    continuous and categorical features and output 3 different plots for 
    visualizing a categorical variable and continuous variable
    '''
    #Swarm plot discrete with continuous
    sns.swarmplot(x=categorical_var, y=continuous_var, data=df)
    plt.show()
    sns.stripplot(x=categorical_var, y=continuous_var, data=df)
    plt.show()
    sns.boxplot(x=categorical_var, y=continuous_var, data=df)
    plt.show()
    sns.barplot(x=categorical_var, y=continuous_var, data=df)
    plt.show()