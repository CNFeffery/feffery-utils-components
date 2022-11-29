import React, { useState, useEffect, useRef } from 'react';
import PropTypes from 'prop-types';
import NProgress from 'nprogress';
import FefferyStyle from './FefferyStyle.react';
// import './nprogress.css';


const parseChildrenToArray = children => {
  if (children && !Array.isArray(children)) {
    return [children];
  }
  return children;
};

// 定义顶部加载进度条组件FefferyTopProgress，api参数参考https://github.com/rstacruz/nprogress
const FefferyTopProgress = (props) => {
  // 取得必要属性或参数
  let {
    id,
    className,
    style,
    children,
    minimum,
    easing,
    speed,
    showSpinner,
    spinning,
    listenPropsMode,
    excludeProps,
    includeProps,
    debug,
    color,
    zIndex,
    setProps,
    loading_state
  } = props;

  // 配置NProgress参数信息
  NProgress.configure({
    minimum,
    easing,
    speed,
    showSpinner
  })

  children = parseChildrenToArray(children)

  const [showSpinning, setShowSpinning] = useState(spinning);
  const timer = useRef();

  useEffect(() => {
    if (loading_state) {
      if (timer.current) {
        clearTimeout(timer.current);
      }
      if (loading_state.is_loading && !showSpinning) {
        // 当listenPropsMode为'default'时
        if (listenPropsMode === 'default') {
          if (debug) {
            console.log(loading_state.component_name + '.' + loading_state.prop_name)
          }
          setShowSpinning(true);
          NProgress.start();
        } else if (listenPropsMode === 'exclude') {
          // 当listenPropsMode为'exclude'模式时
          // 当前触发loading_state的组件+属性组合不在排除列表中时，激活动画
          if (excludeProps.indexOf(loading_state.component_name + '.' + loading_state.prop_name) === -1) {
            if (debug) {
              console.log(loading_state.component_name + '.' + loading_state.prop_name)
            }
            setShowSpinning(true);
            NProgress.start();
          }
        } else if (listenPropsMode === 'include') {
          // 当listenPropsMode为'include'模式时
          // 当前触发loading_state的组件+属性组合在包含列表中时，激活动画
          if (includeProps.indexOf(loading_state.component_name + '.' + loading_state.prop_name) !== -1) {
            if (debug) {
              console.log(loading_state.component_name + '.' + loading_state.prop_name)
            }
            setShowSpinning(true);
            NProgress.start();
          }
        }

      } else if (!loading_state.is_loading && showSpinning) {
        timer.current = setTimeout(() => {
          setShowSpinning(false);
          NProgress.done();
        });
      }
    }
  }, [loading_state]);

  // 返回定制化的前端组件
  return (<div id={id}
    className={className}
    style={style}
    data-dash-is-loading={
      (loading_state && loading_state.is_loading) || undefined
    } >
    <FefferyStyle
      rawStyle={
        `
#nprogress {
  pointer-events: none;
}

#nprogress .bar {
  background: ${color};

  position: fixed;
  z-index: ${zIndex};
  top: 0;
  left: 0;

  width: 100%;
  height: 2px;
}

/* Fancy blur effect */
#nprogress .peg {
  display: block;
  position: absolute;
  right: 0px;
  width: 100px;
  height: 100%;
  box-shadow: 0 0 10px ${color}, 0 0 5px ${color};
  opacity: 1.0;

  -webkit-transform: rotate(3deg) translate(0px, -4px);
  -ms-transform: rotate(3deg) translate(0px, -4px);
  transform: rotate(3deg) translate(0px, -4px);
}

/* Remove these to get rid of the spinner */
#nprogress .spinner {
  display: block;
  position: fixed;
  z-index: ${zIndex};
  top: 15px;
  right: 15px;
}

#nprogress .spinner-icon {
  width: 18px;
  height: 18px;
  box-sizing: border-box;

  border: solid 2px transparent;
  border-top-color: ${color};
  border-left-color: ${color};
  border-radius: 50%;

  -webkit-animation: nprogress-spinner 400ms linear infinite;
  animation: nprogress-spinner 400ms linear infinite;
}

.nprogress-custom-parent {
  overflow: hidden;
  position: relative;
}

.nprogress-custom-parent #nprogress .spinner,
.nprogress-custom-parent #nprogress .bar {
  position: absolute;
}

@-webkit-keyframes nprogress-spinner {
  0% {
    -webkit-transform: rotate(0deg);
  }

  100% {
    -webkit-transform: rotate(360deg);
  }
}

@keyframes nprogress-spinner {
  0% {
    transform: rotate(0deg);
  }

  100% {
    transform: rotate(360deg);
  }
}
`
      }
    />
    {children}
  </div>
  );
}

FefferyTopProgress._dashprivate_isLoadingComponent = true;

// 定义参数或属性
FefferyTopProgress.propTypes = {
  // 组件id
  id: PropTypes.string,

  /**
   * The content of the tab - will only be displayed if this tab is selected
   */
  children: PropTypes.node,

  // css类名
  className: PropTypes.string,

  // 自定义css字典
  style: PropTypes.object,

  // 设置是否处于加载中状态
  spinning: PropTypes.bool,

  // 设置顶端进度条的初始进度值，默认为0.33，取值在0到1之间
  minimum: PropTypes.number,

  // 用于设置同名css动画效果，默认为'ease'
  easing: PropTypes.string,

  // 设置进度条每步递增耗时（单位：毫秒），默认为200
  speed: PropTypes.number,

  // 设置是否渲染右上角圆圈加载动画，默认为true
  showSpinner: PropTypes.bool,

  // 设置是否开启debug模式，开启后，每次动画加载都会在开发者工具的控制台打印prop信息
  debug: PropTypes.bool,

  // 设置自定义监听组件的模式，可选的有'default'、'exclude'、'include'，默认为'default'
  listenPropsMode: PropTypes.oneOf(['default', 'exclude', 'include']),

  // 设置需要忽略输出监听过程的组件信息列表
  // 仅在listenPropsMode为'exclude'时生效
  excludeProps: PropTypes.arrayOf(PropTypes.string),

  // 设置需要包含输出监听过程的组件信息列表
  // 仅在listenPropsMode为'include'时生效
  includeProps: PropTypes.arrayOf(PropTypes.string),

  // 设置顶部进度条色彩，默认为'#29d'
  color: PropTypes.string,

  // 设置顶部进度条的z-index，默认为99999
  zIndex: PropTypes.number,

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
FefferyTopProgress.defaultProps = {
  spinning: false,
  listenPropsMode: 'default',
  excludeProps: [],
  includeProps: [],
  debug: false,
  color: '#29d',
  zIndex: 99999
}

export default FefferyTopProgress;