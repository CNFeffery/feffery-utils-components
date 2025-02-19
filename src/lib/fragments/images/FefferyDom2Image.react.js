// 组件核心
import { domToPng } from 'modern-screenshot';
// 辅助库
import { useAsyncEffect } from 'ahooks';
// 参数类型
import { propTypes, defaultProps } from '../../components/images/FefferyDom2Image.react';

/**
 * 元素转图片组件FefferyDom2Image
 */
const FefferyDom2Image = ({
    targetSelector,
    scale,
    setProps
}) => {

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