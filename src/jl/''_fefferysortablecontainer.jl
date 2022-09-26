# AUTO GENERATED FILE - DO NOT EDIT

export ''_fefferysortablecontainer

"""
    ''_fefferysortablecontainer(;kwargs...)
    ''_fefferysortablecontainer(children::Any;kwargs...)
    ''_fefferysortablecontainer(children_maker::Function;kwargs...)


A FefferySortableContainer component.

Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional)
- `id` (String; optional)
- `className` (String; optional)
- `helperClassName` (String | Dict; optional)
- `loading_state` (optional): . loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional): Determines if the component is loading or not
  - `prop_name` (String; optional): Holds which property is loading
  - `component_name` (String; optional): Holds the name of the component that is loading
- `orders` (Array of Reals; optional)
- `style` (Dict; optional)
"""
function ''_fefferysortablecontainer(; kwargs...)
        available_props = Symbol[:children, :id, :className, :helperClassName, :loading_state, :orders, :style]
        wild_props = Symbol[]
        return Component("''_fefferysortablecontainer", "FefferySortableContainer", "feffery_utils_components", available_props, wild_props; kwargs...)
end

''_fefferysortablecontainer(children::Any; kwargs...) = ''_fefferysortablecontainer(;kwargs..., children = children)
''_fefferysortablecontainer(children_maker::Function; kwargs...) = ''_fefferysortablecontainer(children_maker(); kwargs...)

