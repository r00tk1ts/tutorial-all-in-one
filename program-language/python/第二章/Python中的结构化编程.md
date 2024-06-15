# 结构化编程

**[结构化编程](https://zh.wikipedia.org/zh-cn/%E7%BB%93%E6%9E%84%E5%8C%96%E7%BC%96%E7%A8%8B)**（英语：Structured Programming），是一种最常见的[编程范式](https://zh.wikipedia.org/wiki/%E7%B7%A8%E7%A8%8B%E5%85%B8%E7%AF%84 "编程典范")。它采用[子程序](https://zh.wikipedia.org/wiki/%E5%AD%90%E7%A8%8B%E5%BA%8F "子程序")、[块结构](https://zh.wikipedia.org/wiki/%E5%9D%97%E7%BB%93%E6%9E%84 "块结构")、[for循环](https://zh.wikipedia.org/wiki/For%E8%BF%B4%E5%9C%88 "For循环")以及[while循环](https://zh.wikipedia.org/wiki/While%E8%BF%B4%E5%9C%88 "While循环")等结构，来取代传统的 [goto](https://zh.wikipedia.org/wiki/Goto "Goto")。希望借此来改善[计算机程序](https://zh.wikipedia.org/wiki/%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%A8%8B%E5%BA%8F)的明晰性、质量以及开发时间，并且避免写出[面条式代码](https://zh.wikipedia.org/wiki/%E9%9D%A2%E6%9D%A1%E5%BC%8F%E4%BB%A3%E7%A0%81 "面条式代码")。

> 结构化编程在1960年代开始发展，[科拉多·伯姆](https://zh.wikipedia.org/w/index.php?title=%E7%A7%91%E6%8B%89%E5%A4%9A%C2%B7%E4%BC%AF%E5%A7%86&action=edit&redlink=1)及[朱塞佩·贾可皮尼](https://zh.wikipedia.org/w/index.php?title=%E6%9C%B1%E5%A1%9E%E4%BD%A9%C2%B7%E8%B3%88%E5%8F%AF%E7%9A%AE%E5%B0%BC&action=edit&redlink=1 "朱塞佩·贾可皮尼（页面不存在）")（Giuseppe Jacopini）于1966年5月在《Communications of the ACM》期刊发表[论文](https://zh.wikipedia.org/wiki/%E7%BB%93%E6%9E%84%E5%8C%96%E7%BC%96%E7%A8%8B#cite_note-1)，说明任何一个有goto指令的程序，可以改为完全不使用goto指令的程序，后来[艾兹赫尔·戴克斯特拉](https://zh.wikipedia.org/wiki/%E8%89%BE%E5%85%B9%E8%B5%AB%E5%B0%94%C2%B7%E6%88%B4%E5%85%8B%E6%96%AF%E7%89%B9%E6%8B%89 "艾兹赫尔·戴克斯特拉")在1968年也提出著名的论文[《Go To Statement Considered Harmful》](https://zh.wikipedia.org/wiki/%E7%BB%93%E6%9E%84%E5%8C%96%E7%BC%96%E7%A8%8B#cite_note-dijkstra1968-2)，因此结构化编程开始盛行。

现代编程语言在设计上往往都支持结构化编程这种基础范式，然后再因用途与审美差异，各自再额外支持其他不同的编程范式，比如：[函数式编程](https://zh.wikipedia.org/wiki/%E5%87%BD%E6%95%B0%E5%BC%8F%E7%BC%96%E7%A8%8B "函数式编程")、[指令式编程](https://zh.wikipedia.org/wiki/%E6%8C%87%E4%BB%A4%E5%BC%8F%E7%B7%A8%E7%A8%8B "指令式编程")、[过程式编程](https://zh.wikipedia.org/wiki/%E8%BF%87%E7%A8%8B%E5%BC%8F%E7%BC%96%E7%A8%8B "过程式编程")、[面向对象编程](https://zh.wikipedia.org/wiki/%E9%9D%A2%E5%90%91%E5%AF%B9%E8%B1%A1%E7%A8%8B%E5%BA%8F%E8%AE%BE%E8%AE%A1 "面向对象程序设计")等等。一些语言甚至可以同时支持多种编程范式。

> 比如我们的主角——Python，就同时支持过程式、面向对象和函数式编程。

结构化的程序由简单、有层次的程序流程架构所组成，可分为顺序、分支(选择)和循环(重复)三种结构。

![[Pasted image 20240609165628.png]]

## 顺序结构

顺序结构就是指程序正常的执行流，代码从上到下一行行执行，上一行执行完毕后，再执行下一行代码。

这个没什么好讲的。

## 分支结构

分支是指根据特定的条件，选择数段程序中的某一个来执行，一般会用if..then..else或是switch..case等关键字来设计。

![[Pasted image 20240609165545.png]]

## 循环结构

循环是指重复执行某一段程序，直到(不)满足某个条件，或是某个集合中所有元素均已遍历过才终止。一般设计上使用while,repeat,for,foreach,do..until,do..while等关键字来标识。
![[Pasted image 20240609165709.png]]

# Python中的结构化控制

## 分支语句

Python中的分支语句有两类：if-else和match-case。

### `if`,`else`

`if`是最常用的分支控制语句，在Python中，关键字`if`后面紧跟着一个表达式，根据该表达式的逻辑值检测（详见：[[Python中的变量与表达式]]），来决定代码执行流的走向。

举个例子，我们写一个猜数游戏，由系统生成一个随机的0~100的整数，再让用户输入一个整数，如果输入的整数和系统生成的随机数不一致，就打印"Incorrect"信息，如果一样则什么都不做：

```python
import random

# 使用random包生成0~100的随机数
rng = random.randint(0, 100)
# 用户输入整数
x = int(input("Please enter an integer: "))
# 如果x != rng的逻辑值为True，则打印Incorrect，否则不执行内层代码块
# python的代码块作用域由缩进来控制
if x != rng:
    print("Incorrect")
    
# if语句块结束，无论内层语句块是否执行，都会最终执行到这里
print("The random number is ", rng)
```

```shell
Please enter an integer: 42
Incorrect
The random number is  81
```

如果希望在不满足条件时，能执行其他的代码块，则可以组合使用`else`关键字：

```python
import random

rng = random.randint(0, 100)
x = int(input("Please enter an integer: "))
if x != rng:
    print("Incorrect.")
else:
    print("Bingo!")

print("The random number is ", rng)
```

`if`和`else`的代码块逻辑上是互斥的，程序的执行流根据逻辑值的真假，每次只可能执行到其中的某一组代码块。此外还要注意：`else`关键字后不能有任何的表达式，它后面紧跟着语法上的冒号字符。

当然，正如世间万物并非非黑即白，分支控制也可以有多组，比如，我们现在希望，当用户输入的数字比`rng`大时，输出"Bigger"，比`rng`小时则输出"Smaller"，此时就需要构造三个分支。Python支持级联的`if`语句，可以通过`elif`关键字来控制：

```python
import random

rng = random.randint(0, 100)
x = int(input("Please enter an integer: "))
if x > rng:
    print("Bigger")
elif x < rng:
    print("Smaller")
else:
    print("Bingo!")

print("The random number is ", rng)
```

上面是一种相对惯用的写法，在Python中，分支语句也支持组合嵌套，所以我们也可以像下面这样写：

```python
import random

rng = random.randint(0, 100)
x = int(input("Please enter an integer: "))
if x != rng:
    if x > rng:
        print("Bigger")
    else:
        print("Smaller")
else:
    print("Bingo!")

print("The random number is ", rng)
```

在外层的`if`代码块内部嵌套了一组内层`if..else`，相比于前者，后者显得更加臃肿。

因此，在Python中，if语句的语法结构可以归纳为：

```
if "expression": 
	"suite"
elif[optional] "expression":
	"suite"
else[optional]:
	"suite"
```

### `match`

match语句接受一个表达式，并把它的值与一个或多个case块给出的一系列模式进行匹配，成功匹配的case语句块会得到执行。

> 像是C++,Java,Go等流行的编程语言中，往往会设计一个switch/case语句，用于匹配多值的分支选择情景，但是在Python中原本并没有类似switch/case的语法，直到3.10版本才引入了match-case语句。然而相比switch/case的语法，Python中的match-case更接近Rust,Haskell等语言中的模式匹配。

最简单的形式就是类似其他语言中的switch/case语法：

```python
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        # 多个值可以用'|'来分隔
        case 401 | 403:
		    return "Not allowed"
		case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        # 类似switch-case中的default分支，变量名_作为通配符去匹配所有others情况
        case _:
            return "Something's wrong with the internet"
```

除了基础的类Switch-case的用法外，match更多场景用于较为复杂的模式匹配，通过结构化绑定的语法从case中提取出对应值，类似解包赋值。

对于初学者来说，只需要先掌握match-case的最基础用法即可。

## 循环语句

Python的循环有while和for两种，它们都支持组合嵌套，我们可以灵活地组合嵌套分支语句，甚至构建多层循环结构。

### `while`

while语句会在表达式逻辑值为真时反复执行，语法结构形如：

```
while "expression": 
	"suite"
else[optional]: 
	"suite"
```

还是以猜数游戏举例，前面的程序中，我们仅让用户猜了一次，不论结果如何，就结束了，借助`while`，我们可以实现一个让用户反复猜数，直到猜中的程序：

```python
import random

rng = random.randint(0, 100)
x = int(input("Please enter an integer: "))

while x != rng:
    if x > rng:
        print("Bigger")
    else:
        print("Smaller")
	# 重新输入一个整数，赋值给x
    x = int(input("Try again:"))
else:
	print("Bingo!")
	
print("The random number is ", rng)
```

```shell
Please enter an integer: 50
Smaller
Try again:75
Bigger
Try again:62
Bigger
Try again:56
Smaller
Try again:59
Bigger
Try again:57
Bingo!
The random number is  57
```

我们通过二分法的策略去猜，最终猜到了随机数是57。

> 思考：聪明的小伙伴可以思考一下，采用二分法猜数，至多需要几次一定可以猜到最终结果呢？

### `for`

Python中的for语句用于遍历可迭代(Iterable)对象(例如上一节学到的`str`,`list`,`tuple`,`range`)等，按照它们的顺序逐元素遍历，语法结构形如：

```
for "target_list" in "expression_list":
	suite
else[optional]: 
	suite
```

> for语句也支持一个可选的else子句，初学者可以暂不掌握。

表达式列表会被求值一次，它产生一个Iterable对象，for语句循环遍历每一个对象，执行suite语句块。

举个例子：

```python
l = [1,2,3,4,5]
t = tuple(l)
s = "hello"

print("iterate range object:")
for i in range(5):
    print(i)

print("iterate list object:")
for i in l:
    print(i)

print("iterate tuple object:")
for i in t:
    print(i)

print("iterate str object:")
for i in s:
    print(i)
```

```shell
iterate range object:
0
1
2
3
4
iterate list object:
1
2
3
4
5
iterate tuple object:
1
2
3
4
5
iterate str object:
h
e
l
l
o
```

循环中的变量`i`在每一轮迭代时，都会用目标变量赋值，它本质上是一个复制体，在循环内修改`i`并不会影响到原本的可迭代对象，且在下一轮循环执行的开始，立刻被赋值重置。

这就意味着：

```python
l = [1,2,3,4,5] 
print("iterate list object:")
for i in l:
	# 试图让l的每个元素都自增1
    i += 1
# 此时l依然是[1,2,3,4,5]
print(l)
```

> 如果想要修改l的成员，可以这样做：
> `for i in range(len(l)): l[i] += 1`

### `break`与`continue`

`break`和`continue`都是循环控制语句中的子句，前者用于打断整个循环的执行，后者用于控制本轮循环的结束。**对于多层嵌套的循环来说，二者都只会影响子句所在位置的最内层循环**。

比如，我们可以修改猜数游戏，增加一个最多只能重试6次的限制：

```python
import random

rng = random.randint(0, 100)
x = int(input("Please enter an integer: "))
limit = 6

while x != rng:
    if x > rng:
        print("Bigger")
    else:
        print("Smaller")

	# 如果limit已经减到了0，就意味着不再有重试的机会
    if limit == 0:
        print("Quota exhaust")
        break

    x = int(input("Try again:"))
    limit -= 1
else:
    print("Bingo!")

print("The random number is ", rng)
```

有些用户在输入时可能会忘记条件，输入了一个0~100范围之外的整数，我们希望对于这种情况，提供用户一个重新输入的机会，而不占用重试的次数，改良体验。

这个需求可以通过`continue`来完成：

```python
import random

rng = random.randint(0, 100)
x = int(input("Please enter an integer: "))
limit = 6

while x != rng:
    if x > 100 or x < 0:
        x = int(input("Ingore invalid interger, input again:"))
        continue

    if x > rng:
        print("Bigger")
    else:
        print("Smaller")

    if limit == 0:
        print("Quata exhaust")
        break

    x = int(input("Try again:"))
    limit -= 1
else:
    print("Bingo!")

print("The random number is ", rng)
```

到此，我们的猜数程序就初具雏形了，它虽然还有着各种各样的缺陷，但至少已能满足我们的基本诉求。随着后续的学习，我们还将逐步完善这段代码，进化到完全体。

> 一个肉眼可见的缺陷：产品对用户的心智不能要求过高，尽管要求输入一个整数，但用户很可能会输入乱七八糟的内容，聪明的小伙伴可以自己试一下，如果输入一个非整数，程序在执行过程中会遇到什么问题？

# 附录

- [结构化编程](https://zh.wikipedia.org/zh-cn/%E7%BB%93%E6%9E%84%E5%8C%96%E7%BC%96%E7%A8%8B)
- [Python语言参考手册-简单语句](https://docs.python.org/zh-cn/3/reference/simple_stmts.html)
- [Python语言参考手册-复合语句](https://docs.python.org/zh-cn/3/reference/compound_stmts.html)