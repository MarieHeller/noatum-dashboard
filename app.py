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
                dbc.InputGroupAddon(".00", addon_type="append"),
                ]
                ),

                html.Div([
                    dbc.Label("Crude Oil Price Today", className="label"),
                    dbc.InputGroup([
                        dbc.InputGroupAddon("$", addon_type="prepend"),
                        dbc.Input(id='oil_price', placeholder="Amount", type="number"),
                        dbc.InputGroupAddon(".00", addon_type="append"),
                    ]),
                    html.A("Get oil price", href='https://finance.yahoo.com/quote/CL%3DF%3FP%3DCL%3DF/history?p=CL%3DF%3FP%3DCL%3DF', target="_blank"),
                ]),

                html.Div([
                    dbc.Label("IBEX35 Today", className="label"),
                    dbc.InputGroup([
                        dbc.InputGroupAddon("$", addon_type="prepend"),
                        dbc.Input(id='ibex',placeholder="Amount", type="number"),
                        dbc.InputGroupAddon(".00", addon_type="append"),
                    ]
                    ),
                    html.A("Get IBEX35", href="https://finance.yahoo.com/quote/%5EIBEX/history/"),
                ]),

                html.Div([
                    dbc.Label("Shanghai Index Today", className="label"),
                    dbc.InputGroup([
                        dbc.InputGroupAddon("$", addon_type="prepend"),
                        dbc.Input(id='SSE', placeholder="Amount", type="number"),
                        dbc.InputGroupAddon(".00", addon_type="append"),
                    ]
                    ),
                    html.A("Get SSE", href="https://finance.yahoo.com/quote/000001.ss/history/"),
                ]),

                html.Div([
                    dbc.Label("CNY/USD30", className="label"),
                    dbc.InputGroup([
                        dbc.InputGroupAddon("$", addon_type="prepend"),
                        dbc.Input(id='CNYUSD', placeholder="Amount", type="number"),
                        dbc.InputGroupAddon(".00", addon_type="append"),
                    ]
                    ),
                    html.A("Find exchange rate", href="https://finance.yahoo.com/quote/USDCNY=X/"),
                ]),

                html.Div([
                    dbc.Label("EUR/USD30", className="label"),
                    dbc.InputGroup([
                        dbc.InputGroupAddon("$", addon_type="prepend"),
                        dbc.Input(id='EURUSD', placeholder="Amount", type="number"),
                        dbc.InputGroupAddon(".00", addon_type="append"),
                    ]
                    ),
                    html.A("Find exchange rate", href="https://finance.yahoo.com/quote/EURUSD=X/"),
                ]),

                html.Div([
                    dbc.Label("EUR/CNY30", className="label"),
                    dbc.InputGroup([
                        dbc.InputGroupAddon("$", addon_type="prepend"),
                        dbc.Input(id='EURCNY', placeholder="Amount", type="number"),
                        dbc.InputGroupAddon(".00", addon_type="append"),
                    ]
                    ),
                    html.A("Find exchange rate", href="https://finance.yahoo.com/quote/EURCNY=X%3Fp=EURCNY/"),
                ]),


            ], className="filters card-filters"),
            
            html.Div([
                html.H2("Scenario Selection", className = "headline-2"),
                html.Div([
                    dbc.Label("Geopolitical", className="label"),
                    dbc.InputGroup([
                        dbc.InputGroupAddon("$", addon_type="prepend"),
                        dbc.Input(id='geopolitical', placeholder="Amount", type="number"),
                        dbc.InputGroupAddon(".00", addon_type="append"),
                    ]
                    ),
                ]
                ),

                html.Div([
                    dbc.Label("Sudden Surcharge", className="label"),
                    dbc.InputGroup([
                        dbc.InputGroupAddon("$", addon_type="prepend"),
                        dbc.Input(id='surchage', placeholder="Amount", type="number"),
                        dbc.InputGroupAddon(".00", addon_type="append"),
                    ]
                    ),
                ]
                ),

                html.Div([
                    dbc.Label("Port Congestion", className="label"),
                    dbc.InputGroup([
                        dbc.InputGroupAddon("$", addon_type="prepend"),
                        dbc.Input(id='congestion', placeholder="Amount", type="number"),
                        dbc.InputGroupAddon(".00", addon_type="append"),
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
                    html.Div(id='prediction-content', className="prediction box"),
                ], className= "prediction"),

                html.Div([
                    html.Label("90 Day Forecast (in USD)") ,
                    html.Div(
                        html.P("1678"), 
                    className="box",
                    ),
                ], className= "prediction"),

            ], className="predictions card-predictions"),

         
            # html.Div([
            #     html.H2("Predictions", className = "headline-2"),
            #     html.Div([
            #         html.Label("30 Day Forecast") ,
            #         html.Div(
            #             html.P("1250$"), 
            #         className="box",
            #         ),
            #     ], className= "prediction"),

            #     html.Div([
            #         dbc.Label("90 Day Forecast") ,
            #         html.Div(
            #             html.P("1678,00$"), 
            #         className="box",
            #         ),
            #     ], className= "prediction"),
            # ], className="predictions card-predictions"),
        ], className= "container"
    ),
], 
)

