# FTools

经常使用的工具集合，包括命令、脚本、代码、使用技巧等所有和计算机相关的技术

## python

python 相关技术。

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

## C++

c++ 相关技术。

### boost
boost 库的使用例子：
- `geometry.cpp`: 图形库的使用
-  `GraphicUtils.cpp`: 图形学相关代码

