import numpy as np

def kzhrmodel(t,K,tau):
    arr=(np.array([K]).T*np.exp(-t/np.array([tau]).T))
    return np.sum(arr,axis=0)

def H2RG(rate=1.e-4):
    K1=15625.4
    K2=646.1
    K3=146.
    t1=324.3 #second
    t2=2206.5
    t3=23570.
    K=np.array([K1,K2,K3])
    tau=np.array([t1,t2,t3])
    K=K/np.sum(K)
    K=K*rate
    return K,tau

if __name__ == "__main__":
    import matplotlib.pyplot as plt
    
    t=np.linspace(0,700*60,700*60)
    K,tau=H2RG(0.1)
    fig=plt.figure(figsize=(10,5))
    plt.plot(t/60,kzhrmodel(t,K,tau),label="detector 1 (bad) ")
    K,tau=H2RG(0.001)
    plt.plot(t/60,kzhrmodel(t,K,tau),label="detector 2 (estimated) ")
    plt.yscale("log")
    plt.xlabel("min",fontsize=16)
    plt.legend()
    plt.tick_params(labelsize=16)
    plt.savefig("persistence_ird.png")
    plt.show()
