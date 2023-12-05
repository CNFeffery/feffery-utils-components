import React, { useEffect } from "react";
import { propTypes, defaultProps } from '../../components/sortable/FefferySortableList.react';
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
import { isString, isEqual } from 'lodash';

// import { useWhyDidYouUpdate } from 'ahooks';


const type2icon = new Map([
    ['holder', HolderOutlined],
    ['menu', MenuOutlined],
    ['drag', DragOutlined],
])


const SortableItem = React.memo(
    ({
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

        // useWhyDidYouUpdate('level2', {
        //     ...{
        //         id,
        //         style: containerStyle, // 重命名消除歧义
        //         draggingStyle,
        //         className,
        //         draggingClassName,
        //         children,
        //         handleStyle,
        //         handleClassName,
        //         handlePosition,
        //         handleType,
        //         itemDraggingScale
        //     }
        // });

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
            <div id={id}
                ref={setNodeRef}
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
                }
                children={
                    <>
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
                    </>
                }
            />
        );
    },
    (prevProps, nextProps) => {
        return isEqual(prevProps.children, nextProps.children);
    }
)

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

    // useWhyDidYouUpdate('level1', { ...props });

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

export default React.memo(FefferySortableList);

FefferySortableList.defaultProps = defaultProps;
FefferySortableList.propTypes = propTypes;