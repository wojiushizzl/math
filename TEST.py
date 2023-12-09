import streamlit as st
import random
import pandas as pd
import re

def transform(question):
    # 定义正则表达式模式
    pattern1 = re.compile(r'\d+')
    pattern2 = re.compile(r'(\d+)\s*([+\-*/])\s*(\d+)')

    # 进行匹配
    matches = len(pattern1.findall(question))
    if matches==3:
        question=question+'= ()'
    else:  
        # 进行匹配
        match = pattern2.match(question)
        num1 = int(match.group(1))
        operator1 = match.group(2)
        num2 = int(match.group(3))
        if operator1 == '+':
            question= random.choice([f'(  )-{num1} = {num2}',question+'= ()'])
        if operator1 == '-':
            question=random.choice([f'(  )+{num2} = {num1}',question+'= ()'])
    return question
def question_type1():   # 加减计算填写数字
    while True:
        numq=random.randint(2,3)
        num1 = random.randint(0, 20)
        num2 = random.randint(0, 20)
        num3 = random.randint(0, 20)

        operator1 = random.choice(['+', '-'])
        operator2 = random.choice(['+', '-'])

        if numq ==2:
            question = f"{num1} {operator1} {num2}"
        else:
            question = f"{num1} {operator1} {num2} {operator2} {num3}"
        if 0< eval(question)<20:   #限制难度
            break
    return [transform(question),eval(question)]
def question_type2():   # 填加减符号
    while True:
        num1 = random.randint(0, 20)
        num2 = random.randint(0, 20)

        operator = random.choice(['+', '-'])

        q = f"{num1} {operator} {num2}"
        a=eval(q)
        question = str(num1)+" ◯ "+str(num2) +" = "+ str(a)
        answer=operator
        if 0< a<20:   #限制难度
            break

    return [question,answer]
def question_type3():   # 填大于小于等于 符号
    while True:
        num1 = random.randint(0, 20)
        num2 = random.randint(0, 20)
        num3 = random.randint(0, 20)

        operator = random.choice(['+', '-'])

        q = f"{num1} {operator} {num2}"
        a=eval(q)
        question = q+ " ◯ "+ str(num3)
        if a > num3:
            answer=">"
        elif a == num3:
            answer="="
        else:
            answer = "<"
        if 0< a<20:   #限制难度
            break

    return [question,answer]
def generate_question():
    rand_type=random.randint(1,3)
    # print(rand_type)
    if rand_type==1:
        return question_type1()
    elif rand_type ==2:
        return question_type2()
    elif rand_type ==3:
        return question_type3()
    


def highlight_row(row):
    if (row[ '你的回答'] !='None') :
        if (row[ '答案'] == row['你的回答']) :
            return ['background-color: lightgreen'] * len(row)
        else:
            return ['background-color: lightcoral'] * len(row)
    else:
        return ['background-color: white'] * len(row)

