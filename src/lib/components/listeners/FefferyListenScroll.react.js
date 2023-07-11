import { useEffect } from 'react';
import { useScroll } from 'ahooks';
import PropTypes from 'prop-types';

// 定义滚动条监听组件FefferyListenScroll
const FefferyListenScroll = (props) => {

    let {
        id,
        target,
        setProps,
        loading_state
    } = props;

    const position_ = useScroll(target ? document.getElementById(target) : document)

    useEffect(() => {
        if (position_) {
            setProps({
                position: position_
            })
        }
    }, [position_])

    return <></>;
}

// 定义参数或属性
FefferyListenScroll.propTypes = {
    // 部件id
    id: PropTypes.string,

    // 设置滚动条监听目标元素id，默认为整个页面
    target: PropTypes.string,

    // 监听目标滚动条的水平及竖直方向上的像素偏移量
    position: PropTypes.object,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,

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
    })
};

// 设置默认参数
FefferyListenScroll.defaultProps = {
}

export default FefferyListenScroll;