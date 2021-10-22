# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 12:31:51 2021

@author: yeesa
"""

import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

#Question 1
st.title("My Homework Assignment 4")

#Question 2
st.write('Name: Sarah Yee')
st.markdown("[Linked here is my GitHub Repo!](https://github.com/syee12)")

#Question 3
uploaded_file = st.file_uploader(label = "Please upload a .csv file",
                                 type = "csv")

#Question 4
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
#Question 5
    df = df.applymap(lambda x: np.nan if x == " " else x)

#Question 6
    def can_be_numeric(c):
        try:
            pd.to_numeric(df[c])
            return True
        except:
            return False

    good_cols = [c for c in df.columns if can_be_numeric(c)]
    
#Question 7
    df[good_cols] = df[good_cols].apply(pd.to_numeric, axis = 0)
    
    
#Question 8
    x_axis = st.selectbox("Choose an x-value", good_cols)
    y_axis = st.selectbox("Choose a y-value", good_cols)
    
    
#Question 9
    plotted_values = st.slider("Choose the range of rows that you would like to plot",
                        0, len(df.index)-1, (0, len(df.index)-1))
    
#Question 10
    st.write(f"Plotting ({x_axis},{y_axis}) for rows {plotted_values}")
    
#Question 11
    chart = alt.Chart(df.loc[plotted_values[0]:plotted_values[1]]).mark_circle(
        ).encode(
            x = x_axis,
            y = y_axis,

#Question 12
).properties(
    width = 800,
    height = 400)
    st.altair_chart(chart)