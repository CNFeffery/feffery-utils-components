# AUTO GENERATED FILE - DO NOT EDIT

export ''_fefferyextraspinner

"""
    ''_fefferyextraspinner(;kwargs...)

A FefferyExtraSpinner component.

Keyword arguments:
- `id` (String; optional)
- `backColor` (String; optional)
- `className` (String; optional)
- `color` (String; optional)
- `frontColor` (String; optional)
- `loading_state` (optional): . loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional): Determines if the component is loading or not
  - `prop_name` (String; optional): Holds which property is loading
  - `component_name` (String; optional): Holds the name of the component that is loading
- `size` (Real; optional)
- `sizeUnit` (String; optional)
- `style` (Dict; optional)
- `type` (a value equal to: "ball", "swap", "bars", "grid", "wave", "push", "firework", "stage", "ring", "heart", "guard", "rotate", "spiral", "pulse", "swish", "sequence", "impulse", "cube", "magic", "flag", "fill", "sphere", "domino", "goo", "comb", "pong", "rainbow", "hoop", "flapper", "jellyfish", "trace", "classic", "whisper", "metro"; optional)
"""
function ''_fefferyextraspinner(; kwargs...)
        available_props = Symbol[:id, :backColor, :className, :color, :frontColor, :loading_state, :size, :sizeUnit, :style, :type]
        wild_props = Symbol[]
        return Component("''_fefferyextraspinner", "FefferyExtraSpinner", "feffery_utils_components", available_props, wild_props; kwargs...)
end

