# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 11:42:44 2020

@author: BJK
"""
import torch
import torch.nn.functional as F
import numpy as np
import torch.utils.data as Data
######################################### 网络保存和提取
torch.manual_seed(1)    # reproducible

# 假数据
x = torch.unsqueeze(torch.linspace(-1, 1, 100), dim=1)  # x data (tensor), shape=(100, 1)
y = x.pow(2) + 0.2*torch.rand(x.size())  # noisy y data (tensor), shape=(100, 1)

class Net(torch.nn.Module):
    def __init__(self, n_feature, n_hidden, n_output):
        super(Net, self).__init__()
        self.hidden = torch.nn.Linear(n_feature, n_hidden)
        self.predict = torch.nn.Linear(n_hidden, n_output)

    def forward(self, x):
        x = F.relu(self.hidden(x))
        x = self.predict(x)
        return x

net1 = Net(1, 10, 1)   # 这是我们用这种方式搭建的 net1
# # 另一种方式 简单有限
# net2 = torch.nn.Sequential(
#     torch.nn.Linear(1, 10),
#     torch.nn.ReLU(),
#     torch.nn.Linear(10, 1)
# )

optimizer = torch.optim.SGD(net1.parameters(), lr=0.5)
loss_func = torch.nn.MSELoss()

# 训练
for t in range(100):
    prediction = net1(x)
    loss = loss_func(prediction, y)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
# #保存1
# torch.save(net1, 'net.pkl')  # 保存整个网络
# #提取1
# def restore_net():
#     # restore entire net1 to net2
#     net2 = torch.load('net.pkl')
#     prediction = net2(x)

# #保存2
# torch.save(net1.state_dict(), 'net_params.pkl')
#     # 只保存网络中的参数 (速度快, 占内存少)
# #提取2
# def restore_params():
#     # 新建 net3
#     net3 = torch.nn.Sequential(
#         torch.nn.Linear(1, 10),
#         torch.nn.ReLU(),
#         torch.nn.Linear(10, 1)
#     )

#     # 将保存的参数复制到 net3
#     net3.load_state_dict(torch.load('net_params.pkl'))
#     prediction = net3(x)

########################################## 批处理

torch.manual_seed(1)    # reproducible

BATCH_SIZE = 5
# BATCH_SIZE = 8

x = torch.linspace(1, 10, 10)       # this is x data (torch tensor)
y = torch.linspace(10, 1, 10)       # this is y data (torch tensor)

torch_dataset = Data.TensorDataset(x, y)
loader = Data.DataLoader(
    dataset=torch_dataset,      # torch TensorDataset format
    batch_size=BATCH_SIZE,      # mini batch size
    shuffle=True,               # random shuffle for training
    # num_workers=1,              # 多进程，windows禁止
)


def show_batch():
    for epoch in range(3):   # train entire dataset 3 times
        for step, (batch_x, batch_y) in enumerate(loader):  # for each training step
            # train your data...
            print('Epoch: ', epoch, '| Step: ', step, '| batch x: ',
                  batch_x.numpy(), '| batch y: ', batch_y.numpy())


if __name__ == '__main__':
    show_batch()


input ("\n\n按回车结束:")
