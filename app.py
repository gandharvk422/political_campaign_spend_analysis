import streamlit as st
import plotly.express as px
import pandas as pd
import plotly.io as pio
import plotly.graph_objects as go

results = pd.read_csv("results.csv")
advertisers = pd.read_csv("advertisers.csv")
locations = pd.read_csv("locations.csv")

st.set_page_config(page_title="Political Campaign Spend Analysis", layout="wide", page_icon="📊")

results['State'] = results['State'].str.strip().str.lower()
locations['Location name'] = locations['Location name'].str.strip().str.lower()

merged_data = results.merge(
    locations,
    left_on='State',
    right_on='Location name',
    how='left'
)

pio.templates.default = "plotly_white"

def total_ad_spend_by_state():
    state_ad_spend = merged_data.groupby('State')['Amount spent (INR)'].sum().reset_index()

    fig = px.bar(state_ad_spend, x = 'State', y = 'Amount spent (INR)', labels = {'State': 'State', 'Amount spent (INR)': 'Ad Spend (INR)'}, title='Total Ad Spend by State')
    fig.update_layout(xaxis = {'categoryorder': 'total descending'}, xaxis_tickangle = -90, width = 800, height = 600)

    return st.plotly_chart(fig, use_container_width=True)

def average_voter_turnout_by_state():
    state_voter_turnout = merged_data.groupby('State')['Polled (%)'].mean().reset_index()

    fig = px.bar(state_voter_turnout, x = 'State', y = 'Polled (%)', labels = {'State': 'State', 'Polled (%)': 'Vote Turnout (%)'}, title = 'Average Voter Turnout by State')

    fig.update_layout(xaxis = {'categoryorder': 'total descending'}, xaxis_tickangle = -90, width = 800, height = 600)
    return st.plotly_chart(fig, use_container_width=True)

def top_5_parties_by_ad_spend():
    advertisers['Amount spent (INR)'] = pd.to_numeric(advertisers['Amount spent (INR)'], errors = 'coerce')
    advertisers.dropna(subset = ['Amount spent (INR)'], inplace = True)
    party_ad_spend = advertisers.groupby('Page name')['Amount spent (INR)'].sum().sort_values(ascending=False)
    top_5_parties = party_ad_spend.head(5).reset_index()

    colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

    fig = px.pie(top_5_parties, values = 'Amount spent (INR)', names = 'Page name', title = 'Top 5 Parties by Ad Spend', color_discrete_sequence = colors, labels = {'Page name': 'Political Party', 'Amount spent (INR)': 'Ad Spend (INR)'})

    fig.update_traces(textinfo = 'percent')

    fig.update_layout(showlegend = True, legend = dict(orientation = 'v', yanchor = 'top', y = 1, xanchor = 'left', x = -0.3), title = dict(y = 0.95, x = 0.5, xanchor = 'center', yanchor = 'top'), margin = dict(l = 200, r = 50, t = 100, b = 50))

    return st.plotly_chart(fig, use_container_width=True)

# calculate the correlation between ad spend and voter turnout
correlation = merged_data[['Amount spent (INR)', 'Polled (%)']].corr()

def ad_spend_and_voter_turnout_by_parliamentary_constituency():
    merged_constituency_data = results.merge(locations, left_on='State', right_on='Location name', how = 'left')

    fig = px.scatter(merged_constituency_data, x = 'Amount spent (INR)', y = 'Polled (%)', color = 'State', labels={'Amount spent (INR)': 'Ad Spend (INR)', 'Polled (%)': 'Voter Turnout (%)'}, title = 'Ad Spend and Voter Turnout by Parliamentary Constituency')
    fig.update_layout(width = 800, height = 600)
    return st.plotly_chart(fig, use_container_width=True)

def distribution_of_ad_spend():
    fig = px.histogram(merged_data, x = 'Amount spent (INR)', nbins = 30, marginal = 'box', labels = {'Amount spent (INR)': 'Ad Spend (INR)'}, title = 'Distribution of Ad Spend')
    fig.update_traces(marker = dict(line = dict(color = 'black', width = 1)))
    fig.update_layout(bargap = 0.1, width = 800, height = 600)

    return st.plotly_chart(fig, use_container_width=True)

def ad_spend_and_voter_turnout_by_election_phase():
    phase_analysis = merged_data.groupby('Phase').agg({
        'Amount spent (INR)': 'sum',
        'Polled (%)': 'mean'
    }).reset_index()

    fig = go.Figure()

    fig.add_trace(go.Bar(
        x = phase_analysis['Phase'],
        y = phase_analysis['Amount spent (INR)'],
        name = 'Ad Spend (INR)',
        marker_color = 'indianred',
        yaxis = 'y1'
    ))

    fig.add_trace(go.Scatter(
        x = phase_analysis['Phase'],
        y = phase_analysis['Polled (%)'],
        name = 'Voter Turnout (%)',
        marker_color = 'lightsalmon',
        yaxis = 'y2'
    ))

    fig.update_layout(
        title = 'Ad Spend and Voter Turnout by Election Phase',
        xaxis = dict(title = 'Election Phase'),
        yaxis = dict(
            title = 'Ad Spend (INR)',
            titlefont = dict(color = 'indianred'),
            tickfont = dict(color = 'indianred')
        ),
        yaxis2 = dict(
            title = 'Voter Turnout (%)',
            titlefont = dict(color = 'lightsalmon'),
            tickfont = dict(color = 'lightsalmon'),
            overlaying = 'y',
            side = 'right'
        ),
        legend = dict(x = 0.1, y = 1.1, orientation = 'h'),
        width = 800, height = 600
    )

    return st.plotly_chart(fig, use_container_width=True)

pages = [
    st.Page(total_ad_spend_by_state, title="Total Ad Spend by State"),
    st.Page(average_voter_turnout_by_state, title="Average Voter Turnout by State"),
    st.Page(top_5_parties_by_ad_spend, title="Top 5 Parties by Ad Spend"),
    st.Page(ad_spend_and_voter_turnout_by_parliamentary_constituency, title="Ad Spend and Voter Turnout by Parliamentary Constituency"),
    st.Page(distribution_of_ad_spend, title="Distribution of Ad Spend"),
    st.Page(ad_spend_and_voter_turnout_by_election_phase, title="Ad Spend and Voter Turnout by Election Phase")
    ]

pg = st.navigation(pages, position="sidebar")
pg.run()