# AUTO GENERATED FILE - DO NOT EDIT

export ''_fefferyanimated

"""
    ''_fefferyanimated(;kwargs...)
    ''_fefferyanimated(children::Any;kwargs...)
    ''_fefferyanimated(children_maker::Function;kwargs...)


A FefferyAnimated component.

Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional)
- `id` (String; optional)
- `animate` (Dict; optional)
- `className` (String; optional)
- `initial` (Dict; optional)
- `loading_state` (optional): . loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional): Determines if the component is loading or not
  - `prop_name` (String; optional): Holds which property is loading
  - `component_name` (String; optional): Holds the name of the component that is loading
- `style` (Dict; optional)
"""
function ''_fefferyanimated(; kwargs...)
        available_props = Symbol[:children, :id, :animate, :className, :initial, :loading_state, :style]
        wild_props = Symbol[]
        return Component("''_fefferyanimated", "FefferyAnimated", "feffery_utils_components", available_props, wild_props; kwargs...)
end

''_fefferyanimated(children::Any; kwargs...) = ''_fefferyanimated(;kwargs..., children = children)
''_fefferyanimated(children_maker::Function; kwargs...) = ''_fefferyanimated(children_maker(); kwargs...)

