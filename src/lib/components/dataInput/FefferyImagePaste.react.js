// react核心
import React, { useCallback } from 'react';
import PropTypes from 'prop-types';
// 组件核心
import { Gluejar } from '../../utils/gluejar/dist'
// 辅助库
import { useLoading } from '../utils';

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

/**
 * 粘贴板图片获取组件FefferyImagePaste
 */
const FefferyImagePaste = ({
    id,
    key,
    disabled = false,
    setProps
}) => {

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
            data-dash-is-loading={useLoading()}
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

FefferyImagePaste.propTypes = {
    /**
     * 组件唯一id
     */
    id: PropTypes.string,

    /**
     * 对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果
     */
    key: PropTypes.string,

    /**
     * 监听最近一次图片粘贴事件中载入图片的`base64`字符串及时间戳信息
     */
    imageInfo: PropTypes.exact({
        /**
         * 记录最新粘贴图片的`base64`字符串
         */
        base64: PropTypes.string,
        /**
         * 时间戳信息
         */
        timestamp: PropTypes.number
    }),

    /**
     * 设置是否禁用当前组件的图片粘贴行为监听功能
     * 默认值：`false`
     */
    disabled: PropTypes.bool,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};

export default FefferyImagePaste;