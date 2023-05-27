# AUTO GENERATED FILE - DO NOT EDIT

export ''_fefferyresizable

"""
    ''_fefferyresizable(;kwargs...)
    ''_fefferyresizable(children::Any;kwargs...)
    ''_fefferyresizable(children_maker::Function;kwargs...)


A FefferyResizable component.

Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional)
- `id` (String; optional)
- `bounds` (a value equal to: 'window', 'parent'; optional)
- `className` (String; optional)
- `defaultSize` (optional): . defaultSize has the following type: lists containing elements 'width', 'height'.
Those elements have the following types:
  - `width` (Real | String; optional)
  - `height` (Real | String; optional)
- `direction` (Array of a value equal to: 'top', 'right', 'bottom', 'left', 'topRight', 'bottomRight', 'bottomLeft', 'topLeft's; optional)
- `grid` (Array of Reals; optional)
- `handleClassNames` (optional): . handleClassNames has the following type: lists containing elements 'top', 'right', 'bottom', 'left', 'topRight', 'bottomRight', 'bottomLeft', 'topLeft'.
Those elements have the following types:
  - `top` (String; optional)
  - `right` (String; optional)
  - `bottom` (String; optional)
  - `left` (String; optional)
  - `topRight` (String; optional)
  - `bottomRight` (String; optional)
  - `bottomLeft` (String; optional)
  - `topLeft` (String; optional)
- `handleStyles` (optional): . handleStyles has the following type: lists containing elements 'top', 'right', 'bottom', 'left', 'topRight', 'bottomRight', 'bottomLeft', 'topLeft'.
Those elements have the following types:
  - `top` (Dict; optional)
  - `right` (Dict; optional)
  - `bottom` (Dict; optional)
  - `left` (Dict; optional)
  - `topRight` (Dict; optional)
  - `bottomRight` (Dict; optional)
  - `bottomLeft` (Dict; optional)
  - `topLeft` (Dict; optional)
- `key` (String; optional)
- `loading_state` (optional): . loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional): Determines if the component is loading or not
  - `prop_name` (String; optional): Holds which property is loading
  - `component_name` (String; optional): Holds the name of the component that is loading
- `maxHeight` (Real | String; optional)
- `maxWidth` (Real | String; optional)
- `minHeight` (Real | String; optional)
- `minWidth` (Real | String; optional)
- `style` (Dict; optional)
"""
function ''_fefferyresizable(; kwargs...)
        available_props = Symbol[:children, :id, :bounds, :className, :defaultSize, :direction, :grid, :handleClassNames, :handleStyles, :key, :loading_state, :maxHeight, :maxWidth, :minHeight, :minWidth, :style]
        wild_props = Symbol[]
        return Component("''_fefferyresizable", "FefferyResizable", "feffery_utils_components", available_props, wild_props; kwargs...)
end

''_fefferyresizable(children::Any; kwargs...) = ''_fefferyresizable(;kwargs..., children = children)
''_fefferyresizable(children_maker::Function; kwargs...) = ''_fefferyresizable(children_maker(); kwargs...)

