# AUTO GENERATED FILE - DO NOT EDIT

export ''_fefferymotion

"""
    ''_fefferymotion(;kwargs...)
    ''_fefferymotion(children::Any;kwargs...)
    ''_fefferymotion(children_maker::Function;kwargs...)


A FefferyMotion component.

Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional)
- `id` (String; optional)
- `animate` (Dict | String; optional)
- `className` (String; optional)
- `exit` (Dict | String; optional)
- `initial` (Dict | Bool | String; optional)
- `loading_state` (optional): . loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional): Determines if the component is loading or not
  - `prop_name` (String; optional): Holds which property is loading
  - `component_name` (String; optional): Holds the name of the component that is loading
- `style` (Dict; optional)
- `transition` (optional): . transition has the following type: lists containing elements 'delay', 'repeat', 'repeatType', 'repeatDelay', 'type', 'duration', 'ease', 'times', 'bounce', 'damping', 'mass', 'stiffness', 'velocity'.
Those elements have the following types:
  - `delay` (Real; optional)
  - `repeat` (Real | a value equal to: 'infinity'; optional)
  - `repeatType` (a value equal to: 'loop', 'reverse', 'mirror'; optional)
  - `repeatDelay` (Real; optional)
  - `type` (a value equal to: 'spring', 'tween'; optional)
  - `duration` (Real; optional)
  - `ease` (a value equal to: 'linear', 'easeIn', 'easeOut', 'easeInOut', 'circIn', 'circOut', 'circInOut', 'backIn', 'backOut', 'backInOut', 'anticipate'; optional)
  - `times` (Array of Reals; optional)
  - `bounce` (Real; optional)
  - `damping` (Real; optional)
  - `mass` (Real; optional)
  - `stiffness` (Real; optional)
  - `velocity` (Real; optional)
- `variants` (Dict; optional)
- `viewport` (optional): . viewport has the following type: lists containing elements 'once', 'margin', 'amount'.
Those elements have the following types:
  - `once` (Bool; optional)
  - `margin` (String; optional)
  - `amount` (a value equal to: 'some', 'all'; optional)
- `whileFocus` (Dict | String; optional)
- `whileHover` (Dict | String; optional)
- `whileInView` (Dict | String; optional)
- `whileTap` (Dict | String; optional)
"""
function ''_fefferymotion(; kwargs...)
        available_props = Symbol[:children, :id, :animate, :className, :exit, :initial, :loading_state, :style, :transition, :variants, :viewport, :whileFocus, :whileHover, :whileInView, :whileTap]
        wild_props = Symbol[]
        return Component("''_fefferymotion", "FefferyMotion", "feffery_utils_components", available_props, wild_props; kwargs...)
end

''_fefferymotion(children::Any; kwargs...) = ''_fefferymotion(;kwargs..., children = children)
''_fefferymotion(children_maker::Function; kwargs...) = ''_fefferymotion(children_maker(); kwargs...)

