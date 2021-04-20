# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 09:58:44 2020
好的绘图例子；
svm_sample.py
scatter
####{:>4} 4为数字长度，不够前面加空格，{:>.9}"是指有效数字个数为9
print("[Epoch: {:>4}] cost = {:>.4}".format(epoch + 1, cost.item())

      看代码常用：
print(feature.shape)
plt.figure(1)
###ms是点的大小markersize，lw是线宽linewidth
plt.scatter(feature[:,0].tolist(),feature[:,1].tolist(),marker=".", c='k')
plt.show()

@author: BJK
"""
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
#防止汉字和负号乱码
#matplotlib.use('qt4agg')  
matplotlib.rcParams['font.sans-serif'] = ['SimHei']  
#matplotlib.rcParams['font.family']='sans-serif' 
matplotlib.rcParams['axes.unicode_minus']=False
######################################### 基础使用
#x = np.linspace(-6, 6, 100)
#y1 = 2*x + 1
#y2 = x**2
##设置图标大小和标号                                                                 (1)
#plt.figure(num=3, figsize=(10, 6))
#
##自定义刻度                                                                     (2)
#new_ticks = np.linspace(-np.pi, np.pi,3 )
#plt.xticks(new_ticks)
##自定义刻度2                                                                     (2.1)
#plt.yticks([-2, -1.8, -1, 1.22, 3],
#           [r'$really\ bad$', r'$bad$', r'$normal$', r'$good$', r'$really\ good$'])
#plt.xlim((-5, 5))
#plt.ylim((-2, 3))
##获取句柄，以下是画十字坐标系                                                       (3)
#ax = plt.gca()
#ax.spines['right'].set_color('none')
#ax.spines['top'].set_color('none')
##设置横轴
#ax.xaxis.set_ticks_position('bottom')
#ax.spines['bottom'].set_position(('data', 0))
#ax.yaxis.set_ticks_position('left')
#ax.spines['left'].set_position(('data',0))
## 定义标签位置,完美！                                                             (4)
#plt.xlabel('横轴')
#plt.ylabel('纵轴')
#ax.xaxis.set_label_coords(0.95,0.39)
#ax.yaxis.set_label_coords(0.49,0.95)
#
#ax.set_title('一个蓝色主标题',fontsize='large',fontweight='bold',
#             color='blue',loc ='center',verticalalignment='baseline',rotation=0)   (5)
#
## 画线
#l1,=plt.plot(x, y2,color='black',label='one foreign line')
#l2,=plt.plot(x, y1, color='red',linewidth=1.0, linestyle='-',
#         marker='o',Markersize=2,label='another strange line')
##plt.legend(handles=[l1, l2], labels=['line1', 'line2'],  loc='best')           (6)
#plt.legend(handles=[l1,],loc=0)
## 注释annotate
##plt.annotate(r'$2x+1$', xy=(1,1), xycoords='data', xytext=(+30, -30),
##             textcoords='offset points', fontsize=16,
##             arrowprops=dict(arrowstyle='->', connectionstyle="arc3,rad=.2"))
## 注释text
#plt.text(-4, 1,r'$This\ is\ the\ some\ text.\ \mu\ \sigma_i\ \alpha_t$',           (7)
#         fontdict={'size': 16, 'color': 'r'})
## 设置 x轴 和 y轴 的刻度数字进行透明度设置
##for label in ax.get_xticklabels() + ax.get_yticklabels():
##    label.set_fontsize(12)
##    # 在 plt 2.0.2 或更高的版本中, 设置 zorder 给 plot 在 z 轴方向排序
##    label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.7, zorder=2))
#
#plt.show()
##################################  画图种类
#n = 12
#X = np.arange(n)
#Y1 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
#Y2 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
#
#plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
#plt.bar(X, -Y2, facecolor='#ff9999', edgecolor='white')
#
#plt.xlim(-.5, n)
##plt.xticks(())
#plt.ylim(-1.25, 1.25)
## 隐藏坐标轴
#plt.yticks(())
#
#for x, y in zip(X, Y1):# 将数据打包成元组
#    # ha: horizontal alignment
#    # va: vertical alignment
#    plt.text(x + 0.1, y + 0.05, '%.2f' % y, ha='center', va='bottom')
#
#for x, y in zip(X, Y2):
#    # ha: horizontal alignment
#    # va: vertical alignment
#    plt.text(x + 0.1, -y - 0.05, '%.2f' % y, ha='center', va='top')
#plt.show()

#def f(x,y):
#    # the height function
#    return (1 - x / 2 + x**5 + y**3) * np.exp(-x**2 -y**2)
#
#n = 256
#x = np.linspace(-3, 3, n)
#y = np.linspace(-3, 3, n)
#X,Y = np.meshgrid(x, y)
## 等高图
## X, Y and value for (X,Y) point
#plt.contourf(X, Y, f(X, Y), 8, alpha=.75, cmap=plt.cm.Spectral_r)
## 显示图例颜色条
#plt.colorbar()
## 等高线
#C = plt.contour(X, Y, f(X, Y), 8, colors='black', linewidths=.5)
#
#plt.clabel(C, inline=True, fontsize=10)
#
#plt.xticks(())
#plt.yticks(())
#plt.show()
################### 2d绘图
# a = np.array([0.313660827978, 0.365348418405, 0.423733120134,
#               0.365348418405, 0.439599930621, 0.525083754405,
#               0.423733120134, 0.525083754405, 0.651536351379]).reshape(3,3)
# plt.imshow(a, interpolation='nearest', cmap='bone', origin='lower')
# # 缩小显示图例颜色条
# plt.colorbar(shrink=.92)
# plt.show()
################### 3D绘图
# fig = plt.figure(figsize=(6, 4))
# ax = Axes3D(fig)

# X = np.arange(-4, 4, 0.25)
# Y = np.arange(-4, 4, 0.25)
# X, Y = np.meshgrid(X, Y)    # x-y 平面的网格
# R = np.sqrt(X ** 2 + Y ** 2)
# # height value
# Z = np.sin(R)

# ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.get_cmap('rainbow'))
# dg=ax.contourf(X, Y, Z, zdir='z', offset=-2, cmap=plt.get_cmap('rainbow'))
# fig.colorbar(dg,ax=ax,shrink=0.6)
# ax.set_zlim(-2,2)

# plt.show()
############################## #####################     多图绘制
# plt.figure()

# ax1=plt.subplot(211)
# ax1.set_title('第一个子标题')
# ax1.plot([0,1],[0,1])

# ax2=plt.subplot(223)
# ax2.set_title('第二个子标题')
# ax2.plot([0,1],[0,1])

# ax3=plt.subplot(224)
# ax3.plot([0,1],[0,1])

# plt.tight_layout()

# #other method 1      用于画大小不一的子图
# ax1 = plt.subplot2grid((3, 3), (0, 0), colspan=3)
# ax1.plot([1, 2], [1, 2])    # 画小图
# ax1.set_title('ax1_title')  # 设置小图的标题
# ax2 = plt.subplot2grid((3, 3), (1, 0), colspan=2)
# ax3 = plt.subplot2grid((3, 3), (1, 2), rowspan=2)

#other method 2         子图大小相同
f, ax= plt.subplots(2, 2, sharex=False, sharey=False)
ax[0,0].scatter([1,2], [1,2])
plt.tight_layout()
plt.show()
######## ############################       图中图
# fig=plt.figure()
# # 创建数据
# x = [1, 2, 3, 4, 5, 6, 7]
# y = [1, 3, 4, 2, 5, 8, 6]
# left, bottom, width, height = 0.1, 0.1, 0.8, 0.8
# ax1 = fig.add_axes([left, bottom, width, height])
# ax1.plot(x, y, 'r')
# ax1.set_xlabel('x')
# ax1.set_ylabel('y')
# ax1.set_title('title')
# #规范式
# left, bottom, width, height = 0.2, 0.6, 0.25, 0.25
# ax2 = fig.add_axes([left, bottom, width, height])
# ax2.plot(y, x, 'b')
# ax2.set_xlabel('x')
# ax2.set_ylabel('y')
# ax2.set_title('title inside 1')
# #简单式
# plt.axes([0.6, 0.2, 0.25, 0.25])
# plt.plot(y[::-1], x, 'g') # 注意对y进行了逆序处理
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('title inside 2')

########## 次坐标轴
x = np.arange(0, 10, 0.1)
y1 = 0.05 * x**2
y2 = -1 * y1

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()

line1,= ax1.plot(x, y1, 'g-',label='green')   # green, solid line
# 网格线
ax1.grid()

ax1.set_xlabel('X data')
ax1.set_ylabel('Y1 data', color='g')

line2,= ax2.plot(x, y2, 'b--',label='blue') # blue
ax2.set_ylabel('Y2 data', color='b')
plt.legend(handles=[line1, line2], 
            # labels=['line1', 'line2'], 
            loc='best')


###################################### 动画

# from matplotlib import animation
# fig, ax = plt.subplots()

# x = np.arange(0, 2*np.pi, 0.01)
# line, = ax.plot(x, np.sin(x))

# def animate(i):
#     line.set_ydata(np.sin(x + i/10.0))
#     return line,

# def init():
#     line.set_ydata(np.sin(x))
#     return line,

# ani = animation.FuncAnimation(fig=fig,
#                               func=animate,
#                               frames=300,#帧数，也就是动画运行的完成度
#                               init_func=init,
#                               interval=20,#每帧占用的时间
#                               blit=True)
# ani.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])
plt.show()
#input ("\n\n按回车结束:")