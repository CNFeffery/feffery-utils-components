# AUTO GENERATED FILE - DO NOT EDIT

export ''_fefferyhexcolorpicker

"""
    ''_fefferyhexcolorpicker(;kwargs...)

A FefferyHexColorPicker component.

Keyword arguments:
- `id` (String; optional)
- `className` (String; optional)
- `color` (String; optional)
- `loading_state` (optional): . loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional): Determines if the component is loading or not
  - `prop_name` (String; optional): Holds which property is loading
  - `component_name` (String; optional): Holds the name of the component that is loading
- `showAlpha` (Bool; optional)
- `style` (Dict; optional)
"""
function ''_fefferyhexcolorpicker(; kwargs...)
        available_props = Symbol[:id, :className, :color, :loading_state, :showAlpha, :style]
        wild_props = Symbol[]
        return Component("''_fefferyhexcolorpicker", "FefferyHexColorPicker", "feffery_utils_components", available_props, wild_props; kwargs...)
end

