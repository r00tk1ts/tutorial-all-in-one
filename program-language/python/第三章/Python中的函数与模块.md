# 函数

[函数](https://zh.wikipedia.org/zh-cn/%E5%87%BD%E6%95%B0)本是数学中的一个概念，它用于描述集合$X$(定义域)到集合$Y$(值域)的一种映射关系。而在大部分编程语言中，也有一个“函数”的概念，但此函数非彼函数，在程序设计领域，函数(function)是一种[子程序(subroutine)](https://zh.wikipedia.org/wiki/%E5%AD%90%E7%A8%8B%E5%BA%8F)，它在一个程序项目中相对独立完成某个子功能，由一到多个语句块组成。

## 函数的作用

函数实际上是对某一个子功能的抽象，那么为何要做这种抽象呢？既然已经学习过了上一节课的[[Python中的结构化编程]]，我们只需要使用顺序、分支和循环结构平铺直叙，完成我们的工作不就大功告成了吗？

的确，这样做当然可行，但难免缺乏必要的抽象，容易写出大段重复的代码。软件工程向来提倡不要重复造轮子，对于特定的子功能，我们可以通过一次性的封装，将其抽象成独立的函数，以便于复用。

> 编程大师Martin Fowler曾言：“**代码有很多种坏味道，重复是最坏的一种！**”

除了函数(function)以外，在编程语言中我们还经常会遇到另外两个与之相似的概念：过程(procedure)和方法(method)，它们与函数一样，也是一种子程序。在大部分语言中，过程和函数几乎是同等的概念（比如C语言），方法则是在OOP(面向对象编程)语言中的术语，它和类与对象绑定。

## 函数的定义

在前两个章节的学习中，我们其实已经使用过了很多函数，诸如`type,id,len`。那么函数在Python中是如何定义的呢？在[语言参考手册](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#function-definitions)中它显得相当复杂：

```
funcdef ::= [decorators] "def" funcname [type_params] "(" [parameter_list] ")"
			["->" expression] ":" suite
decorators ::= decorator+
decorator ::= "@" assignment_expression NEWLINE
parameter_list ::= defparameter ("," defparameter)* "," "/" ["," [parameter_list_no_posonly]] | parameter_list_no_posonly
parameter_list_no_posonly ::= defparameter ("," defparameter)* ["," [parameter_list_starargs]] | parameter_list_starargs
parameter_list_starargs ::= "*" [parameter] ("," defparameter)* ["," ["**" parameter [","]]] | "**" parameter [","]
parameter ::= identifier [":" expression]
defparameter ::= parameter ["=" expression]
funcname ::= identifier
```

我们暂且忽略规则中诸如decorators，type_params, parameter_list_starargs等复杂的optional部分，实际上函数的定义相当简单：只需要定义一个函数的名称funcname，并声明参数列表parameter_list即可。形如：

```python
# 函数名是my_abs，参数列表中只有一个参数：x
def my_abs(x):
	if x < 0:
		return -x
	else:
		return x
```

Python支持可选地显示声明返回类型，如果不声明则语言会根据return语句后的表达式进行推导（得益于动态类型的设计）。如果没有`return`语句，或者`return`后什么都不写，则函数默认返回一个特殊的值：`None`。

> 许多语言都对空值做了特殊的处理，像是C中的`void`, C++中的`nullptr`，处理手法各不相同。Python中对于空值的处理是单独设计了一个`NoneType`类型，它的值只有一个`None`。

函数定义并不会执行函数体，只有当函数被显式调用时才会使用传递的参数执行函数体的语句块。

> 函数定义是一条可执行语句。 它执行时会在当前局部命名空间中将函数名称绑定到一个函数对象。 这个函数对象包含对当前全局命名空间的引用，作为函数被调用时所使用的全局命名空间。

```python
while True:
	n = input("Please enter a number: ")
	# 函数的调用可以嵌套：
	# 使用n作为参数调用了my_abs，返回的结果又作为print的参数调用了print对结果进行了打印
	print(my_abs(n))
```

### 形参与实参

函数在定义时，书写的参数名称一般被称为形参(formal parameter)，而在被调用时，传递的实际参数被称为实参(actual argument)。Python在设计上，变量使用引用语义(Reference Semantics)，因此，参数是按引用（即内存地址）来传递。

> Java,C#,Python的变量都是引用语义，变量名称只是绑定到内存中具体变量的一个标签，已废弃变量堆内存的回收依赖于GC(Garbage Collector)。而像是C,C++则是标准的值语义，它们需要自己维护变量的生命期，对于需要引用传递的情况，则直接传递指针型。还有一些特立独行的，像是GO是值语义，但slice和map除外，Rust无需GC，因为它有高贵的所有权。

> 关于值语义和引用语义，可以参考[C++模板从入门到劝退(0)——左值与右值#值语义](https://r00tk1ts.github.io/2022/05/27/C++%E6%A8%A1%E6%9D%BF%E4%BB%8E%E5%85%A5%E9%97%A8%E5%88%B0%E5%8A%9D%E9%80%80(0)%E2%80%94%E2%80%94%E5%B7%A6%E5%80%BC%E4%B8%8E%E5%8F%B3%E5%80%BC/#%E5%80%BC%E8%AF%AD%E4%B9%89)

按引用传递意味着，当你将一个对象作为实参传递给函数时，实际上传递的是该对象的引用，而不是对象本身。因此，在函数内部对形参的修改会影响到原始对象。但是，对于不可变类型（如数字、字符串和元组），由于它们的值是不可变的，所以在函数内部对这些类型的形参进行修改不会影响到原始对象，而是会重新绑定到一个新的对象上。

对`list`型可变对象来说：

```python
def modify_list(lst):
    lst.append("new item")

my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # 输出：[1, 2, 3, 'new item']
```

而对`int`型不可变对象来说：

```python
def modify_integer(num):
	# 这里对num的赋值操作，实际上是让num绑定到了另一个int对象上
    num = num + 1

my_number = 10
modify_integer(my_number)
print(my_number)  # 输出：10，而不是11
```

> 思考：如果在modify_list的最后增加一句`lst = []`，外部`print(my_list)`的结果会是什么？

#### 位置参数

对于有多个参数的函数来说，实参与形参按位置一一对应，即：**位置参数**。这也是最常规的情况：

```python
def add(a, b):
	return a + b

# 3传给a，5传给b
print(add(3,5))
```

#### 关键字参数

也可以通过显式地指定参数名称，来明确参数的对应关系，此时，顺序可以任意调换：

```python
print(add(b=5, a=3))
```

这种`kwarg=value`形式的参数，被称作：**关键字参数**。如果在函数调用时，同时包含位置参数和关键字参数，那么位置参数必须全部放置于关键字参数之前。

### 参数默认值

Python中的函数形参可以有默认值，在实参传递时，如果缺省则会使用该默认值。

例如：

```python
def add(lst, base=0):
	result = base
	for elem in lst:
		result += elem
	return result

# base使用默认值0
print(add(range(1,10)))

# base使用参数值100
print(add(range(1,10), 100))
```

### 特殊参数

到此，我们已知对于Python的函数，常规情况下参数既可以按位置传递、也可以按关键字指定传递。为了让代码更加明晰，Python语言在设计上对参数的传递方式做了一种较为复杂的语法约束：

```python
def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
      -----------    ----------     ----------
        |             |                  |
        |        Positional or keyword   |
        |                                - Keyword only
         -- Positional only
```

`/` 和 `*` 是可选的。这些符号表明形参如何把参数值传递给函数：位置、位置或关键字、关键字。

> 关键字形参也叫作命名形参。

说明：

- 使用仅限位置形参，可以让用户无法使用形参名。形参名没有实际意义时，强制调用函数的实参顺序时，或同时接收位置形参和关键字时，这种方式很有用。
- 当形参名有实际意义，且显式名称可以让函数定义更易理解时，阻止用户依赖传递实参的位置时，才使用关键字。
- 对于 API，使用仅限位置形参，可以防止未来修改形参名时造成破坏性的 API 变动。

### 可变参数列表

上述的函数参数都是固定的，调用函数时也是按位置或关键字一一对应，实际上，大部分编程语言还支持一种更灵活的参数：可变参数列表。

可变参数列表(variadic parameter list)是一种在调用时可以接收零到任意多个异构参数的特殊参数。它通常在形参列表的末尾，Python中以星号表达式来定义，如:

```python
# args是一个任意参数列表
def add(base, *args)
	result = base
	for arg in args:
		result += arg
	return result
```

`*args`的后面仅能设置关键字参数，不能再设置位置参数，聪明的小伙伴可以想想为什么？

`args`实际上接收的是一个`tuple`，当然，它是个`Iterable`对象，所以可以用`for`循环来遍历。

> 很多语言都支持可变参数列表，但是手法上八仙过海、各显神通。

可变参数列表也可以传递给其他函数或方法：

```python
def concat(*args, sep="/"):
	return sep.join(args)
```

### 特殊的关键字参数

相对于可变参数列表，Python还支持另外一种相当灵活的参数，它是一种特别的关键字参数，可以对关键字参数进行聚合，通过双星号表达式来定义：

```python
# kwargs是字典型关键字参数，它必须放在位置参数和可变参数列表之后
def add(base, *args, **kwargs):
	result = base
	for arg in args:
		result += arg
	for value in kwargs.values():
		result += value
	return result

print(add(0, 1, 2, a=3, b=4)) # 10
```

函数调用`add(0, 1, 2, a=3, b=4)`中，`0`按位置匹配`base`形参，`1,2`匹配到`args`可变参数列表，`a=3,b=4`匹配到`kwargs`，`kwargs`接收一个`dict`，它包含与函数中已定义形参对应之外的所有关键字参数。

> `kwargs.values()`是使用`dict`的`values`方法，它返回一个由`value`组成的 `Iterable`对象。

# 模块

编写好的特定子功能，终归是需要一种手段把它维护起来，让我们后续能够像用标准库包函数那样方便的使用。在Python中，我们通过模块(module)来管理函数，将封装好的函数打包成模块，方便在其他地方重复使用。

像是在猜数游戏`guess.py`中，我们曾使用了Python标准库的`random`模块的randint函数来生成随机数。

在Python中，每个文件天生就是一个模块，模块名就是它的文件名。

比如我们来实现一个计算斐波那契数的函数，写入到`fibo.py`：

```python
def fib(n):   
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result
```

此时，**同目录下**的另一个python脚本代码就可以通过`import`语法来使用`fib`函数：

```python
import fibo

# 调用fibo模块的fib函数
print(fibo.fib(100))
```

## 模块的引用

大型模块往往包含非常丰富的函数，它们本身也会`import`其他模块的函数来完成自己的功能，还是以`random`为例，我们可以在python的lib下找到：

![[Pasted image 20240615221314.png]]

random.py中包含了我们使用的randint函数的定义。

我们走读random.py的代码，也会发现，它确实也`import`了相当多的其他模块：

![[Pasted image 20240615221447.png]]

每个模块都会包含可执行语句和函数定义，它们用于初始化模块，仅在`import`语句首次遇到模块名时执行。

除了`import`语句外，还可以使用变种的`from import`语句，`import`语句导入模块后，想要使用模块内定义的函数，必须使用模块名作为前缀，比如：`random.randint(0,100)`来调用`randint`函数。而`from import`则可以移除对模块名前缀的引用：

```python
from random import randint

# 无需random前缀
n = randint(0, 100)
```

> 但from import只能导入所需的函数，如果希望导入random中所有名称，可以用`from xxx import *`语句，但并不推荐。

`from import`语法移除了对包名前缀的书写，虽然让代码更精简了，但却可能引入一个问题：不同模块的函数重名问题，为了解决这个问题，可以使用`as`子句来设置别名。

## 模块搜索路径

当导入一个名为`random`的模块时，解释器首先会搜索具有该名称的内置模块。 这些模块的名称在 [`sys.builtin_module_names`](https://docs.python.org/zh-cn/3/library/sys.html#sys.builtin_module_names "sys.builtin_module_names") 中列出。 如果未找到，它将在变量 [`sys.path`](https://docs.python.org/zh-cn/3/library/sys.html#sys.path "sys.path") 所给出的目录列表中搜索名为 `spam.py` 的文件。 [`sys.path`](https://docs.python.org/zh-cn/3/library/sys.html#sys.path "sys.path") 是从这些位置初始化的:

- 被命令行直接运行的脚本所在的目录（或未指定文件时的当前目录）。
- [`PYTHONPATH`](https://docs.python.org/zh-cn/3/using/cmdline.html#envvar-PYTHONPATH) （目录列表，与 shell 变量 `PATH` 的语法一样）。
- 依赖于安装的默认值（按照惯例包括一个 `site-packages` 目录，由 [`site`](https://docs.python.org/zh-cn/3/library/site.html#module-site "site: Module responsible for site-specific configuration.") 模块处理）。

初始化后，Python 程序可以更改 [`sys.path`](https://docs.python.org/zh-cn/3/library/sys.html#sys.path "sys.path")。脚本所在的目录先于标准库所在的路径被搜索。这意味着，脚本所在的目录如果有和标准库同名的文件，那么加载的是该目录里的，而不是标准库的。

## 模块定义的名称

可以用`dir()`内置函数来查看任意模块内定义的名称，比如我们来看看`random`：

```python
>>> import random
>>> dir(random)
['BPF', 'LOG4', 'NV_MAGICCONST', 'RECIP_BPF', 'Random', 'SG_MAGICCONST', 'SystemRandom',
'TWOPI', '_ONE', '_Sequence', '__all__', '__builtins__', '__cached__', '__doc__', '__file
__', '__loader__', '__name__', '__package__', '__spec__', '_accumulate', '_acos', '_bisec
t', '_ceil', '_cos', '_e', '_exp', '_fabs', '_floor', '_index', '_inst', '_isfinite', '_l
gamma', '_log', '_log2', '_os', '_pi', '_random', '_repeat', '_sha512', '_sin', '_sqrt',
'_test', '_test_generator', '_urandom', '_warn', 'betavariate', 'binomialvariate', 'choic
e', 'choices', 'expovariate', 'gammavariate', 'gauss', 'getrandbits', 'getstate', 'lognor
mvariate', 'normalvariate', 'paretovariate', 'randbytes', 'randint', 'random', 'randrange
', 'sample', 'seed', 'setstate', 'shuffle', 'triangular', 'uniform', 'vonmisesvariate', '
weibullvariate']
```

应有尽有，也可以看到我们熟悉的randint函数。

## 包

包(Package)是通过使用“带点号模块名”来构造 Python 模块命名空间的一种方式。 例如，模块名 `A.B` 表示名为 `A` 的包中名为 `B` 的子模块。 就像使用模块可以让不同模块的作者不必担心彼此的全局变量名一样，使用带点号模块名也可以让 NumPy 或 Pillow 等多模块包的作者也不必担心彼此的模块名冲突。

Python安装后，标准库内的所有包都是可用的，如果需要使用第三方包，则需要按需安装。

> 现代编程语言都有自己的包管理能力，Python可以用pip工具来方便的安装第三方Package。

比如标准库的http包，它的构成如下：

![[Pasted image 20240615223813.png]]

> 它们和标准库的模块一样，也在`sys.path`中，故可以通过`import`找到。

每个包都得有个`__init__.py`文件(最简单的情况下，它的内容甚至可以为空)来标识该目录是一个包而非其他，它一般用来执行包的初始化代码、设置`__all__`变量等。

当我们需要使用`http`包中某个子模块比如`client`时，需要书写`import http.client`，或是`from http import client`来导入。前者在导入后使用时，必须携带完整的前缀`http.client`，后者则直接写`client.`即可。与前文模块的规则本质上并无二致。

> 思考一下：我们知道`from module import *`会导入模块内所有定义的名称，那么`from package import *`会如何呢？会导入所有子模块吗？

# 附录

- [子程序(subroutine)](https://zh.wikipedia.org/wiki/%E5%AD%90%E7%A8%8B%E5%BA%8F)
- [Python Tutorial - 函数定义详解](https://docs.python.org/zh-cn/3/tutorial/controlflow.html#more-on-defining-functions)
- [Python语言手册-函数定义](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#function-definitions)
- [Python Tutorial - 模块](https://docs.python.org/zh-cn/3/tutorial/modules.html)

