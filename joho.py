import streamlit as st


st.title('初めてのStreamlit')
st.write('これから作品を作っていきます')

text = st.text_input("あなたの名前を教えて")
st.write("あなたの名前は"+text+"です")

conditon = st.slider("あなたの今の調子は？",0,100,50)
st.write("コンディション",conditon)

option = st.selectbox(
    "好きな数字を教えてください",
    list(["1番","2番","3番","4番",])
)
st.write("あなたが選択したのは"+option+"です")


import time
st.sidebar.write("プログレスバーの表示")

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'読み込み中{i+1}%')
    bar.progress(i+1)
    time.sleep(0.001)

left_column,right_column = st.columns(2)

button = left_column.button("右カラムに文字を表示")
if button:
    right_column.write("ここは右カラムです")

from PIL import Image
img = Image.open("room.jpg")

st.image(img,caption="生活場面",use_column_width=True)


import pandas as pd
import numpy as np

df = pd.DataFrame(
    np.random.rand(100,2)/[50,50] + [36.64,138.19],
    columns = ['lat','lon']#lat lon 緯度と経度
)
#緯度と経度から地図に書き込む
st.map(df)
st.table(df)