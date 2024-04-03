import React, { useRef, useEffect } from 'react';
import SliderCaptcha from 'rc-slider-captcha';
import createPuzzle from 'create-puzzle';
import { propTypes, defaultProps } from '../components/FefferySliderCaptcha.react';

/**
 * 滑块验证码组件FefferySliderCaptcha
 */
const FefferySliderCaptcha = (props) => {
    let {
        id,
        style,
        className,
        imgSrc,
        xOffset,
        imgWidth,
        mode,
        tipText,
        showRefreshIcon,
        autoRefreshOnError,
        errorHoldDuration,
        placement,
        refresh,
        setProps,
        loading_state
    } = props;

    // 记录x轴动态偏移量
    const offsetXRef = useRef(0);
    // 手动刷新用
    const actionRef = useRef();

    // 手动刷新
    useEffect(() => {
        if (refresh) {
            actionRef.current?.refresh()
            setProps({ refresh: false })
        }
    }, [refresh])

    return (
        <SliderCaptcha
            id={id}
            style={style}
            className={className}
            actionRef={actionRef}
            request={
                () => createPuzzle(
                    imgSrc,
                    {
                        format: 'blob'
                    }
                ).then((res) => {
                    // 更新x轴动态偏移量
                    offsetXRef.current = res.x;
                    return {
                        bgUrl: res.bgUrl,
                        puzzleUrl: res.puzzleUrl
                    };
                })
            }
            onVerify={
                async (data) => {
                    if (data.x >= offsetXRef.current - xOffset && data.x < offsetXRef.current + xOffset) {
                        // 验证成功
                        setProps({
                            verifyResult: {
                                status: 'success',
                                timestamp: Date.now()
                            }
                        })
                        return Promise.resolve();
                    }
                    // 验证失败
                    setProps({
                        verifyResult: {
                            status: 'error',
                            timestamp: Date.now()
                        }
                    })
                    return Promise.reject();
                }
            }
            bgSize={{
                width: imgWidth
            }}
            mode={mode}
            tipText={tipText}
            showRefreshIcon={showRefreshIcon}
            autoRefreshOnError={autoRefreshOnError}
            errorHoldDuration={errorHoldDuration}
            placement={placement}
            data-dash-is-loading={
                (loading_state && loading_state.is_loading) || undefined
            } />
    );
}

export default FefferySliderCaptcha;

FefferySliderCaptcha.defaultProps = defaultProps;
FefferySliderCaptcha.propTypes = propTypes;