# 一、注册GitHub账号
## 1.1、创建一个新仓库
## 1.2、创建一个分支
## 1.3、修改ReadMe内容
### 1.3.1 Readme编写使用Markdown格式
# 二、安装GitHub Desktop
## 2.1、下载GitHub Desktop
## 2.2、填入GitHub注册的用户名邮件等相关信息
## 2.3、在GitHub Desktop上修改代码或者文件，并发出合并请求
## 2.4、在GitHub上处理并同意合并
## 2.5、评论分支的改动
## 2.6、删除已被合并分支
# 三、安装Python
# 四、安装Sublime Text 3
# 五、Mac的一些常规操作
## 5.1 显示键盘
    - 点击搜狗输入法 > 显示虚拟键盘    可查看各个键所对应的符号
## 5.1 搜狗输入法输入罗马数字设置
    - 菜单栏－修改（编辑）－表情与符号－左上角（齿轮图标）－自定义列表－选中 数字-全部。
## 5.1 Mac快捷键
### 5.1.1 截屏

功能     | 快捷键
-------- | --------
截取全屏  | <kbd>Command</kbd> + <kbd>shift</kbd> + <kbd>3</kbd>
截取自定义范围屏幕  | <kbd>Command</kbd> + <kbd>shift</kbd> + <kbd>4</kbd>
截取当前活动窗口  | <kbd>Command</kbd> + <kbd>shift</kbd> + <kbd>4</kbd> + <kbd>space</kbd>  
### 5.1.2 字符输入

字符     | 快捷键
-------- | --------
•  | <kbd>option</kbd> + <kbd>8</kbd>
## 5.2、Mac设置
## 5.3、文件管理
### 5.3.1 获取文件路径
  - 鼠标右键点击文件，选择显示简介可以查看文件所在的目录，这和windows上点击路径兰结果一致，但使用起来不太方便，因为这只显示了文件所在目录的路径，文件的绝对路径还需要加上文件名
  - 将文件拖入浏览器，文件路径会显示在地址栏
  - 打开终端程序，将文件拖进去，路径会自动打印出来
### 5.3.2 打开Library（资源库）文件夹
Mac 上的~/Library 文件夹是默认为隐藏的。有时候就会用到这个文件夹来查看我安装在Mac上的应用程序所在的位置。
- 方法一：打开Finder --> 按住<kbd>Option</kbd>键 --> 点击资源库
- 方法二：打开Finder --> 点击前往 --> 选择前往文件夹 --> 输入框内输入"/资源库"或者"~/Library" --> 点击前往
- 方法三：永久打开。打开Finder --> 点击前往 --> 点击个人 --> 点击上方齿轮并选择查看显示选项 --> 勾选显示"资源库"文件夹
# 六、问题集
## 6.1、sublime repl插件安装后无法正常使用
## 6.2、sublime Text 3 Preferance 按钮为灰色
## 6.3、Sublime Text 3 install package无法正常安装
### 6.3.1 install package时的报错
  - Package Control  There are no packages available for installation
  ![](../../Users/shan/Desktop/屏幕快照\ 2019-01-12\ 上午11.15.53.png)
    - 原因分析：官方提供的Package Control不能用
    - Package Control.sublime-package 文件为空
    - Package Control: Error downloading channel. HTTP error 404 downloading https://packagecontrol.io/channel_v3.json.
      https://packagecontrol.io/channel_v3.json无法访问
        - 解决办法：使用Cargo VPN 翻墙访问https://packagecontrol.io网站
