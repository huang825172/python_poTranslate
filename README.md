# .po File translator

*为啥要用英文呢*

这是一个基于 Python 实现的 .po 文件自动翻译工具

翻译操作分为三个阶段：
   + 读取 .po 文件
   + 过滤文件中需要翻译的字段，**去除转义等特殊字符**
   + 调用 **百度翻译API** 进行翻译
   + 将结果写入新的 .po 文件
   
目前的代码分为三个 python package
   + libbdtranslate 对百度翻译API的restful调用，尚未实现
   + libpo 对 .po 文件的读取和过滤，其中的 filter 需要重新设计
   + potranslator 调用前两个包进行翻译工作
   
当前的开发方向主要有三个：
   + 实现对百度翻译API的restful调用（技术难度最低，可以考虑延后实现）修改 libbdtranslate 包
   + 实现翻译工作的异步进行，多线程以及线程同步（技术难度中等）修改 potranslator 包、
   + 提高 filter 准确性（技术难度较高，去读一下 po 文件就会发现，标准格式的还好，截断的标记简直是垃圾桶）修改 filter.process 实现

共同开发

共同进步