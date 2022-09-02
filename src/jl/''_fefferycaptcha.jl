# AUTO GENERATED FILE - DO NOT EDIT

export ''_fefferycaptcha

"""
    ''_fefferycaptcha(;kwargs...)

A FefferyCaptcha component.

Keyword arguments:
- `id` (String; optional)
- `bgColor` (String; optional)
- `captcha` (String; optional)
- `charNum` (Real; optional)
- `className` (String; optional)
- `fontSize` (Real; optional)
- `height` (Real; optional)
- `loading_state` (optional): . loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional): Determines if the component is loading or not
  - `prop_name` (String; optional): Holds which property is loading
  - `component_name` (String; optional): Holds the name of the component that is loading
- `style` (Dict; optional)
- `width` (Real; optional)
"""
function ''_fefferycaptcha(; kwargs...)
        available_props = Symbol[:id, :bgColor, :captcha, :charNum, :className, :fontSize, :height, :loading_state, :style, :width]
        wild_props = Symbol[]
        return Component("''_fefferycaptcha", "FefferyCaptcha", "feffery_utils_components", available_props, wild_props; kwargs...)
end

