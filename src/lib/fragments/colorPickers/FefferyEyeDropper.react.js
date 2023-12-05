import { useEffect } from 'react';
import useEyeDropper from 'use-eye-dropper';
import { propTypes, defaultProps } from '../../components/colorPickers/FefferyEyeDropper.react';

// 定义色彩拾取组件FefferyEyeDropper
const FefferyEyeDropper = (props) => {

    // 取得必要属性或参数
    const {
        id,
        enable,
        setProps,
        loading_state
    } = props;

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

    return (
        <div
            id={id}
            data-dash-is-loading={
                (loading_state && loading_state.is_loading) || undefined
            } />
    );
}

export default FefferyEyeDropper;

FefferyEyeDropper.defaultProps = defaultProps;
FefferyEyeDropper.propTypes = propTypes;