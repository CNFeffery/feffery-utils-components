// react核心
import React from 'react';
// 组件核心
import Tilt from 'react-parallax-tilt';
// 辅助库
import useCss from '../../hooks/useCss'
import { isString } from 'lodash';
import { useLoading } from '../utils';
// 参数类型
import PropTypes from 'prop-types';

/**
 * 倾斜悬浮组件FefferyTiltHover
 */
const FefferyTiltHover = ({
    id,
    children,
    className,
    style,
    key,
    listenMove,
    listenEnter,
    listenLeave,
    tiltEnable = true,
    tiltReverse = false,
    tiltAngleXInitial = 0,
    tiltAngleYInitial = 0,
    tiltMaxAngleX = 20,
    tiltMaxAngleY = 20,
    tiltAxis = undefined,
    tiltAngleXManual = null,
    tiltAngleYManual = null,
    glareEnable = false,
    glareMaxOpacity = 0.7,
    glareColor = '#ffffff',
    glareBorderRadius = '0',
    glarePosition = 'bottom',
    glareReverse = false,
    scale = 1,
    perspective = 1000,
    flipVertically = false,
    flipHorizontally = false,
    reset = true,
    transitionEasing = 'cubic-bezier(.03,.98,.52,.99)',
    transitionSpeed = 400,
    trackOnWindow = false,
    gyroscope = false,
    setProps
}) => {

    const onMove = ({ tiltAngleX, tiltAngleY, tiltAngleXPercentage, tiltAngleYPercentage, glareAngle, glareOpacity, eventType }) => {
        setProps({ listenMove: { tiltAngleX: tiltAngleX, tiltAngleY: tiltAngleY, tiltAngleXPercentage: tiltAngleXPercentage, tiltAngleYPercentage: tiltAngleYPercentage, glareAngle: glareAngle, glareOpacity: glareOpacity, eventType: eventType } })
    }

    const onEnter = (eventType) => {
        setProps({ listenEnter: { eventType: eventType } })
    }

    const onLeave = (eventType) => {
        setProps({ listenLeave: { eventType: eventType } })
    }

    return (
        <Tilt
            id={id}
            className={
                isString(className) ?
                    className :
                    (className ? useCss(className) : undefined)
            }
            style={style}
            key={key}
            tiltEnable={tiltEnable}
            tiltReverse={tiltReverse}
            tiltAngleXInitial={tiltAngleXInitial}
            tiltAngleYInitial={tiltAngleYInitial}
            tiltMaxAngleX={tiltMaxAngleX}
            tiltMaxAngleY={tiltMaxAngleY}
            tiltAxis={tiltAxis}
            tiltAngleXManual={tiltAngleXManual}
            tiltAngleYManual={tiltAngleYManual}
            glareEnable={glareEnable}
            glareMaxOpacity={glareMaxOpacity}
            glareColor={glareColor}
            glareBorderRadius={glareBorderRadius}
            glarePosition={glarePosition}
            glareReverse={glareReverse}
            scale={scale}
            perspective={perspective}
            flipVertically={flipVertically}
            flipHorizontally={flipHorizontally}
            reset={reset}
            transitionEasing={transitionEasing}
            transitionSpeed={transitionSpeed}
            trackOnWindow={trackOnWindow}
            gyroscope={gyroscope}
            onMove={onMove}
            onEnter={onEnter}
            onLeave={onLeave}
            data-dash-is-loading={useLoading()} >
            {children}
        </Tilt>
    );
}

