关于补全问题：  
根据网站 [segmentfault] <https://segmentfault.com/q/1010000008971601?_ea=1808149> 的说法  
> 目前已经算是解决了这个问题。  
在上述问题中，我采用的是pip在线安装python-opencv，
安装好之后，pip在python的安装路径下的Lib->site-packages中创建了一个文件夹CV2，
也就是说python-opencv被安装在了Lib->site-packages->CV2中；
而之后我改用第三方的一个离线安装包进行安装，其中opencv-python被安装在了Lib->site-packages下，并没有创建额外的文件夹。
而采用后者，就不会出现上述问题。因此我推测上述问题的是pip在在线安装python-opencv造成的。  

解决方法：
```python
from cv2 import cv2
```