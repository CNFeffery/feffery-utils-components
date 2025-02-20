// react核心
import React, { useCallback, useEffect, useRef } from 'react';
// 组件核心
import Captcha from 'react-captcha-code';
// 辅助库
import { useLoading } from '../../components/utils';
// 参数类型
import { propTypes, defaultProps } from '../../components/verification/FefferyCaptcha.react';

/**
 * 验证码组件FefferyCaptcha
 */
const FefferyCaptcha = ({
    id,
    key,
    style,
    className,
    charNum,
    height,
    width,
    bgColor,
    fontSize,
    refresh,
    setProps
}) => {

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
            key={key}
            className={className}
            style={style}
            ref={captchaRef}
            charNum={charNum}
            height={height}
            width={width}
            bgColor={bgColor}
            fontSize={fontSize}
            onChange={handleChange}
            data-dash-is-loading={useLoading()} />
    );
}

export default FefferyCaptcha;

FefferyCaptcha.defaultProps = defaultProps;
FefferyCaptcha.propTypes = propTypes;