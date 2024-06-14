# Learn-AI-test-class

> 随便记录一些和AI测试相关的内容


## 集成了AI能力的测试平台

### applitools

* [applitools eyes 基于视觉检查的自动化测试](./platform/applitools_eyes.md)

### testim

* [Testim 由 AI 加持的自动化测试能力](./platform/Testim_IO.md)

### mabl

* [mabl AI 自动化测试测试平台体验](./platform/mabl.md)

### ReTest

* ReTest： https://retest.de/ **需要邮件联系体验**

### aggplant

* 官网: https://www.keysight.com/us/en/products/software/software-testing.html

* Eggplant 视频教程

https://www.bilibili.com/video/BV1QL4y1n75k/

https://www.bilibili.com/video/BV12L41177yn


### Test.AI

文档：https://docs.test.ai/

### appvance

官网：https://appvance.ai/


## 基于大模型的自动化解决方案

* [AppAgent基于通义千问VL操作App实践](./tools/AppAgent_used.md)

* 使用 GPT4V+AI Agent 做自动 UI 测试的探索 | 京东云技术团队

https://segmentfault.com/a/1190000044503658

https://github.com/microsoft/SoM

https://github.com/microsoft/autogen

https://github.com/ddupont808/GPT-4V-Act/


## appium插件

* [我花了两周时间，为了体验appium AI定位元素](./tools/appium_ai_plugin.md)

## 其他资料：

[未来已来，人工智能测试势不可挡：介绍9款AI测试工具](https://www.sohu.com/a/226070300_453160)


[AI在测试中的应用](https://blog.csdn.net/albee2/article/details/100161691)


[AI大模型在测试中的深度应用与实践案例](https://blog.csdn.net/rjdeng/article/details/139246321)


[人工智能教程](https://www.cbedai.net/)


## 总结

这些天搜集了一下自动化在AI领域的进展。

1. AI加持的自动化测试平台：
   - applitools eyes、Testim、mabl 等，通过录制回放提供自动化测试用例的编写。但是，不是简单的元素定位，页面元素变了照样能回放，AI 加持下稳定性提升。
   - 收费，背后原理不得而知。

2.  一个基于LLM的多模态代理。
   - 原理：先将web/app页面截图，添加标记。将 prompt 和 图片交给 大模型识图（例如 `GTP-4V`，`通义千问-VL`等），由大模型识别并操作。
   - 从目前对 AppAgent 的体验结果，**很不靠谱**，需要对特定App训练，prompt 如何精准的描述测试需求也有要求。

3.  基于LLM 协助生成自动化脚本。
   - 这种方式可以提升编写自动化脚本的效率，通过描述需求，例如： `pytest + playwright 生成一个登录的自动化测试， 要求...`。
   - 其实LLM 生成的代码，核心的部分还是需要我们完成，比如 `登录的账号`，`登录的元素定位`，生成的代码只是模板代码，如果我们足够熟悉自动化脚本的编写，这个提升就不明显了。
