# 一、安装
## 1、下载地址https://www.jetbrains.com/pycharm/
## 2、注册码
## 3、安装过程中的设置
# 二、使用
## 1、设置
### 1.1 主题设置
- 系统自带主题设置
    -Pycharm --> Preferences --> Editor --> Color Scheme 
- 网络下载主题设置
    - Pycharm --> Preferences --> Editor --> Color Scheme --> 点击齿轮 --> Import Scheme --> 点击选择需要安装的主题包 --> 点击Open
## 2、新建工程
## 3、文件及文件夹
### 3.1 查看Pycharm在Mac中的安装文件夹
- 打开Finder --> 打开Library或者资源库 --> 打开Preferences --> 打开PyCharm2018.3
### 3.2 查看工程项目位置
- 打开Finder --> 点击用户 --> 点击shan --> 点击PycharmProjects
### 3.3 新建文件
#### 3.3.1 新建.py文件
- 右键 > New > Python File > 输入想要的文件名 > OK
![1](https://raw.githubusercontent.com/Aghanim-H/Photo/master/Pycharm/Pycharm_New.png#pic_center)![2](https://raw.githubusercontent.com/Aghanim-H/Photo/master/Pycharm/Pycharm_New_Python%20File.png)![3](https://raw.githubusercontent.com/Aghanim-H/Photo/master/Pycharm/Pycharm_New_Python%20File_.png)
#### 3.3.2 新建.md文件
- 右键 > New > File > 输入想要的文件名.md > OK
![1](https://raw.githubusercontent.com/Aghanim-H/Photo/master/Pycharm/Pycharm_New.png)![2](https://raw.githubusercontent.com/Aghanim-H/Photo/master/Pycharm/Pycharm_New_File.png)![3](https://raw.githubusercontent.com/Aghanim-H/Photo/master/Pycharm/Pycharm_New_File_.png)
## 4、上传修改后的文件至Github
- 先点击commit 然后VCS --> Git --> Push
- 出现提示框 git-credential-osxkeychain 输入Mac开机密码即可
## 5、快捷键
功能|快捷键
|:----:|:----:|
注释|<kbd>Command</kbd> + <kbd>/</kbd>
保存|<kbd>Command</kbd> + <kbd>S</kbd>
缩进|<kbd>tab</kbd>
退缩进|<kbd>shift</kbd> + <kbd>tab</kbd>
删除选中行整行|<kbd>Command</kbd> + <kbd>delete</kbd>
打开最近访问过的文件|<kbd>Ctrl</kbd> + <kbd>E</kbd>
打开最近编辑过的文件|<kbd>Ctrl</kbd> + <kbd>shift</kbd> + <kbd>E</kbd>
万能搜索|连按两下 <kbd>shift</kbd>
全局搜索关键字|<kbd>Ctrl</kbd> + <kbd>shift</kbd> + <kbd>F</kbd>
全局替换|<kbd>Ctrl</kbd> + <kbd>shift</kbd> + <kbd>R</kbd>
访问历史粘贴板|<kbd>Ctrl</kbd> + <kbd>shift</kbd> + <kbd>V</kbd>
智能提示选择合适的操作|<kbd>alt</kbd> + <kbd>enter</kbd>
任意位置另起一行|<kbd>shift</kbd> + <kbd>enter</kbd>
历史输入?|<kbd>alt</kbd> + <kbd>/</kbd>
撤销|<kbd>command</kbd> + <kbd>Z</kbd>
选择多行|<kbd>alt</kbd> + <kbd>↑</kbd> 或 <kbd>↓</kbd>
大写变小写|<kbd>command</kbd> + <kbd>shift</kbd> + <kbd>U</kbd>
使用网页搜索选中的字|<kbd>command</kbd> + <kbd>shift</kbd> + <kbd>L</kbd>
替换|<kbd>Command</kbd> + <kbd>R</kbd>
显示Tool Buttons|连按两下 <kbd>command</kbd>
## 6、环境配置
- numpy使用
    - 问题一、ModuleNotFoundError: No module named 'numpy'
        - 解决办法：
            - Pycharm --> Preferences --> Project：XX --> Project Interpreter --> Project Interpreter：下拉框选择show all --> 点击左下角 + 号按钮 --> Virtualenv Environment --> Existing environment --> 点击OK --> 点击OK
# 三、调试