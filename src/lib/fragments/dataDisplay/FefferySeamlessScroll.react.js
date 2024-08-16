import React, { useState, useMemo, useEffect, useRef } from 'react';
import copyObj from 'comutils/copyObj';
import { propTypes, defaultProps } from '../../components/dataDisplay/FefferySeamlessScroll.react';

require('comutils/animationFrame')();

const useDidUpdateEffect = (fn, inputs) => {
    const didMountRef = useRef(false);
    useEffect(() => {
        if (didMountRef.current) fn();
        else didMountRef.current = true;
    }, inputs);
};

// 定义无缝滚动组件组件FefferySeamlessScroll
const FefferySeamlessScroll = (props) => {
    const {
        id,
        key,
        leftSwitchChildren,
        rightSwitchChildren,
        children,
        className,
        style,
        data,
        classOption,
        setProps,
        loading_state
    } = props;

    const wrapRef = useRef(null);
    const realBoxRef = useRef(null);
    const slotListRef = useRef(null);
    const xPos = useRef(0);
    const yPos = useRef(0);
    const delay = useRef(0);
    const height = useRef(0);
    const width = useRef(0);
    const realBoxWidth = useRef(0);
    const realBoxHeight = useRef(0);
    const startPos = useRef(null);
    const endPos = useRef(null);
    const startPosX = useRef(null);
    const startPosY = useRef(null);
    const reqFrame = useRef(null);
    const singleWaitTime = useRef(null);
    const isHover = useRef(false);
    const ease = useRef('ease-in');

    const [xPosTrigger, setXPosTrigger] = useState(0);
    const [yPosTrigger, setYPosTrigger] = useState(0);
    const [delayTrigger, setDelayTrigger] = useState(0);
    const [heightTrigger, setHeightTrigger] = useState(0);
    const [widthTrigger, setWidthTrigger] = useState(0);
    const [realBoxWidthTrigger, setRealBoxWidthTrigger] = useState(0);
    const [easeTrigger, setEaseTrigger] = useState(0);

    const [copyHtml, setCopyHtml] = useState('');
    const [leftSwitchState, setLeftSwitchState] = useState(null);
    const [rightSwitchState, setRightSwitchState] = useState(null);
    const [leftSwitch, setLeftSwitch] = useState(null);
    const [rightSwitch, setRightSwitch] = useState(null);
    const [pos, setPos] = useState(null);

    const defaultOption = useMemo(() => {
        return {
            step: 1, //步长
            limitMoveNum: 5, //启动无缝滚动最小数据数
            hoverStop: true, //是否启用鼠标hover控制
            direction: 1, // 0 往下 1 往上 2向左 3向右
            openTouch: true, //开启移动端touch
            singleHeight: 0, //单条数据高度有值hoverStop关闭
            singleWidth: 0, //单条数据宽度有值hoverStop关闭
            waitTime: 1000, //单步停止等待时间
            switchOffset: 30,
            autoPlay: true,
            navigation: false,
            switchSingleStep: 134,
            switchDelay: 400,
            switchDisabledClass: 'disabled',
            isSingleRemUnit: false // singleWidth/singleHeight 是否开启rem度量
        }
    }, [])

    const options = useMemo(() => {
        return copyObj({}, defaultOption, classOption)
    }, [classOption])

    useEffect(() => {
        setLeftSwitchState(() => xPos.current < 0)
    }, [xPosTrigger])

    useEffect(() => {
        setRightSwitchState(() => Math.abs(xPos.current) < (realBoxWidth.current - width.current))
    }, [xPosTrigger, realBoxWidthTrigger, widthTrigger])

    useEffect(() => {
        setLeftSwitch(() => {
            return {
                position: 'absolute',
                margin: `${height.current / 2}px 0 0 -${options.switchOffset}px`,
                transform: 'translate(-100%,-50%)'
            }
        })
    }, [heightTrigger, options.switchOffset])

    useEffect(() => {
        setRightSwitch(() => {
            return {
                position: 'absolute',
                margin: `${height.current / 2}px 0 0 ${width.current + options.switchOffset}px`,
                transform: 'translateY(-50%)'
            }
        })
    }, [heightTrigger, widthTrigger, options.switchOffset])

    const leftSwitchClass = useMemo(() => {
        return leftSwitchState ? '' : options.switchDisabledClass
    }, [leftSwitchState, options.switchDisabledClass])

    const rightSwitchClass = useMemo(() => {
        return rightSwitchState ? '' : options.switchDisabledClass
    }, [rightSwitchState, options.switchDisabledClass])

    const float = useMemo(() => {
        return isHorizontal ? { float: 'left', overflow: 'hidden' } : { overflow: 'hidden' }
    }, [isHorizontal])

    useEffect(() => {
        setPos(() => {
            return {
                transform: `translate(${xPos.current}px,${yPos.current}px)`,
                transition: `all ${ease.current} ${delay.current}ms`,
                overflow: 'hidden'
            }
        })
    }, [xPosTrigger, yPosTrigger, easeTrigger, delayTrigger])

    const navigation = useMemo(() => {
        return options.navigation
    }, [options.navigation])

    const autoPlay = useMemo(() => {
        if (navigation) return false
        return options.autoPlay
    }, [navigation])

    const scrollSwitch = useMemo(() => {
        return data.length >= options.limitMoveNum
    }, [data.length, options.limitMoveNum])

    const hoverStopSwitch = useMemo(() => {
        return options.hoverStop && autoPlay && scrollSwitch
    }, [options.hoverStop, autoPlay, scrollSwitch])

    const canTouchScroll = useMemo(() => {
        return options.openTouch
    }, [options.openTouch])

    const isHorizontal = useMemo(() => {
        return options.direction > 1
    }, [options.direction])

    const baseFontSize = useMemo(() => {
        return options.isSingleRemUnit ? parseInt(window.getComputedStyle(document.documentElement, null).fontSize) : 1
    }, [options.isSingleRemUnit])

    const realSingleStopWidth = useMemo(() => {
        return options.singleWidth * baseFontSize
    }, [options.singleWidth, baseFontSize])

    const realSingleStopHeight = useMemo(() => {
        return options.singleHeight * baseFontSize
    }, [options.singleHeight, baseFontSize])

    const step = useMemo(() => {
        let singleStep
        let step = options.step
        if (isHorizontal) {
            singleStep = realSingleStopWidth
        } else {
            singleStep = realSingleStopHeight
        }
        if (singleStep > 0 && singleStep % step > 0) {
            console.error('如果设置了单步滚动,step需是单步大小的约数,否则无法保证单步滚动结束的位置是否准确。~~~~~')
        }
        return step
    }, [options.step, isHorizontal, realSingleStopWidth, realSingleStopHeight])

    const reset = () => {
        _cancle()
        _initMove()
    }

    const leftSwitchClick = () => {
        if (!leftSwitchState) return
        // 小于单步距离
        if (Math.abs(xPos.current) < options.switchSingleStep) {
            xPos.current = 0;
            setXPosTrigger((t) => t + 1)
            return
        }
        xPos.current += options.switchSingleStep
        setXPosTrigger((t) => t + 1)
    }

    const rightSwitchClick = () => {
        if (!rightSwitchState) return
        // 小于单步距离
        if ((realBoxWidth.current - width.current + xPos.current) < options.switchSingleStep) {
            xPos.current = width.current - realBoxWidth.current
            setXPosTrigger((t) => t + 1)
            return
        }
        xPos.current -= options.switchSingleStep
        setXPosTrigger((t) => t + 1)
    }

    const _cancle = () => {
        cancelAnimationFrame(reqFrame.current || '')
    }

    const touchStart = (e) => {
        if (!canTouchScroll) return
        let timer
        const touch = e.targetTouches[0] //touches数组对象获得屏幕上所有的touch，取第一个touch
        const { waitTime, singleHeight, singleWidth } = options
        startPos.current = {
            x: touch.pageX,
            y: touch.pageY
        } //取第一个touch的坐标值
        startPosY.current = yPos.current //记录touchStart时候的posY
        startPosX.current = xPos.current //记录touchStart时候的posX
        if (!!singleHeight && !!singleWidth) {
            if (timer) clearTimeout(timer)
            timer = setTimeout(() => {
                _cancle()
            }, waitTime + 20)
        } else {
            _cancle()
        }
    }

    const touchMove = (e) => {
        //当屏幕有多个touch或者页面被缩放过，就不执行move操作
        if (!canTouchScroll || e.targetTouches.length > 1 || e.scale && e.scale !== 1) return
        const touch = e.targetTouches[0]
        const { direction } = options
        endPos.current = {
            x: touch.pageX - startPos.current.x,
            y: touch.pageY - startPos.current.y
        }
        event.preventDefault(); //阻止触摸事件的默认行为，即阻止滚屏
        const dir = Math.abs(endPos.current.x) < Math.abs(endPos.current.y) ? 1 : 0 //dir，1表示纵向滑动，0为横向滑动
        if (dir === 1 && direction < 2) {  // 表示纵向滑动 && 运动方向为上下
            yPos.current = startPosY.current + endPos.current.y
            setYPosTrigger((t) => t + 1)
        } else if (dir === 0 && direction > 1) { // 为横向滑动 && 运动方向为左右
            xPos.current = startPosX.current + endPos.current.x
            setXPosTrigger((t) => t + 1)
        }
    }

    const touchEnd = () => {
        if (!canTouchScroll) return
        let timer
        const direction = options.direction
        delay.current = 50
        setDelayTrigger((t) => t + 1)
        if (direction === 1) {
            if (yPos.current > 0) {
                yPos.current = 0
                setYPosTrigger((t) => t + 1)
            }
        } else if (direction === 0) {
            let h = realBoxHeight.current / 2 * -1
            if (yPos.current < h) {
                yPos.current = h
                setYPosTrigger((t) => t + 1)
            }
        } else if (direction === 2) {
            if (xPos.current > 0) {
                xPos.current = 0
                setXPosTrigger((t) => t + 1)
            }
        } else if (direction === 3) {
            let w = realBoxWidth.current * -1
            if (xPos.current < w) {
                xPos.current = w
                setXPosTrigger((t) => t + 1)
            }
        }
        if (timer) clearTimeout(timer)
        timer = setTimeout(() => {
            delay.current = 0
            setDelayTrigger((t) => t + 1)
            _move()
        }, delay.current)
    }

    const enter = () => {
        if (hoverStopSwitch) _stopMove()
    }

    const leave = () => {
        if (hoverStopSwitch) _startMove()
    }

    const scrollEnd = () => { }

    const _move = () => {
        // 鼠标移入时拦截_move()
        if (isHover.current) return
        _cancle() //进入move立即先清除动画 防止频繁touchMove导致多动画同时进行
        reqFrame.current = requestAnimationFrame(
            function () {
                const h = realBoxHeight.current / 2  //实际高度
                const w = realBoxWidth.current / 2 //宽度
                let { direction, waitTime } = options
                if (direction === 1) { // 上
                    if (Math.abs(yPos.current) >= h) {
                        scrollEnd()
                        yPos.current = 0
                        setYPosTrigger((t) => t + 1)
                    }
                    yPos.current -= step
                    setYPosTrigger((t) => t + 1)
                } else if (direction === 0) { // 下
                    if (yPos.current >= 0) {
                        scrollEnd()
                        yPos.current = h * -1
                        setYPosTrigger((t) => t + 1)
                    }
                    yPos.current += step
                    setYPosTrigger((t) => t + 1)
                } else if (direction === 2) { // 左
                    if (Math.abs(xPos.current) >= w) {
                        scrollEnd()
                        xPos.current = 0
                        setXPosTrigger((t) => t + 1)
                    }
                    xPos.current -= step
                    setXPosTrigger((t) => t + 1)
                } else if (direction === 3) { // 右
                    if (xPos.current >= 0) {
                        scrollEnd()
                        xPos.current = w * -1
                        setXPosTrigger((t) => t + 1)
                    }
                    xPos.current += step
                    setXPosTrigger((t) => t + 1)
                }
                if (singleWaitTime.current) clearTimeout(singleWaitTime.current)
                if (!!realSingleStopHeight) { //是否启动了单行暂停配置
                    if (Math.abs(yPos.current) % realSingleStopHeight < step) { // 符合条件暂停waitTime
                        singleWaitTime.current = setTimeout(() => {
                            _move()
                        }, waitTime)
                    } else {
                        _move()
                    }
                } else if (!!realSingleStopWidth) {
                    if (Math.abs(xPos.current) % realSingleStopWidth < step) { // 符合条件暂停waitTime
                        singleWaitTime.current = setTimeout(() => {
                            _move()
                        }, waitTime)
                    } else {
                        _move()
                    }
                } else {
                    _move()
                }
            }.bind(wrapRef.current)
        )
    }

    const _initMove = () => {
        const { switchDelay } = options
        _dataWarm(data)
        setCopyHtml('') //清空copy
        if (isHorizontal) {
            height.current = wrapRef.current.offsetHeight
            setHeightTrigger((t) => t + 1)
            width.current = wrapRef.current.offsetWidth
            setWidthTrigger((t) => t + 1)
            let slotListWidth = slotListRef.current.offsetWidth
            // 水平滚动设置warp width
            if (autoPlay) {
                // 修正offsetWidth四舍五入
                slotListWidth = slotListWidth * 2 + 1
            }
            realBoxRef.current.style.width = slotListWidth + 'px'
            realBoxWidth.current = slotListWidth
            setRealBoxWidthTrigger((t) => t + 1)
        }

        if (autoPlay) {
            ease.current = 'ease-in'
            setEaseTrigger((t) => t + 1)
            delay.current = 0
            setDelayTrigger((t) => t + 1)
        } else {
            ease.current = 'linear'
            setEaseTrigger((t) => t + 1)
            delay.current = switchDelay
            setDelayTrigger((t) => t + 1)
            return
        }

        // 是否可以滚动判断
        if (scrollSwitch) {
            let timer
            if (timer) clearTimeout(timer)
            setCopyHtml(slotListRef.current.innerHTML)
            setTimeout(() => {
                realBoxHeight.current = realBoxRef.current.offsetHeight
                _move()
            }, 0);
        } else {
            _cancle()
            xPos.current = 0
            setXPosTrigger((t) => t + 1)
            yPos.current = 0
            setYPosTrigger((t) => t + 1)
        }
    }

    const _dataWarm = (data) => {
        if (data.length > 100) {
            console.warn(`数据达到了${data.length}条有点多哦~,可能会造成部分老旧浏览器卡顿。`);
        }
    }

    const _startMove = () => {
        isHover.current = false //开启_move
        _move()
    }

    const _stopMove = () => {
        isHover.current = true //关闭_move
        // 防止频频hover进出单步滚动,导致定时器乱掉
        if (singleWaitTime.current) clearTimeout(singleWaitTime.current)
        _cancle()
    }

    useEffect(() => {
        window.addEventListener('scrollend', scrollEnd);
        _initMove()

        return () => {
            window.removeEventListener('scrollend', scrollEnd);
            _cancle()
            clearTimeout(singleWaitTime.current)
        }
    }, [])

    useDidUpdateEffect(() => {
        _dataWarm(data)
        reset()
    }, [data])

    useDidUpdateEffect(() => {
        if (autoPlay) {
            reset()
        } else {
            _stopMove()
        }
    }, [autoPlay])

    return (
        <div
            id={id}
            key={key}
            className={className}
            style={style}
            ref={wrapRef}
        >
            {navigation && (
                <div
                    style={leftSwitch}
                    class={leftSwitchClass}
                    onClick={leftSwitchClick}
                >
                    {leftSwitchChildren}
                </div>
            )}
            {navigation && (
                <div
                    style={rightSwitch}
                    class={rightSwitchClass}
                    onClick={rightSwitchClick}
                >
                    {rightSwitchChildren}
                </div>
            )}
            <div
                ref={realBoxRef}
                style={pos}
                onMouseEnter={enter}
                onMouseLeave={leave}
                onTouchStart={touchStart}
                onTouchMove={touchMove}
                onTouchEnd={touchEnd}
            >
                <div ref={slotListRef} style={float}>
                    {children}
                </div>
                <div dangerouslySetInnerHTML={{ __html: copyHtml }} style={float}></div>
            </div>
        </div>
    );
}

export default FefferySeamlessScroll;

FefferySeamlessScroll.defaultProps = defaultProps;
FefferySeamlessScroll.propTypes = propTypes;