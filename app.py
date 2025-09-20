import streamlit as st
import pandas as pd
import numpy as np
from streamlit import columns

#title text
st.title("hello stream lit")
##simple text

st.write("this is a simple write")
df=pd.DataFrame({'a':[1,2,3], 'b':[4,5,6]})
st.write("this is data frame ")
st.write(df)
linechart_data=pd.DataFrame(
    np.random.randn(20, 3),columns=['a','b','c']
)
st.line_chart(linechart_data)