import { useEffect } from 'react';
import { useFullscreen } from 'ahooks';
import PropTypes from 'prop-types';

/**
 * 全屏化组件FefferyFullscreen
 */
const FefferyFullscreen = (props) => {
    // 取得必要属性或参数
    const {
        targetId,
        isFullscreen,
        pageFullscreen,
        setProps,
        loading_state
    } = props;

    const [
        _isFullscreen,
        {
            enterFullscreen,
            exitFullscreen
        }
    ] = useFullscreen(
        () => document.getElementById(targetId),
        {
            pageFullscreen: pageFullscreen
        }
    );

    useEffect(() => {
        if (!targetId) {
            const onFullscreenChange = (e) => {
                if (document.fullscreenElement) {
                    setProps({
                        isFullscreen: true
                    })
                } else {
                    setProps({
                        isFullscreen: false
                    })
                }
            }
            document.addEventListener('fullscreenchange', onFullscreenChange)
            return () => {
                document.removeEventListener('fullscreenchange', onFullscreenChange)
            }
        }
    }, [])

    useEffect(() => {
        if (targetId) {
            if (isFullscreen) {
                enterFullscreen()
            } else {
                exitFullscreen()
            }
        } else {
            if (isFullscreen && !document.fullscreenElement) {
                // 若当前处于非全屏状态
                document.documentElement.requestFullscreen()
            } else if (!isFullscreen && document.fullscreenElement) {
                // 若当前处于全屏状态
                document.exitFullscreen()
            }
        }
    }, [isFullscreen])

    useEffect(() => {
        if (_isFullscreen !== isFullscreen) {
            setProps({
                isFullscreen: _isFullscreen
            })
        }
    }, [_isFullscreen])

    return <></>;
}

FefferyFullscreen.propTypes = {
    /**
     * 组件唯一id
     */
    id: PropTypes.string,

    /**
     * 对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果
     */
    key: PropTypes.string,

    /**
     * 设置要全屏化的目标元素id，缺省时会以整个页面作为全屏化目标
     */
    targetId: PropTypes.string,

    /**
     * 设置或监听目标元素的全屏化状态
     * 默认值：`false`
     */
    isFullscreen: PropTypes.bool,

    /**
     * 配置是否启用页面全屏，可进一步设置页面全屏根元素对应的css类名及`z-index`值
     * 默认值：`false`
     */
    pageFullscreen: PropTypes.oneOfType([
        PropTypes.bool,
        PropTypes.exact({
            /**
             * 设置页面全屏根元素对应的css类名
             */
            className: PropTypes.string,
            /**
             * 设置页面全屏根元素对应的`z-index`值
             */
            zIndex: PropTypes.number
        })
    ]),

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
    isFullscreen: false,
    pageFullscreen: false
}

export default FefferyFullscreen;