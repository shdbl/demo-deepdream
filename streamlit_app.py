import streamlit as st
from PIL import Image

def change_alpha(img, alpha_factor):
    # 打开图片


    # 确保图片为RGBA格式
    img = img.convert('RGBA')

    # 获取图片的尺寸和每个像素的颜色值
    width, height = img.size
    pixels = img.load()

    # 遍历图片的每个像素
    for x in range(width):
        for y in range(height):
            # 获取当前像素的颜色值
            r, g, b, a = pixels[x, y]

            # 保留原本透明的像素不变，修改其他像素的透明度
            if a != 0:
                new_alpha = int(a * alpha_factor)
                new_alpha = max(0, min(255, new_alpha))  # 保证透明度在0到255之间
                pixels[x, y] = (r, g, b, new_alpha)

    # 保存修改后的图片
    return img

st.title("修改图片透明度")

uploaded_file=st.file_uploader("选择一个 png 文件",type="png")

if uploaded_file is not None:
    img=Image.open(uploaded_file)
    st.image(img)
    alpha=st.slider('透明度',min_value=0.0,max_value=1.0,value=0.5,step=0.05)
    pic=change_alpha(img, alpha)
    st.image(pic)

