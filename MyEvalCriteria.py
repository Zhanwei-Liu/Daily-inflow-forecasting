#!/usr/bin/env python
# coding: utf-8
import numpy as np
from sklearn.metrics import  mean_absolute_error
def rmse(predictions, targets):
    """
        计算均方根误差亦称标准误差；
        RMSE（Root Mean Square Error）
    """
    return np.sqrt(((predictions - targets) ** 2).mean())

def corr(predictions, targets):
    
    """
        计算Pearson相关系数
    """
    return np.corrcoef(predictions.reshape(1,-1),targets.reshape(1,-1))[1,0]

def mae(predictions, targets):
    """
        计算MSE（Mean Square Error）均方误差
    """
    return mean_absolute_error(predictions,targets)

def mape(predictions, targets):
    '''
    //TODO
    '''
    return (abs(predictions - targets)/targets).mean()*100

def accuacy(predictions, targets,p=0.2):
    
    '''
    //TODO
    '''
    result = np.array(abs(predictions - targets)/targets).flatten()
    return result[result<p].shape[0]/result.shape[0]*100

def ce(predictions, targets):
    
    '''
    //TODO
    '''
    ave = targets.mean()
    return 1- ((predictions - targets) ** 2).sum()/np.array([(i-ave)**2 for i in targets]).sum()

def KGE(predictions, targets):
    
    '''
    //TODO
    '''
    r = np.corrcoef(predictions.reshape(1,-1),targets.reshape(1,-1))[1,0]
    sigma = np.std(predictions)/np.std(targets)
    theta = np.mean(predictions)/np.mean(targets)
    return 1-((r-1)**2+(sigma-1)**2+(theta-1)**2)**0.5

def PFC(predictions, targets):
    '''
    //TODO
    '''
    threshold = (targets).mean()/3
    idx = predictions>threshold
    predictions,targets = predictions[idx],targets[idx]
    if (((predictions - targets)**2).sum())**0.5==0:
        return 0
    return (((predictions - targets)**2*targets**2).sum())**0.25/(((predictions - targets)**2).sum())**0.5

def ia(predictions, targets):
    '''
    //TODO
    '''
    ave = np.mean(targets)
    return 1-((predictions - targets) ** 2).sum()/(np.array([(abs(i-ave)+abs(j-ave))**2 for i,j in zip(targets,predictions)])).sum()
def MS4E(predictions, targets):
    '''
    //TODO
    '''
    n = targets.shape[0]
    return ((predictions - targets) ** 4).sum()/n
def BHV(predictions, targets, threshold=1722):
    '''
    //ref(doi):10.1029/2007WR006716
    '''
    idx = predictions>threshold
    predictions,targets = predictions[idx],targets[idx]
    return (predictions - targets).sum()/targets.sum()*100