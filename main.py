import streamlit as st
import time


st.title('Streamlit 超入門')

st.write('プレグレスバー')
'Start!!'
# バーの表示　（イメージ：ローディング画面）
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f"Iteration {i +1}")
    bar.progress(i + 1) #バーの進捗が増えていく
    time.sleep(0.1) # 0.1毎にforが繰り返される
    
'done!!!!!'

# # sleepで指定した秒数毎に繰り返し処理が行われる
# for i in range(100):
#     print(i)
#     time.sleep(0.1)

# 初回時は下ターミナルに
# streamlit run main.py と入力



# st.title('Streamlit 超入門')
# st.write('Interactive Widgets')


# # エキスパンダー　問い合わせ　Q&Aとかによく使うやつ
# expander = st.expander('問い合わせ')
# expander.write('問い合わせ内容を書く')

# # 2カラムレイアウト
# left_column, right_column = st.columns(2)
# button = left_column.button('右カラムに文字を表示')
# if button:
#     right_column.write('ここは右カラム')

# サイドバー
#st.write('Interactive Widgets')
#text1 = st.sidebar.text_input('あなたの趣味を教えて下さい。')
#condition1 = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)
#'あなたの趣味：', text1
#'コンディション：', condition1

# テキスト入力による、値の動的変化
# st.write('Interactive Widgets')
# text = st.text_input('あなたの趣味を教えて下さい。')
# 'あなたの趣味：', text

# スライダーの実装
# condition = st.slider('あなたの今の調子は？', 0 ,100, 50)
# 'コンディション：', condition

# プルダウンの数字リストを作成し、ユーザーに指定させることができる
# また指定した数字を反映させることができる
# option = st.selectbox(
#     'あなたが好きな数字を教えて下さい。',
#     list(range(1,11))
# )
# 'あなたの好きな数字は', option,'です'
# # チェックボックスを用いて画像の表示
# if st.checkbox('Show Image'):
#     img = Image.open('2023-01-14_11h13_29.png')
#     st.image(img, caption='SIMS 3', use_column_width=True)



# # 画像の表示
# st.write('Display Image')
# img = Image.open('2023-01-14_11h13_29.png')
# st.image(img, caption='SIMS 3', use_column_width=True)


# st.write('DateFream')

# df03 = pd.DataFrame(
#     np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
#     columns = ['lat', 'lon']    
# )
# st.map(df03)


# df02 = pd.DataFrame(
#     np.random.rand(20, 3),
#     columns=['a', 'b', 'C']
# )
# # 折れ線グラフで表示する
# st.line_chart(df02)

# # 棒グラフ
# st.bar_chart(df02)



# df = pd.DataFrame({
#     '1列目': [1, 2, 3, 4],
#     '2列目': [10, 20, 30, 40]
# })
# st.write(df.style.highlight_max(axis=0), width=300, height=300)
# # writeでも出力できるが、dataframeだとフレームの大きさpxでの変更が可能
# # .style.highlight_max(axis=0) はハイライト指定　axis=0 or 1 
# st.dataframe(df.style.highlight_max(axis=0), width=300, height=300)

# # 静的な表示をさせる場合
# st.table(df.style.highlight_max(axis=0))

"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""