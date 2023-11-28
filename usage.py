import json
import dash
from dash import html
import feffery_utils_components as fuc
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        fuc.FefferyAPlayer(
            id='aplayer',
            lrcType=1,
            audio=[
                {
                    'name': '向云端',
                    'artist': '小霞/海洋Bo',
                    'url': 'http://isure.stream.qqmusic.qq.com/M500000Xv09t2pjQtH.mp3?guid=4176148&vkey=44EAF1EEA767F3402ABC3D359BB8F53E3A6A3E08C32D507C4A59D55C323C15B7F0A59EA5227F5EDF42122C564930B34AE531F5FA1896769A&uin=&fromtag=120042',
                    'cover': 'http://y.qq.com/music/photo_new/T002R300x300M00000152o5W2z6PSk_2.jpg?max_age=2592000',
                    'lrc': '[00:00.00]APlayer\n[00:04.01]is\n[00:08.02]amazing',
                    'theme': '#ebd0c2'
                },
                {
                    'name': '失眠情歌',
                    'artist': 'L（桃籽）',
                    'url': 'http://isure.stream.qqmusic.qq.com/M500000HJcoP22jH3W.mp3?guid=6043356&vkey=FD1BF50F9671D6AC8AF09ED763520ACFD5BFE6A82F1E8F246685FEFEAE20DCADB03F265CC4D6CC86C7F49D7820C3882F58169C0927EA757F&uin=&fromtag=120042',
                    'cover': 'http://y.qq.com/music/photo_new/T002R300x300M000000tBAfV4PQul6_1.jpg?max_age=2592000',
                    'theme': '#ebd0c2'
                },
            ]
        ),
        fuc.FefferyFancyButton(
            id='play-button',
            type='primary',
            children='播放',
            style={
               'margin': '5px'
            }
        ),
        fuc.FefferyFancyButton(
            id='pause-button',
            type='primary',
            children='暂停',
            style={
               'margin': '5px'
            }
        ),
        fuc.FefferyFancyButton(
            id='back-button',
            type='primary',
            children='上一首',
            style={
               'margin': '5px'
            }
        ),
        fuc.FefferyFancyButton(
            id='next-button',
            type='primary',
            children='下一首',
            style={
                'margin': '5px'
            }
        ),
        fuc.FefferyFancyButton(
            id='seek-button',
            type='primary',
            children='跳到一分钟处',
            style={
                'margin': '5px'
            }
        ),
        fuc.FefferyFancyButton(
            id='show-notice-button',
            type='primary',
            children='显示通知',
            style={
                'margin': '5px'
            }
        ),
        fuc.FefferyFancyButton(
            id='show-lyc-button',
            type='primary',
            children='显示歌词',
            style={
                'margin': '5px'
            }
        ),
        fuc.FefferyFancyButton(
            id='hide-lyc-button',
            type='primary',
            children='隐藏歌词',
            style={
                'margin': '5px'
            }
        ),
        fuc.FefferyFancyButton(
            id='show-list-button',
            type='primary',
            children='显示列表',
            style={
                'margin': '5px'
            }
        ),
        fuc.FefferyFancyButton(
            id='hide-list-button',
            type='primary',
            children='隐藏列表',
            style={
                'margin': '5px'
            }
        ),
        fuc.FefferyFancyButton(
            id='add-button',
            type='primary',
            children='添加音乐',
            style={
                'margin': '5px'
            }
        ),
        fuc.FefferyFancyButton(
            id='remove-button',
            type='primary',
            children='移除音乐',
            style={
                'margin': '5px'
            }
        ),
        fuc.FefferyFancyButton(
            id='switch-button',
            type='primary',
            children='切换到第二首',
            style={
                'margin': '5px'
            }
        ),
        fuc.FefferyFancyButton(
            id='clear-button',
            type='primary',
            children='清空音乐',
            style={
                'margin': '5px'
            }
        ),
        fuc.FefferyFancyButton(
            id='destroy-button',
            type='primary',
            children='销毁播放器',
            style={
                'margin': '5px'
            }
        ),
        html.Div(id='app-container-output')
    ],
    id='app-container',
    style={
        'padding': 50
    }
)


