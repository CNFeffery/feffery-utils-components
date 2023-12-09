import React, { useEffect } from 'react';
import { QRCodeSVG, QRCodeCanvas } from 'qrcode.react';
import PropTypes from 'prop-types';

// 定义二维码生成组件FefferyQRCode
const FefferyQRCode = (props) => {
    // 取得必要属性或参数
    const {
        id,
        key,
        renderer,
        value,
        size,
        bgColor,
        fgColor,
        level,
        includeMargin,
        imageSettings,
        setProps,
        loading_state
    } = props;

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
            data-dash-is-loading={
                (loading_state && loading_state.is_loading) || undefined
            }
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
        data-dash-is-loading={
            (loading_state && loading_state.is_loading) || undefined
        } />;
}

// 定义参数或属性
FefferyQRCode.propTypes = {
    /**
     * 组件id
     */
    id: PropTypes.string,

    /**
     * 辅助刷新用唯一标识key值
     */
    key: PropTypes.string,

    /**
     * 设置二维码所表达的信息值
     */
    value: PropTypes.string.isRequired,

    /**
     * 设置像素边长，默认为128
     */
    size: PropTypes.number,

    /**
     * 设置背景色，默认为'#FFFFFF'
     */
    bgColor: PropTypes.string,

    /**
     * 设置前景色，默认为'#000000'
     */
    fgColor: PropTypes.string,

    /**
     * 设置解析精度，可选的有'L'、'M'、'Q'、'H'
     * 默认为'L'
     */
    level: PropTypes.oneOf(['L', 'M', 'Q', 'H']),

    /**
     * 设置是否添加外边距，默认为false
     */
    includeMargin: PropTypes.bool,

    /**
     * 配置二维码中心图片信息
     */
    imageSettings: PropTypes.exact({
        /**
         * 设置图片src
         */
        src: PropTypes.string,

        /**
         * 设置图片像素高度，默认为二维码size的10%
         */
        height: PropTypes.number,

        /**
         * 设置图片像素宽度，默认为二维码size的10%
         */
        width: PropTypes.number,

        /**
         * 设置图片四周是否添加环绕白边，默认为true
         */
        excavate: PropTypes.bool
    }),

    /**
     * 指定渲染引擎，可选的有'svg'、'canvas'，默认为'svg'
     */
    renderer: PropTypes.oneOf(['svg', 'canvas']),

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
    setProps: PropTypes.func,
};

// 设置默认参数
FefferyQRCode.defaultProps = {
    renderer: 'svg',
    size: 128,
    bgColor: '#FFFFFF',
    fgColor: '#000000',
    level: 'L',
    includeMargin: false
}

export default FefferyQRCode;