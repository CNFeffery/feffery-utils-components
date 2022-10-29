# AUTO GENERATED FILE - DO NOT EDIT

export ''_fefferysticky

"""
    ''_fefferysticky(;kwargs...)
    ''_fefferysticky(children::Any;kwargs...)
    ''_fefferysticky(children_maker::Function;kwargs...)


A FefferySticky component.

Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional)
- `id` (String; optional)
- `bottomBoundary` (Real | String; optional)
- `enabled` (Bool; optional)
- `loading_state` (optional): . loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional): Determines if the component is loading or not
  - `prop_name` (String; optional): Holds which property is loading
  - `component_name` (String; optional): Holds the name of the component that is loading
- `top` (Real | String; optional)
- `zIndex` (Real | String; optional)
"""
function ''_fefferysticky(; kwargs...)
        available_props = Symbol[:children, :id, :bottomBoundary, :enabled, :loading_state, :top, :zIndex]
        wild_props = Symbol[]
        return Component("''_fefferysticky", "FefferySticky", "feffery_utils_components", available_props, wild_props; kwargs...)
end

''_fefferysticky(children::Any; kwargs...) = ''_fefferysticky(;kwargs..., children = children)
''_fefferysticky(children_maker::Function; kwargs...) = ''_fefferysticky(children_maker(); kwargs...)

