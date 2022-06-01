import React, { Component } from 'react';
import Split from 'react-split'
import { isNil, omit } from 'ramda';
import '../styles.css'

const parseChildrenToArray = children => {
    if (children && !Array.isArray(children)) {
        return [children];
    }
    return children;
};


const resolveChildProps = child => {
    // This may need to change in the future if https://github.com/plotly/dash-renderer/issues/84 is addressed
    if (
        // disabled is a defaultProp (so it's always set)
        // meaning that if it's not set on child.props, the actual
        // props we want are lying a bit deeper - which means they
        // are coming from Dash
        isNil(child.props.disabled) &&
        child.props._dashprivate_layout &&
        child.props._dashprivate_layout.props
    ) {
        // props are coming from Dash
        return child.props._dashprivate_layout.props;
    } else {
        // else props are coming from React (e.g. Demo.js, or Tabs.test.js)
        return child.props;
    }
};

// 定义分割面板组件FefferySplit，api参数参考https://github.com/nathancahill/split/tree/master/packages/splitjs
export default class FefferySplit extends Component {

    render() {
        // 取得必要属性或参数
        let {
            children,
            id,
            className,
            style,
            sizes,
            minSize,
            maxSize,
            expandToMin,
            gutterSize,
            dragInterval,
            direction,
            cursor,
            setProps,
            loading_state
        } = this.props;

        children = parseChildrenToArray(children)

        // const splitPanes = children.map(
        //     (child) => {
        //         let childProps = resolveChildProps(child)

        //         const {
        //             id,
        //             className,
        //             style,
        //             loading_state,
        //             ...otherProps
        //         } = childProps;

        //         return (
        //             <div
        //                 id={id}
        //                 className={className}
        //                 style={style}
        //                 loading_state={loading_state}
        //                 {...omit(
        //                     ['setProps', 'persistence', 'persistence_type', 'persisted_props'],
        //                     otherProps
        //                 )}>
        //             </div>
        //         );
        //     }
        // )

        // 返回向页面注入的快捷键监听
        return (
            <Split id={id}
                className={className ? `feffery-split-${direction}` + ' ' + className : `feffery-split-${direction}`}
                style={style}
                sizes={sizes}
                minSize={minSize}
                maxSize={maxSize}
                expandToMin={expandToMin}
                gutterSize={gutterSize}
                snapOffset={1}
                dragInterval={dragInterval}
                direction={direction}
                cursor={cursor}
                onDragEnd={(e) => {
                    setProps({ sizes: e })
                }}
                data-dash-is-loading={
                    (loading_state && loading_state.is_loading) || undefined
                }
            >
                {children}
            </Split>
        );
    }
}

// 定义参数或属性
FefferySplit.propTypes = {

    children: PropTypes.node,

    // 部件id
    id: PropTypes.string,

    // css类名
    className: PropTypes.string,

    // 自定义css字典
    style: PropTypes.object,

    // 记录当前最新的sizes变动情况，分别为每个子元素盒子设置百分比尺寸
    sizes: PropTypes.arrayOf(PropTypes.number),

    // 设置每个子元素盒子的最小像素尺寸，默认为100
    minSize: PropTypes.oneOfType([
        // 统一设置最小尺寸
        PropTypes.number,
        // 逐一设置最小尺寸
        PropTypes.arrayOf(PropTypes.number)
    ]),

    // 设置每个子元素盒子的最大像素尺寸，默认为Infinity即无限制
    maxSize: PropTypes.oneOfType([
        // 统一设置最大尺寸
        PropTypes.number,
        // 逐一设置最大尺寸
        PropTypes.arrayOf(PropTypes.number)
    ]),

    // 设置当有子元素盒子的初始宽度小于设定的minSize时，是否自动调整到minSize，默认为false
    expandToMin: PropTypes.bool,

    // 设置间隙像素尺寸，默认为10
    gutterSize: PropTypes.number,

    // 设置拖拽行为的像素移动步长，默认为1
    dragInterval: PropTypes.number,

    // 设置分割方向，可选的有'horizontal'、'vertical'
    direction: PropTypes.oneOf(['horizontal', 'vertical']),

    // 设置拖拽分隔条时的鼠标指针，当direction='horizontal'时默认为'col-resize'
    // 当direction='vertical'时默认为'row-resize'
    cursor: PropTypes.string,

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
    setProps: PropTypes.func
};

// 设置默认参数
FefferySplit.defaultProps = {
    direction: 'horizontal'
}