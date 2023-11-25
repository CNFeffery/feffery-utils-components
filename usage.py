import json
import dash
from dash import html
import feffery_utils_components as fuc
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        fuc.FefferyMusicPlayer(
            id='music-player',
            customizeColor='#f63',
            audioLists=[
                {
                    'name': 'Despacito',
                    'cover': 'http://res.cloudinary.com/alick/image/upload/v1502689731/Despacito_uvolhp.jpg',
                    'musicSrc': 'http://res.cloudinary.com/alick/video/upload/v1502689683/Luis_Fonsi_-_Despacito_ft._Daddy_Yankee_uyvqw9.mp3',
                    'extraParams': {
                        'singer': 'Luis Fonsi'
                    }
                },
                {
                    'name': 'Dorost Nemisham',
                    'cover': 'https://res.cloudinary.com/ehsanahmadi/image/upload/v1573758778/Sirvan-Khosravi-Dorost-Nemisham_glicks.jpg',
                    'musicSrc': 'https://res.cloudinary.com/ehsanahmadi/video/upload/v1573550770/Sirvan-Khosravi-Dorost-Nemisham-128_kb8urq.mp3',
                    'extraParams': {
                        'singer': 'Sirvan Khosravi'
                    }
                },
            ],
            showLyric=True
        )
    ],
    style={
        'padding': 50
    }
)

if __name__ == '__main__':
    app.run(debug=True)
