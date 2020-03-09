#!/usr/bin/env python
# coding: utf-8
import pandas as pd
data = pd.read_csv('2011-2018再分析和流量数据.csv',index_col=0)
def Preparation(data,Qlag,Rlag,reanalysis=[],isreanalysis=False,leadtime=1):
    """
    Preparation data for model.
    Note: for all reanalysis data, default lag 1.

    Parameters
    ----------
    data : pandas DataFrame,
        All data.
    maxlag: int,range=[1,inf]
        max lag.
    Qlag: list
        all inflow lag.
    Rlag: list
        all rainfall lag.
    reanalysis：list
        name of selected reanalysis variables. 
    Returns
    -------
    X: array_like
        input data.
    y:array_like
        output data

    See Also
    --------
    rely on pandas
    """
    X = pd.DataFrame()
    for q in Qlag:
        X['Q(t-%d)'%(q+leadtime-1)] = data.Q.shift(q+leadtime-1)
    for r in Rlag:
        X['R(t-%d)'%(r+leadtime-1)] = data.real_p.shift(r+leadtime-1)
    X['y'] = data.Q
    if not isreanalysis:
        X.dropna(axis=0,how='any',inplace=True)
        return X.drop(['y'],axis=1),X.y
    else:
        redata = data[reanalysis].shift(leadtime)
        col = ['%s(t-%d)'%(c,leadtime) for c in reanalysis]
        redata.columns = col 
        X = pd.concat([X,redata],axis=1)
        X.dropna(axis=0,how='any',inplace=True)
        return X.drop(['y'],axis=1),X.y

def Preparation2(data,Qlag,Rlag,reanalysis={},isreanalysis=False,leadtime=1):
    """
    Preparation data for model.
    Note: for all reanalysis data, default lag 1.

    Parameters
    ----------
    data : pandas DataFrame,
        All data.
    maxlag: int,range=[1,inf]
        max lag.
    Qlag: list
        all inflow lag.
    Rlag: list
        all rainfall lag.
    reanalysis：dic
        name of selected reanalysis variables. 
    Returns
    -------
    X: array_like
        input data.
    y:array_like
        output data

    See Also
    --------
    rely on pandas
    """
    X = pd.DataFrame()
    if leadtime > max(Qlag):
        X['Q(t-%d)'%(leadtime)] = data.Q.shift(leadtime)
    else:
        for q in Qlag:
            if leadtime > q:
                continue
            else:
                X['Q(t-%d)'%(q)] = data.Q.shift(q)
    if leadtime > max(Rlag):
        X['R(t-%d)'%(leadtime)] = data.real_p.shift(leadtime)
    else:
        for r in Rlag:
            if leadtime > r:
                continue
            else:
                X['R(t-%d)'%(r)] = data.real_p.shift(r)
    X['y'] = data.Q
    if not isreanalysis:
        X.dropna(axis=0,how='any',inplace=True)
        return X.drop(['y'],axis=1),X.y
    else:
        for re in reanalysis:
            if reanalysis[re] >= leadtime:
                X['%s(t-%d)'%(re,reanalysis[re])] = data[re].shift(reanalysis[re]) 
            else:
                X['%s(t-%d)'%(re,leadtime)] = data[re].shift(leadtime) 
        X.dropna(axis=0,how='any',inplace=True)
        return X.drop(['y'],axis=1),X.y

