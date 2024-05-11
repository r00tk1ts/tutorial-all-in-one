# Python简介

[Python](https://en.wikipedia.org/wiki/Python_(programming_language))是一种解释型高级语言，它最早于80年代由荷兰人 吉多·范罗苏姆（Guido von Rossum）研发，坊间传闻龟叔（Guido谐音）在1989年的圣诞节，百无聊懒之际，动手发明了这一脚本解释型语言，而这一语言的得名，则是源于BBS电视剧《Monty Python的飞行马戏团》，龟叔是忠实的爱好者。

> Guido在2005年入职Google，2012年跳槽到Dropbox直至2019年退休。退休后不甘寂寞又在2020年加入了微软。

随着时代的发展，Python的特性与设计一直在革新，它的能力越来越全面，社区也越来越繁荣，时至2024，Python已经是世界上最流行的编程语言，没有之一。[TIOBE](https://www.tiobe.com/tiobe-index/)是一个统计世界上编程语言流行度的网站，从下图可以看到，Python在2023.4和2024.4都稳居榜首，遥遥领先。
![[Pasted image 20240428145505.png]]

# Python编年简史

经过数十年的发展，当前Python的最新稳定版本是3.12.3，期间大小升级无数，生态也愈发成熟。每次的迭代变更都陈列在[官方文档-What's New In Python](https://docs.python.org/3/whatsnew/index.html)中。

编年简史：
- 1989.12 - 1991.2：Python 0.9.0问世，龟叔发布了最初的代码。用C语言实现了Python解释器（即官方的CPython）。
	- 核心特性：类与继承、异常处理、函数；
	- 核心类型：`list`, `dict`, `str`;
- 1994.1：Python 1.0发布，这标志着Python作为一门编程语言正式开宗立派;
	- 新增函数式编程特性：`lambda`, `map`, `filter`, `reduce`;
	- 1.0->1.4发展过程中引入了若干好用的特性，例如缺省参数值、复数支持等；
- 2000.10：Python 2.0发布，相比于1.0它更加成熟，在后续版本迭代中逐步走向完全体，直至2020年在2.7版本刻下休止符。
	- 新增函数式编程特性：列表推导式、静态嵌套作用域与闭包；
	- 编码升级：支持Unicode；
	- 统一对象模型、引入迭代器、生成器；
- 2008.12：Python 3.0发布，它对语言做了大量修订导致与Python 2无法兼容，此后，市场慢慢过渡到3.0时代，Python 2随着时间洪流逐渐消亡。
	- 语法差异
	- 性能升级
	- 字符串和字节的差异化处理，更好的支持Unicode
	- 标准库的扩充与升级，如异步I/O模块、协程、日期和时间库等
	
> 软件的版本号一般分三段，形如：A.B.C，其中A表示大版本号，当软件整体重写升级或出现不向前兼容的改变时，才会增加A；B表示功能更新，出现新功能时增加B；C表示小小修小补，只要有修改就增加C。

![[Pasted image 20240506165102.png]]
# Python语言核心

## 审美与设计理念

每一种编程语言都有它自己独特的审美和设计理念，Python也不例外。这其中包括语言特性的支持，大到编程范式，小至语法糖，归根结底，是编程语言的设计理念与哲学。

Python的设计理念是：**优雅、简单、明确**。它被深深烙印在语言的DNA中，我们在Python解释器中输入`import this`即可看到：

```
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
优美胜于丑陋。
明了胜于晦涩。
简洁胜于复杂。
复杂胜于凌乱。
扁平胜于嵌套。
间隔胜于紧凑。

Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
可读性很重要。
特例亦不可违背原则，即使实用比纯粹更优。
错误绝不能悄悄忽略，除非它明确需要如此。
面对不确定性，拒绝妄加猜测。
任何问题应有一种，最好只有一种，显而易见的解决方法。
尽管这方法一开始并非如此直观，除非你是荷兰人。

Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
做优于不做，
然而不假思索还不如不做。
如果一个方案难以理解，那它一定不好。
如果一个方案很容易理解，那它可能是一个好方案。
命名空间是一种绝妙的理念，我们应当多加利用。
```

这些箴言被称作”**Python之禅**“。除了表达的核心理念之外，还着重强调：做一件事只应使用甚至是只应有一种方法。这和其他语言像是C++, Perl的表现大相径庭。

> 更多有关编程语言的审美与设计理念，可以参考我撰写的编程导论系列的文章：[格物致知(2)——语言千百，殊途同归](https://r00tk1ts.github.io/2023/06/13/%E6%A0%BC%E7%89%A9%E8%87%B4%E7%9F%A5(2)%E2%80%94%E2%80%94%E8%AF%AD%E8%A8%80%E5%8D%83%E7%99%BE%EF%BC%8C%E6%AE%8A%E9%80%94%E5%90%8C%E5%BD%92/)。

## 核心三件套

尽管Python强调简明，但并不意味着简陋。Python实际上支持多种编程范式，它完全支持结构化编程和面向对象编程，支持一定程度的函数式编程、元编程。

但无论支持何种范式，对于一门编程语言来说，都离不开核心的三件套：**语法和语义**、**标准库**和**生态环境**。

> 实际上对于编程语言来说，最为重要的东西其实在核心三件套之上，那就是语言的实现。Python的官方实现被称作CPython，得名于它的解释器是用C语言编写。官方不仅定义了标准，还提供了具体的CPython实现，这和C,C++这类语言不太一样。当然，除了官方以外，第三方厂商也可以自己去实现Python，比如知名的PyPy,Jython
![[Pasted image 20240508113021.png]]
这些第三方实现体一般都是为了适配不同的环境，或是针对标准实现的性能不满意（这就不得不提饱受诟病的GIL），才应运而生。然而相比于和Python标准穿一条裤子的CPython，在新标准特性的支持上第三方实现体难免要滞后一些。 

### 语法和语义

Python的语法就如它的设计理念一样：简明。这主要在以下三个方面得以体现：
1. 较短的关键字约定，如`def`,`with`,`pass`;
2. 遵循越位规则，使用缩进来形成语法块，替代其他语言中繁琐的花括号；
3. 使用动态类型系统（但是强类型）；

相比于Python，像是C++、Java等语言写起来就显得相当笨重繁琐，比如在Python中定义一个整型数组，我们可以写成：`v = [1,2,3]`(type of `list`)，而在C++中则要写`std::vector<int> v{1,2,3};`。

### 标准库

标准库对于语言来说，就好比是宗门的底蕴，底蕴丰厚的门派更容易受到门徒的追随。随着Python社区的日渐强盛，标准库所集成的能力也愈发全面。

[Python标准库](https://docs.python.org/3/library/index.html)主要包含了以下能力：

- 内置函数、常量、类型和异常；
- 文本和二进制数据处理库；
- 泛用的数据结构
- 数值计算与统计
- 文件访问与数据压缩归档、持久化能力
- 函数式编程组件
- 网络与通信

通过标准库所提供的丰富能力，我们在编写程序时将如鱼得水，省去了去到处找轮子、甚至重新造轮子的功夫。

### 生态环境

Python自2.0版本起，代码便托管到SourceForge（后迁移至GitHub）开源，让更多的人可以参与开发。开源模式吸引了大量开发者加入社区，用户也持续增长。在2001年，在Guido的号召下，非盈利组织PSF (Python Software Foundation)正式成立，负责维护Python语言的发展与推广，支持Python社区，保护知识产权，Guido担任该组织的理事。

由于开源社区的积极活跃，为了保证代码的质量，合入流程被规范化成PEP (Python Enhancement Proposals)。Python开发者可以发起PEP，来提出语言的改进或支持新功能，这份PEP在社区共同讨论，经过几轮的修改并最终达成共识后，才能够加入到官方文档（作为未来版本的一部分）。

> PEP有争议的部分，早期都是由Guido亲自下场裁定（这就是语言之父作为话事人的power），但出于各方面原因，Guido在2018年放弃了这个特权，社区成立了指导委员会（委员通过选举）来操刀。

> 最近闹得沸沸扬扬、Google裁撤Python团队的新闻中，大名鼎鼎的Thomas Wouters就是现任委员，Python 3.12和Python 3.13都是由他主持发布的。

语言的开放性，让Python在近20年的发展中欣欣向荣。而对于开发者来说，选择一门语言，除却对审美与设计的认同外，最为核心的要素在于语言的生态是否满足需求。

 > 实际上，Python发展至今，不能只归功于开源社区的运营模式，领域巨头公司的大力支持亦是中流砥柱。但是话又说回来，弱水三千能得巨头公司青睐，或许又得益于它的设计理念。
 
2022年10~12月，PSF和JetBrains合作开展了[第6次年度官方Python开发者调查](https://lp.jetbrains.com/python-developers-survey-2022/)，收集了来自近 200 个国家和地区的 23,000 多名 Python 开发者和爱好者的反馈，反映出该语言及其周围生态系统的状态。

![[Pasted image 20240506195304.png]]

从上图可以看到，Python在数据分析和Web开发上受众最广，紧随其后的是机器学习、系统运维和网络爬虫。2021和2022年的占比数据相差无几，而事实上对Python生态来说，这五个方向确实是最为火热。

这里的数据分析主要是指数值分析(或者叫科学计算？)，它是计算机最初的应用场景，也是编程语言所必备的基础能力，Python能够在这一领域拿下高达51%的占比，主要得益于强大的第三方库，诸如：`numpy`,`pandas`,`scipy`等等。

Web开发则历史悠久，随着互联网的发展，Python是最早一批投身于Web开发的编程语言，得益于起步较早，陆续诞生了一些好用的开发框架（~~如业界知名的两个Web开发框架Django和Flask就深受广大培训班的喜爱）~~。

随着硬件的发展，2011年后人工智能开始发力，从机器学习到深度学习，从专才小模型到通才大模型，AI发展如日中天。Python几乎垄断了这个领域的生态，不仅早早诞生了知名的机器学习库：`scikit-learn`奠定了在机器学习领域开发的饼图，其后更是迎来了两位重量级选手PyTorch和TensorFlow(分别由Facebook和Google研发)，随着AI的发展步入深度学习时代。

此外，可以观察到部分开发者也会选择用Python去做游戏、计算机图形学、移动端开发，显然，在这些领域Python属实不太擅长，生态较为匮乏，故而占比较低。

# Python环境配置
## Python安装

登录[官网](https://www.python.org/)，找到对应平台，一键下载安装：
![[Pasted image 20240507110442.png]]
官网包罗万象，有详尽的文档资料、社区组织、新闻资讯等，可自行食用。

## Python开发环境

### 交互式命令行
![[Pasted image 20240510152808.png]]
> 官方的交互式命令行体验较差，可以用更高级的诸如ipython来获得更好的体验。
### 编辑器

推荐VSCode
![[Pasted image 20240510153522.png]]

### IDE

推荐PyCharm
![[Pasted image 20240510153438.png]]
# 编程演示

在[[编程导论]]中曾提及，真实的编程是一个按图索骥、层层套娃的过程。就让我们站在新手的视角，一步一个脚印，[从零绘制出Python Version Timeline](code/draw.py)。
![[Pasted image 20240511151106.png]]
# 附录

- [Python 生态发展之路](https://zhuanlan.zhihu.com/p/398406235)
- [Python Developers Survey 2022 Results](https://lp.jetbrains.com/python-developers-survey-2022/)
- [Python Wikipedia](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Python Documentation](https://docs.python.org/3/library/index.html)