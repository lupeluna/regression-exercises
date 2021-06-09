

def plot_residuals(y, yhat):  
    #baseline
    df['yhat_baseline'] = df.y.mean()
    
    # residuals
    df['residuals'] = df.y - df.yhat
    df['baseline_residuals'] = df.y - df.yhat_baseline
    
    fig, ax = plt.subplots(figsize=(13, 7))
    ax.hist(df.baseline_residuals, label='baseline residuals', alpha=.6)
    ax.hist(df.residuals, label='model residuals', alpha=.6)
    ax.legend()
    
    
    
def regression_errors(y, yhat, df):
    #SSE
    SSE = mean_squared_error(df[y], df[yhat])*len(df)   
    #ESS
    ESS = sum((df[yhat] - df[y].mean())**2)
    #TSS
    TSS = ESS + SSE
    #MSE
    MSE = SSE/len(df)
    #RMSE
    RMSE = sqrt(MSE)
    return SSE, ESS, TSS, MSE, RMSE



def baseline_mean_errors(y, yhat, df):
    '''
    This function takes in actual value and predicted value
    then outputs: the SSE, MSE, and RMSE for the baseline model
    '''
    df['residuals_baseline']= df[y]- df[yhat]
    sse_baseline = (df.residuals_baseline **2).sum()
    n = df.shape[0]
    mse_baseline = sse_baseline/n
    rmse_baseline = math.sqrt(mse_baseline)

    print(f''' 
        sse_baseline: {sse_baseline: .4f}
        mse_baseline: {mse_baseline: .4f}
        rmse_baseline: {rmse_baseline: .4f}
        ''')
    
    

    
def better_than_baseline(y, yhat, df):
    #baseline 
    MSE_baseline = mean_squared_error(df[y], df.yhat_baseline)
    RMSE_baseline = sqrt(MSE_baseline)
    
    #Model
    MSE = mean_squared_error(df[y], df[yhat])
    #root mean squared error (RMSE)
    RMSE = sqrt(MSE)
    print ('Model performs better than the baseline')
    if RMSE < RMSE_baseline :
        return True
    else:
        return False  
    