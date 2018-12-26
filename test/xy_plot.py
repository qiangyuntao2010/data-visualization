#!/usr/bin/env python
# coding=utf-8
import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-1,1,10)
y1=x**3
y2=x**2

plt.figure()
l1,=plt.plot(x,y1)
l2,=plt.plot(x,y2,color='green',linewidth=1,linestyle='--')
plt.xlim(-1,2)
plt.ylim(-1,2)
plt.xlabel('This is x axis')
plt.ylabel('This is y axis')

plt.xticks(x)
plt.yticks([-1,0,1],['$really\ bad$','$normal$','$very\ good\ \\alpha$'])

#gca='get current axis'
ax=plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0))
plt.legend(handles=[l1,l2,],labels=['line1','line2'],loc='best')


plt.show()
