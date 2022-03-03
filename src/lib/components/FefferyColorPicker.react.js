import { Component } from 'react';
import { SketchPicker } from 'react-color';


// 定义取色组件FefferyColorPicker
export default class FefferyColorPicker extends Component {
    render() {
        // 取得必要属性或参数
        const {
            id,
            className,
            style,
            type,
            color,
            setProps,
            loading_state
        } = this.props;

        console.log({ color })

        if (type === 'sketch') {
            return (<SketchPicker id={id}
                className={className}
                style={style}
                color={color}
                // onChange={(c, event) => console.log({ c, event })}
                onChangeComplete={(c, event) => {
                    console.log({ c })
                    setProps({
                        color: c.rgb
                    })
                }}
                data-dash-is-loading={
                    (loading_state && loading_state.is_loading) || undefined
                } />);
        }


    }

}
// 定义参数或属性
FefferyColorPicker.propTypes = {
    // 部件id
    id: PropTypes.string,

    // css类名
    className: PropTypes.string,

    // 自定义css字典
    style: PropTypes.object,

    // 设置取色器类型
    type: PropTypes.oneOf([
        'sketch',
        'chrome',
        'block',
        'github',
        'hue',
        'alpha',
        'twitter',
        'circle',
        'slider',
        'compact',
        'swatches'
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
    })
};

// 设置默认参数
FefferyColorPicker.defaultProps = {
    type: 'sketch'
}