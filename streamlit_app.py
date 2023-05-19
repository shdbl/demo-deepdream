import streamlit as st
import random
import time

# 统计抽奖次数和距离保底的次数
cjcs=0
xbd=30
with open('./redeem_code.txt','r') as file:
    for line in file.readlines():
        if line.strip().endswith('#'):
            cjcs+=1
            xbd-=1
        elif line.strip().endswith('%'):
            cjcs+=1
            xbd=30

# 定义函数，用于验证密码是否正确
def check_and_update_code(input_code):
    lines=[]
    found=False
    with open('./redeem_code.txt','r') as file:
        for line in file:
            line=line.strip()
            if line==input_code:
                found=True
                lines.append(f"{line}#")
            else:
                lines.append(line)
    if found:
        with open('./redeem_code.txt','w') as file:
            file.write("\n".join(lines))

    return found

# 定标记抽中保底
def sign_baodi(input_code):
    lines=[]
    with open('./redeem_code.txt','r') as file:
        for line in file:
            line=line.strip()
            if line==input_code+'#':
                lines.append(f"{line}%")
            else:
                lines.append(line)

        with open('./redeem_code.txt','w') as file:
            file.write("\n".join(lines))



# 定义奖项及其对应的权重
prizes = {
    "一等奖": 1,
    "二等奖": 3,
    "三等奖": 6
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
st.subheader(f'距离保底{xbd}')
pw = st.text_input("请输入兑换码")
# 如果密码输入框不为空
if pw:
    # 验证密码是否正确
    if check_and_update_code(pw):
        # 在页面上显示抽奖按钮
        result = lucky_draw()
        if result=='一等奖':
            sign_baodi(pw)
        # 在页面上显示抽奖结果
        st.balloons()
        time.sleep(1)
        st.success("抽中了{}！".format(result))

    else:
        # 在页面上显示密码错误提示
        st.write("兑换码错误，请重新输入！")
