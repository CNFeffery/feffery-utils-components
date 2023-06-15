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
} from "@dnd-kit/sortable";
import { CSS } from "@dnd-kit/utilities";
import { MenuOutlined } from "@ant-design/icons";

const SortableItem = ({ id, style: containerStyle, children, handleStyle, handlePosition }) => {
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
                scaleY: 1
            }
        ),
        transition,
        display: 'flex',
        alignItems: 'center',
        ...containerStyle
    };

    return (
        <div ref={setNodeRef}
            {...attributes}
            style={style}>
            {handlePosition === 'end' ? <div style={{ flex: 'auto' }}>{children}</div> : null}
            <MenuOutlined style={{
                color: '#737373',
                touchAction: "none",
                cursor: isDragging ? 'grabbing' : 'grab',
                flex: 'none',
                ...handleStyle
            }}
                ref={setActivatorNodeRef}
                {...listeners} />
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
        items,
        handlePosition,
        setProps,
        loading_state
    } = props;

    useEffect(() => {
        setProps({
            currentOrder: items.map(item => item.id)
        })
    }, [items])

    const sensors = useSensors(
        useSensor(PointerSensor),
    );

    const onSortEnd = (e) => {
        let { active, over } = e;
        if (active?.id !== over?.id) {
            let activeIndex = items.findIndex((item) => item.id === active?.id);
            let overIndex = items.findIndex((item) => item.id === over?.id);
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
            <SortableContext items={items} strategy={verticalListSortingStrategy}>
                <ul id={id}
                    style={{
                        paddingLeft: 0,
                        ...style
                    }}
                    className={className}
                    data-dash-is-loading={
                        (loading_state && loading_state.is_loading) || undefined
                    }>
                    {items.map((item) => (
                        <SortableItem id={item.id}
                            key={item.id}
                            style={item.style}
                            children={item.content}
                            handleStyle={handleStyle}
                            handlePosition={handlePosition} />
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

    // 组件css类
    className: PropTypes.string,

    key: PropTypes.string,

    // 必填参数，用于定义当前排序列表组件的各子元素
    items: PropTypes.arrayOf(
        PropTypes.exact({
            // 对应当前子元素的唯一标识
            id: PropTypes.oneOfType([PropTypes.number, PropTypes.string]).isRequired,

            // 当前子元素内容
            content: PropTypes.node,

            // 当前子元素容器css样式
            style: PropTypes.object
        })
    ).isRequired,

    // 设置拖拽手柄位置，默认为'start'
    handlePosition: PropTypes.oneOf(['start', 'end']),

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
    handlePosition: 'start'
}

export default FefferySortableList;