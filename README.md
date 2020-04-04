# FTools

经常使用的工具集合，包括命令、脚本、代码、使用技巧等所有和计算机相关的技术

## 常用命令总结

- 扫描指定网段，demo: `nmap -sP 192.168.1.1-150`
- 查看指定主机的TCP服务: `nmap ip`，特例 `nmap localhost`
- 查看本机端口(TCP/UDP)占用情况: `lsof -i:端口号`，输出包含PID、命令名等，默认只能看本用户启动的服务
- 查看本机所有进程: `ps aux | less`，可以查看命令地址

## python

python 相关技术。

- `img-gray.py`: 将图片转为灰度图

### `GraphicUtils.py`

图形学相关代码，包含下列函数：

- `ScalarProduct`: 向量点积
- `ShortestPoint`: 找出一条线段中与指定点距离最短的点
- `ShortestDist`: 找出指定点到线段的最短距离
- `IsClockwise`: 判断二维平面多边形是否顺时针绘制
- `UnitNormalVector`: 获取单位法向量

### `pywc.py`

脚本命令，用于字数统计(中/英文、数字、空白符统计)，统计结果中各个标签的含义：

- *English word* ：表示英文单词个数
- *Chinese char* ：表示中文个数，其中中文的标点符号都视为一个中文
- *Digit word* ：表示数字个数，其中 类似`12.34`会被视为两个数字
- *Sum* ：表示上述三者之和
- *Blank char* ：空白符个数，如`\n`、` `、`\t`都为空白符
- *Line* ：总行数
- *Space line* ：空行数，如果一行中只有`\n`或`\r\n`即为空行
- *Non-spade line* ：非空行数（计算有效代码量时使用）

使用案例1，统计指定文件的内容：
```sh
$ cat test.txt
你abc好，世界。
12.31 hello

find结束

$ pywc.py test.txt
English word : 3
Chinese char : 6
Digit word : 2
Sum : 11
--------------------
Blank char : 6
Lines : 5
Space line : 2
Non-space line : 3
```

使用案例2，通过管道传递数据：
```sh
$ cat test.txt | pywc.py
English word : 3
Chinese char : 6
Digit word : 2
Sum : 11
--------------------
Blank char : 6
Lines : 5
Space line : 2
Non-space line : 3
```

### `plantuml2img.py`

将 markdown 中的 plantuml 代码块全部输出为图片格式，使用该脚本需要完成以下依赖的安装：

- 安装 graphviz
- 安装 VS Code
- 在 VS Code 中安装 PlantUML 

通常来说，svg、png、latex、等格式都能正常导出，但pdf不能正常导出，变通方法为：生成svg格式 -> 用浏览器打开该svg格式图片 -> 打印页面为pdf格式。

要求：markdown 中的 plantuml 代码段必须以`@startuml 名称`开始、`@enduml`结尾，或者以`@startmindmap 名称`开始，`endmindmap`结尾，其中的名称即为导出文件的名称，如果没有设置名称，则视为不导出。

通过 `plantuml2img.py -h` 可以查看使用方法。

## C++

c++ 相关技术。

### boost
boost 库的使用例子：
- `geometry.cpp`: 图形库的使用
-  `GraphicUtils.cpp`: 图形学相关代码

