import PropTypes from 'prop-types';
import useCss from '../../hooks/useCss';
import { useWindowSize } from '@reactuses/core';

// 定义固定布局组件FefferyFixed
const FefferyFixed = (props) => {
    // 取得必要属性或参数
    const {
        id,
        key,
        style,
        className,
        children,
        mode,
        followImageWidth,
        followImageHeight,
        followImageContainerPosition,
        followImageContainerSize,
        setProps,
        loading_state
    } = props;

    // 视口尺寸监听
    const { width: windowWidth, height: windowHeight } = useWindowSize();

    if (mode === 'follow-image') {
        // 计算最新的图片实际像素宽度、像素高度
        let followImageWidthExact;
        let followImageHeightExact;
        if (windowWidth >= windowHeight) {
            followImageWidthExact = windowHeight * (followImageWidth / followImageHeight);
            followImageHeightExact = windowHeight;
        } else {
            followImageWidthExact = windowWidth;
            followImageHeightExact = windowWidth * (followImageHeight / followImageWidth);
        }

        // 根据实际情况计算当前固定容器的像素位置、像素尺寸信息
        return (
            <div id={id}
                key={key}
                style={{
                    ...style,
                    position: 'fixed',
                    ...(
                        windowWidth >= windowHeight ?
                            {
                                left: 0.5 * windowWidth - 0.5 * followImageWidthExact + followImageContainerPosition[0] * followImageWidthExact,
                                top: followImageContainerPosition[1] * followImageHeightExact,
                                width: followImageWidthExact * followImageContainerSize[0],
                                height: followImageHeightExact * followImageContainerSize[1]
                            } :
                            {
                                left: followImageContainerPosition[0] * followImageWidthExact,
                                top: 0.5 * windowHeight - 0.5 * followImageHeightExact + followImageContainerPosition[1] * followImageHeightExact,
                                width: followImageWidthExact * followImageContainerSize[0],
                                height: followImageHeightExact * followImageContainerSize[1]
                            }
                    )
                }}
                className={
                    isString(className) ?
                        className :
                        (className ? useCss(className) : undefined)
                }
                data-dash-is-loading={
                    (loading_state && loading_state.is_loading) || undefined
                }>{children}</div>
        );
    }
    return <></>;
}


// 定义参数或属性
FefferyFixed.propTypes = {
    /**
     * 组件id
     */
    id: PropTypes.string,

    /**
     * 强制刷新用
     */
    key: PropTypes.string,

    /**
     * 组件子元素
     */
    children: PropTypes.node,

    /**
     * 自定义css字典
     */
    style: PropTypes.object,

    /**
     * css类名
     */
    className: PropTypes.oneOfType([
        PropTypes.string,
        PropTypes.object
    ]),

    /**
     * 必填，用于设置固定布局模式，可选的有'follow-image'（跟随object-fit为contain的全屏图片）
     */
    mode: PropTypes.oneOf(['follow-image']).isRequired,

    // mode='follow-image'时的参数
    /**
     * 跟随目标图片原始像素宽度
     */
    followImageWidth: PropTypes.number,

    /**
     * 跟随目标图片原始像素高度
     */
    followImageHeight: PropTypes.number,

    /**
     * 以目标图片左上角为原点下，当前容器的左上角比例坐标，格式：(x_ratio, y_ratio)
     */
    followImageContainerPosition: PropTypes.arrayOf(PropTypes.number),

    /**
     * 当前容器宽度、高度分别占目标图片对应宽度、高度的比例，格式：(width_ratio, height_ratio)
     */
    followImageContainerSize: PropTypes.arrayOf(PropTypes.number),

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
FefferyFixed.defaultProps = {
}

export default FefferyFixed;