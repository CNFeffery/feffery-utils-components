// 组件核心
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
// 辅助库
import { useLoading } from "../../components/utils";
// 参数类型
import { propTypes, defaultProps } from '../../components/loadingAnimations/FefferyExtraSpinner.react';

/**
 * 额外加载动画组件FefferyExtraSpinner
 */
const FefferyExtraSpinner = ({
    id,
    style,
    className,
    key,
    type,
    size,
    color,
    frontColor,
    backColor
}) => {

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
        key={key}
        data-dash-is-loading={useLoading()}>
        {spinner}
    </div>;
}

export default FefferyExtraSpinner;

FefferyExtraSpinner.defaultProps = defaultProps;
FefferyExtraSpinner.propTypes = propTypes;