# 📊 Political Campaign Spend Analysis

This project is an interactive **Streamlit web application** that
analyzes the relationship between **political ad spending** and **voter
turnout** across different states, constituencies, and election phases.
The project uses data from election results, advertiser information, and
location mappings to uncover insights into how campaign spending impacts
electoral participation.

## 🚀 Features

-   **Total Ad Spend by State** -- Visualize how much was spent on ads
    across states.\
-   **Average Voter Turnout by State** -- Explore average voter turnout
    rates across states.\
-   **Top 5 Parties by Ad Spend** -- Pie chart highlighting the biggest
    spenders.\
-   **Ad Spend vs Voter Turnout by Constituency** -- Scatter plot
    showing correlations.\
-   **Distribution of Ad Spend** -- Histogram with boxplot overlay for
    ad spending distribution.\
-   **Ad Spend vs Voter Turnout by Election Phase** -- Combined bar &
    line chart analyzing trends across election phases.

## 📂 Project Structure

    ├── app.py                # Streamlit app with all visualizations  
    ├── Notebook.ipynb        # Exploratory data analysis & preprocessing steps  
    ├── results.csv           # Election results dataset  
    ├── advertisers.csv       # Advertiser and spending dataset  
    ├── locations.csv         # Location/constituency mapping dataset  
    └── README.md             # Project documentation  

## 🛠️ Tech Stack

-   **Python**\
-   **Streamlit** -- For building the interactive dashboard\
-   **Plotly (Express & Graph Objects)** -- For interactive
    visualizations\
-   **Pandas** -- Data cleaning and analysis

## 📊 Datasets

1.  **Results Dataset (`results.csv`)** -- Election results, states,
    turnout percentages.\
2.  **Advertisers Dataset (`advertisers.csv`)** -- Spending details by
    political parties.\
3.  **Locations Dataset (`locations.csv`)** -- Mapping of states and
    constituencies.

## ▶️ How to Run

1.  Clone the repository:

    ``` bash
    git clone <repo-url>
    cd <repo-folder>
    ```

2.  Install dependencies:

    ``` bash
    pip install -r requirements.txt
    ```

3.  Run the Streamlit app:

    ``` bash
    streamlit run app.py
    ```

4.  Open in your browser at: **http://localhost:8501**

## 📈 Insights

-   Higher spending doesn't always translate into higher turnout.\
-   Some states show clear correlations between ad spend and voter
    participation.\
-   Spending patterns vary significantly across election phases.

## 🔮 Future Improvements

-   Add filters for year/region/party.\
-   Incorporate demographic data for deeper insights.\
-   Enhance dashboard with trend forecasting models.
