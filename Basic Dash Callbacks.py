import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    dcc.Input(id='my-id', value='initial Value', type='text'),
    html.Div(id='my-div')
])


# Input and output are described declaratively.
# Input is rendered in the value property of the given component
# Output is rendered in the child property of the given component
@app.callback(
    Output(component_id='my-div', component_property='children'),
    # Input is iterable that's why it is in a list.
    [Input(component_id='my-id', component_property='value')]
)
# Dash provides the function with the new input value
# Dash returns the value to be rendered in the Output component.
def update_output_div(input_value):
    return "You've entered '{}'".format(input_value)


if __name__ == '__main__':
    app.run_server(debug=True)
