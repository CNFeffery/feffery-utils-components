# AUTO GENERATED FILE - DO NOT EDIT

export ''_fefferyautoanimate

"""
    ''_fefferyautoanimate(;kwargs...)
    ''_fefferyautoanimate(children::Any;kwargs...)
    ''_fefferyautoanimate(children_maker::Function;kwargs...)


A FefferyAutoAnimate component.

Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional)
- `id` (String; optional)
- `className` (String; optional)
- `duration` (Real; optional)
- `easing` (String; optional)
- `loading_state` (optional): . loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional): Determines if the component is loading or not
  - `prop_name` (String; optional): Holds which property is loading
  - `component_name` (String; optional): Holds the name of the component that is loading
- `style` (Dict; optional)
"""
function ''_fefferyautoanimate(; kwargs...)
        available_props = Symbol[:children, :id, :className, :duration, :easing, :loading_state, :style]
        wild_props = Symbol[]
        return Component("''_fefferyautoanimate", "FefferyAutoAnimate", "feffery_utils_components", available_props, wild_props; kwargs...)
end

''_fefferyautoanimate(children::Any; kwargs...) = ''_fefferyautoanimate(;kwargs..., children = children)
''_fefferyautoanimate(children_maker::Function; kwargs...) = ''_fefferyautoanimate(children_maker(); kwargs...)