@app.callback(
    Output('prediction-content', 'children'),
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
    State('EURCNY', 'value')],
    prevent_initial_call=True
)
    
def update_output(n_clicks, dropdown_carrier, dropdown_origin, dropdown_destination, freight_rate, oil_price, ibex, SSE, CNYUSD, EURUSD, EURCNY):
    if n_clicks is None:
        raise PreventUpdate

    else:
        today = date.today()
        date30= date.today() + timedelta(days=30)
        month = date30.month
        day = date30.day
        weekday= date30.weekday()

        if month <7:
            month = month + 0.1 

        month= str(month)
        weekday = str(weekday)
        
        df= pd.DataFrame(columns = ['Day', 'Price30', 'CNY/USD30', 'EUR/USD30', 'EUR/CNY30', 'SSE30',
        'Ibex30', 'Crude_Oil30', 'ALGECIRAS', 'BARCELONA', 'BILBAO', 'VALENCIA',
        'VIGO', 'SHANGHAI', 'ANL', 'APL', 'CHINA SHIPPING', 'CMA-CGM', 'COSCO',
        'EVERGREEN', 'HAMBURG SUD', 'HANJIN', 'HAPAG LLOYD', 'HMM', 'K-LINE',
        'MAERSK', 'MOL', 'MSC', 'NIPPON', 'ONE', 'OOCL', 'UASC', 'YANG MING',
        '0', '1', '2', '3', '4', '5', '6', '1.1', '2.1', '3.1', '4.1', '5.1',
        '6.1', '7', '8', '9', '10', '11', '12'])
        
        df.loc[0] = 0
        
        df['Day'] = day
        df['Price30'] = freight_rate
        df['CNY/USD30'] = CNYUSD
        df['EUR/USD30'] = EURUSD
        df['EUR/CNY30'] = EURCNY
        df['SSE30'] = SSE
        df['Ibex30'] = ibex
        df['Crude_Oil30'] = oil_price
        df[dropdown_destination] = 1
        df[dropdown_origin] = 1
        df[dropdown_carrier] = 1
        df[weekday] = 1
        df[month] = 1
        
        rf = pickle.load(open('/Users/marieheller/OneDrive - Universitat Ramón Llull/01_Courses/02_Term 2/Noatum - Capstone/Final Models/model.sav', 'rb'))
        
        prediction = rf.predict(df)
        pred = round(prediction[0]/100) * 100
        
        return pred

if __name__ == "__main__":
    app.run_server(debug=True)



    #   dcc.RadioItems(
    #                 options=[
    #                     {'label': '  Optimistic', 'value': 'Optimistic'},
    #                     {'label': '  Neutral', 'value': 'Neutral'},
    #                     {'label': '  Pessimistic', 'value': 'Pessimistic'}
    #                 ], labelStyle = dict(display='block'),
    #                 value=''),