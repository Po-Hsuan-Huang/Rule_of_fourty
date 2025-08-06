import dash
from dash import html, dcc, Input, Output, State
import plotly.graph_objs as go

# Initial data
initial_data = [
    ("Visa (V)",            66.77,   11.38,   570.0),
    ("TSMC (TSM)",          49.63,   38.60,   710.0),
    ("Broadcom (AVGO)",     31.76,   16.40,   660.0),
    ("Palantir (PLTR)",     26.83,   48.00,    65.0),
    ("Quad (QUAD)",          3.95,   -9.80,     0.22),
    ("Supermicro (SMCI)",    5.30,   47.00,    78.0),
    ("Axon (AXON)",          0.70,   33.00,    24.0),
    ("MercadoLibre (MELI)", 12.20,   34.00,    92.0),
    ("Credo (CRDO)",        20.39,  126.34,    18.93),
    ("Rocket Lab (RKLB)",  -43.11,   32.00,    21.45),
    ("Spotify (SPOT)",       9.68,   21.00,   133.0),
    ("Microsoft (MSFT)",    44.90,   18.00,  3966.0),
    ("Tencent (TCEHY)",     31.87,   12.90,   645.57),
    ("Joby Aviation (JOBY)", -5532.8, -9470.0, 14.86),
    ("Cloudflare (NET)",    -9.27,   27.80,    72.42),
    ("NVidia (NVDA)", 69.2 , 49.11,4340),     #4.3T


]

slope = -41 / 39  # ≈ -1.051
avg_intercept = sum(y - slope * x for _, x, y, z in initial_data) / len(initial_data)

# Create Dash app
app = dash.Dash(__name__)
server = app.server  # For deployment if needed

app.layout = html.Div([
    html.H1("Stock Quality Rule of 40"),
    html.Div([
        html.Label("Company Ticker Label:"),
        dcc.Input(id='input-label', type='text', placeholder='e.g. NVDA'),
        html.Button('Add Company', id='submit-button', n_clicks=0),
        html.Label("Adjusted Operating Margin (%):"),
        dcc.Input(id='input-margin', type='number', step=0.01),
        html.Label("YoY Revenue Growth (%):"),
        dcc.Input(id='input-growth', type='number', step=0.01),
        html.Label("Market Cap (Billion):"),
        dcc.Input(id='input-market-cap', type='number', step=0.01)

    ], style={'margin': '20px'}),
    dcc.Store(id='company-data', data=initial_data),
    dcc.Graph(id='scatter-plot')

])

@app.callback(
    Output('company-data', 'data'),
    Input('submit-button', 'n_clicks'),
    State('input-label', 'value'),
    State('input-margin', 'value'),
    State('input-growth', 'value'),
    State('input-market-cap', 'value'),
    State('company-data', 'data'),
)
def update_data(n_clicks, label, margin, growth, cap, data):
    if n_clicks > 0 and label and margin is not None and growth is not None:
        data.append((label, margin, growth, cap))
    return data

@app.callback(
    Output('scatter-plot', 'figure'),
    Input('company-data', 'data')
)

def update_plot(data):
    labels, margins, growths, caps = zip(*data)
    intercept = 40 #sum(y - slope * x for x, y in zip(margins, growths)) / len(margins)

    # Regression line
    x_line = list(range(0, int(max(margins)) + 5))
    y_line = [slope * x + intercept for x in x_line]

    scatter = go.Scatter(
        x=margins,
        y=growths,
        mode='markers+text',
        text=labels,
        textposition='top center',
        marker=dict(
            size=caps,
            sizemode='area',
            sizeref=2.*max(caps)/(80.**2),  # adjust for visual scaling
            sizemin=5,
            color='cyan'
        ), # Changed marker color for dark mode visibility
        name='Companies'
    )

    line = go.Scatter(
        x=x_line,
        y=y_line,
        mode='lines',
        name='Rule of 40 Frontier',
        line=dict(color='red', dash='dash')
    )

    layout = go.Layout(
        xaxis=dict(
            title='Adjusted Operating Margin (%)',
            range = [0,75],
            dtick=10,
            gridcolor='#444444', # Darker grid lines
            zerolinecolor='#666666',
            tickfont=dict(color='#f0f0f0'), # Light tick labels
            title_font=dict(color='#f0f0f0') # Light title font
        ),
        yaxis=dict(
            title='YoY Revenue Growth (%)',
            range=[0, 145],
            dtick=10,
            gridcolor='#444444', # Darker grid lines
            zerolinecolor='#666666',
            tickfont=dict(color='#f0f0f0'), # Light tick labels
            title_font=dict(color='#f0f0f0'), # Light title font
        ),
        showlegend=True,
        width=1200,
        height=800,

        plot_bgcolor='#333333', # Dark background for the plot area
        paper_bgcolor='#222222', # Dark background for the entire figure
        font=dict(color='#f0f0f0') # Default font color for the graph
    )




    return go.Figure(data=[scatter, line], layout=layout)





if __name__ == '__main__':
    app.run(debug=True)
