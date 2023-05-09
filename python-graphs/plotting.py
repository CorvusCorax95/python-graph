import random

import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats
import streamlit as st


def _density_plot(df, title, x1, x2):
	plt.style.use('dark_background')
	df.plot.density(linewidth=1, figsize=(20, 10))
	plt.title(title)


def make_data():
	n_list = []
	name_list = []
	for i in range(5):
		a = random.uniform(0, 5)
		b = random.uniform(0, 5)
		r = stats.beta.rvs(a, b, size=1000)
		n_list.append(r)
		name = "a: " + str(round(a, 2)) + " b: " + str(round(b, 2))
		name_list.append(name)

	df = pd.DataFrame(n_list, index=name_list).transpose()

	return df


def make_plots():
	show_data()


def show_data():
	col_left, col_mid, col_right = st.columns(3)
	with col_left:
		st.subheader("Original Data")
		df = make_data()
		st.write(df)
		st.pyplot(_density_plot(df, "Raw Random Data", -0.2, 1.2))
		st.pyplot(_boxplot(df))

	with col_mid:
		st.subheader("Mean Normalized Data")
		mean_norm_df = mean_norm(df)
		st.write(mean_norm_df)
		st.pyplot(_density_plot(mean_norm_df, "Mean-Normalized Data", -3, 3))
		st.pyplot(_boxplot(mean_norm_df))
	with col_right:
		st.subheader("MinMax Normalized Data")
		minmax_norm_df = minmax_norm(df)
		st.write(minmax_norm_df)
		st.pyplot(_density_plot(minmax_norm_df, "Mean-Normalized Data", -0.2,
		                        0.2))
		st.pyplot(_boxplot(minmax_norm_df))


def mean_norm(df):
	sample_list = df.columns.values.tolist()
	norm_df = (df[sample_list] - df[sample_list].mean()) / df[sample_list].std()
	return norm_df

def minmax_norm(df):
	sample_list = df.columns.values.tolist()
	mm_df = (df[sample_list] - df[sample_list].min()) / (
			df[sample_list].max() - df[sample_list].min())
	return mm_df

def _boxplot(df):
	plt.style.use('dark_background')
	df.boxplot(fontsize="large")
