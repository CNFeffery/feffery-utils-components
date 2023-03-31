# AUTO GENERATED FILE - DO NOT EDIT

export ''_fefferyunmount

"""
    ''_fefferyunmount(;kwargs...)
    ''_fefferyunmount(children::Any;kwargs...)
    ''_fefferyunmount(children_maker::Function;kwargs...)


A FefferyUnmount component.

Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional)
- `id` (String; optional)
- `isUnmount` (Bool; optional)
- `loading_state` (optional): . loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional): Determines if the component is loading or not
  - `prop_name` (String; optional): Holds which property is loading
  - `component_name` (String; optional): Holds the name of the component that is loading
"""
function ''_fefferyunmount(; kwargs...)
        available_props = Symbol[:children, :id, :isUnmount, :loading_state]
        wild_props = Symbol[]
        return Component("''_fefferyunmount", "FefferyUnmount", "feffery_utils_components", available_props, wild_props; kwargs...)
end

''_fefferyunmount(children::Any; kwargs...) = ''_fefferyunmount(;kwargs..., children = children)
''_fefferyunmount(children_maker::Function; kwargs...) = ''_fefferyunmount(children_maker(); kwargs...)

