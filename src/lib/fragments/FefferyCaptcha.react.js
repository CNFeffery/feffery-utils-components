import React, { useCallback, useEffect, useRef } from 'react';
import PropTypes from 'prop-types';
import Captcha from 'react-captcha-code';
import { propTypes, defaultProps } from '../components/FefferyCaptcha.react';

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
        refresh,
        setProps,
        loading_state
    } = props;

    // 返回定制化的前端部件
    const handleChange = useCallback((captcha) => {
        setProps({ captcha: captcha })
    }, []);

    // 当refresh变化为true时强制刷新验证码
    useEffect(() => {
        if (refresh && captchaRef.current) {
            captchaRef.current.refresh()
            setProps({ refresh: false })
        }
    }, [refresh])

    const captchaRef = useRef(<HTMLCanvasElement />);

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
            onChange={handleChange}
            data-dash-is-loading={
                (loading_state && loading_state.is_loading) || undefined
            } />
    );
}

export default FefferyCaptcha;

FefferyCaptcha.defaultProps = defaultProps;
FefferyCaptcha.propTypes = propTypes;