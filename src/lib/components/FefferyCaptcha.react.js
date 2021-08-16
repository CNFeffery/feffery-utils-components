import React, { useCallback, useRef } from 'react';
import Captcha from 'react-captcha-code';

// 定义验证码部件FefferyCaptcha，api参数参考https://github.com/WebEngineerLi/react-captcha

const FefferyCaptcha = (props) => {
    // 取得必要属性或参数
    let {
        id,
        className,
        style,
        charNum,
        height,
        width,
        bgColor,
        fontSize,
        setProps
    } = props;

    // 返回定制化的前端部件
    const handleChange = useCallback((captcha) => {
        setProps({ captcha: captcha })
    }, []);

    const captchaRef = useRef(< HTMLCanvasElement />);

    return (
        <Captcha id={id}
            className={className}
            style={style}
            ref={captchaRef}
            charNum={charNum}
            height={height}
            width={width}
            bgColor={bgColor}
            fontSize={fontSize}
            onChange={handleChange} />
    );
}

// 定义参数或属性
FefferyCaptcha.propTypes = {
    // 部件id
    id: PropTypes.string,

    // css类名
    className: PropTypes.string,

    // 自定义css字典
    style: PropTypes.object,

    // 对应当前的验证码字符串
    captcha: PropTypes.string,

    // 设置验证码字符数量
    charNum: PropTypes.number,

    // 设置验证码的像素高度，默认为40
    height: PropTypes.number,

    // 设置验证码的像素宽度，默认为100
    width: PropTypes.number,

    // 设置验证码图片背景色，默认为'#DFF0D8'
    bgColor: PropTypes.string,

    // 设置验证码字体像素大小，默认为25
    fontSize: PropTypes.number,

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
FefferyCaptcha.defaultProps = {
    charNum: 4
}

export default FefferyCaptcha;