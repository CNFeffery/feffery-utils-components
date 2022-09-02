# AUTO GENERATED FILE - DO NOT EDIT

export ''_fefferysplit

"""
    ''_fefferysplit(;kwargs...)
    ''_fefferysplit(children::Any;kwargs...)
    ''_fefferysplit(children_maker::Function;kwargs...)


A FefferySplit component.

Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional)
- `id` (String; optional)
- `className` (String; optional)
- `cursor` (String; optional)
- `direction` (a value equal to: 'horizontal', 'vertical'; optional)
- `dragInterval` (Real; optional)
- `expandToMin` (Bool; optional)
- `gutterSize` (Real; optional)
- `loading_state` (optional): . loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional): Determines if the component is loading or not
  - `prop_name` (String; optional): Holds which property is loading
  - `component_name` (String; optional): Holds the name of the component that is loading
- `maxSize` (Real | Array of Reals; optional)
- `minSize` (Real | Array of Reals; optional)
- `sizes` (Array of Reals; optional)
- `style` (Dict; optional)
"""
function ''_fefferysplit(; kwargs...)
        available_props = Symbol[:children, :id, :className, :cursor, :direction, :dragInterval, :expandToMin, :gutterSize, :loading_state, :maxSize, :minSize, :sizes, :style]
        wild_props = Symbol[]
        return Component("''_fefferysplit", "FefferySplit", "feffery_utils_components", available_props, wild_props; kwargs...)
end

''_fefferysplit(children::Any; kwargs...) = ''_fefferysplit(;kwargs..., children = children)
''_fefferysplit(children_maker::Function; kwargs...) = ''_fefferysplit(children_maker(); kwargs...)

