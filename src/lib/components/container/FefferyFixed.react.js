// react核心
import PropTypes from 'prop-types';
// 辅助库
import { isString } from 'lodash';
import { useWindowSize } from '@reactuses/core';
import { useLoading } from '../utils';
// 自定义hooks
import useCss from '../../hooks/useCss';

/**
 * 固定布局组件FefferyFixed
 */
const FefferyFixed = ({
    id,
    style,
    className,
    children,
    mode,
    followImageWidth,
    followImageHeight,
    followImageContainerPosition,
    followImageContainerSize,
    setProps
}) => {

    // 视口尺寸监听
    const { width: windowWidth, height: windowHeight } = useWindowSize();

    if (mode === 'follow-image') {
        // 计算最新的图片实际像素宽度、像素高度
        let followImageWidthExact;
        let followImageHeightExact;
        if ((windowHeight / windowWidth) <= (followImageHeight / followImageWidth)) {
            followImageWidthExact = windowHeight * (followImageWidth / followImageHeight);
            followImageHeightExact = windowHeight;
        } else {
            followImageWidthExact = windowWidth;
            followImageHeightExact = windowWidth * (followImageHeight / followImageWidth);
        }

        // 根据实际情况计算当前固定容器的像素位置、像素尺寸信息
        return (
            <div id={id}
                style={{
                    ...style,
                    position: 'fixed',
                    ...(
                        (windowHeight / windowWidth) <= (followImageHeight / followImageWidth) ?
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
                data-dash-is-loading={useLoading()}>{children}</div>
        );
    }
    return <></>;
}

FefferyFixed.propTypes = {
    /**
     * 组件唯一id
     */
    id: PropTypes.string,

    /**
     * 对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果
     */
    key: PropTypes.string,

    /**
     * 组件型，内嵌元素
     */
    children: PropTypes.node,

    /**
     * 当前组件css样式
     */
    style: PropTypes.object,

    /**
     * 当前组件css类名
     */
    className: PropTypes.oneOfType([
        PropTypes.string,
        PropTypes.object
    ]),

    /**
     * 必填，设置固定布局模式，可选的有`'follow-image'`（跟随对应`css`属性`object-fit`为`contain`的全屏图片）
     */
    mode: PropTypes.oneOf(['follow-image']).isRequired,

    /**
     * 当`mode='follow-image'`时，设置跟随目标图片原始像素宽度
     */
    followImageWidth: PropTypes.number,

    /**
     * 当`mode='follow-image'`时，设置跟随目标图片原始像素高度
     */
    followImageHeight: PropTypes.number,

    /**
     * 当`mode='follow-image'`时，以目标图片左上角为原点，当前容器的左上角比例坐标，格式如`[x_ratio, y_ratio]`
     */
    followImageContainerPosition: PropTypes.arrayOf(PropTypes.number),

    /**
     * 当`mode='follow-image'`时，当前容器宽度、高度分别占目标图片对应宽度、高度的比例，格式如`[width_ratio, height_ratio]`
     */
    followImageContainerSize: PropTypes.arrayOf(PropTypes.number),

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
};

export default FefferyFixed;