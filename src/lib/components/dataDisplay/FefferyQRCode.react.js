// react核心
import React from 'react';
import PropTypes from 'prop-types';
// 组件核心
import { QRCodeSVG, QRCodeCanvas } from 'qrcode.react';
// 辅助库
import { useLoading } from '../utils';

/**
 * 二维码生成组件FefferyQRCode
 */
const FefferyQRCode = ({
    id,
    key,
    renderer = 'svg',
    value,
    size = 128,
    bgColor = '#FFFFFF',
    fgColor = '#000000',
    level = 'L',
    includeMargin = false,
    imageSettings,
    setProps
}) => {

    const component_loading = useLoading();

    if (renderer === 'canvas') {
        return (<QRCodeCanvas
            id={id}
            key={key}
            value={value}
            size={size}
            bgColor={bgColor}
            fgColor={fgColor}
            level={level}
            includeMargin={includeMargin}
            imageSettings={{
                excavate: true,
                ...imageSettings
            }}
            data-dash-is-loading={component_loading}
        />);
    }

    return <QRCodeSVG
        id={id}
        value={value}
        size={size}
        bgColor={bgColor}
        fgColor={fgColor}
        level={level}
        includeMargin={includeMargin}
        imageSettings={{
            excavate: true,
            ...imageSettings
        }}
        data-dash-is-loading={component_loading} />;
}

FefferyQRCode.propTypes = {
    /**
     * 组件唯一id
     */
    id: PropTypes.string,

    /**
     * 对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果
     */
    key: PropTypes.string,

    /**
     * 设置二维码所表达的信息值
     */
    value: PropTypes.string.isRequired,

    /**
     * 二维码像素边长
     * 默认值：`128`
     */
    size: PropTypes.number,

    /**
     * 背景色
     * 默认值：`'#FFFFFF'`
     */
    bgColor: PropTypes.string,

    /**
     * 前景色
     * 默认值：`'#000000'`
     */
    fgColor: PropTypes.string,

    /**
     * 解析精度，可选项有`'L'`、'M'、'Q'、'H'
     * 默认值：`'L'`
     */
    level: PropTypes.oneOf(['L', 'M', 'Q', 'H']),

    /**
     * 是否添加外边距
     * 默认值：`false`
     */
    includeMargin: PropTypes.bool,

    /**
     * 配置二维码中心图片信息
     */
    imageSettings: PropTypes.exact({
        /**
         * 图片地址
         */
        src: PropTypes.string,

        /**
         * 图片像素高度，默认为二维码`size`的`10%`
         */
        height: PropTypes.number,

        /**
         * 图片像素宽度，默认为二维码`size`的`10%`
         */
        width: PropTypes.number,

        /**
         * 图片四周是否添加环绕白边
         * 默认值：`true`
         */
        excavate: PropTypes.bool
    }),

    /**
     * 指定渲染引擎，可选项有`'svg'`、`'canvas'`
     * 默认值：`'svg'`
     */
    renderer: PropTypes.oneOf(['svg', 'canvas']),

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
};

export default FefferyQRCode;