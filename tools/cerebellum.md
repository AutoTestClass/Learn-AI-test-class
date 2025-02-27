## 基于 selenium 和 claude3 的AI自动化工具

cerebellum是一个轻量级浏览器代理，通过键盘和鼠标操作在网页上实现用户定义的目标。

### cerebellum 的特点

* 兼容所有支持 Selenium 的浏览器。
* 使用用户提供的 JSON 数据填写表单。
* 接受运行时指令以动态调整浏览策略和操作。

### Cerebellum 是如何工作的

1. 网页浏览被简化为导航一个有向图。
2. 每个网页是一个包含可见元素和数据的节点。
3. 用户的操作，例如点击或输入，是在节点之间移动的边。
4. Cerebellum 从一个网页开始，目标是到达一个体现完成目标的目标节点。
5. 它使用大型语言模型（LLM）通过分析页面内容和交互元素来找到新的节点。
6. LLM 根据当前状态和过去的操作决定下一个动作。
7. Cerebellum 执行 LLM 计划的动作，并将新的状态反馈给 LLM 以进行下一步。
8. 该过程在 LLM 决定目标已达到或无法实现时结束。

### cerebellum 安装使用

目前 cerebellum 支持 TypeScript 和 Python 两个版本。好吧！我知道大家应该只关心Python版本。

* 首先，通过 pip 安装

```
pip install cerebellum
```

* 然后，设置你的 Anthropic API key, 即 claude3 的API key。

```
export ANTHROPIC_API_KEY='your-api-key'
```

> 这一步是设置系统环境变量，cerebellum 代码中会读取电脑的这个环境变量。

* 最后，编写 cerebellum 脚本

```py
from seleniumbase import get_driver
from cerebellum import AnthropicPlanner, BrowserAgent, BrowserAgentOptions, pause_for_input

def main():
   driver = get_driver()

   try:
      # Set your starting page
      driver.get("https://www.google.com")

      # Define your goal
      goal = "Show me the wikipedia page of the creator of Bitcoin"

      # Create the Cerebellum browser agent
      planner = AnthropicPlanner()

      options = BrowserAgentOptions(pause_after_each_action=True)

      agent = BrowserAgent(driver, planner, goal, options)
      agent.pause_after_each_action = False

      pause_for_input()
      # Have Cerebellum takeover website navigation
      agent.start()

      # Goal has now been reached, you may interact with the Selenium driver any way you want
      pause_for_input()

   finally:
      driver.quit()


if __name__ == "__main__":
   main()
```


### cerebellum 分析

很遗憾~!，我花费了半天时间没弄到 `Anthropic API key`, 官方支付需要绑定信用卡，我国内的信用卡用不了。国内的一些代理的API，无法直接使用，因为 cerebellum 比较深度的依赖 anthropic-sdk-python。

我看了一下源码，可以替换 openai API 或 国内的一些模型的 API，估计要花费写时间重写。

https://github.com/anthropics/anthropic-sdk-python

抛去 anthropic 部分的依赖，cerebellum 并没有太多的自己的东西了，主要依赖如下：

```shell
seleniumbase = "^4.32.9"
anthropic = "^0.39.0"
pillow = "^11.0.0"
```

__seleniumbase__

通过示例可以看到使用`seleniumbase` 获取浏览器驱动和打开浏览器页面。seleniumbase 又依赖于selenium 和 pytest，自动化操作的核心还是我们传统的技术。


__pillow__

pillow 是Python的图像处理库，我的理解应该是将页面截图并进行处理。


__anthropic__

anthropic 识别用于识别自动化意图。

```py
goal = "Show me the wikipedia page of the creator of Bitcoin"
```

首先，通过 “creator of Bitcoin” 获取到比特币的创造者是：“Satoshi Nakamoto”， 再从提取“wikipedia” 关键信息，最后组成搜索关键字：“Satoshi Nakamoto wikipedia” 。

接下来，页面截图分析，识别google搜索框，并输入关键字并搜索，最后，在结果中获得维基百科的链接，并打开连接。

![](../image/cerebellum-running.png)

### 总结

我们之前曾介绍过 AppAgent 工具，cerebellum 的思路类似，核心基于LLM模型本身的能力。

再次，表示遗憾，没弄到 `Anthropic API key` 导致上面的例子我没真正的跑一下，这偏文章写的不那么踏实了。

感兴趣评论区留言，我打算花点时间把 cerebellum 替换为其他可用的模型，claude3 虽然优势明显，倒也不至于非他不可。
