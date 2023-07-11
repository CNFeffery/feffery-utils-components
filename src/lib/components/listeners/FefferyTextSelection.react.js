import React, { useEffect } from 'react';
import { useTextSelection } from 'ahooks';
import PropTypes from 'prop-types';

// 定义文字选中监听组件FefferyTextSelection
const FefferyTextSelection = (props) => {

    const {
        targetId,
        setProps
    } = props;

    const selection = useTextSelection(document.getElementById(targetId));

    useEffect(() => {
        if (selection?.text) {
            setProps({
                selectedTextInfo: {
                    timestamp: Date.now(),
                    ...selection
                }
            })
        }
    }, [selection])

    return <></>;
}

// 定义参数或属性
FefferyTextSelection.propTypes = {
    // 部件id
    id: PropTypes.string,

    // 设置目标监听容器的id
    targetId: PropTypes.string,

    // 用于监听最近一次目标容器内文本选中事件相关信息
    selectedTextInfo: PropTypes.object,

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
FefferyTextSelection.defaultProps = {
}

export default React.memo(FefferyTextSelection);