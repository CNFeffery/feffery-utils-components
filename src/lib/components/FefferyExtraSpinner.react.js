import {
    BallSpinner,
    SwapSpinner,
    BarsSpinner,
    GridSpinner,
    WaveSpinner,
    PushSpinner,
    FireworkSpinner,
    StageSpinner,
    RingSpinner,
    HeartSpinner,
    GuardSpinner,
    RotateSpinner,
    SpiralSpinner,
    PulseSpinner,
    SwishSpinner,
    SequenceSpinner,
    ImpulseSpinner,
    CubeSpinner,
    MagicSpinner,
    FlagSpinner,
    FillSpinner,
    SphereSpinner,
    DominoSpinner,
    GooSpinner,
    CombSpinner,
    PongSpinner,
    RainbowSpinner,
    HoopSpinner,
    FlapperSpinner,
    JellyfishSpinner,
    TraceSpinner,
    ClassicSpinner,
    WhisperSpinner,
    MetroSpinner
} from "react-spinners-kit";
import PropTypes from 'prop-types';


// 定义额外加载动画组件FefferyExtraSpinner，api参考https://github.com/dmitrymorozoff/react-spinners-kit
// 取得必要属性或参数
const FefferyExtraSpinner = (props) => {
    // 取得必要属性或参数
    const {
        id,
        style,
        className,
        type,
        size,
        color,
        frontColor,
        backColor,
        loading_state
    } = props;

    let spinner;

    if (type === 'ball') {
        spinner = <BallSpinner
            size={size || 40}
            color={color}
            frontColor={frontColor}
            backColor={backColor}
        />;
    } else if (type === 'swap') {
        spinner = <SwapSpinner
            size={size || 40}
            color={color}
            frontColor={frontColor}
            backColor={backColor}
        />;
    } else if (type === 'bars') {
        spinner = <BarsSpinner
            size={size || 40}
            color={color}
            frontColor={frontColor}
            backColor={backColor}
        />;
    } else if (type === 'grid') {
        spinner = <GridSpinner
            size={size || 40}
            color={color}
            frontColor={frontColor}
            backColor={backColor}
        />;
    } else if (type === 'wave') {
        spinner = <WaveSpinner
            size={size || 40}
            color={color}
            frontColor={frontColor}
            backColor={backColor}
        />;
    } else if (type === 'push') {
        spinner = <PushSpinner
            size={size || 40}
            color={color}
            frontColor={frontColor}
            backColor={backColor}
        />;
    } else if (type === 'firework') {
        spinner = <FireworkSpinner
            size={size || 40}
            color={color}
            frontColor={frontColor}
            backColor={backColor}
        />;
    } else if (type === 'stage') {
        spinner = <StageSpinner
            size={size || 40}
            color={color}
            frontColor={frontColor}
            backColor={backColor}
        />;
    } else if (type === 'ring') {
        spinner = <RingSpinner
            size={size || 40}
            color={color}
            frontColor={frontColor}
            backColor={backColor}
        />;
    } else if (type === 'heart') {
        spinner = <HeartSpinner
            size={size || 40}
            color={color}
            frontColor={frontColor}
            backColor={backColor}
        />;
    } else if (type === 'guard') {
        spinner = <GuardSpinner
            size={size || 40}
            color={color}
            frontColor={frontColor}
            backColor={backColor}
        />;
    } else if (type === 'rotate') {
        spinner = <RotateSpinner
            size={size || 40}
            color={color}
            frontColor={frontColor}
            backColor={backColor}
        />;
    } else if (type === 'spiral') {
        spinner = <SpiralSpinner
            size={size || 40}
            color={color}
            frontColor={frontColor}
            backColor={backColor}
        />;
    } else if (type === 'pulse') {
        spinner = <PulseSpinner
            size={size || 40}
            color={color}
            frontColor={frontColor}
            backColor={backColor}
        />;
    } else if (type === 'swish') {
        spinner = <SwishSpinner
            size={size || 40}
            color={color}
            frontColor={frontColor}
            backColor={backColor}
        />;
    } else if (type === 'sequence') {
        spinner = <SequenceSpinner
            size={size || 40}
            color={color}
            frontColor={frontColor}
            backColor={backColor}
        />;
    } else if (type === 'impulse') {
        spinner = <ImpulseSpinner
            size={size || 40}
            color={color}
            frontColor={frontColor}
            backColor={backColor}
        />;
    } else if (type === 'cube') {
        spinner = <CubeSpinner
            size={size || 40}
            color={color}
            frontColor={frontColor}
            backColor={backColor}
        />;
    } else if (type === 'magic') {
        spinner = <MagicSpinner
            size={size || 40}
            color={color}
            frontColor={frontColor}
            backColor={backColor}
        />;
    } else if (type === 'flag') {
        spinner = <FlagSpinner
            size={size || 40}
            color={color}
            frontColor={frontColor}
            backColor={backColor}
        />;
    } else if (type === 'fill') {
        spinner = <FillSpinner
            size={size || 40}
            color={color}
            frontColor={frontColor}
            backColor={backColor}
        />;
    } else if (type === 'sphere') {
        spinner = <SphereSpinner
            size={size || 40}
            color={color}
            frontColor={frontColor}
            backColor={backColor}
        />;
    } else if (type === 'domino') {
        spinner = <DominoSpinner
            size={size || 40}
            color={color}
            frontColor={frontColor}
            backColor={backColor}
        />;
    } else if (type === 'goo') {
        spinner = <GooSpinner
            size={size || 40}
            color={color}
            frontColor={frontColor}
            backColor={backColor}
        />;
    } else if (type === 'comb') {
        spinner = <CombSpinner
            size={size || 40}
            color={color}
            frontColor={frontColor}
            backColor={backColor}
        />;
    } else if (type === 'pong') {
        spinner = <PongSpinner
            size={size || 40}
            color={color}
            frontColor={frontColor}
            backColor={backColor}
        />;
    } else if (type === 'rainbow') {
        spinner = <RainbowSpinner
            size={size || 40}
            color={color}
            frontColor={frontColor}
            backColor={backColor}
        />;
    } else if (type === 'hoop') {
        spinner = <HoopSpinner
            size={size || 40}
            color={color}
            frontColor={frontColor}
            backColor={backColor}
        />;
    } else if (type === 'flapper') {
        spinner = <FlapperSpinner
            size={size || 40}
            color={color}
            frontColor={frontColor}
            backColor={backColor}
        />;
    } else if (type === 'jellyfish') {
        spinner = <JellyfishSpinner
            size={size || 40}
            color={color}
            frontColor={frontColor}
            backColor={backColor}
        />;
    } else if (type === 'trace') {
        spinner = <TraceSpinner
            size={size || 40}
            color={color}
            frontColor={frontColor}
            backColor={backColor}
        />;
    } else if (type === 'classic') {
        spinner = <ClassicSpinner
            size={size || 40}
            color={color}
            frontColor={frontColor}
            backColor={backColor}
        />;
    } else if (type === 'whisper') {
        spinner = <WhisperSpinner
            size={size || 40}
            color={color}
            frontColor={frontColor}
            backColor={backColor}
        />;
    } else if (type === 'metro') {
        spinner = <MetroSpinner
            size={size || 40}
            color={color}
            frontColor={frontColor}
            backColor={backColor}
        />;
    }

    return <div
        id={id}
        style={{
            ...{
                display: 'flex',
                justifyContent: 'center'
            },
            ...style
        }}
        className={className}
        data-dash-is-loading={
            (loading_state && loading_state.is_loading) || undefined
        }>
        {spinner}
    </div>;
}


// 定义参数或属性
FefferyExtraSpinner.propTypes = {
    // 部件id
    id: PropTypes.string,

    style: PropTypes.object,

    className: PropTypes.string,

    // 加载动画类型
    type: PropTypes.oneOf([
        "ball", "swap", "bars", "grid", "wave", "push", "firework",
        "stage", "ring", "heart", "guard", "rotate", "spiral", "pulse",
        "swish", "sequence", "impulse", "cube", "magic", "flag", "fill",
        "sphere", "domino", "goo", "comb", "pong", "rainbow", "hoop",
        "flapper", "jellyfish", "trace", "classic", "whisper", "metro"
    ]),

    // 设置尺寸
    size: PropTypes.number,

    // 设置尺寸值单位，默认为'px'
    sizeUnit: PropTypes.string,

    // 设置颜色
    color: PropTypes.string,

    // 设置前景色
    frontColor: PropTypes.string,

    // 设置背景色
    backColor: PropTypes.string,

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
FefferyExtraSpinner.defaultProps = {
    sizeUnit: 'px',
    type: 'ball',
    color: '#1890ff',
    frontColor: '#def6ff',
    backColor: '#1890ff'
}

export default FefferyExtraSpinner;