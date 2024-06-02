def OU_process(mu,sigma,theta,n,paths,x0,T):
    dt=T/n-1
    X=np.zeros((paths,n))
    X[:,0]=x0
    std_dt=np.sqrt(((sigma**2)/(2*mu))*(1-np.exp(-2*mu*dt)))
    W=np.random.normal(0,1,size=(paths,n))
    for t in range(0,n-1):
        X[:,t+1]=theta+(X[:,t]-theta)*np.exp(-1*mu*dt)+std_dt*W[:,t]
    return X
