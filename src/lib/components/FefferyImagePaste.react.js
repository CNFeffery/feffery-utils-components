import React, { useCallback } from 'react';
import PropTypes from 'prop-types';
import { Gluejar } from '../utils/gluejar'

const urlToBase64 = (url) => {
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

// 定义粘贴板图片获取组件FefferyImagePaste，api参数参考https://github.com/charliewilco/react-gluejar
const FefferyImagePaste = (props) => {
    // 取得必要属性或参数
    let {
        id,
        key,
        disabled,
        setProps,
        loading_state
    } = props;

    // 监听图片粘贴事件
    const handlePaste = useCallback(async (files) => {
        if (files.images.length !== 0) {
            let result = await urlToBase64(files.images[files.images.length - 1])
            setProps({
                imageInfo: {
                    base64: result,
                    timestamp: Date.parse(new Date())
                }
            })
        }
    }, []);

    return (
        <div id={id}
            key={key}
            data-dash-is-loading={
                (loading_state && loading_state.is_loading) || undefined
            }
        >
            <Gluejar onPaste={(files) => {
                if (!disabled) {
                    handlePaste(files)
                }
            }}
                onError={() => null}
                container={document.querySelector('#container')} />
        </div >
    );
}

// 定义参数或属性
FefferyImagePaste.propTypes = {
    // 组件id
    id: PropTypes.string,

    // 辅助刷新用唯一标识key值
    key: PropTypes.string,

    // 监听最近一次图片粘贴事件中载入图片的base64字符串及时间戳信息
    imageInfo: PropTypes.exact({
        // 记录最新粘贴图片的base64字符串
        base64: PropTypes.string,
        // 时间戳信息
        timestamp: PropTypes.number
    }),

    // 设置是否禁用当前组件的图片粘贴行为监听功能，默认为false
    disabled: PropTypes.bool,

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
FefferyImagePaste.defaultProps = {
    disabled: false
}

export default FefferyImagePaste;