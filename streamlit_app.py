import requests
import streamlit as st
from bs4 import BeautifulSoup

url = "https://www.google.com/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36",
}


try:
    response=requests.get(url,headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    # 在此处添加您要提取的信息
    # 例如，提取所有段落或其他元素
    # paragraphs = soup.find_all("p")
    st.write(soup.text)
except:
    st.write('访问失败')
