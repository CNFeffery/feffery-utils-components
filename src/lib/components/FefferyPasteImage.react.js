import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { Card, Button } from 'antd';
import { Gluejar } from '@charliewilco/gluejar'
import { DeleteOutlined } from '@ant-design/icons';
import './styles.css'
import 'antd/dist/antd.css';

function urlToBase64(url) {
    return new Promise((resolve, reject) => {
        let image = new Image();
        image.onload = function () {
            let canvas = document.createElement('canvas');
            canvas.width = this.naturalWidth;
            canvas.height = this.naturalHeight;
            // 将图片插入画布并开始绘制
            canvas.getContext('2d').drawImage(image, 0, 0);
            // result
            let result = canvas.toDataURL('image/png')
            resolve(result);
        };
        // CORS 策略，会存在跨域问题https://stackoverflow.com/questions/20424279/canvas-todataurl-securityerror
        image.setAttribute("crossOrigin", 'Anonymous');
        image.src = url;
        // 图片加载失败的错误处理
        image.onerror = () => {
            reject(new Error('urlToBase64 error'));
        };
    }
    )
}


// 定义图片粘贴组件FefferyPasteImage，api参数参考https://github.com/charliewilco/react-gluejar
export default class FefferyPasteImage extends Component {
    render() {
        // 取得必要属性或参数
        let {
            id,
            className,
            style,
            currentPastedImages,
            setProps
        } = this.props;

        console.log({ currentPastedImages })

        return (
            <div id={id}
                className={className}
                style={style}>
                <Gluejar
                    key={1}
                    onPaste={
                        (files) => {
                            console.log({ files })
                        }
                    }
                    onError={err => console.error(err)}>
                    {({ images }) => {
                        if (images.length > 0) {
                            setProps({
                                currentPastedImages: images
                            })

                            return (
                                <Card style={{ height: '100%' }}>
                                    {
                                        images.map((image, idx) => {
                                            return (
                                                <Card.Grid
                                                    style={{ width: '25%', paddnig: 0, cursor: 'pointer' }}
                                                >
                                                    <Button shape="circle" icon={<DeleteOutlined />}
                                                        style={{ float: 'right', 'marginBottom': 5 }} />
                                                    <img src={image} key={image} alt={`Pasted: ${image}`} style={{ width: '100%', borderTop: '1px solid #f0f0f0' }} />
                                                </Card.Grid>
                                            );
                                        }
                                        )
                                    }
                                </Card>
                            );
                        }
                        return null;
                    }
                    }
                </Gluejar>
            </div >
        );
    }
}

// 定义参数或属性
FefferyPasteImage.propTypes = {
    // 部件id
    id: PropTypes.string,

    /**
     * The content of the tab - will only be displayed if this tab is selected
     */
    children: PropTypes.node,

    // css类名
    className: PropTypes.string,

    // 自定义css字典
    style: PropTypes.object,

    // 存储当前保存的所有图片的base64字符串
    currentPastedImages: PropTypes.arrayOf(PropTypes.string),

    loading_state: PropTypes.shape({
        /**
         * Determines if the component is loading or not
         */
        is_loading: PropTypes.bool,
        /**
         * Holds which property is loading
         */
        prop_name: PropTypes.string,
        /**
         * Holds the name of the component that is loading
         */
        component_name: PropTypes.string
    }),

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};

// 设置默认参数
FefferyPasteImage.defaultProps = {
    className: 'feffery-paste-image-container',
    currentPastedImages: []
}
