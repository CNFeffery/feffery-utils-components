# AUTO GENERATED FILE - DO NOT EDIT

export ''_fefferyfancybutton

"""
    ''_fefferyfancybutton(;kwargs...)
    ''_fefferyfancybutton(children::Any;kwargs...)
    ''_fefferyfancybutton(children_maker::Function;kwargs...)


A FefferyFancyButton component.

Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional)
- `id` (String; optional)
- `after` (a list of or a singular dash component, string or number; optional)
- `before` (a list of or a singular dash component, string or number; optional)
- `className` (String | Dict; optional)
- `debounceWait` (Real; optional)
- `disabled` (Bool; optional)
- `href` (String; optional)
- `key` (String; optional)
- `loading_state` (optional): . loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional): Determines if the component is loading or not
  - `prop_name` (String; optional): Holds which property is loading
  - `component_name` (String; optional): Holds the name of the component that is loading
- `nClicks` (Real; optional)
- `ripple` (Bool; optional)
- `style` (Dict; optional)
- `target` (String; optional)
- `type` (a value equal to: 'primary', 'secondary', 'danger'; optional)
"""
function ''_fefferyfancybutton(; kwargs...)
        available_props = Symbol[:children, :id, :after, :before, :className, :debounceWait, :disabled, :href, :key, :loading_state, :nClicks, :ripple, :style, :target, :type]
        wild_props = Symbol[]
        return Component("''_fefferyfancybutton", "FefferyFancyButton", "feffery_utils_components", available_props, wild_props; kwargs...)
end

''_fefferyfancybutton(children::Any; kwargs...) = ''_fefferyfancybutton(;kwargs..., children = children)
''_fefferyfancybutton(children_maker::Function; kwargs...) = ''_fefferyfancybutton(children_maker(); kwargs...)

