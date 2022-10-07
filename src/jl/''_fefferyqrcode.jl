# AUTO GENERATED FILE - DO NOT EDIT

export ''_fefferyqrcode

"""
    ''_fefferyqrcode(;kwargs...)

A FefferyQRCode component.

Keyword arguments:
- `id` (String; optional)
- `bgColor` (String; optional)
- `fgColor` (String; optional)
- `imageSettings` (optional): . imageSettings has the following type: lists containing elements 'src', 'height', 'width', 'excavate'.
Those elements have the following types:
  - `src` (String; optional)
  - `height` (Real; optional)
  - `width` (Real; optional)
  - `excavate` (Bool; optional)
- `includeMargin` (Bool; optional)
- `level` (a value equal to: 'L', 'M', 'Q', 'H'; optional)
- `loading_state` (optional): . loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional): Determines if the component is loading or not
  - `prop_name` (String; optional): Holds which property is loading
  - `component_name` (String; optional): Holds the name of the component that is loading
- `renderer` (a value equal to: 'svg', 'canvas'; optional)
- `size` (Real; optional)
- `value` (String; required)
"""
function ''_fefferyqrcode(; kwargs...)
        available_props = Symbol[:id, :bgColor, :fgColor, :imageSettings, :includeMargin, :level, :loading_state, :renderer, :size, :value]
        wild_props = Symbol[]
        return Component("''_fefferyqrcode", "FefferyQRCode", "feffery_utils_components", available_props, wild_props; kwargs...)
end

