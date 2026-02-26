// react核心
import { useRef, useEffect } from 'react';
// 组件核心
import SliderCaptcha from 'rc-slider-captcha';
import createPuzzle from 'create-puzzle';
// 辅助库
import { useSize } from 'ahooks';
import { useLoading } from '../../components/utils';
// 参数类型
import { propTypes, defaultProps } from '../../components/verification/FefferySliderCaptcha.react';

/**
 * 滑块验证码组件FefferySliderCaptcha
 */
const FefferySliderCaptcha = ({
    id,
    key,
    style,
    className,
    imgSrc,
    xOffset,
    imgWidth,
    imgHeight,
    mode,
    tipText,
    showRefreshIcon,
    autoRefreshOnError,
    errorHoldDuration,
    placement,
    refresh,
    block,
    setProps
}) => {

    // 记录x轴动态偏移量
    const offsetXRef = useRef(0);
    // 手动刷新用
    const actionRef = useRef();
    // 父容器ref
    const wrapperRef = useRef();
    // 父容器尺寸监听
    const wrapperSize = useSize(wrapperRef);

    // 手动刷新
    useEffect(() => {
        if (refresh) {
            actionRef.current?.refresh()
            setProps({ refresh: false })
        }
    }, [refresh])

    return (
        <div ref={wrapperRef}>
            <SliderCaptcha
                id={id}
                key={key}
                style={style}
                className={className}
                actionRef={actionRef}
                request={
                    mode === 'slider' ?
                        undefined :
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
                        // slider 模式：滑块划到最右侧即为验证通过
                        if (mode === 'slider') {
                            const effectiveWidth = block ? wrapperSize?.width : imgWidth;
                            if (data.sliderOffsetX + 40 + xOffset >= effectiveWidth) {
                                setProps({
                                    verifyResult: {
                                        status: 'success',
                                        timestamp: Date.now()
                                    }
                                })
                                return Promise.resolve();
                            }
                        } else {
                            // embed/float 模式：原有逻辑
                            if (data.x >= offsetXRef.current - xOffset && data.x < offsetXRef.current + xOffset) {
                                setProps({
                                    verifyResult: {
                                        status: 'success',
                                        timestamp: Date.now()
                                    }
                                })
                                return Promise.resolve();
                            }
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
                    width: block ? wrapperSize?.width : imgWidth,
                    height: imgHeight
                }}
                mode={mode}
                tipText={tipText}
                showRefreshIcon={showRefreshIcon}
                autoRefreshOnError={autoRefreshOnError}
                errorHoldDuration={errorHoldDuration}
                placement={placement}
                data-dash-is-loading={useLoading()} />
        </div>
    );
}

export default FefferySliderCaptcha;

FefferySliderCaptcha.defaultProps = defaultProps;
FefferySliderCaptcha.propTypes = propTypes;