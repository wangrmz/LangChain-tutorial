from langchain_openai import ChatOpenAI
import os


print(os.environ['OPENAI_API_KEY'])
print(os.environ['OPENAI_BASE_URL'])


# 调用非对话模型

# 调用对话模型
# 必须设置的3个参数
# (default="gpt-3.5-turbo", alias="model") 默认使用gpt-3.5-turbo模型
chat_model = ChatOpenAI(model="gpt-4o-mini",
                        base_url=os.environ['OPENAI_BASE_URL'],
                        api_key=os.environ['OPENAI_API_KEY']
)


# 调用模型
response = chat_model.invoke('什么是langchain')

# 查看相应的文本
print(response.content)

'''
Langchain 是一种用于构建基于语言模型的应用程序的框架，旨在简化与大型语言模型（如 OpenAI 的 GPT 系列）的集成和交互。它提供了一系列工具和组件，使开发者能够创建更复杂和强大的应用程序，充分利用语言模型的能力。

Langchain 的主要功能包括：

1. **链式调用**：通过将多个处理步骤串联在一起，创建复杂的工作流。例如，可以先进行数据处理，然后调用语言模型进行生成，最后再进行结果的后处理。

2. **数据连接**：支持与各种数据源（如 API、数据库、文件等）的集成，使得语言模型可以访问和使用这些外部数据。

3. **检索增强生成**：结合检索系统和语言模型，使得模型在生成内容时可以基于外部知识，提高生成内容的准确性和相关性。

4. **工具和机器人**：提供集成各种工具的能力，扩展应用的功能，比如调用外部 API、执行计算等。
'''
