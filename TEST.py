import streamlit as st
import random
import pandas as pd
def generate_question():
    while True:
        num1 = random.randint(0, 20)
        num2 = random.randint(0, 20)
        operator = random.choice(['+', '-'])
        question = f"{num1} {operator} {num2}"
        if 0< eval(question)<20:
            break
    return question
def highlight_row(row):
    if (row[ '答案'] !=None) :
        if (row[ '答案'] == row['你的回答']) :
            return ['background-color: lightgreen'] * len(row)
        else:
            return ['background-color: lightcoral'] * len(row)
    else:
        return ['background-color: white'] * len(row)

def main():
    st.title("20以内加减法出题器")
    # 初始化 session_state
    # st.sidebar()

    question_num=100
    coly,colz= st.columns(2)

    with colz:
        if st.button("确定",use_container_width=True):
            # 在这里你可以处理用户按下回车的逻辑，例如执行计算或其他操作
            st.session_state.flag = True
            st.session_state.i += 1
    if 'flag' not in st.session_state:
        st.session_state.flag = False
    if 'questions' not in st.session_state:
        st.session_state.questions = []
        for i in range(question_num):
            st.session_state.questions.append([generate_question()])
    print(st.session_state.questions)
    if 'i' not in st.session_state:
        st.session_state.i=0
    print("第一次",st.session_state.i)
    # 显示当前题目
    colq,cola=st.columns(2)

    try:
        with colq:
            st.header("题目:"+"       "+st.session_state.questions[st.session_state.i][0])


        st.text(str(st.session_state.i + 1) + '/' + str(question_num))
    except:
        with coly:

            st.success("完成答题！")
            st.success("刷新网页重新开始！")

    # 获取用户输入
    # user_answer = st.number_input("请输入你的答案:", value=None)
    if 'input' not in st.session_state:
        st.session_state.input = ''
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


    if st.button("0",use_container_width=True):
        st.session_state.input += "0"
    with cola:
        input_text = st.text_input("", value=st.session_state.input)


    # 检查用户答案
    try:
        print("第二次",st.session_state.i)
        if st.session_state.input=='':
            user_answer = 0
        else:
            user_answer = int(st.session_state.input)
            print(user_answer)
        if st.session_state.i==0:
            with coly:

               st.success("开始答题吧！")
        elif st.session_state.flag==True:
            print(st.session_state.flag)
            try:
                right_answer = int(eval(st.session_state.questions[st.session_state.i - 1][0]))
                print(right_answer)
            except:
                with coly:

                   st.success("刷新网页重新开始！")
            if eval(st.session_state.questions[st.session_state.i-1][0]) == user_answer:
                with coly:

                    st.success("回答正确！")
            else:
                with coly:

                    st.error(f"回答错误。正确答案是: {right_answer}")
            st.session_state.questions[st.session_state.i - 1].append(str(right_answer))
            print('a')
            st.session_state.questions[st.session_state.i - 1].append(str(user_answer))
            print('b')

            print('c')
            st.session_state.input=''
            st.session_state.flag = False
        df = pd.DataFrame(st.session_state.questions, columns=['题目', '答案', '你的回答'])

        styled_df = df.style.apply(highlight_row, axis=1)

        st.dataframe(styled_df,use_container_width=True)

    except ValueError:
        with coly:
            print("")

           # st.warning("请输入一个有效的整数作为答案。")

    print(st.session_state.questions)
    user_answer=None
    # st.table(st.session_state.questions)




if __name__ == "__main__":
    main()
