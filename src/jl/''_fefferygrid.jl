# AUTO GENERATED FILE - DO NOT EDIT

export ''_fefferygrid

"""
    ''_fefferygrid(;kwargs...)
    ''_fefferygrid(children::Any;kwargs...)
    ''_fefferygrid(children_maker::Function;kwargs...)


A FefferyGrid component.

Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional)
- `id` (String; optional)
- `allowOverlap` (Bool; optional)
- `autoSize` (Bool; optional)
- `breakpoints` (Dict with Strings as keys and values of type Real; optional)
- `className` (String; optional)
- `cols` (Dict with Strings as keys and values of type Real | Real; optional)
- `compactType` (a value equal to: 'vertical', 'horizontal'; optional)
- `containerPadding` (Array of Reals | Dict with Strings as keys and values of type Array of Reals; optional)
- `height` (Real; optional)
- `isBounded` (Bool; optional)
- `isDraggable` (Bool; optional)
- `isResizable` (Bool; optional)
- `key` (String; optional)
- `layouts` (optional): . layouts has the following type: Dict with Strings as keys and values of type Array of lists containing elements 'i', 'x', 'y', 'w', 'h', 'minW', 'maxW', 'minH', 'maxH', 'static', 'isDraggable', 'isResizable', 'isBounded', 'moved'.
Those elements have the following types:
  - `i` (String; optional)
  - `x` (Real; optional)
  - `y` (Real; optional)
  - `w` (Real; optional)
  - `h` (Real; optional)
  - `minW` (Real; optional)
  - `maxW` (Real; optional)
  - `minH` (Real; optional)
  - `maxH` (Real; optional)
  - `static` (Bool; optional)
  - `isDraggable` (Bool; optional)
  - `isResizable` (Bool; optional)
  - `isBounded` (Bool; optional)
  - `moved` (Bool | Real | String | Dict | Array; optional)s | Array of lists containing elements 'i', 'x', 'y', 'w', 'h', 'minW', 'maxW', 'minH', 'maxH', 'static', 'isDraggable', 'isResizable', 'isBounded', 'moved'.
Those elements have the following types:
  - `i` (String; optional)
  - `x` (Real; optional)
  - `y` (Real; optional)
  - `w` (Real; optional)
  - `h` (Real; optional)
  - `minW` (Real; optional)
  - `maxW` (Real; optional)
  - `minH` (Real; optional)
  - `maxH` (Real; optional)
  - `static` (Bool; optional)
  - `isDraggable` (Bool; optional)
  - `isResizable` (Bool; optional)
  - `isBounded` (Bool; optional)
  - `moved` (Bool | Real | String | Dict | Array; optional)s
- `loading_state` (optional): . loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional): Determines if the component is loading or not
  - `prop_name` (String; optional): Holds which property is loading
  - `component_name` (String; optional): Holds the name of the component that is loading
- `margin` (Array of Reals | Dict with Strings as keys and values of type Array of Reals; optional)
- `placeholderBackground` (String; optional)
- `placeholderBorder` (String; optional)
- `placeholderBorderRadius` (String; optional)
- `placeholderOpacity` (Real; optional)
- `rowHeight` (Real; optional)
- `style` (Dict; optional)
"""
function ''_fefferygrid(; kwargs...)
        available_props = Symbol[:children, :id, :allowOverlap, :autoSize, :breakpoints, :className, :cols, :compactType, :containerPadding, :height, :isBounded, :isDraggable, :isResizable, :key, :layouts, :loading_state, :margin, :placeholderBackground, :placeholderBorder, :placeholderBorderRadius, :placeholderOpacity, :rowHeight, :style]
        wild_props = Symbol[]
        return Component("''_fefferygrid", "FefferyGrid", "feffery_utils_components", available_props, wild_props; kwargs...)
end

''_fefferygrid(children::Any; kwargs...) = ''_fefferygrid(;kwargs..., children = children)
''_fefferygrid(children_maker::Function; kwargs...) = ''_fefferygrid(children_maker(); kwargs...)

