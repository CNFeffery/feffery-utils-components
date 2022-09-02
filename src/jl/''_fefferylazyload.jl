# AUTO GENERATED FILE - DO NOT EDIT

export ''_fefferylazyload

"""
    ''_fefferylazyload(;kwargs...)
    ''_fefferylazyload(children::Any;kwargs...)
    ''_fefferylazyload(children_maker::Function;kwargs...)


A FefferyLazyLoad component.

Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional)
- `id` (String; optional)
- `className` (String; optional)
- `height` (Real | String; optional)
- `loading_state` (optional): . loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional): Determines if the component is loading or not
  - `prop_name` (String; optional): Holds which property is loading
  - `component_name` (String; optional): Holds the name of the component that is loading
- `offset` (Real; optional)
- `style` (Dict; optional)
- `throttle` (Real; optional)
- `visible` (Bool; optional)
- `width` (Real | String; optional)
"""
function ''_fefferylazyload(; kwargs...)
        available_props = Symbol[:children, :id, :className, :height, :loading_state, :offset, :style, :throttle, :visible, :width]
        wild_props = Symbol[]
        return Component("''_fefferylazyload", "FefferyLazyLoad", "feffery_utils_components", available_props, wild_props; kwargs...)
end

''_fefferylazyload(children::Any; kwargs...) = ''_fefferylazyload(;kwargs..., children = children)
''_fefferylazyload(children_maker::Function; kwargs...) = ''_fefferylazyload(children_maker(); kwargs...)

