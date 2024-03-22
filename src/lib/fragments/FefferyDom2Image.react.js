import { useAsyncEffect } from 'ahooks';
import { domToPng } from 'modern-screenshot';
import { propTypes, defaultProps } from '../components/FefferyDom2Image.react';

/**
 * 元素转图片组件FefferyDom2Image
 */
const FefferyDom2Image = (props) => {
    const {
        targetSelector,
        scale,
        setProps,
        loading_state
    } = props;

    // 每次targetSelector更新时，异步进行目标元素转图片操作
    useAsyncEffect(async () => {
        if (targetSelector) {
            // 检查目标元素是否有效
            let target = document.querySelector(targetSelector);
            if (target) {
                domToPng(
                    target,
                    {
                        scale: scale
                    }
                ).then(
                    dataUrl => {
                        setProps({
                            screenshotResult: {
                                selector: targetSelector,
                                status: 'success',
                                dataUrl: dataUrl,
                                timestamp: new Date().getTime()
                            }
                        })
                    }
                )
            } else {
                setProps({
                    screenshotResult: {
                        selector: targetSelector,
                        status: 'failed',
                        dataUrl: null,
                        timestamp: new Date().getTime()
                    }
                })
            }
            setProps({ targetSelector: null })
        }
    }, [targetSelector])

    return <></>;
}

export default FefferyDom2Image;

FefferyDom2Image.defaultProps = defaultProps;
FefferyDom2Image.propTypes = propTypes;