FefferyTiltHover.propTypes = {
    /**
     * 组件唯一id
     */
    id: PropTypes.string,

    /**
     * 对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果
     */
    key: PropTypes.string,

    /**
     * 组件型，要进行倾斜悬浮效果编排的目标元素
     */
    children: PropTypes.node,

    /**
     * 当前组件css样式
     */
    style: PropTypes.object,

    /**
     * 当前组件css类名，支持[动态css](/advanced-classname)
     */
    className: PropTypes.oneOfType([
        PropTypes.string,
        PropTypes.object
    ]),

    /**
     * 设置是否启用倾斜效果
     * 默认为`true`
     */
    tiltEnable: PropTypes.bool,

    /**
     * 设置是否反转倾斜方向
     * 默认为`false`
     */
    tiltReverse: PropTypes.bool,

    /**
     * 设置x轴上的初始倾斜值（度）
     * 默认为`0`
     */
    tiltAngleXInitial: PropTypes.number,

    /**
     * 设置y轴上的初始倾斜值（度）
     * 默认为`0`
     */
    tiltAngleYInitial: PropTypes.number,

    /**
     * 设置x轴上的的最大倾斜旋转（度），范围为`0`到`90`
     * 默认为`20`
     */
    tiltMaxAngleX: PropTypes.number,

    /**
     * 设置y轴上的最大倾斜旋转（度），范围为`0`到`90`
     * 默认为`20`
     */
    tiltMaxAngleY: PropTypes.number,

    /**
     * 启用单轴倾斜，可选值为`'x'`或`'y'`
     */
    tiltAxis: PropTypes.oneOf(['x', 'y']),

    /**
     * 设置在x轴上手动倾斜旋转（度）
     */
    tiltAngleXManual: PropTypes.number,

    /**
     * 设置在y轴上手动倾斜旋转（度）
     */
    tiltAngleYManual: PropTypes.number,

    /**
     * 设置是否启用眩光效果
     * 默认为`false`
     */
    glareEnable: PropTypes.bool,

    /**
     * 设置最大眩光不透明度，范围`0`到`1`
     * 默认为`0.7`
     */
    glareMaxOpacity: PropTypes.number,

    /**
     * 设置眩光效果的颜色
     * 默认为`'#ffffff'`
     */
    glareColor: PropTypes.string,

    /**
     * 设置眩光效果的边框半径，接受任何标准的`CSS`边框半径。如果眩光颜色与页面颜色不同，则很有用
     * 默认为`'0'`
     */
    glareBorderRadius: PropTypes.string,

    /**
     * 设置眩光效果的位置，可选的值为`'top'`、`'right'`、`'bottom'`、`'left'`、`'all'`
     * 默认为`'bottom'`
     */
    glarePosition: PropTypes.oneOf(['top', 'right', 'bottom', 'left', 'all']),

    /**
     * 设置是否反转眩光方向
     * 默认为`false`
     */
    glareReverse: PropTypes.bool,

    /**
     * 设置组件的比例（`1.5 = 150%`，`2 = 200%`，等）
     * 默认为`1`
     */
    scale: PropTypes.number,

    /**
     * 定义对象（包装/子组件）与用户的距离。越低，倾斜度越大
     * 默认为`1000`
     */
    perspective: PropTypes.number,

    /**
     * 设置是否启用组件的垂直翻转
     * 默认为`false`
     */
    flipVertically: PropTypes.bool,

    /**
     * 设置是否启用组件的水平翻转
     * 默认为`false`
     */
    flipHorizontally: PropTypes.bool,

    /**
     * 设置是否必须在事件中重置效果
     * 默认为`true`
     */
    reset: PropTypes.bool,

    /**
     * 设置在操作组件时过渡效果
     * 默认为`'cubic-bezier(.03,.98,.52,.99)'`
     */
    transitionEasing: PropTypes.string,

    /**
     * 设置在操作组件时的过渡速度
     * 默认为`400`
     */
    transitionSpeed: PropTypes.number,

    /**
     * 设置是否跟踪整个窗口上的鼠标和触摸事件
     * 默认为`false`
     */
    trackOnWindow: PropTypes.bool,

    /**
     * 设置是否启用设备方向检测
     * 默认为`false`
     */
    gyroscope: PropTypes.bool,

    /**
     * 监听用户在组件上移动时触发的事件数据
     */
    listenMove: PropTypes.object,

    /**
     * 监听用户进入组件时触发的事件数据
     */
    listenEnter: PropTypes.object,

    /**
     * 监听用户离开组件时触发的事件数据
     */
    listenLeave: PropTypes.object,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
};

export default FefferyTiltHover;