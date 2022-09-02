# AUTO GENERATED FILE - DO NOT EDIT

export ''_fefferyinviewport

"""
    ''_fefferyinviewport(;kwargs...)
    ''_fefferyinviewport(children::Any;kwargs...)
    ''_fefferyinviewport(children_maker::Function;kwargs...)


A FefferyInViewport component.

Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional)
- `id` (String; optional)
- `inViewport` (Bool; optional)
- `loading_state` (optional): . loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional): Determines if the component is loading or not
  - `prop_name` (String; optional): Holds which property is loading
  - `component_name` (String; optional): Holds the name of the component that is loading
- `threshold` (Real; optional)
"""
function ''_fefferyinviewport(; kwargs...)
        available_props = Symbol[:children, :id, :inViewport, :loading_state, :threshold]
        wild_props = Symbol[]
        return Component("''_fefferyinviewport", "FefferyInViewport", "feffery_utils_components", available_props, wild_props; kwargs...)
end

''_fefferyinviewport(children::Any; kwargs...) = ''_fefferyinviewport(;kwargs..., children = children)
''_fefferyinviewport(children_maker::Function; kwargs...) = ''_fefferyinviewport(children_maker(); kwargs...)

