import openai
import streamlit as st

# 用你自己的API密钥替换“your_api_key”
openai.api_key = "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"

# 创建一个文本生成请求
response = openai.Completion.create(
  engine="text-davinci-002",  # 选择你想要使用的引擎
  prompt="什么是人工智能?",  # 输入文本提示
  max_tokens=100,  # 生成文本的最大长度
  n=1,  # 生成文本的数量
  stop=None,  # 设置停止生成文本的标记
  temperature=0.7,  # 控制生成文本的创造性（较高的值会导致更具创意的生成，较低的值会导致更保守的生成）
)

# 从响应中获取生成的文本
generated_text = response.choices[0].text.strip()

# 打印生成的文本
st.write(generated_text)

