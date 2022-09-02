# AUTO GENERATED FILE - DO NOT EDIT

export ''_fefferyvirtuallist

"""
    ''_fefferyvirtuallist(;kwargs...)
    ''_fefferyvirtuallist(children::Any;kwargs...)
    ''_fefferyvirtuallist(children_maker::Function;kwargs...)


A FefferyVirtualList component.

Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional)
- `id` (String; optional)
- `className` (String; optional)
- `height` (Real; required)
- `itemHeight` (Real; required)
- `loading_state` (optional): . loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional): Determines if the component is loading or not
  - `prop_name` (String; optional): Holds which property is loading
  - `component_name` (String; optional): Holds the name of the component that is loading
- `style` (Dict; optional)
"""
function ''_fefferyvirtuallist(; kwargs...)
        available_props = Symbol[:children, :id, :className, :height, :itemHeight, :loading_state, :style]
        wild_props = Symbol[]
        return Component("''_fefferyvirtuallist", "FefferyVirtualList", "feffery_utils_components", available_props, wild_props; kwargs...)
end

''_fefferyvirtuallist(children::Any; kwargs...) = ''_fefferyvirtuallist(;kwargs..., children = children)
''_fefferyvirtuallist(children_maker::Function; kwargs...) = ''_fefferyvirtuallist(children_maker(); kwargs...)

