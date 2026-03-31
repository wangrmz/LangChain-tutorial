# import  langchain
# import  sys
# import openai
#
# print('版本：',langchain.__version__) # 0.3.25
# print(openai.__version__) # 1.81.0
# print(sys.version) # 3.10.20
#
#
#


from openai import OpenAI

# 1. API Key
API_KEY = "sk-sp-4063d985245149c3a1570ce2bed271fb"

# 2. Base URL (关键！必须是 coding 子域名，不是 dashscope 主域名)
# 错误: https://dashscope.aliyuncs.com/compatible-mode/v1
# 正确: https://coding.dashscope.aliyuncs.com/v1
BASE_URL = "https://coding.dashscope.aliyuncs.com/v1"

# 3. Model Name (关键！必须使用配置中存在的具体模型 ID)
# 错误: qwen-max, qwen-plus (这些是通用名，coding 接口可能不识别)
# 正确: qwen3.5-plus, qwen3-max-2026-01-23 (照搬 json 中的 id)
MODEL_NAME = "qwen3.5-plus"

print(f"🚀 正在连接阿里云 Coding Plan 专用接口...")
print(f"   URL: {BASE_URL}")
print(f"   Model: {MODEL_NAME}")

try:
    llm = OpenAI(
        base_url=BASE_URL,
        api_key=API_KEY
    )
    print("✅ 模型初始化成功！")

    # 快速连通性测试
    print("🔍 正在进行连通性测试...")
    completion = llm.chat.completions.create(
        model=MODEL_NAME,
        messages=[{
            'role':'system','content':'you are my time'
        },{
            'role': 'user', 'content': '你是谁？'
        }]
    )
    print(f"✅ 连通性测试通过: {completion.choices[0].message.content}...")

except Exception as e:
    print(f"❌ 初始化或测试失败: {e}")
    print("💡 检查点：1. URL 是否为 coding.dashscope... 2. Model ID 是否在 json 列表中")
    exit(1)