def main():
    st.title("Yodo 学数学")
    # 初始化 session_state
    # 在侧边栏设置内容
    # sidebar_option = st.sidebar.selectbox("Select an option", ["Option 1", "Option 2", "Option 3"])
    default=100
    question_num= st.sidebar.number_input("设置题目数量 ： ", min_value=10, max_value=200, value=default, step=10)

    if 'flag' not in st.session_state:
        st.session_state.flag = False
    if ('questions' not in st.session_state) :
        st.session_state.questions = []
        for i in range(question_num):
            st.session_state.questions.append(generate_question())
    st.session_state.questions=st.session_state.questions[:question_num]
    print(st.session_state.questions)
    if 'score' not in st.session_state:
        st.session_state.score=0
    if 'i' not in st.session_state:
        st.session_state.i=0
    print("1st",st.session_state.i)
    colq,cola=st.columns(2)

    try:
        with colq:
            st.header("题目:"+"       "+st.session_state.questions[st.session_state.i][0])


        st.text(str(st.session_state.i + 1) + '/' + str(question_num))
    except:
        st.success("完成答题！ 得分："+str(st.session_state.score))
        st.success("刷新网页重新开始！")

    if 'input' not in st.session_state:
        st.session_state.input = ''
    # 创建符号按钮
    coldayu,colxiaoyu,coldengyu,coljia,coljian=st.columns(5)
    with coldayu:
        if st.button("大于    >",use_container_width=True):
            st.session_state.input += ">"
    with colxiaoyu:
        if st.button("小于    <",use_container_width=True):
            st.session_state.input += "<"
    with coldengyu:
        if st.button("等于    =",use_container_width=True):
            st.session_state.input += "="
    with coljia:
        if st.button("加    +",use_container_width=True):
            st.session_state.input += "+"  
    with coljian:
        if st.button("减    -",use_container_width=True):
            st.session_state.input += "-" 
    # 创建数字按钮
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("1",use_container_width=True):
            st.session_state.input += "1"

    with col2:
        if st.button("2",use_container_width=True):
            st.session_state.input += "2"

    with col3:
        if st.button("3",use_container_width=True):
            st.session_state.input += "3"

    col4, col5, col6 = st.columns(3)
    with col4:
        if st.button("4",use_container_width=True):
            st.session_state.input += "4"
    with col5:
        if st.button("5",use_container_width=True):
            st.session_state.input += "5"
    with col6:
        if st.button("6",use_container_width=True):
            st.session_state.input += "6"

    col7, col8, col9 = st.columns(3)
    with col7:
        if st.button("7",use_container_width=True):
            st.session_state.input += "7"
    with col8:
        if st.button("8",use_container_width=True):
            st.session_state.input += "8"
    with col9:
        if st.button("9",use_container_width=True):
            st.session_state.input += "9"
    col000,colz,colf=st.columns(3)
    def f() :
        if st.session_state.i < question_num:
            st.session_state.flag = True
            st.session_state.i += 1
        else:
            st.success("完成答题！")
            st.success("刷新网页重新开始！")
    with colf:
        if st.button("😀确定",use_container_width=True,on_click=f):
            print("")
    with colz:
        if st.button("◀取消",use_container_width=True):
            st.session_state.input=''
    with col000:
        if st.button("0",use_container_width=True):
            st.session_state.input += "0"
    with cola:
        # input_text = st.text_input("", value=st.session_state.input)
        st.header(st.session_state.input)
    # 检查用户答案
    try:
        print("2nd",st.session_state.i)
        if st.session_state.input=='':
            user_answer = 0
        else:
            user_answer = st.session_state.input
        if st.session_state.i==0:
           st.success("开始答题吧！")
        elif st.session_state.flag==True:
            right_answer = str(st.session_state.questions[st.session_state.i - 1][1])
            # if int(st.session_state.questions[st.session_state.i - 1][1]) == user_answer:
            #     st.success("回答正确！真棒！(●'◡'●)")
            # else:
            #     st.error(f"回答错误。(；′⌒`)    正确答案是: {right_answer}")
            st.session_state.questions[st.session_state.i - 1].append(str(user_answer))
            st.session_state.input=''
            st.session_state.flag = False
        df = pd.DataFrame(st.session_state.questions, columns=['题目', '答案', '你的回答'])
        df['答案'] = df['答案'].astype(str)
        df['你的回答'] = df['你的回答'].astype(str)
        df['正确与否']=df['答案']==df['你的回答']
        st.session_state.score=str(df['正确与否'].sum())+"/"+str(question_num)
        styled_df = df.style.apply(highlight_row, axis=1)
        if st.session_state.i ==question_num:
            st.dataframe(styled_df,use_container_width=True)

    except ValueError:
        print("")
           # st.warning("请输入一个有效的整数作为答案。")
           
    user_answer=None




if __name__ == "__main__":
    main()
