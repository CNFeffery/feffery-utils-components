import { useEffect } from 'react';
import { useFullscreen } from 'ahooks';
import PropTypes from 'prop-types';

// 定义全屏化组件FefferyFullscreen，api参数参考：https://ahooks.js.org/zh-CN/hooks/use-fullscreen
const FefferyFullscreen = (props) => {
    // 取得必要属性或参数
    const {
        id,
        targetId,
        isFullscreen,
        setProps,
        loading_state
    } = props;

    const [
        _isFullscreen,
        {
            enterFullscreen,
            exitFullscreen,
            toggleFullscreen,
            isEnabled,
        }
    ] = useFullscreen(
        () => document.getElementById(targetId)
    );

    useEffect(() => {
        if (isFullscreen) {
            enterFullscreen()
        } else {
            exitFullscreen()
        }
    }, [isFullscreen])

    useEffect(() => {
        if (_isFullscreen !== isFullscreen) {
            setProps({
                isFullscreen: _isFullscreen
            })
        }
    }, [_isFullscreen])

    return (
        <div
            id={id}
            data-dash-is-loading={
                (loading_state && loading_state.is_loading) || undefined
            } />
    );
}


// 定义参数或属性
FefferyFullscreen.propTypes = {
    // 部件id
    id: PropTypes.string,

    // 设置要全屏化的目标元素id，必填
    targetId: PropTypes.string.isRequired,

    // 设置或监听目标元素的全屏化状态，默认为false
    isFullscreen: PropTypes.bool,

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
FefferyFullscreen.defaultProps = {
    isFullscreen: false
}

export default FefferyFullscreen;