@app.callback(
    [Output('aplayer', 'play'),
     Output('aplayer', 'pause'),
     Output('aplayer', 'skipBack'),
     Output('aplayer', 'skipForward'),
     Output('aplayer', 'seek'),
     Output('aplayer', 'notice'),
     Output('aplayer', 'showLrc'),
     Output('aplayer', 'hideLrc'),
     Output('aplayer', 'showList'),
     Output('aplayer', 'hideList')],
    [Input('play-button', 'nClicks'),
     Input('pause-button', 'nClicks'),
     Input('back-button', 'nClicks'),
     Input('next-button', 'nClicks'),
     Input('seek-button', 'nClicks'),
     Input('show-notice-button', 'nClicks'),
     Input('show-lyc-button', 'nClicks'),
     Input('hide-lyc-button', 'nClicks'),
     Input('show-list-button', 'nClicks'),
     Input('hide-list-button', 'nClicks')],
    prevent_initial_call=True
)
def callback_operate_aplayer(play_button_n_clicks, pause_button_n_clicks, back_button_n_clicks, next_button_n_clicks, seek_button_n_clicks, show_notice_button_n_clicks, show_lyc_button_n_clicks, hide_lyc_button_n_clicks, show_list_button_n_clicks, hide_list_button_n_clicks):
    trigger_id = dash.ctx.triggered_id
    if trigger_id == 'play-button':
        return [True, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update]
    if trigger_id == 'pause-button':
        return [dash.no_update, True, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update]
    if trigger_id == 'back-button':
        return [dash.no_update, dash.no_update, True, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update]
    if trigger_id == 'next-button':
        return [dash.no_update, dash.no_update, dash.no_update, True, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update]
    if trigger_id == 'seek-button':
        return [dash.no_update, dash.no_update, dash.no_update, dash.no_update, {'isSeek': True, 'time': 60}, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update]
    if trigger_id == 'show-notice-button':
        return [dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, {'isShow': True, 'text': '这是一条通知'}, dash.no_update, dash.no_update, dash.no_update, dash.no_update]
    if trigger_id == 'show-lyc-button':
        return [dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, True, dash.no_update, dash.no_update, dash.no_update]
    if trigger_id == 'hide-lyc-button':
        return [dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, True, dash.no_update, dash.no_update]
    if trigger_id == 'show-list-button':
        return [dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, True, dash.no_update]
    if trigger_id == 'hide-list-button':
        return [dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, True]
    return [dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update]


@app.callback(
    [Output('aplayer', 'addList'),
     Output('aplayer', 'removeList'),
     Output('aplayer', 'switchList'),
     Output('aplayer', 'clearList'),
     Output('aplayer', 'destroy')],
    [Input('add-button', 'nClicks'),
     Input('remove-button', 'nClicks'),
     Input('switch-button', 'nClicks'),
     Input('clear-button', 'nClicks'),
     Input('destroy-button', 'nClicks')],
    prevent_initial_call=True
)
def callback_operate_aplayer_list(add_button_n_clicks, remove_button_n_clicks, switch_button_n_clicks, clear_button_n_clicks, destroy_button_n_clicks):
    trigger_id = dash.ctx.triggered_id
    if trigger_id == 'add-button':
        return [{'isAdd': True, 'audio': [{'name': 'test', 'url': '', 'cover': '', 'artist': 'test', 'theme': '#ebd0c2'}]}, dash.no_update, dash.no_update, dash.no_update, dash.no_update]
    if trigger_id == 'remove-button':
        return [dash.no_update, {'isRemove': True, 'index': 1}, dash.no_update, dash.no_update, dash.no_update]
    if trigger_id == 'switch-button':
        return [dash.no_update, dash.no_update, {'isSwitch': True, 'index': 1}, dash.no_update, dash.no_update]
    if trigger_id == 'clear-button':
        return [dash.no_update, dash.no_update, dash.no_update, True, dash.no_update]
    if trigger_id == 'destroy-button':
        return [dash.no_update, dash.no_update, dash.no_update, dash.no_update, True]
    return [dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update]


@app.callback(
    Output('app-container-output', 'children'),
    [Input('aplayer', 'currentPlayAudioInfo'),
     Input('aplayer', 'currentPauseAudioInfo'),
     Input('aplayer', 'currentSeekAudioInfo'),
     Input('aplayer', 'currentNoticeInfo'),
     Input('aplayer', 'currentListAddAudioInfo'),
     Input('aplayer', 'currentListRemoveAudioInfo'),
     Input('aplayer', 'currentListSwitchAudioInfo')],
    prevent_initial_call=True
)
def callback_operate_aplayer_output(currentPlayAudioInfo, currentPauseAudioInfo, currentSeekAudioInfo, currentNoticeInfo, currentListAddAudioInfo, currentListRemoveAudioInfo, currentListSwitchAudioInfo):
    data = {
        'currentPlayAudioInfo': currentPlayAudioInfo,
        'currentPauseAudioInfo': currentPauseAudioInfo,
        'currentSeekAudioInfo': currentSeekAudioInfo,
        'currentNoticeInfo': currentNoticeInfo,
        'currentListAddAudioInfo': currentListAddAudioInfo,
        'currentListRemoveAudioInfo': currentListRemoveAudioInfo,
        'currentListSwitchAudioInfo': currentListSwitchAudioInfo
    }
    return fuc.FefferyJsonViewer(
        data=data
    )


if __name__ == '__main__':
    app.run(debug=True)
