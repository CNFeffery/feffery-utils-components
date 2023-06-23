import React, { useEffect } from "react";
import PropTypes from 'prop-types';
import {
    DndContext,
    useSensors,
    useSensor,
    PointerSensor,
    closestCenter,
} from "@dnd-kit/core";
import {
    arrayMove,
    SortableContext,
    useSortable,
    verticalListSortingStrategy,
    horizontalListSortingStrategy
} from "@dnd-kit/sortable";
import { CSS } from "@dnd-kit/utilities";
import { HolderOutlined, MenuOutlined, DragOutlined } from "@ant-design/icons";
import useCss from "../../hooks/useCss";
import { isString } from 'lodash';


const type2icon = new Map([
    ['holder', HolderOutlined],
    ['menu', MenuOutlined],
    ['drag', DragOutlined],
])


const SortableItem = ({
    id,
    style: containerStyle, // 重命名消除歧义
    draggingStyle,
    className,
    draggingClassName,
    children,
    handleStyle,
    handleClassName,
    handlePosition,
    handleType,
    itemDraggingScale
}) => {

    const {
        attributes,
        listeners,
        setNodeRef,
        transform,
        transition,
        setActivatorNodeRef,
        isDragging
    } = useSortable({ id: id });

    const style = {
        transform: CSS.Transform.toString(
            transform && {
                ...transform,
                scaleY: 1,
                ...(
                    isDragging ?
                        {
                            scaleX: itemDraggingScale,
                            scaleY: itemDraggingScale
                        } :
                        {}
                )
            }
        ),
        transition,
        display: 'flex',
        alignItems: 'center',
        ...containerStyle,
        ...(
            isDragging
                ? {
                    position: 'relative',
                    zIndex: 999,
                    ...draggingStyle
                }
                : {}
        )
    };

    return (
        <div ref={setNodeRef}
            {...attributes}
            style={style}
            className={
                isDragging ?
                    (
                        isString(className) ?
                            className :
                            (className ? useCss(className) : undefined)
                    ) :
                    (
                        isString(draggingClassName) ?
                            draggingClassName :
                            (draggingClassName ? useCss(draggingClassName) : undefined)
                    )
            }>
            {handlePosition === 'end' ? <div style={{ flex: 'auto' }}>{children}</div> : null}
            {React.createElement(
                type2icon.get(handleType),
                {
                    style: {
                        color: '#737373',
                        touchAction: "none",
                        cursor: isDragging ? 'grabbing' : 'grab',
                        flex: 'none',
                        ...handleStyle
                    },
                    className: (
                        isString(handleClassName) ?
                            handleClassName :
                            (handleClassName ? useCss(handleClassName) : undefined)
                    ),
                    ref: setActivatorNodeRef,
                    ...listeners
                }
            )}
            {handlePosition === 'start' ? <div style={{ flex: 'auto' }}>{children}</div> : null}
        </div>
    );
};

// 定义排序列表组件FefferySortable
const FefferySortableList = (props) => {

    const {
        id,
        style,
        handleStyle,
        className,
        handleClassName,
        items,
        direction,
        itemDraggingScale,
        handlePosition,
        handleType,
        setProps,
        loading_state
    } = props;

    useEffect(() => {
        setProps({
            currentOrder: items.map(item => item.key)
        })
    }, [items])

    const sensors = useSensors(
        useSensor(PointerSensor),
    );

    const onSortEnd = (e) => {
        let { active, over } = e;
        if (active?.id !== over?.id) {
            let activeIndex = items.findIndex((item) => item.key === active?.id);
            let overIndex = items.findIndex((item) => item.key === over?.id);
            setProps({
                items: arrayMove([...items], activeIndex, overIndex)
            })
        }
    };

    return (
        <DndContext
            sensors={sensors}
            collisionDetection={closestCenter}
            onDragEnd={onSortEnd}
        >
            <SortableContext
                items={items.map(item => { return { ...item, id: item.key }; })}
                strategy={
                    direction === 'horizontal' ?
                        horizontalListSortingStrategy :
                        verticalListSortingStrategy
                }>
                <ul id={id}
                    style={{
                        paddingLeft: 0,
                        ...style
                    }}
                    className={
                        isString(className) ?
                            className :
                            (className ? useCss(className) : undefined)
                    }
                    data-dash-is-loading={
                        (loading_state && loading_state.is_loading) || undefined
                    }>
                    {items.map((item) => (
                        <SortableItem id={item.key}
                            key={item.key}
                            style={item.style}
                            draggingStyle={item.draggingStyle}
                            className={item.className}
                            draggingClassName={item.draggingClassName}
                            children={item.content}
                            handleStyle={handleStyle}
                            handleClassName={handleClassName}
                            handlePosition={handlePosition}
                            handleType={handleType}
                            itemDraggingScale={itemDraggingScale} />
                    ))}
                </ul>
            </SortableContext>
        </DndContext>
    )
}

// 定义参数或属性
FefferySortableList.propTypes = {
    // 部件id
    id: PropTypes.string,

    // 组件css样式
    style: PropTypes.object,

    // 拖拽手柄css样式
    handleStyle: PropTypes.object,

    // 拖拽手柄css类
    handleClassName: PropTypes.oneOfType([
        PropTypes.string,
        PropTypes.object
    ]),

    // 组件css类
    className: PropTypes.oneOfType([
        PropTypes.string,
        PropTypes.object
    ]),

    key: PropTypes.string,

    // 必填参数，用于定义当前排序列表组件的各子元素
    items: PropTypes.arrayOf(
        PropTypes.exact({
            // 对应当前子元素的唯一标识
            key: PropTypes.oneOfType([PropTypes.number, PropTypes.string]).isRequired,

            // 当前子元素内容
            content: PropTypes.node,

            // 当前子元素容器css样式
            style: PropTypes.object,

            // 当前子元素容器css类
            className: PropTypes.oneOfType([
                PropTypes.string,
                PropTypes.object
            ]),

            // 当前子元素处于拖拽中状态下的css样式
            draggingStyle: PropTypes.object,

            // 当前子元素处于拖拽中状态下的css类
            draggingClassName: PropTypes.oneOfType([
                PropTypes.string,
                PropTypes.object
            ])
        })
    ).isRequired,

    // 设置排序列表的方向，可选的有'vertical'和'horizontal'
    // 默认：'vertical'
    direction: PropTypes.oneOf(['vertical', 'horizontal']),

    // 设置子项处于拖拽中状态下的缩放比例，默认为1即不缩放
    itemDraggingScale: PropTypes.number,

    // 设置拖拽手柄位置，默认为'end'
    handlePosition: PropTypes.oneOf(['start', 'end']),

    // 设置内置的推拽手柄图标类型，默认为'holder'
    handleType: PropTypes.oneOf(['holder', 'menu', 'drag']),

    // 监听当前items顺序对应的子项id数组
    currentOrder: PropTypes.arrayOf(
        PropTypes.oneOfType([
            PropTypes.number,
            PropTypes.string
        ])
    ),

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
    setProps: PropTypes.func,
};

// 设置默认参数
FefferySortableList.defaultProps = {
    direction: 'vertical',
    itemDraggingScale: 1,
    handlePosition: 'end',
    handleType: 'holder'
}

export default React.memo(FefferySortableList);