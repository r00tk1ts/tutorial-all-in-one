程序设计说得通俗一点就是：使用编程语言将数据和表达式按照特定的语法组织成合规的语句，编写好的程序被翻译成机器指令，交给机器去执行。

# 数据类型

每个数据的背后，都有它自己特定的类型。在程序设计领域有个很重要的概念：类型系统(Type system)，用于定义如何将编程语言中的数值和表达式归类为不同的对应类型。而在类型系统中，[数据类型](https://zh.wikipedia.org/zh-cn/%E8%B3%87%E6%96%99%E9%A1%9E%E5%9E%8B)(Data type)用于约束数据的解释。

大部分编程语言都内置了多种数据类型，它们一般被分为两类：原始类型和复合类型，像是布尔型、整型、浮点型等机器可以直接表达的一般是原始类型（不能进一步被分解），一些较为复杂的像是数组、字符串等则是复合类型，此外，用户也可以自定义嵌套类型，它也是复合类型。

# Python内置类型

[Python内置类型](https://docs.python.org/zh-cn/3/library/stdtypes.html)相当丰富，只是它在标准中没有刻意去区分原始类型和复合类型(~~Python这种乱七八糟的语言，不用搞那么清楚~~)。
![[Pasted image 20240516194149.png]]

## 变量与常量

数据类型一般由变量或常量来承载，顾名思义，变量在运行时值可以发生改变，而常量则不行。Python在语法上没有支持常量，通常在我们需要定义常量时，会使用惯用法：全大写命名来标志某个变量作为常量使用，比如定义：`PI = 3.14159265359`。

> 圆周率`PI`被视为常量，但实际上它是个变量。

### 变量命名

每个变量都需要命名，在Python中，变量命名需要遵循以下规则：
- 硬性规则：
    - 规则1：变量名由**字母**、数字和**下划线**构成，数字不能开头。
    - 规则2：**大小写敏感**
    - 规则3：变量名**不能与Python语言的关键字**(如if,else)和**保留字**（如已有的函数、模块等的名字）**重名**。
- 非硬性规则：
    - 规则1：变量名通常使用小写英文字母，多个单词用下划线进行连接。
    - 规则2：受保护的变量用单个下划线开头。
    - 规则3：私有的变量用两个下划线开头。

> Python变量命名的字母指的是Unicode字符，所以你甚至可以用中文来命名，但并不推荐，特殊字符像是!,@,#等在代码中有特殊含义的字符不能用于命名。

[[Python简介]]有提到Python支持的是动态类型系统，所谓的动态，是指变量可以直接使用、无需声明类型：

```shell
>>> a = 4
>>> b = "hello"
>>> c = []
>>> d = 3.14
>>> e = True
>>> f = 2+3j
# 内置函数type可以输出变量的类型
>>> type(a)
<class 'int'>
>>> type(b)
<class 'str'>
>>> type(c)
<class 'list'>
>>> type(d)
<class 'float'>
>>> type(e)
<class 'bool'>
>>> type(f)
<class 'complex'>
```

> 主流社区一般认定Python是动态强类型语言，但关于强弱性历来有争议，关于这一话题，推荐阅读[格物致知(2)——语言千百，殊途同归](https://r00tk1ts.github.io/2023/06/13/%E6%A0%BC%E7%89%A9%E8%87%B4%E7%9F%A5(2)%E2%80%94%E2%80%94%E8%AF%AD%E8%A8%80%E5%8D%83%E7%99%BE%EF%BC%8C%E6%AE%8A%E9%80%94%E5%90%8C%E5%BD%92/#%E5%BC%BA%E7%B1%BB%E5%9E%8B%E4%B8%8E%E5%BC%B1%E7%B1%BB%E5%9E%8B)。

## 数字类型

支持三种不同的数字类型：整型、浮点型和复数型。

### 整型

大部分编程语言都会对整型数设置一个表达范围，像是C++中有`int64_t, int32_t, int16_t`用于表示64位、32位、16位的有符号数，与之对应的还有`uint64_t`这种64位无符号数的类型。在做数值计算时，我们经常要考虑会溢出(overflow)的可能性。

然而Python的整型`int`非常夸张，它具有无限的精度，这意味着它没有大小限制，它也不区分有符号和无符号，默认都是有符号数（即可以表达负数）。

> 所以一些数值特别大的计算，Python具有天然的相性，也是OI赛棍处理这类问题的最爱。

### 浮点型

浮点数一般用来表达小数，之所以称为浮点数，是因为按照科学记数法表示时，一个浮点数的小数点位置是可变的，比如，$1.23*10^9$和$12.3*10^8$是完全相等的（一般对于很大或很小的浮点数，才会用科学计数法表示）。

一些语言会区分单精度和双精度，它们所表达的范围以及内部表示法有所差异。Python则一步到位，支持且仅支持双精度浮点数，类型为`float`(在C、C++、Java等语言中`float`一般是单精度，`double`才是双精度)。

> CPython实现中，浮点数类型使用的就是C中的`double`。

### 复数型

复数`complex`类型则包含实部和虚部，分别用一个浮点数来表示。可以通过`z.real`和`z.imag`成员访问的方式提取到实部或虚部。

复数在日常编程中并不常用，初学者了解即可。

### 类型的创建与表达

数字型通常由数字字面值或内置的函数与运算表达式结果来创建。

**字面值**

对于字面值来说，规则如下：
1. 不带修饰的整数字面值会生成整型。
2. 包含小数点或幂运算符的字面值会生成浮点型。
3. 字面值末尾携带`j`或`J`后缀的是复数的虚部。

上例的`a,d,f`三个变量就是通过字面值来创建：

```shell
>>> a = 4
>>> d = 3.14
>>> f = 2+3j
>>> type(a)
<class 'int'>
>>> type(d)
<class 'float'>
>>> type(f)
<class 'complex'>
```

通过内置函数`type`可以看到三个变量的类型。


**运算表达式**

生成的类型取决于参与运算的操作数的类型，对于多元运算符来说，较窄的类型会向上拓宽。

> 对Python来说，整数比浮点数窄，浮点数比复数窄。

所有数字类型都支持下列算术运算：

| 运算       | 结果：           |
| -------- | ------------- |
| `x + y`  | _x_ 和 _y_ 的和  |
| `x - y`  | _x_ 和 _y_ 的差  |
| `x * y`  | _x_ 和 _y_ 的乘积 |
| `x / y`  | _x_ 和 _y_ 的商  |
| `x // y` | _x_ 和 _y_ 的商数 |
| `x % y`  | `x / y` 的余数   |
| `-x`     | _x_ 取反        |
| `+x`     | _x_ 不变        |
| `x ** y` | _x_ 的 _y_ 次幂  |

当表达式中同时存在多个运算符时，要根据[运算符优先级](https://docs.python.org/zh-cn/3/reference/expressions.html#operator-summary)和结合律来判定计算规则。

```shell
>>> a = 2 + 2
>>> b = (50 - 5 * 6) / 4
>>> c = 8 / 5
>>> type(a)
<class 'int'>
>>> type(b)
<class 'float'>
>>> type(c)
<class 'float'>
```

**函数**

对于函数来说，取决于它的返回类型。Python为内置类型都内置了对应的构造函数：

```shell
>>> a = int(5)
>>> b = float(4.3e-5)
>>> c = complex(3)
>>> a
5
>>> b
4.3e-05
>>> c
(3+0j)
>>> type(a)
<class 'int'>
>>> type(b)
<class 'float'>
>>> type(c)
<class 'complex'>
>>>
>>> d = int(b) # narrowing cast
>>> d
0
>>> type(d)
<class 'int'>
```

构造函数通常在需要做显式类型转换时被使用，当从宽类型到窄类型做转换时，会发生narrowing cast。

> 从`float`到`int`有着更优雅的math.floor()和math.ceil()方法来替代。

再如内置函数abs(_x_)[](https://docs.python.org/3/library/functions.html#abs "Link to this definition"):

> Return the absolute value of a number. The argument may be an integer, a floating point number, or an object implementing [`__abs__()`](https://docs.python.org/3/reference/datamodel.html#object.__abs__ "object.__abs__"). If the argument is a complex number, its magnitude is returned.

它会返回数字型的绝对值，类型则取决于你传入的`x`类型本身：

```shell
# 整型返回的还是int
>>> a = -5
>>> b = abs(a)
>>> print(b)
5
>>> type(b)
<class 'int'>
# 浮点数返回的还是float
>>> b = abs(a)
>>> print(b)
3.14
>>> type(b)
<class 'float'>
# 对复数来说，返回的是模，类型是float
>>> a = 3+4j
>>> b = abs(a)
>>> print(b)
5.0
>>> type(b)
<class 'float'>
```

## 布尔型

布尔型`bool`用于表示真值与假值，它只有两个常量实例：`True`和`False`。它们常被用在逻辑值检测和布尔运算中。

内置构造函数`bool()`可以将任意值转为布尔值（应用下文的逻辑值检测结果）。

> `bool`实际上是`int`的子类。

## 序列类型

序列类型分为可变序列和不可变序列。在Python中最常用的可变序列类型是`list`(列表)，最常用的不可变序列类型是`tuple`(元组)。

无论何种序列，它们都支持以下的操作：

| 运算                     | 结果：                                         |
| ---------------------- | ------------------------------------------- |
| `x in s`               | 如果 _s_ 中的某项等于 _x_ 则结果为 `True`，否则为 `False`   |
| `x not in s`           | 如果 _s_ 中的某项等于 _x_ 则结果为 `False`，否则为 `True`   |
| `s + t`                | _s_ 与 _t_ 相拼接                               |
| `s * n` 或 `n * s`      | 相当于 _s_ 与自身进行 _n_ 次拼接                       |
| `s[i]`                 | _s_ 的第 _i_ 项，起始为 0                          |
| `s[i:j]`               | _s_ 从 _i_ 到 _j_ 的切片                         |
| `s[i:j:k]`             | _s_ 从 _i_ 到 _j_ 步长为 _k_ 的切片                 |
| `len(s)`               | _s_ 的长度                                     |
| `min(s)`               | _s_ 的最小项                                    |
| `max(s)`               | _s_ 的最大项                                    |
| `s.index(x[, i[, j]])` | _x_ 在 _s_ 中首次出现项的索引号（索引号在 _i_ 或其后且在 _j_ 之前） |
| `s.count(x)`           | _x_ 在 _s_ 中出现的总次数                           |

不可变序列类型普遍支持内置函数`hash()`，可变类型则不支持。前者可以作为`dict`的键，`dict`将在后文讲解。

除了上述操作外，可变类型因其可变特性还支持一些额外操作：

| 运算                       | 结果                                              |
| ------------------------ | ----------------------------------------------- |
| `s[i] = x`               | 将 _s_ 的第 _i_ 项替换为 _x_                           |
| `s[i:j] = t`             | 将 _s_ 从 _i_ 到 _j_ 的切片替换为可迭代对象 _t_ 的内容           |
| `del s[i:j]`             | 等同于 `s[i:j] = []`                               |
| `s[i:j:k] = t`           | 将 `s[i:j:k]` 的元素替换为 _t_ 的元素                     |
| `del s[i:j:k]`           | 从列表中移除 `s[i:j:k]` 的元素                           |
| `s.append(x)`            | 将 _x_ 添加到序列的末尾 (等同于 `s[len(s):len(s)] = [x]`)   |
| `s.clear()`              | 从 _s_ 中移除所有项 (等同于 `del s[:]`)                   |
| `s.copy()`               | 创建 _s_ 的浅拷贝 (等同于 `s[:]`)                        |
| `s.extend(t)` 或 `s += t` | 用 _t_ 的内容扩展 _s_ (基本上等同于 `s[len(s):len(s)] = t`) |
| `s *= n`                 | 使用 _s_ 的内容重复 _n_ 次来对其进行更新                       |
| `s.insert(i, x)`         | 在由 _i_ 给出的索引位置将 _x_ 插入 _s_ (等同于 `s[i:i] = [x]`) |
| `s.pop()` 或 `s.pop(i)`   | 提取在 _i_ 位置上的项，并将其从 _s_ 中移除                      |
| `s.remove(x)`            | 删除 _s_ 中第一个 `s[i]` 等于 _x_ 的项目。                  |
| `s.reverse()`            | 就地将列表中的元素逆序。                                    |
> 一些语言把序列型称作顺序容器。

### list

中文名称作“列表”，通常用于存放同构数据（也就是相同类型的数据集合），但它也支持存放异构结构。

常见的创建列表方式：
```shell
# 通过一对方括号：[]创建
>>> l = []
>>> type(l)
<class 'list'>
# 方括号内可以初始化成员，多个成员按逗号分隔
>>> l = [1]
>>> len(l)
1
>>> type(l)
<class 'list'>
>>> l = [1,3,5]
>>> len(l)
3
>>> type(l)
<class 'list'>
# 还可以使用列表推导式
>>> l = [x for x in range(10)]
>>> type(l)
<class 'list'>
>>> len(l)
10
>>> l
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# 也可以是用内置的构造函数
>>> l = list()
>>> type(l)
<class 'list'>
>>> len(l)
0
# 可以传入一个iterable对象作为参数来初始化成员
>>> l = list(range(1,5))
>>> type(l)
<class 'list'>
>>> len(l)
4
>>> l
[1, 2, 3, 4]
```

除了上述序列类型的公共操作外，`list`还单独支持`sort`方法。`sort`会原地排序，使用`<`比较操作符来对各元素进行比较。

```shell
>>> l = [7,4,2,5,3,6]
>>> l.sort()
>>> l
[2, 3, 4, 5, 6, 7]
```

### tuple

中文名称作“元组”，是不可变序列，通常用来存储异构数据（当然也支持存放同构数据，如用作不可变序列）。

常见的创建元组方式：

```shell
# 使用一对圆括号来表示空元组：()
>>> t = ()
>>> type(t)
<class 'tuple'>
# 多个成员用逗号分隔，为了与括号表达式做区分，单个成员也需要逗号
>>> t = (1,)
>>> type(t)
<class 'tuple'>
>>> t
(1,)
>>> t = (1,3,5)
>>> type(t)
<class 'tuple'>
>>> t
(1, 3, 5)
# 也可以仅保留逗号，省略括号
>>> t = 1,
>>> type(t)
<class 'tuple'>
>>> t
(1,)
>>> t = 1,3,5
>>> type(t)
<class 'tuple'>
>>> t
(1, 3, 5)
# 还可以使用内置构造函数
>>> t = tuple(list(range(1,5)))
>>> t
(1, 2, 3, 4)
>>> type(t)
<class 'tuple'>
```

> 生成元组的其实是逗号而不是圆括号，圆括号只是可选的，生成空元组或需要避免语法歧义的情况除外。 例如，`f(a, b, c)` 是在调用函数时附带三个参数，而 `f((a, b, c))` 则是在调用函数时附带一个三元组。

### `str`

字符串是日常编程中最为常用的类型，在Python中，内置了`str`文本序列类型，用作字符串，它是由Unicode码构成的不可变序列类型。

> 关于编码知识，可以参考[格物致知(0)——系统漫游](https://r00tk1ts.github.io/2023/04/13/%E6%A0%BC%E7%89%A9%E8%87%B4%E7%9F%A5(0)%E2%80%94%E2%80%94%E7%B3%BB%E7%BB%9F%E6%BC%AB%E6%B8%B8/#%E7%BC%96%E7%A0%81%E4%BB%8Eascii%E5%88%B0utf8)中编码一节。

Python中的字符串字面值有三种写法：
- 单引号：`'hello'`，'the "world"'(允许包含双引号)
- 双引号：`"hello"`，`"you're"`(允许包含单引号)
- 三重引号：常用于超长字符串、文档注释，可灵活跨行。
```python
'''
User Guide
'''

"""
Hello, world

Welcome to use Python!
"""
```

> 一些特殊字符无法直接使用字面值的方式书写在字符串value中，此时需要通过转义来完成，参考： [字符串与字节串字面值](https://docs.python.org/zh-cn/3/reference/lexical_analysis.html#strings) ，其中包括所支持的 [转义序列](https://docs.python.org/zh-cn/3/reference/lexical_analysis.html#escape-sequences)，以及禁用大多数转义序列处理的 `r` ("raw") 前缀。

```python
>>> s = 'hello\tworld'
>>> print(s)
hello	world
>>> len(s)
11
>>> 'wo' in s
True
>>> 'wd' in s
False
>>> s.count('l')
3
```

除了常规的不可变序列类型所支持的操作外，`str`还内置了非常丰富的成员方法(method)：

```python
>>> s.find('lo')
3
>>> s.replace('o', '0')
'hell0\tw0rld'
>>> s.split('\t')
['hello', 'world']
```

> 更多方法不一一枚举，详见: https://docs.python.org/zh-cn/3/library/stdtypes.html#string-methods

### `bytes`,`bytearray`

在日常编程中，与文本序列相对应的是二进制序列，Python使用内置类型`bytes`和`bytearray`来支持。二进制序列相比文本序列没有那么常用，一般常用于(反)序列化，底层数据封装等场景，新手入门先简单了解即可。

#### `bytes`

单个字节构成的不可变序列，表达方式与`str`类似，只是增加了一个前缀`b`：
- 单引号：`b'\x41\x42\x43'`
- 双引号：b = b"\x30\x31\x32"
- 三重引号:

> 字面值只允许使用ASCII字符，超出范围的二进制值必须使用转义序列来表达。

```python
>>> abc = b'\x41\x42\x43'
>>> abc
b'ABC'
>>> b = b"\x30\x31\x32"
>>> print(b)
b'012'
>>> b[0:1]
b'0'
>>> a = bytes(20)
>>> a
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
>>> b = bytes(range(20))
>>> b
b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\r\x0e\x0f\x10\x11\x12\x13'
```

#### `bytearray`

与`bytes`对应的可变序列类型：

```python
# 没有专属的字面值创建语法，必须通过内置的构造函数来创建
>>> a = bytearray()
>>> a
bytearray(b'')
>>> b = bytearray(10)
>>> b
bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
>>> c = bytearray(range(20))
>>> c
bytearray(b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\r\x0e\x0f\x10\x11\x12\x13')
```

`bytearray`和`byte`也都支持非常丰富的成员方法，这一点与`str`如出一辙。

> Python内置的二进制序列的核心类型是`memoryview`，其设计上的核心概念是[缓冲区协议](https://docs.python.org/zh-cn/3/c-api/buffer.html#bufferobjects)，对于操纵二进制的场景往往对性能有较高的要求，Python以此来避免冗余的拷贝。

## 集合类型

集合类型是由具有唯一性（通俗理解就是不重复）的[hashable](https://docs.python.org/zh-cn/3/glossary.html#term-hashable)对象所构成的无序多项集。常用于成员包含检测、序列去重、数学的集合类计算（交集、并集、差集等）。

Python使用内置的`set`和`frozenset`来支持集合类型。前者是可变类型，后者不可变。

常见的创建方法：

```python
# 通过构造函数，传入一个iterable对象
>>> s = set('abc')
>>> s
{'c', 'b', 'a'}
>>> s.add('d')
>>> s
{'c', 'd', 'b', 'a'}
>>> s.remove('a')
>>> s
{'c', 'd', 'b'}
# 通过字面值方式创建
>>> s = {'jack', 'mark'}
>>> type(s)
<class 'set'>
>>> s
{'mark', 'jack'}
# 使用集合推导式
>>> s = {x for x in 'passenger' if x not in 'abc'}
>>> s
{'s', 'r', 'g', 'p', 'e', 'n'}
```

正如序列类型一般，集合类型也支持丰富的操作，最常见的操作有3个：
- `len(s)`：返回集合 _s_ 中的元素数量（即 _s_ 的基数）。
- `x in s`：检测 _x_ 是否为 _s_ 中的成员。
- `x not in s`：检测 _x_ 是否非 _s_ 中的成员。
此外，集合类型还支持集合数学运算以及比较运算。

## 映射类型

即俗称的Key-Value（键值）字典型，Python使用`dict`来支持，它是可变对象。

字典的Key必须是可以[hashable](https://docs.python.org/zh-cn/3/glossary.html#term-hashable) 的值，因为字典是有序的，它需要根据哈希值来做内部的比较操作。

字典型的创建方法：

```python
# 使用花括号+逗号分割字面值创建
>>> d = {'jack': 1, 'mark': '2', 'chriss': 5, 'andrew': 3}
>>> d
{'jack': 1, 'mark': '2', 'chriss': 5, 'andrew': 3}
# 使用字典推导式
>>> d = {x: x ** 2 for x in range(10)}
>>> d
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
# 使用构造函数,传入kwargs
>>> a = dict(one=1, two=2, three=3)
>>> a
{'one': 1, 'two': 2, 'three': 3}
```

> `dict`有多个重载构造函数，初学者当前只需要了解即可，随着日后知识图谱的延展，自然而然可以理解它的设计。

字典型也支持多种操作，常见的操作如下：
- `list(d)`：返回字典`d`中所有的Key `list`。
- `len(d)`：返回字典`d`的项数。
- `d[key]`：返回 _d_ 中以 _key_ 为键的项。 如果映射中不存在 _key_ 则会引发 [`KeyError`](https://docs.python.org/zh-cn/3/library/exceptions.html#KeyError "KeyError")。
- `d[key] = value`：将 `d[key]` 设为 _value_。
- `del d[key]`：将 `d[key]` 从 _d_ 中移除。 如果映射中不存在 _key_ 则会引发 [`KeyError`](https://docs.python.org/zh-cn/3/library/exceptions.html#KeyError "KeyError")。
- `key in d`：如果 _d_ 中存在键 _key_ 则返回 `True`，否则返回 `False`。
- `key not in d`：等价于 `not key in d`。
- `iter(d)`：返回以字典的键为元素的迭代器。 这是 `iter(d.keys())` 的快捷方式。
- `clear()`：移除字典中的所有元素。
- `items()`：返回由字典项 (`(键, 值)` 对) 组成的一个新视图。
- `keys()`：返回由字典键组成的一个新视图。
- `values()`：返回由字典值组成的一个新视图。

> 视图是Python设计中的一个概念，详见[视图对象文档](https://docs.python.org/zh-cn/3/library/stdtypes.html#dict-views)。
> 
# 表达式与运算符

表达式是个很大的概念，他们是构成编程语言语句的基本单元，表达式可以组合嵌套，根据特定的运算规则完成想要的功能。比如上文的`a = 3+5`，`a`是定义的变量，`3+5`是算术表达式，`=`是赋值运算符，它们共同组成了一条赋值语句。

> 新手上路没必要把各种概念理解得特别清楚，那是进阶之路语言律师的选修课。

## 赋值运算符

除了通过简单的`=`来完成赋值运算外，还有一些复合的赋值运算符，它们与算术运算耦合，比如：

`+=` `-=` `*=` `/=` `%=` `//=` `**=` `&=` `|=` `^=` `>>=` `<<=`

赋值运算符是所有运算里优先级最低的。

> 对于大多数语言来说，运算符的优先级是：赋值 < 逻辑 < 关系 < 算术

## 布尔运算

布尔运算有3种：`or`, `and`, `not`即或、与、非。按优先级升序排列：

| 运算        | 结果：                                        |
| --------- | ------------------------------------------ |
| `x or y`  | 如果 _x_ 为真值，则 _x_，否则 _y_                    |
| `x and y` | if _x_ is false, then _x_, else _y_        |
| `not x`   | if _x_ is false, then `True`, else `False` |

对于`or`和`and`来说，它们具有短路特性：
- `or`: 只有在第一个参数为假值时才会对第二个参数求值。
- `and`：只有在第一个参数为真值时才会对第二个参数求值。

> 一些语言也称其为逻辑运算。

### 逻辑值检测

真值和假值的判定由逻辑值检测来完成，任何对象都可以进行逻辑值检测，以便在`if`,`while`等分支/循环语句的条件判定时使用，对象默认都具有真值，在Python中只有以下对象具有假值：
- 被定义为假值的常量: `None` 和 `False`
- 任何数值类型的零: `0`, `0.0`, `0j`, `Decimal(0)`, `Fraction(0, 1)`
- 空的序列和多项集: `''`, `()`, `[]`, `{}`, `set()`, `range(0)`

此外，用户自定义`class`如果对`__bool__()`成员方法返回`False`，或者`__len__()`方法返回`0`，也被视为具有假值。

## 比较运算

Python有8种比较运算符，它们优先级相同（且都高于布尔运算），比较运算可以任意串联，按左结合（如`x < y <= z` 等价于 `x < y and y <= z`）：

| 运算       | 含意      | 备注    |
| -------- | ------- | ----- |
| `<`      | 严格小于    |       |
| `<=`     | 小于或等于   |       |
| `>`      | 严格大于    |       |
| `>=`     | 大于或等于   |       |
| `==`     | 等于      | 总有定义  |
| `!=`     | 不等于     |       |
| `is`     | 对象标识    | 无法自定义 |
| `is not` | 否定的对象标识 | 无法自定义 |

相同类型的对象可以进行比较，不同类型的对象不能进行比较运算（除了数字型）。特别地，对`tuple`和`list`来说，实际上是通过比较对应元素的字典序（因此相等意味着序列长度相同且每对元素两两相等）。

> 一些语言也称其为关系运算。

## 算术运算

数字型特有的运算表达式，优先级高于比较运算。已在前文**运算表达式结果**一节中叙述。

```shell
# 相当于(3 + 5) > 7
>>> 3 + 5 > 7
True
```

### 位运算

位运算可以看作是一种特殊的算术运算，它按bit去计算。

| 运算       | 结果：               | 备注                     |
| -------- | ----------------- | ---------------------- |
| `x \| y` | _x_ 和 _y_ 按位 _或_  | (4)                    |
| `x ^ y`  | _x_ 和 _y_ 按位 _异或_ | (4)                    |
| `x & y`  | _x_ 和 _y_ 按位 _与_  | (4)                    |
| `x << n` | _x_ 左移 _n_ 位      | 等价于乘以 `pow(2, n)`      |
| `x >> n` | _x_ 右移 _n_ 位      | 等价于除以 `pow(2, n)`，向下取整 |
| `~x`     | _x_ 逐位取反          |                        |
> Note：
> 1. Python的负数不支持移位运算(抛出ValueError异常)。
> 2. 逐位取反运算`~`已于3.12版本弃用。

```shell
# 1是0b01,2是0b10,1|2得到0b11,也就是3
>>> 1|2 == 3
True
# 0b01 & 0b10得到0b00，也就是0
>>> 1 & 2 == 0
True
# 异或运算规则：相同得0，不同得1，故0b01 ^ 0b10还是得到3，即0b11
>>> print(bin(1^2))
0b11
```


# 附录

- [Python内置类型](https://docs.python.org/zh-cn/3/library/stdtypes.html#numeric-types-int-float-complex)
- [Python指南](https://docs.python.org/zh-cn/3.10/tutorial/introduction.html#numbers)