# AUTO GENERATED FILE - DO NOT EDIT

export ''_fefferysplitpane

"""
    ''_fefferysplitpane(;kwargs...)
    ''_fefferysplitpane(children::Any;kwargs...)
    ''_fefferysplitpane(children_maker::Function;kwargs...)


A FefferySplitPane component.

Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional)
- `id` (String; optional)
- `className` (String; optional)
- `loading_state` (optional): . loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional): Determines if the component is loading or not
  - `prop_name` (String; optional): Holds which property is loading
  - `component_name` (String; optional): Holds the name of the component that is loading
- `style` (Dict; optional)
"""
function ''_fefferysplitpane(; kwargs...)
        available_props = Symbol[:children, :id, :className, :loading_state, :style]
        wild_props = Symbol[]
        return Component("''_fefferysplitpane", "FefferySplitPane", "feffery_utils_components", available_props, wild_props; kwargs...)
end

''_fefferysplitpane(children::Any; kwargs...) = ''_fefferysplitpane(;kwargs..., children = children)
''_fefferysplitpane(children_maker::Function; kwargs...) = ''_fefferysplitpane(children_maker(); kwargs...)

