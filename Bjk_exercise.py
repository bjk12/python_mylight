# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
# import torch
# #variable 被淘汰
# from torch.autograd import Variable
import matplotlib
import matplotlib.pyplot as plt
# #device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
# bjktable=pd.DataFrame(columns=[x for x in range(4)], dtype=np.float64)
# bjktable=bjktable.append(
#             pd.Series(
#                 [0]*4, index=[x for x in range(4)],name='a'
#                 )
#             )
# bjktable=bjktable.append(
#             pd.Series(
#                 [0]*4,
#                 ),
#             ignore_index=True,
#             )
# print(bjktable)
class student(object):
    def fun1(self):
        self.name1 = 'ssss'
        for i in range(1):
            print(self.name1)
    def fun2(self):
        print(self.name1+"hello")

a=student()
a.fun1()
a.fun2()

# 保存模型
# from sklearn.externals import joblib
# joblib.dump(pca,'pca.pkl')
# joblib.load('pca.pkl')

# 保存数据
# import numpy as np
# np.savez('ab.npz',k_a=a,k_b=b)
# c=np.load('ab.npz')
# print (c['k_a'])
# print (c['k_b'])

# data=[[1,2],[3,4]]
# temp=np.arange(10)
# np_data =np.array(data)
# print(np_data)
# tensor =torch.Tensor(np_data)
# print(temp[:3])
# print(
#       '\nnumpy:\n',np_data.dot(np_data),#向量相乘，np.multiply()为各元素相乘
      
# #     tensor.dot只接受一维张量
#     '\ntorch:\n',tensor.mm(tensor)#mm为矩阵相乘，mul为各元素相乘
#       )

# import torch
# a=torch.Tensor([[1,1,1,1],
#    [2,2,2,2],[3,3,3,3],[4,4,4,4],[5,5,5,5],[6,6,6,6],[7,7,7,7]])
# b=torch.Tensor([[3,3,3],
#    [4,4,4]])
# c=torch.Tensor([[0,0,0],
#    [6,6,6]])
# # print("a=",a.data.numpy())
# # print("b=",b.data.numpy())
# # print("c=",c.data.numpy())
# d=torch.Tensor([1,2,3,4]).reshape(1,4)
# #向量与矩阵相乘，如果是行向量则逐行按位相乘，如果是列向量则逐列按位相乘
# e=d*a
# # print("e=",e.numpy())

# fig1=plt.figure(1,(5,4))
# ax1=fig1.add_subplot(221)
# ax1.scatter(a.numpy()[:,0],a.numpy()[:,1],c=a.numpy()[:,3],alpha=0.5,cmap='RdYlGn')
# ax2=fig1.add_subplot(122)
# ax2.scatter(b.numpy()[0,:],b.numpy()[1,:],c=c.numpy()[1,:],alpha=0.5,cmap='RdYlGn')
# plt.tight_layout()
# plt.show()


# d=np.stack((a,b,c),axis=0)
# print('"axis=0":\n',d)

# d=np.stack((a,b,c),axis=1)
# print('"axis=1":\n',d)

# d=np.stack((a,b,c),axis=2)
# print('"axis=2":\n',d)

# a=np.array([1,2,4])
# b=np.array([1,2,6])
# print (a*b)

# import turtle
# turtle.speed(1)
# turtle.fd(30)
# turtle.left(90)
# turtle.fd(25)
# turtle.left(45)
# turtle.fillcolor("green")
# turtle.begin_fill()
# turtle.circle(-80, 90)#圆心在海龟的右边
# turtle.right(90)
# turtle.circle(-80, 90)
# turtle.end_fill()
# turtle.done()
