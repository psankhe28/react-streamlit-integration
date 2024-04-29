import streamlit as st
import numpy as np
from scipy.stats import binom
import plotly.graph_objs as go

def plot_distribution(distribution, params):
    if distribution == 'Normal':
        x = np.linspace(-10, 10, 1000)
        mean, std = params['mean'], params['std']
        y = (1 / (std * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mean) / std) ** 2)
        fig = go.Figure(data=go.Scatter(x=x, y=y))
        fig.update_layout(title='Normal Distribution',
                          xaxis_title='Value',
                          yaxis_title='Probability Density')
        st.plotly_chart(fig)
    elif distribution == 'Binomial':
        n, p = params['n'], params['p']
        x = np.arange(0, n+1)
        y = binom.pmf(x, n, p)
        fig = go.Figure(data=go.Scatter(x=x, y=y, mode='markers+lines'))
        fig.update_layout(title='Binomial Distribution',
                          xaxis_title='Number of Successes',
                          yaxis_title='Probability')
        st.plotly_chart(fig)

def main():
    st.title('Interactive Distribution Visualization')
    distributions = ['Normal', 'Binomial']
    selected_distribution = st.selectbox('Select Distribution:', distributions)

    if selected_distribution == 'Normal':
        mean = st.slider('Mean:', -10.0, 10.0, 0.0)
        std = st.slider('Standard Deviation:', 0.1, 10.0, 1.0)
        params = {'mean': mean, 'std': std}
        plot_distribution(selected_distribution, params)
    elif selected_distribution == 'Binomial':
        n = st.slider('Number of Trials (n):', 1, 100, 10)
        p = st.slider('Probability of Success (p):', 0.0, 1.0, 0.5)
        params = {'n': n, 'p': p}
        plot_distribution(selected_distribution, params)

if __name__ == '__main__':
    main()