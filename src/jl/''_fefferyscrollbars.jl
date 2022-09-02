# AUTO GENERATED FILE - DO NOT EDIT

export ''_fefferyscrollbars

"""
    ''_fefferyscrollbars(;kwargs...)
    ''_fefferyscrollbars(children::Any;kwargs...)
    ''_fefferyscrollbars(children_maker::Function;kwargs...)


A FefferyScrollbars component.

Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional)
- `id` (String; optional)
- `autoHide` (Bool; optional)
- `className` (String; optional)
- `classNames` (optional): . classNames has the following type: lists containing elements 'content', 'scrollContent', 'scrollbar', 'track'.
Those elements have the following types:
  - `content` (String; optional)
  - `scrollContent` (String; optional)
  - `scrollbar` (String; optional)
  - `track` (String; optional)
- `forceVisible` (Bool | a value equal to: 'x', 'y'; optional)
- `loading_state` (optional): . loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional): Determines if the component is loading or not
  - `prop_name` (String; optional): Holds which property is loading
  - `component_name` (String; optional): Holds the name of the component that is loading
- `scrollbarMaxSize` (Real; optional)
- `scrollbarMinSize` (Real; optional)
- `style` (Dict; optional)
- `timeout` (Real; optional)
"""
function ''_fefferyscrollbars(; kwargs...)
        available_props = Symbol[:children, :id, :autoHide, :className, :classNames, :forceVisible, :loading_state, :scrollbarMaxSize, :scrollbarMinSize, :style, :timeout]
        wild_props = Symbol[]
        return Component("''_fefferyscrollbars", "FefferyScrollbars", "feffery_utils_components", available_props, wild_props; kwargs...)
end

''_fefferyscrollbars(children::Any; kwargs...) = ''_fefferyscrollbars(;kwargs..., children = children)
''_fefferyscrollbars(children_maker::Function; kwargs...) = ''_fefferyscrollbars(children_maker(); kwargs...)

