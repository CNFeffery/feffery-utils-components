# AUTO GENERATED FILE - DO NOT EDIT

export ''_fefferyguide

"""
    ''_fefferyguide(;kwargs...)

A FefferyGuide component.

Keyword arguments:
- `id` (String; optional)
- `arrow` (Bool; optional)
- `className` (String; optional)
- `closable` (Bool; optional)
- `hotspot` (Bool; optional)
- `loading_state` (optional): . loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional): Determines if the component is loading or not
  - `prop_name` (String; optional): Holds which property is loading
  - `component_name` (String; optional): Holds the name of the component that is loading
- `localKey` (String; required)
- `locale` (a value equal to: 'zh', 'en'; optional)
- `mask` (Bool; optional)
- `maskClassName` (String; optional)
- `modalClassName` (String; optional)
- `nextText` (String; optional)
- `okText` (String; optional)
- `prevText` (String; optional)
- `showPreviousBtn` (Bool; optional)
- `step` (Real; optional)
- `stepText` (String; optional)
- `steps` (required): . steps has the following type: Array of lists containing elements 'selector', 'targetPos', 'title', 'content', 'placement', 'offset'.
Those elements have the following types:
  - `selector` (String; optional)
  - `targetPos` (optional): . targetPos has the following type: lists containing elements 'top', 'left', 'width', 'height'.
Those elements have the following types:
  - `top` (Real; optional)
  - `left` (Real; optional)
  - `width` (Real; optional)
  - `height` (Real; optional)
  - `title` (String; optional)
  - `content` (String; optional)
  - `placement` (a value equal to: 'top', 'bottom', 'left', 'right', 'top-left', 'top-right', 'bottom-left', 'bottom-right', 'left-top', 'left-bottom', 'right-top', 'right-bottom'; optional)
  - `offset` (optional): . offset has the following type: lists containing elements 'x', 'y'.
Those elements have the following types:
  - `x` (Real; optional)
  - `y` (Real; optional)s
- `style` (Dict; optional)
"""
function ''_fefferyguide(; kwargs...)
        available_props = Symbol[:id, :arrow, :className, :closable, :hotspot, :loading_state, :localKey, :locale, :mask, :maskClassName, :modalClassName, :nextText, :okText, :prevText, :showPreviousBtn, :step, :stepText, :steps, :style]
        wild_props = Symbol[]
        return Component("''_fefferyguide", "FefferyGuide", "feffery_utils_components", available_props, wild_props; kwargs...)
end

