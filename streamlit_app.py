import openai
import streamlit as st

# 用你自己的API密钥替换“your_api_key”
openai.api_key = "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"

# 创建一个文本生成请求
response = openai.Completion.create(
  engine="davinci-codex",
  prompt="Create a Python function to add two numbers:",
  temperature=0.5,
  max_tokens=50,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0,
)

# 从响应中获取生成的文本
generated_text = response.choices[0].text.strip()

# 打印生成的文本
st.write(generated_text)

