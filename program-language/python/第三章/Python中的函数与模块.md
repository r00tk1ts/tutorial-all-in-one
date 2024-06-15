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

对于有多个参数的函数来说，实参与形参按位置一一对应，即：

```python
def add(a, b):
	return a + b

# 3传给a，5传给b
print(add(3,5))
```

也可以通过显式地指定参数名称，来明确参数的对应关系，此时，顺序可以任意指定：

```python
print(add(b=5, a=3))
```

> 思考：如果多个参数中，部分使用了参数名指定，剩下的则没有使用，此时参数的对应关系如何判定？
> 
### 默认参数值

Python中的函数可以有默认的参数值，在实参传递时，如果缺省则会使用该默认值。

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

### 可变参数


# 模块