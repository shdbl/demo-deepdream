import streamlit as st
import random
import time
from PIL import Image

path="./redeem_code.txt"

# 统计抽奖次数和距离保底的次数
cjcs=0
xbd=10
dbd=50
with open(path,'r') as file:
    for line in file.readlines():
        if line.strip().endswith('#'):
            cjcs+=1
            xbd-=1
            dbd-=1
        elif line.strip().endswith('%'):
            cjcs+=1
            xbd=10
        elif line.strip().endswith('@'):
            cjcs+=1
            dbd=50


# 定义函数，用于验证密码是否正确
def check_and_update_code(input_code):
    lines=[]
    found=False
    with open(path,'r') as file:
        for line in file:
            line=line.strip()
            if line==input_code:
                found=True
                lines.append(f"{line}#")
            else:
                lines.append(line)
    if found:
        with open(path,'w') as file:
            file.write("\n".join(lines))

    return found

# 定标记抽中保底
def sign_xiaobaodi(input_code):
    lines=[]
    with open(path,'r') as file:
        for line in file:
            line=line.strip()
            if line==input_code+'#':
                lines.append(f"{line}%")
            else:
                lines.append(line)

        with open(path,'w') as file:
            file.write("\n".join(lines))

def sign_dabaodi(input_code):
    lines=[]
    with open(path,'r') as file:
        for line in file:
            line=line.strip()
            if line==input_code+'#':
                lines.append(f"{line}@")
            else:
                lines.append(line)

        with open(path,'w') as file:
            file.write("\n".join(lines))


# 定义奖项及其对应的权重
if xbd>0 and dbd>0:
    prizes = {
        "终极礼物": 1,
        "周末吃饭": 6,
        "小礼品": 13,
        "切好的水果": 40,
        "小零食": 140
    }
elif dbd<=0:
    prizes={
        "终极礼物":200,
        "周末吃饭":0,
        "小礼品":0,
        "切好的水果":0,
        "小零食":0
    }
elif xbd<=0:
    prizes={
        "终极礼物":0,
        "周末吃饭":200,
        "小礼品":0,
        "切好的水果":0,
        "小零食":0
    }

# 定义函数，用于抽奖
def lucky_draw():
    # 获取所有奖项的权重总和
    total_weight = sum(prizes.values())
    # 随机生成一个0-总和之间的整数
    rand_num = random.randint(0, total_weight)
    # 初始化当前权重为0
    current_weight = 0
    # 遍历奖项及其对应的权重
    for prize, weight in prizes.items():
        # 将当前权重加上当前奖项的权重
        current_weight += weight
        # 如果当前权重大于等于随机生成的数字，则抽中当前奖项
        if current_weight >= rand_num:
            return prize

# 在页面上显示密码输入框
st.header('已抽次数：{}'.format(cjcs))
st.subheader(f'距离小保底{xbd}，距离大保底{dbd}')
pw = st.text_input("请输入兑换码")
# 如果密码输入框不为空
if pw:
    # 验证密码是否正确
    if check_and_update_code(pw):
        # 在页面上显示抽奖按钮
        result = lucky_draw()
        if result=='周末吃饭':
            sign_xiaobaodi(pw)
        elif result=='终极礼物':
            sign_dabaodi(pw)
        # 在页面上显示抽奖结果
        st.balloons()
        time.sleep(1)
        st.success("抽中了{}！".format(result))
        st.write("")
        image=Image.open('./{}.png'.format(result))
        st.image(image,caption='Your caption here',use_column_width=True)

    else:
        # 在页面上显示密码错误提示
        st.write("兑换码错误，请重新输入！")

