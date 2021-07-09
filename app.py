import dash
import dash_core_components as dcc
from dash_core_components import Input
import dash_html_components as html
from dash_html_components import Output
import pandas as pd
import dash_bootstrap_components as dbc
import pandas as pd
from datetime import date
from datetime import datetime  
from datetime import timedelta
import pickle
from dash.dependencies import Input, Output, State

df= pd.DataFrame(columns = ['Day', 'Price30', 'CNY/USD30', 'EUR/USD30', 'EUR/CNY30', 'SSE30',
       'Ibex30', 'Crude_Oil30', 'ALGECIRAS', 'BARCELONA', 'BILBAO', 'VALENCIA',
       'VIGO', 'SHANGHAI', 'ANL', 'APL', 'CHINA SHIPPING', 'CMA-CGM', 'COSCO',
       'EVERGREEN', 'HAMBURG SUD', 'HANJIN', 'HAPAG LLOYD', 'HMM', 'K-LINE',
       'MAERSK', 'MOL', 'MSC', 'NIPPON', 'ONE', 'OOCL', 'UASC', 'YANG MING',
       '0', '1', '2', '3', '4', '5', '6', '1.1', '2.1', '3.1', '4.1', '5.1',
       '6.1', '7', '8', '9', '10', '11', '12'])

app = dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
    html.Div([
        html.Div(
            html.H1(children="Freight Rate Predictions", className="headline-1")
        ),
        html.Div(
            html.Img(src=app.get_asset_url('Logo-Noatum.png'), className="logo"), 
        )
    ],
        className="header"
    ),
    
    html.Div(
        [
            html.Div([
                html.H2("Input Options", className="headline-2"),
                html.Div([
                    dbc.Label("Carrier", className="label"),
                    dcc.Dropdown(id="dropdown_carrier", placeholder="Select Carrier",
                            options=[{"label": "ANL", "value": "ANL"},
                            {"label": "APL", "value": "APL"},
                            {"label": "China Shipping", "value": "China Shipping"},
                            {"label": "CMA-CGM", "value": "CMA-CGM"},
                            {"label": "COSCO", "value": "COSCO"},
                            {"label": "EVERGREEN", "value": "EVERGREEN"},
                            {"label": "HAMBURG SUD", "value": "HAMBURG SUD"},
                            {"label": "HANJIN", "value": "HANJIN"},
                            {"label": "HAPAG LLOYD", "value": "HAPAG LLOYD"},
                            {"label": "HMM", "value": "HMM"},
                            {"label": "K-LINE", "value": "K-LINE"},
                            {"label": "MAERSK", "value": "MAERSK"},
                            {"label": "MOL", "value": "MOL"},
                            {"label": "MSC", "value": "MSC"},
                            {"label": "NIPPON", "value": "NIPPON"},
                            {"label": "ONE", "value": "ONE"},
                            {"label": "OOCL", "value": "OOCL"},
                            {"label": "UASC", "value": "UASC"},
                            {"label": "YANG MING", "value": "YANG MING"},]
                    ),
                ]),

                html.Div([
                    dbc.Label("Origin", className="label"),
                    dcc.Dropdown(id="dropdown_origin", placeholder="Select Origin",
                            options=[{"label": "Shanghai", "value": "Shanghai"}],
                    ),
                ]),
                
                html.Div([
                    dbc.Label("Destination", className="label"),
                    dcc.Dropdown(id="dropdown_destination", placeholder="Select Destination",
                            options=[{"label": "Algeciras", "value": "Algeciras"}, 
                            {"label": "Barcelona", "value": "Barcelona"},
                            {"label": "Bilbao", "value": "Bilbao"},
                            {"label": "Valencia", "value": "Valencia"},
                            {"label": "Vigo", "value": "Vigo"}],
                    ),
                ]),

                dbc.Label("Freight Rate Today", className="label"),
                dbc.InputGroup([
                dbc.InputGroupAddon("$", addon_type="prepend"),
                dbc.Input(id='freight_rate', placeholder="Amount", type="number"),
                ]
                ),

                html.Div([
                    dbc.Label("Crude Oil Price Today", className="label"),
                    dbc.InputGroup([
                        dbc.InputGroupAddon("$", addon_type="prepend"),
                        dbc.Input(id='oil_price', placeholder="Amount", type="number"),
                    ]),
                    html.A("Get oil price", href='https://finance.yahoo.com/quote/CL%3DF%3FP%3DCL%3DF/history?p=CL%3DF%3FP%3DCL%3DF', target="_blank"),
                ]),

                html.Div([
                    dbc.Label("IBEX35 Today", className="label"),
                    dbc.InputGroup([
                        dbc.InputGroupAddon("$", addon_type="prepend"),
                        dbc.Input(id='ibex',placeholder="Amount", type="number"),
                    ]
                    ),
                    html.A("Get IBEX35", href="https://finance.yahoo.com/quote/%5EIBEX/history/"),
                ]),

                html.Div([
                    dbc.Label("SSE Composite Index Today", className="label"),
                    dbc.InputGroup([
                        dbc.InputGroupAddon("$", addon_type="prepend"),
                        dbc.Input(id='SSE', placeholder="Amount", type="number"),
                    ]
                    ),
                    html.A("Get SSE", href="https://finance.yahoo.com/quote/000001.ss/history/", target="_blank"),
                ]),

                html.Div([
                    dbc.Label("CNY/USD", className="label"),
                    dbc.InputGroup([
                        dbc.InputGroupAddon("$", addon_type="prepend"),
                        dbc.Input(id='CNYUSD', placeholder="Amount", type="number"),
                    ]
                    ),
                    html.A("Find exchange rate", href="https://finance.yahoo.com/quote/USDCNY=X/", target="_blank"),
                ]),

                html.Div([
                    dbc.Label("EUR/USD", className="label"),
                    dbc.InputGroup([
                        dbc.InputGroupAddon("$", addon_type="prepend"),
                        dbc.Input(id='EURUSD', placeholder="Amount", type="number"),
                    ]
                    ),
                    html.A("Find exchange rate", href="https://finance.yahoo.com/quote/EURUSD=X/", target="_blank"),
                ]),

                html.Div([
                    dbc.Label("EUR/CNY", className="label"),
                    dbc.InputGroup([
                        dbc.InputGroupAddon("$", addon_type="prepend"),
                        dbc.Input(id='EURCNY', placeholder="Amount", type="number"),
                    ]
                    ),
                    html.A("Find exchange rate", href="https://finance.yahoo.com/quote/EURCNY=X%3Fp=EURCNY/", target="_blank"),
                ]),


            ], className="filters card-filters"),
            
            html.Div([
                html.H2("Scenario Selection", className = "headline-2"),
                html.Div([
                    dbc.Label("Geopolitical", className="label"),
                    dbc.InputGroup([
                        dbc.InputGroupAddon("$", addon_type="prepend"),
                        dbc.Input(id='geopolitical', placeholder="Amount", type="number"),
                    ]
                    ),
                ]
                ),

                html.Div([
                    dbc.Label("Sudden Surcharge", className="label"),
                    dbc.InputGroup([
                        dbc.InputGroupAddon("$", addon_type="prepend"),
                        dbc.Input(id='surcharge', placeholder="Amount", type="number"),
                    ]
                    ),
                ]
                ),

                html.Div([
                    dbc.Label("Port Congestion", className="label"),
                    dbc.InputGroup([
                        dbc.InputGroupAddon("$", addon_type="prepend"),
                        dbc.Input(id='congestion', placeholder="Amount", type="number"),
                    ]
                    ),
                ]
                ),
        
            ], className="scenarios card-scenarios"),

            html.Div([
                html.Div([
                    html.H2("Predictions", className = "headline-2"),
                    html.Button(id='my-button', children='Predict', className='button'),
                ], className='prediction-header'),
                
                html.Div([
                    html.Label("30 Day Forecast (in USD)"),
                    html.Div(id='prediction-content-30', className="prediction box"),
                ], className= "prediction"),

                html.Div([
                    html.Label("90 Day Forecast (in USD)"),
                    html.Div(id='prediction-content-90', className="prediction box"),
                ], className= "prediction"),

            ], className="predictions card-predictions"),
        ], className= "container"
    ),
], 
)

@app.callback([
    Output('prediction-content-30', 'children'),
    Output('prediction-content-90', 'children')],
    [Input('my-button', 'n_clicks')],
    [State('dropdown_carrier', 'value'),
    State('dropdown_origin', 'value'),
    State('dropdown_destination', 'value'),
    State('freight_rate', 'value'),
    State('oil_price', 'value'),
    State('ibex', 'value'),
    State('SSE', 'value'),
    State('CNYUSD', 'value'),
    State('EURUSD', 'value'),
    State('EURCNY', 'value'),
    State('geopolitical', 'value'),
    State('surcharge', 'value'),
    State('congestion', 'value')],
    prevent_initial_call=True
)
    
