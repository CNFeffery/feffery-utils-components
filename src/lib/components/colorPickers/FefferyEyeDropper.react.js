import { useEffect } from 'react';
import useEyeDropper from 'use-eye-dropper'
import PropTypes from 'prop-types';

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


// 定义参数或属性
FefferyEyeDropper.propTypes = {
    // 部件id
    id: PropTypes.string,

    // 设置是否启用色彩拾取模式，默认为false
    enable: PropTypes.bool,

    // 用于监听最近一次取色完成后得到的16进制色彩值
    color: PropTypes.string,

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
FefferyEyeDropper.defaultProps = {
    enable: false
}

export default FefferyEyeDropper;