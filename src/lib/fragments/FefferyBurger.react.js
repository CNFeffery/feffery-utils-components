import Hamburger, {
    Squash,
    Cross,
    Twirl,
    Fade,
    Slant,
    Spiral,
    Divide,
    Turn,
    Pivot,
    Sling,
    Squeeze,
    Spin,
    Rotate
} from 'hamburger-react';
import { propTypes, defaultProps } from '../components/FefferyBurger.react';

/**
 * 动态菜单图标组件FefferyBurger
 */
const FefferyBurger = (props) => {
    let {
        id,
        className,
        style,
        type,
        toggled,
        size,
        direction,
        duration,
        distance,
        color,
        rounded,
        setProps,
        loading_state
    } = props;

    // 构建参数
    let config = {
        id,
        className,
        style,
        toggled,
        toggle: (e) => setProps({ toggled: e }),
        size,
        direction,
        duration,
        distance,
        color,
        rounded
    }

    switch (type) {
        case 'default':
            return <Hamburger {...config} />;
        case 'squash':
            return <Squash {...config} />;
        case 'cross':
            return <Cross {...config} />;
        case 'twirl':
            return <Twirl {...config} />;
        case 'fade':
            return <Fade {...config} />;
        case 'slant':
            return <Slant {...config} />;
        case 'spiral':
            return <Spiral {...config} />;
        case 'divide':
            return <Divide {...config} />;
        case 'turn':
            return <Turn {...config} />;
        case 'pivot':
            return <Pivot {...config} />;
        case 'sling':
            return <Sling {...config} />;
        case 'squeeze':
            return <Squeeze {...config} />;
        case 'spin':
            return <Spin {...config} />;
        case 'rotate':
            return <Rotate {...config} />;
        default:
            return <></>;
    }
}

export default FefferyBurger;

FefferyBurger.defaultProps = defaultProps;
FefferyBurger.propTypes = propTypes;