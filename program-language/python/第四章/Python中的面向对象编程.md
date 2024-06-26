# 面向对象编程

**面向对象编程**（英语：Object-oriented programming，[缩写](https://zh.wikipedia.org/wiki/%E7%BC%A9%E5%86%99 "缩写")：OOP）是一种非常流行的[编程范式](https://zh.wikipedia.org/wiki/%E7%BC%96%E7%A8%8B%E8%8C%83%E5%9E%8B "编程范型")，它将对象(object)作为程序的基本单元，每一个对象都是类(class)的实例(instance)，类是自定义的嵌套复杂类型，它包含成员数据和成员方法，它们随着对象的实例化而生产，成员方法一般用来操纵对象的成员数据。

OOP的抽象方法将程序设计成彼此相关的对象，对象相对独立，但可以互相访问，这与传统的指令式/过程式的思路恰恰相反（将程序看作一系列[函数](https://zh.wikipedia.org/wiki/%E5%87%BD%E6%95%B0 "函数")的集合，或者直接就是一系列对电脑下达的指令）。每一个对象都应该能够接受数据、处理数据并将数据传达给其它对象。

OOP应用于程序设计，可以提高软件的复用性、灵活性和扩展性，许多主流编程语言都支持OOP范式，例如: C++,Java,C#,Javascript等等。我们的主角Python也支持OOP。

> 严格意义上的OOP最早出现于上世纪70年代诞生的Smalltalk语言，程序中的数据和操纵数据的方法在逻辑上是一个整体，即对象。对象可以接收消息，通过消息传递让多个对象协同，以此可以构造结构清晰的系统来降低软件整体的复杂度。当然，OOP也不是解决软件开发中所有问题的“银弹”（银弹？tan90°）。可以参考IBM360系统之父弗雷德里克·布鲁克斯所发表的论文《没有银弹：软件工程的本质性与附属性工作》和软件工程经典著作《人月神话》一书。

## 类与对象

大部分实现了OOP的编程语言，核心概念往往由三者构成：封装(Encapsulation)、继承(Inheritance)、多态(Polymorphism)。
- 封装：把一组数据和处理数据的方法组成**对象**，把行为相同的对象归纳为**类(class)**，隐藏内部细节。
- 继承：构建复杂关系，实现类的特化和泛化，达到代码可重用和可扩展特性。
- 多态：实现基于对象类型的动态分发。由继承而产生的多种子类，其对象对同一行为会做出不同的响应。

### 封装

类是一个抽象的概念，对象是其具体的实例。比如说“犬”可以看成一个类，它会包含犬的一切基础特征，比如品种、毛皮颜色(数据)以及可以吠叫(方法)的能力。而具体的每一条狗则是一个对象，它们的特征值有所差异。我们把这些基础特征封装在“犬”类的内部，并逐一设置访问权限(例如：public,private,protected)，对外隐藏细节。

> 隐藏细节的好处就在于：外部调用者无需知道狗是怎么叫的？他只需要调用犬类对象的吠叫方法，就可以让狗叫。

### 继承

继承是在类与类之间构建父子关系，子类继承父类，在设计上，这意味着子类也是一种父类，只是相比于父类，它可能更加具体。比如，“犬”类可以是“动物”类的子类，每个“动物”类都可以有一些基础特征，比如重量、尺寸等成员数据(属性)，以及吃饭、睡觉等成员方法(行为)。“犬”类也是一种动物，但“动物”类相比“犬”类更加抽象，而向下，“犬”类也可以有更具体的子类，比如“中华田园犬”类，“牧羊犬”类等等。

子类会继承父类的属性和行为，与此同时，它还可以有自己独特的属性和方法。比如“犬”类相比于“动物”类，它有自己的毛皮颜色属性。

我们通过伪代码观察父类和子类的使用：

```
// ------------------------------------------------
类 犬
开始
	公有成员:
		吠(): {...}
结束

类 中华田园犬 : 继承犬
开始
结束

类 牧羊犬 : 继承犬
开始
　　公有成员:
　　　　放牧(): {...}
结束

// ------------------------------------------------
定义 大黄 是 中华田园犬
大黄.吠()      /* 注意这里调用的是犬类的吠方法。*/
大黄.放牧()    /* 错误：中华田园犬没有放牧方法。*/

定义 小白 是 牧羊犬
小白.吠()      /* 注意这里调用的是犬类的吠方法。*/
小白.放牧()    /* 这里调用的是牧羊犬类的放牧方法。*/
```

显然，父类的好处在于让多个子类可以共享一些公共的方法，而无需为每一种具体犬类都实现一遍吠方法，减少了重复代码的编写。

> 一些编程语言还支持多重继承，即类可以同时继承多个父类，多重继承历来复杂，褒贬不一，面相初学者，就不长篇大论了。

> 事实上类与继承的这种设计，近些年饱受诟病，尤其是针对Java这种纯OOP语言。一些学者认为继承与多态的设计并没有降低系统复杂度，表面看编写的代码变少了，但本质上只是压缩而非抽象。这一论点也得到了一部分社区的认可，新生代的许多语言诸如Go, Rust已经放弃了类继承这种古典OOP的设计手法，而是换用“数据与行为分离”，即“组合”的方式。详见:[格物致知(2)——语言千百，殊途同归/#设计哲学](https://r00tk1ts.github.io/2023/06/13/%E6%A0%BC%E7%89%A9%E8%87%B4%E7%9F%A5(2)%E2%80%94%E2%80%94%E8%AF%AD%E8%A8%80%E5%8D%83%E7%99%BE%EF%BC%8C%E6%AE%8A%E9%80%94%E5%90%8C%E5%BD%92/#%E8%AE%BE%E8%AE%A1%E5%93%B2%E5%AD%A6)。

### 多态

多态这个概念实际上比较大，但是大部分采用类继承实现的OOP语言，一般提到的多态都是指动态多态，即：运行时的动态绑定能力。

> 比如C++中有静态多态和动态多态，前者一般通过CRTP等手法来实现编译期绑定，后者则是类继承虚函数的手法来实现运行时绑定。

子类继承父类的方法后，还可以对方法进行重写(override)，不同的子类可以对父类的同一个方法给出不同的实现版本，这样的方法在程序运行时就会表现出多态行为（调用相同的方法，做了不同的事情）。

一般来讲，我们通过父类类型的引用或者指针，指向一个子类类型，当访问某个被重写的方法时，会在运行时调用子类的对应方法，而非父类（如果有重写的话）。通过这种方式，我们能够做到基于对象类型的动态分发，提高了编写抽象代码的灵活性。

多态是面向对象编程中最精髓的部分，也是对初学者来说最难以理解和灵活运用的部分。

> override和overwrite这两个术语中文一般都翻译成重写，但在特定的编程语言中，两者的语义是不一样的，比如在C++中，override是指以具有相同签名的函数覆盖父类中的虚函数，而overwrite则是用签名不一致的同名函数覆盖父类中的虚函数，或是签名相同的函数覆盖父类中的非虚函数。这两个词经常被混淆。

# Class in Python

Python中的类和许多编程语言一样，都使用`class`作为关键字。Python支持多重继承、派生类的override（以实现多态），类可以封装任意数量和类型的数据、以及成员方法。

Python当中所有的成员(数据和方法)都是公开的(即Java,C++中的共有`public`)，所有成员函数都可以被override(即C++中的虚函数)。

> Python class的设计类似于C++和Modula-3中类的结合体。

## 类的定义

最简单的类定义语法如下：

```python
class ClassName:
    <statement-1>
    .
    .
    .
    <statement-N>
```

类似函数定义语法，必须先定义才能够使用。当进入类定义时，将创建一个局部作用域，所有对局部变量的赋值都是在这个作用域之内。

举个例子，我们定义一个`MyClass`类：

```python
class MyClass:
	"""A simple example class"""
	# class variable shared by all instances
	i = 12345
	
	def f(self):
		return 'hello world'
```

`MyClass.i`和`MyClass.f`是对类属性的引用，它们会返回一个整数和一个函数对象。

```python
>>> MyClass.i
12345
>>> MyClass.f
<function MyClass.f at 0x100a6aa20>
```

类属性是被所有类的实例所共享的。

### 类的实例化

对已创建好的类来说，实例化对象使用函数表示法，可以把类名看作是一个不带参数的函数，返回一个对象实例：

```python
# 构造一个MyClass类对象x
x = MyClass()

# 调用类函数对象，打印'hello world'，self参数需要传入一个MyClass对象
print(MyClass.f(x))
# 调用方法对象，打印'hello world'，相当于隐式传入了一个x作为self
print(x.f())

# 对象实例也可以访问到类属性，打印12345
print(x.i)

# 但对x.i的重新赋值会让x对象内的属性i重新绑定到一个新对象上，并不会影响MyClass.i
# 此时的x.i是x对象的成员数据属性，而非类属性
x.i = 54321
print(x.i) # 54321
print(MyClass.i) # 12345
```

这里对成员方法的访问，是通过`.`操作符：对象`.`属性。

许多类都希望，在创建对象实例时，可以做一些初始化操作，Python允许为类定义一个`__init_()`特殊方法，如是：

```python
class MyClass:
	def __init__(self):
		# instance variable unique to each instance
		self.data = []

# 此时会调用__init__()，此时x拥有一个独占的data成员数据属性，值为空list
x = MyClass()
```

`__init__`还可以支持任意多个参数，只需要按需设计即可，比如：

```python
class Complex:
...     def __init__(self, realpart, imagpart):
...         self.r = realpart
...         self.i = imagpart
...
>>> x = Complex(3.0, -4.5)
>>> x.r, x.i
(3.0, -4.5)
```

### 数据属性和方法

正如上例所见，得益于动态类型的设计，在Python的对象中，数据属性无需声明，它们就像局部变量那样，会在第一次赋值时自动产生。利用这一机制，我们可以方便的在任意场合，按需对class对象增加数据属性。

```python
x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
# 可以通过del关键字来删除对象的某个属性
del x.counter
```

> 像是C++中的数据成员，都得严格在class中提前定义好，才能够被对象引用，否则就是编译错误：undefined member 

与数据属性相对应的，还有一种引用称为“方法”。方法是从属于对象的函数，它的名称查找依赖于所属的类。根据定义，一个类中所有是函数对象的属性都是定义了其实例的相应方法（即，`x.f`是有效的方法引用，是因为`MyClass.f`是一个函数）。

```python
# 但a.f和Myclass.f还是有区别的，前者是方法对象，后者是函数对象
>>> a = MyClass()
>>> type(a.f)
<class 'method'>
>>> type(MyClass.f)
<class 'function'>
```

如果对象的属性名称和所属类的某个属性重名了，那么对于“对象`.`属性”会优先查找到对象实例的那一个。

除了用此前学习过的`dir`内置函数来查看对象实例所包含的属性外，Python还支持三个内置函数来操纵对象的属性：

- `hasattr(obj, 'x')`: `obj`是否有属性`x`，返回一个布尔值
- `setattr(obj, 'x', 1)`: 为`obj`设置`x`属性，值为1
- `getattr(obj, 'x')`: 获取`obj`的`x`属性，如果不存在会抛`AttributeError`

### 私有属性

Python中的private属性是以双下划线开头，但不能以双下划线结尾的属性，比如`__spam, __test_，它们不能被外部代码访问。

> 实际上Python没有真正意义上的private属性，它只是通过一种叫做名称改写的方式来模拟。

 > 形如`__init__`这种以双下划线开头，且以双下划线结尾的属性，是特殊属性，它们可以被直接访问。初学者常常把他们和private属性搞混。

此外，对于单下划线开头的属性，在惯用法上也认为它们是内部的，不希望被外部所引用的属性（尽管外部实际上可以引用）。

## 继承和多态

Python中的派生类定义语法如下：

```python
class DerivedClassName(BaseClassName):
    <statement-1>
    .
    .
    .
    <statement-N>
```

名称`BaseClassName`必须对`DerivedClassName`可见（术语描述：定义于可从包含所派生的类的定义的作用域访问的命名空间中）。

> 当然也可以通过`modname.BaseClassName`来继承其他模块的基类。

派生类定义的执行过程与基类相同。当解析属性引用时，如果请求的属性在类中找不到，将继续在基类中查找。 如果基类本身也派生自其他某个类，则此规则将被递归地应用。

> 对于没有指定基类的class，默认都从`object`类继承。`object`类是Python中的顶级类，所有的类都是它的子类。

派生类可以overwrite基类的方法，不同的子类可以对父类的同一个方法给出不同的实现版本，这样的方法在程序运行时就会表现出多态行为（调用相同的方法，做了不同的事情）。

以这样一个简单的例子来进行描述：

```python
class Animal:
    def __init__(self, name):
        # 设置动物名称，作为实例属性
        self.name = name

    def eat(self):
        print('{} is eating...', self.name)

    def sleep(self):
        print('{} is sleeping...', self.name)

    def talk(self):
        # 不知道是什么动物，所以默认行为直接pass不实现
        pass

class Dog(Animal):
    def talk(self):
        print('{} is talking, wang wang wang...')

class Cat(Animal):
    def talk(self):
        print('{} is talking, miao miao miao...')

def animal_live(animal):
    animal.eat()
    # 根据animal实际的类型，调用overwrite的talk方法
    animal.talk()
    animal.sleep()

dog = Dog('大黄')
cat = Cat('小白')

animal_live(dog)
animal_live(cat)
```

### 类对象检查

两个内置函数可被用于继承机制的对象类型检查：

-  `isinstance(obj, int)` : 检查一个实例的类型，仅会在 `obj.__class__` 为 `int` 或某个派生自 `int`的类时为 `True`。
- `issubclass(classA, classB)` : 检查类的继承关系，如果classA是classB的子类，则返回`True`。比如`issubclass(bool, int)`为真，但`issubclass(float, int)`为假。

### 多重继承

Python支持多重继承，语法形如：

```python
class DerivedClassName(Base1, Base2, Base3):
    <statement-1>
    .
    .
    .
    <statement-N>
```

多重继承在实际应用中可能会面临一些问题，比如多个父类具有同名的属性，那么在访问属性时究竟使用的是谁的属性，这一点是“不确定的”（受Python的方法解析顺序影响，主要是为了解决菱形继承的基类多次访问问题）。因此，在设计类的继承关系时，就要慎重考虑。

对于支持多重继承的语言来说，一般会采用一种被称为Mixin的策略：通过继承多个父类进行组合，父类之间相互解耦，来避免过多层次的单继承。

> 比如Server可以是gRPC协议或HTTP协议，模型可以是多进程、多线程或是协程，那么就可以将两个维度解耦。从原本是多层结构的单继承$2*3$，变成简单的$2+3$组合。

# 附录

- [面向对象程序设计](https://zh.wikipedia.org/zh-cn/%E9%9D%A2%E5%90%91%E5%AF%B9%E8%B1%A1%E7%A8%8B%E5%BA%8F%E8%AE%BE%E8%AE%A1)
- [Python Tutorial-Class](https://docs.python.org/zh-cn/3/tutorial/classes.html)