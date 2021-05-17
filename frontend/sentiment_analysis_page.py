import streamlit as st

from constants.config import TWITTER_DATASET, YAHOO_DATASET, VADER
from scripts.pipelines.training_pipeline_unsupervised import model_training

from core.utils.plots_sentiment_analysis import plot_piechart, plot_most_frequent, \
    plot_length_distributionsV2, plot_informative_table

container_1 = st.beta_container()
container_2 = st.beta_container()

def app():

    model_name = VADER
    seed = 2021

    data_params_twitter = {'data_path': 'resources/twitter_dataset/TSLA.csv',
                   'dataset_type': TWITTER_DATASET,
                   'preprocessed': False,
                   'vectorization': None,
                   'vector_params': None,
                   'imbalance': None,
                   'imb_params': None,
                   'test_size': 0.99,
                   'shuffle': False,
                   'train': False}

    data_params_yahoo = {'data_path': 'resources/yahoo_dataset/AAPL-News-cleaned.csv',
                   'dataset_type': YAHOO_DATASET,
                   'preprocessed': False,
                   'vectorization': None,
                   'vector_params': None,
                   'imbalance': None,
                   'imb_params': None,
                   'test_size': 0.99,
                   'shuffle': False,
                   'train': False}

    model_params = {}

    _, labels_twitter, data_twitter = model_training(model_name, data_params_twitter, model_params, seed)
    _, labels_yahoo, data_yahoo = model_training(model_name, data_params_yahoo, model_params, seed)

    # ticker
    st.title('TESLA - TSLA')

    # informative table
    st.dataframe(plot_informative_table(data_twitter,data_yahoo))

    # pie charts
    st.markdown("<h3> SENTIMENT ANALYSIS </h3>",unsafe_allow_html=True)
    st.plotly_chart(plot_piechart(labels_twitter, labels_yahoo))

    # top k elements
    # st.markdown("<h3> MOST FREQUENT WORDS </h3>", unsafe_allow_html=True)
    # slider_ph = st.empty()
    # [min, max, default, step]
    # value = slider_ph.slider("Select the number of words to show", 5, 15, 10, 1)
    # st.plotly_chart(plot_most_frequent(data, data, value))

    # length distribution
    st.markdown("<h3> LENGTH DISTRIBUTION </h3>", unsafe_allow_html=True)
    st.plotly_chart(plot_length_distributionsV2(data_twitter, labels_twitter, data_yahoo, labels_yahoo))

