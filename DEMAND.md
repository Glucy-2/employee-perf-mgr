# 程序设计题：企业员工业绩管理系统

## 1 系统的基本功能

本课题要求编写Python程序实现对员工信息和业绩信息的管理。一个综合的员工业绩管理系统，要求能够管理若干个员工各季度工作业绩，需要实现以下功能：读取以数据文件形式存储的员工信息；可以按工号增加、修改、删除员工的信息；按照工号、姓名、名次等方式查询员工信息；可以按照工号顺序浏览员工信息；可以统计各季度工作的最高业绩、最低业绩和平均业绩；计算每个员工的总业绩并进行排名。

系统内的所有信息必须以文件的方式存储在硬盘中，员工信息文件，存放了员工的工号，姓名，性别，各个季度的业绩，四个季度的总业绩，依据总业绩的排名。格式如下：

```csv
B01,Tom,Male,70,80,90,85

B02,Rose,Female,70,80,90,75

B03,Jack,Male,80,90, 95,70

……
```

## 2 要求及提示

### 2.1 基本要求

系统提供的基本功能包括：

1. 系统内的相关信息文件由程序设计人员预先从键盘上录入，文件中的数据记录不得少于20条；
2. 设计并实现系统的相关界面，提供良好的交互界面；
3. 排序功能：能实现由用户选择按各项数据升序或降序排序对查询出的信息进行显示；
4. 可以添加/删除/修改员工信息；
5. 可以添加/删除/修改业绩信息；
6. 查询员工信息：

   - 输入一个工号，查出此人的基本信息并显示输出。
   - 输入一个工号，查询出此员工的所有业绩情况。
7. 查询业绩信息：

   - 输入一个季度时，查询此季度的最高业绩、最低业绩和平均业绩。

### 2.2 选做要求

1. 使用Tkinter或其他GUI函数库，为本课题设计一个可视化的界面，要求界面美观、布局合理、功能正确以及对用户的错误操作能够进行友好提示。

### 2.3 提示

程序的总体框图如下：

```mermaid
graph LR

员工业绩管理系统 ----> 用户登录模块
员工业绩管理系统 ----> 用户密码修改模块

员工业绩管理系统 --> 员工信息维护

员工信息维护 --> 添加员工信息模块
员工信息维护 --> 修改员工信息模块
员工信息维护 --> 删除员工信息模块

员工业绩管理系统 --> 业绩信息维护

业绩信息维护 --> 添加员工信息模块
业绩信息维护 --> 修改员工信息模块
业绩信息维护 --> 删除员工信息模块


员工业绩管理系统 --> 信息查询/统计

信息查询/统计 --> 员工信息查询模块
信息查询/统计 --> 业绩信息查询模块
信息查询/统计 --> 其他信息查询模块

```

图1 员工业绩管理系统总体框图

数据结构：

依据给定的员工信息、季度信息和业绩信息，定义员工类，设计内容如下：

```python
class Staff(object):
    #员工信息类
    def __init__(self, num ,name, gender, score):
        self.num = num                   	#工号
        self.name = name                 	#姓名
        self.gender = gender             	#性别
        self.score = score               	#各季度业绩
        self.total = None               	#总业绩
        self.rank = None                 	#名次

```

### 2.4 其他要求

1. 在上述功能要求的基础上，为了提高本课程的成绩，可以和任课教师沟通，为程序设计题添加一些额外的功能。
2. 变量、方法命名符合规范。
3. 注释详细：每个变量都要求有注释说明用途；方法有注释说明功能，对参数、返回值也要以注释的形式说明用途；关键的语句段要求有注释解释。
4. 程序的层次清晰，可读性强。

## 3 开发环境

开发环境使用Python3以上版本，开发工具可以选择IDLE或者PyCharm等集成开发工具。

## 4 阶段提示

### 第一阶段

本阶段任务：

1. 建立分组
2. 确立课程设计题目
3. 根据选题撰写设计题文档（从课程网站直接下载doc文档）
4. 修改模板代码student.py设计数据对象的结构定义
5. 修改模板代码main.py构建程序主体框架

实施建议：

1. 请确认和你一起完成本课程的小组成员，建议2-3个同学建立一个小组，选出一个同学作为小组长，并请组长在第一次课下课前和任课教师确认分组情况。
2. 请和你的小组成员参考本文件夹中“题目样稿”文档的内容讨论你们的设计课题，题目自拟，课题中尽量不包含“学生”和“游戏”这两个主题，讨论完毕后，直接修改该文档，请注意不要改动该文档的结构和格式。（从课程网站中选题）
3. 结合讨论后确定的设计题目，修改文件夹中main.py和student.py中的代码，main.py中包含的是程序的主体设计框架，student.py包含了数据对象的结构定义，因为各自课题内容的数据对象不同，请自行修改student.py的文件名。
4. 完成上述工作后，尽快将工作成果交给任课教师审核，并核定每个同学的工作量。

### 第二阶段

本阶段任务：

1. 创建数据文件
2. 完成从数据文件中读写数据的功能
3. 能够将读取的数据显示在界面中

实施建议：

1. 结合各自的设计课题，创建对应的数据文件，数据文件中的数据量不小于20条，且数据中的内容尽量贴近现实，例如：不要用名著中的人物来命名、电话号码不要是 `1234567890`等。
2. 完成本课题中创建数据文件、读写数据文件等功能。
3. 完成从键盘输入创建数据对象等功能函数的定义。
4. 通过调用上述程序中的函数，实现主程序中显示数据的功能。
5. 完成上述工作后，尽快将工作成果交给任课教师审核，并核定每个同学的工作量。

### 第三阶段

本阶段任务：

1. 完成对数据对象的添加、修改、删除的功能

实施建议：

1. 完成根据指定的字段内容进行数据比对及删除指定数据对象等功能函数的定义。
2. 通过调用上述程序中的函数，实现主程序中对数据进行添加、修改、删除的功能。
3. 完成上述工作后，尽快将工作成果交给任课教师审核，并核定每个同学的工作量。

### 第四阶段

本阶段任务：

1. 完成对数据进行统计分析的功能

实施建议：

1. 完成关于数据统计分析功能的函数定义。
2. 通过调用上述程序中的函数，实现主程序中对数据进行统计分析的功能。
3. 完成上述工作后，尽快将工作成果交给任课教师审核，并核定每个同学的工作量。

### 第五阶段

本阶段任务：

1. 为设计课题增加图形化界面，在图形化界面中尽可能多地实现前阶段的功能

实施建议：

1. 使用百度搜索Tkinter的相关教程，自学Tkinter的相关内容。
2. 在阶段4的工作成果基础上，建立一个新的主程序，在其中增加关于程序界面设计的相关代码。
3. 在上述代码中，调用阶段4定义的各类函数功能，并将各个功能的结果显示在图形界面中。
4. 为图形化界面程序，添加一个用户登录的提示框，只有输入了正确的用户名和密码之后才允许进入主程序。
5. 完成上述工作后，尽快将工作成果交给任课教师审核，并核定每个同学的工作量。
