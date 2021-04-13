# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 17:23:30 2020

@author: BJK
"""
"""
args explanition:
    p:covariance
    x:state
    z:observation
    u:control
    Pred:predict
    Est:estatemation
    Q：表示过程激励噪声的协方差，它是状态转移矩阵与实际过程之间的误差。
    R：表示测量噪声协方差，和仪器相关的一个特性，
    陀螺仪，角加速度，动态响应好->作测量值
    加速度，加速度（角度），动态响应差->作估计值
"""
import numpy as np
import math 
import matplotlib
import matplotlib.pyplot as plt

#防止汉字和负号乱码
matplotlib.rcParams['font.sans-serif'] = ['SimHei']  
matplotlib.rcParams['axes.unicode_minus']=False

Q=np.diag([0.1,0.1,math.radians(1.0),1.0])**2
R=np.diag([1.0,math.radians(40.0)])**2
dt=0.1
def motion_model(x,u):
    B=np.matrix([[dt*math.cos(x[2,0]),0.0],
                  [dt*math.sin(x[2,0]),0.0],
                  [0.0,dt],
                  [1.0,0.0]])
    x=x+B*u
    return x
#def observe_model(z):
#    H=
#    pass
#def JacoMo(xEst,u):
#    return jMo
#def JacoOb(xEst):
#    return jOb
def JacoMo(x, u):
    """
    Jacobian of Motion Model
    motion model
    x_{t+1} = x_t+v*dt*cos(yaw)
    y_{t+1} = y_t+v*dt*sin(yaw)
    yaw_{t+1} = yaw_t+omega*dt
    v_{t+1} = v{t}
    so
    dx/dyaw = -v*dt*sin(yaw)
    dx/dv = dt*cos(yaw)
    dy/dyaw = v*dt*cos(yaw)
    dy/dv = dt*sin(yaw)
    
    雅克比矩阵：
    [[x/dx,x/dy,x/dyaw,x/dv]                   1,  0,  x/dyaw,  x/dv
    [y/dx,y/dy,y/dyaw,y/dv]]               =>  0,  1,  y/dyaw,  y/dv
    [yaw/dx,yaw/dy,yaw/dyaw,yaw/dv]]           0,   0,    1,      0
    [v/dx,v/dy,v/dyaw,v/dv]]                   0,   0,    0,      1
    """
    
    yaw = x[2, 0]
    v = u[0, 0]
    jF = np.matrix([[1.0, 0.0, -dt * v * math.sin(yaw), dt * math.cos(yaw)],
        [0.0, 1.0, dt * v * math.cos(yaw), dt * math.sin(yaw)],
        [0.0, 0.0, 1.0, 0.0],
        [0.0, 0.0, 0.0, 1.0]])
 
    return jF
 
 
def JacoOb(x):
    # Jacobian of Observation Model
    '''
    状态方程：x=A*x+B*u
    输出方程：y=C*x+D*u     (一般没有D)
    下面提到的jH，类似这里的C
    '''
    jH = np.matrix([
        [1, 0, 0, 0],
        [0, 1, 0, 0]
    ])
 
    return jH

###以下是本程序最精髓的一条函数
def ekf_estimation(xEst,pEst,z,u):
    # 预测，k-1时刻对k时刻的推测值（1）
    xPre=motion_model(xEst,u)
    jMo=JacoMo(xEst,u)   # Jacobin of motion model
    jOb=JacoOb(xEst)
    #推测值与真实值之间的误差协方差矩阵（2）
    pPre=jMo*pEst*jMo.T+Q
    #中间变量
    s=jOb*pPre*jOb.T+R
    ##卡尔曼增益，即预测值的不可信度（3）
    k=pPre*jOb.T*np.linalg.inv(s)
    
    # 更新估计
    #中间变量，亦可以说是对推测值的观测值H（k|k-1）
    zPre=jOb*xPre
    #利用卡尔曼增益对k-1时刻的推测值和当前测量值加权得到  当前时刻的估计值（4），是下一轮（1）的输入
    ####z-zPre，是测量值误差
    xEst=xPre+k*(z-zPre)
    ##更新k时刻估计值与真实值之间的误差协方差矩阵（5），是下一轮（2）的输入
    pEst=(np.eye(len(xEst)) - k*jOb)*pPre
    return xEst,pEst
def input_data(xTrue,xImu):
    u=np.matrix([1.0,0.1]).T#角速度 和 线速度 不变
    #更新当前位置
    xTrue=motion_model(xTrue,u)
    
    #引入噪声
    Qsim=np.diag([0.5,0.5])**2
    Rsim=np.diag([1.0,math.radians(5.0)])**2
    #GPS
    z=np.matrix([xTrue[0,0]+np.random.randn()*Qsim[0,0],
                 xTrue[1,0]+np.random.randn()*Qsim[1,1]]).T
    ud=np.matrix([u[0,0]+np.random.randn()*Rsim[0,0],
                  u[1,0]+np.random.randn()*Rsim[1,1]]).T
    xImu=motion_model(xImu,ud)
    return ud,z,xTrue,xImu
 
if __name__=="__main__":
    xEst=np.matrix(np.zeros((4,1)))
    xTrue=xEst
    xImu=xTrue
    pEst=np.eye(4)
    t=0.1
    #以下是用于绘图的参数，不用管
    hTrue=xTrue
    hEst=xEst
    hz=np.zeros((2,1))
    hImu=xImu
    plt.ion()
    for i in range(314):
        u,z,xTrue,xImu=input_data(xTrue,xImu)
    ###z是测量到的位置（短时误差大，长期稳定），u是测量到的速度（短时误差小，长期误差累积）
        xEst,pEst=ekf_estimation(xEst,pEst,z,u)
        hTrue=np.hstack((hTrue,xTrue))
        hEst=np.hstack((hEst,xEst))
        hImu=np.hstack((hImu,xImu))
        hz=np.hstack((hz,z))
        if i%100==0:
            # plot
            plt.cla()
            ###GPS数据 
            l1,=plt.plot(np.array(hz[0,:]).flatten(),
                         np.array(hz[1,:]).flatten(),".g",label="GPS",ms=1)
            ###计划路径
            l2,=plt.plot(np.array(hTrue[0,:]).flatten(),
                     np.array(hTrue[1,:]).flatten(),"-b")
            ####扩展卡尔曼预测结果
            l3,=plt.plot(np.array(hEst[0,:]).flatten(),
                     np.array(hEst[1,:]).flatten(),"-r")
            #单纯依靠惯导的结果
            l4,=plt.plot(np.array(hImu[0,:]).flatten(),
                     np.array(hImu[1,:]).flatten(),"-k")
            plt.legend(handles=[l1,l2,l3,l4], 
                       labels=['GPS','True','EKF','惯性单元'],
                       loc='best')
            plt.axis('equal')
            plt.pause(0.01)
    plt.ioff()
    plt.show()
input ("\n\n按回车结束:")