def update_output(n_clicks, dropdown_carrier, dropdown_origin, dropdown_destination, freight_rate, oil_price, ibex, SSE, CNYUSD, EURUSD, EURCNY, geopolitical, surcharge, congestion):
    if n_clicks is None:
        raise PreventUpdate

    else:
        date30= date.today() + timedelta(days=30)
        month30 = date30.month
        day30 = date30.day
        weekday30= str(date30.weekday())
        
        if month30 <7:
            month30 = month30 + 0.1 

    month30= str(month30)
    
    df_30= pd.DataFrame(columns = ['Day', 'Price30', 'CNY/USD30', 'EUR/USD30', 'EUR/CNY30', 'SSE30',
       'Ibex30', 'Crude_Oil30', 'ALGECIRAS', 'BARCELONA', 'BILBAO', 'VALENCIA',
       'VIGO', 'SHANGHAI', 'ANL', 'APL', 'CHINA SHIPPING', 'CMA-CGM', 'COSCO',
       'EVERGREEN', 'HAMBURG SUD', 'HANJIN', 'HAPAG LLOYD', 'HMM', 'K-LINE',
       'MAERSK', 'MOL', 'MSC', 'NIPPON', 'ONE', 'OOCL', 'UASC', 'YANG MING',
       '0', '1', '2', '3', '4', '5', '6', '1.1', '2.1', '3.1', '4.1', '5.1',
       '6.1', '7', '8', '9', '10', '11', '12'])
    
    df_30.loc[0] = 0
    
    df_30['Day'] = day30
    df_30['Price30'] = freight_rate
    df_30['CNY/USD30'] = CNYUSD
    df_30['EUR/USD30'] = EURUSD
    df_30['EUR/CNY30'] = EURCNY
    df_30['SSE30'] = SSE
    df_30['Ibex30'] = ibex
    df_30['Crude_Oil30'] = oil_price
    df_30[dropdown_destination] = 1
    df_30[dropdown_origin] = 1
    df_30[dropdown_carrier] = 1
    df_30[weekday30] = 1
    df_30[month30] = 1
    
    rf_30 = pickle.load(open('/Users/marieheller/OneDrive - Universitat Ramón Llull/01_Courses/02_Term 2/Noatum - Capstone/Final Models/model_30.sav', 'rb'))
    
    prediction_30 = rf_30.predict(df_30)
    pred_30 = round(prediction_30[0][0]/100) * 100
    pred_30 = pred_30 + geopolitical + surcharge + congestion

    #90days prediction
    date90= date.today() + timedelta(days=90)
    month90 = date90.month
    day90 = date90.day
    weekday90= str(date90.weekday())

    if month90 <7:
        month90 = month90 + 0.1 

    month90= str(month90)
    
    df_90 = pd.DataFrame(columns =['Day', 'Price90', 'CNY/USD90', 'EUR/USD90', 'EUR/CNY90', 'SSE90',
       'Ibex90', 'Crude_Oil90', 'ALGECIRAS', 'BARCELONA', 'BILBAO', 'VALENCIA',
       'VIGO', 'SHANGHAI', 'ANL', 'APL', 'CHINA SHIPPING', 'CMA-CGM', 'COSCO',
       'EVERGREEN', 'HAMBURG SUD', 'HANJIN', 'HAPAG LLOYD', 'HMM', 'K-LINE',
       'MAERSK', 'MSC', 'NIPPON', 'ONE', 'OOCL', 'UASC', 'YANG MING', '0', '1',
       '2', '3', '4', '5', '6', '1.1', '2.1', '3.1', '4.1', '5.1', '6.1', '7',
       '8', '9', '10', '11', '12'])


    df_90.loc[0] = 0
    
    df_90['Day'] = day90
    df_90['Price90'] = freight_rate
    df_90['CNY/USD90'] = CNYUSD
    df_90['EUR/USD90'] = EURUSD
    df_90['EUR/CNY90'] = EURCNY
    df_90['SSE90'] = SSE
    df_90['Ibex90'] = ibex
    df_90['Crude_Oil90'] = oil_price
    df_90[dropdown_destination] = 1
    df_90[dropdown_origin] = 1
    df_90[dropdown_carrier] = 1
    df_90[weekday90] = 1
    df_90[month90] = 1

    
    rf_90 = pickle.load(open('/Users/marieheller/OneDrive - Universitat Ramón Llull/01_Courses/02_Term 2/Noatum - Capstone/Final Models/model_90_regr.sav', 'rb'))
    prediction_90 = rf_90.predict(df_90)
    pred_90 = round(prediction_90[0][0]/100) * 100
    pred_90 = pred_90 + geopolitical + surcharge + congestion + 1000

    return pred_30, pred_90



if __name__ == "__main__":
    app.run_server(debug=True)
