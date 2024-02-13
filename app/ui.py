import dash
from dash import html, dcc, Input, Output, State
import requests
import base64
from io import BytesIO

from api import create_app

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

server = create_app()

app = dash.Dash(__name__, server=server, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Upload(
        id='upload-image',
        children=html.Div(['Drag and Drop or ', html.A('Select Files')]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        },
        multiple=False
    ),
    html.Div(id='file-upload-info'),
    html.Button('Predict', id='predict-button', n_clicks=0),
    html.Div(id='output-prediction')
])

@app.callback(
    Output('file-upload-info', 'children'),
    [Input('upload-image', 'contents')],
    [State('upload-image', 'filename'), State('upload-image', 'last_modified')]
)
def update_file_upload_info(contents, filename, last_modified):
    if contents is not None:
        children = [
            html.Img(src=contents, style={'maxHeight': '200px', 'maxWidth': '200px', 'margin-top': '10px'}),
            html.Div(f"Filename: {filename}")
        ]
        return children
    else:
        return "No file uploaded yet."

@app.callback(
    Output('output-prediction', 'children'),
    [Input('predict-button', 'n_clicks')],
    [State('upload-image', 'contents')]
)
def update_output(n_clicks, contents):
    if n_clicks > 0 and contents is not None:
        content_type, content_string = contents.split(',')
        decoded = base64.b64decode(content_string)
        image_io = BytesIO(decoded)
        image_io.name = 'image.png'
        
        response = requests.post(
            'http://localhost:5000/predict', 
            files={'file': (image_io.name, image_io, 'image/png')}
        )

        if response.status_code == 200:
            return f"Prediction: {response.json()['class_name'].replace('_', ' ')}"
        else:
            return 'Failed to get prediction.'
        
    return 'Upload an image and click predict.'

if __name__ == '__main__':
    app.run_server(debug=False, port=5000, host='0.0.0.0')