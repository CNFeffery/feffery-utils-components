// react核心
import { useEffect } from 'react';
// 组件核心
import useEyeDropper from 'use-eye-dropper';
// 辅助库
import { useLoading } from '../../components/utils';
// 参数类型
import { propTypes, defaultProps } from '../../components/colorPickers/FefferyEyeDropper.react';

/**
 * 色彩拾取组件FefferyEyeDropper
 */
const FefferyEyeDropper = ({
    id,
    enable,
    setProps,
}) => {

    const { open, close, isSupported } = useEyeDropper()

    const pickColor = () => {
        open()
            .then(e => {
                setProps({
                    color: e.sRGBHex,
                    enable: false
                })
            })
            // 手动退出时，将enable重置为false
            .catch(error => setProps({
                enable: false
            }))
    }

    useEffect(() => {
        // 若当前浏览器支持EyeDropper API
        if (isSupported()) {
            if (enable) {
                // 启用色彩拾取模式
                pickColor()
            } else {
                // 可控关闭色彩拾取模式
                close()
            }
        }
    }, [enable])

    return <></>;
}

export default FefferyEyeDropper;

FefferyEyeDropper.defaultProps = defaultProps;
FefferyEyeDropper.propTypes = propTypes;