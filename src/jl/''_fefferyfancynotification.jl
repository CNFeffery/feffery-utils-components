# AUTO GENERATED FILE - DO NOT EDIT

export ''_fefferyfancynotification

"""
    ''_fefferyfancynotification(;kwargs...)
    ''_fefferyfancynotification(children::Any;kwargs...)
    ''_fefferyfancynotification(children_maker::Function;kwargs...)


A FefferyFancyNotification component.

Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional)
- `id` (String; optional)
- `autoClose` (Bool | Real; optional)
- `bodyClassName` (String; optional)
- `className` (String; optional)
- `closable` (Bool; optional)
- `closeOnClick` (Bool; optional)
- `containerId` (String; optional)
- `draggable` (Bool; optional)
- `draggablePercent` (Real; optional)
- `hideProgressBar` (Bool; optional)
- `key` (String; optional)
- `limit` (Real; optional)
- `loading_state` (optional): . loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional): Determines if the component is loading or not
  - `prop_name` (String; optional): Holds which property is loading
  - `component_name` (String; optional): Holds the name of the component that is loading
- `newestOnTop` (Bool; optional)
- `pauseOnHover` (Bool; optional)
- `position` (a value equal to: 'top-right', 'top-center', 'top-left', 'bottom-right', 'bottom-cente', 'bottom-left'; optional)
- `progressClassName` (String; optional)
- `progressStyle` (Dict; optional)
- `style` (Dict; optional)
- `theme` (a value equal to: 'light', 'dark', 'colored'; optional)
- `toastClassName` (String; optional)
- `type` (a value equal to: 'info', 'success', 'warning', 'error'; optional)
- `visible` (Bool; optional)
"""
function ''_fefferyfancynotification(; kwargs...)
        available_props = Symbol[:children, :id, :autoClose, :bodyClassName, :className, :closable, :closeOnClick, :containerId, :draggable, :draggablePercent, :hideProgressBar, :key, :limit, :loading_state, :newestOnTop, :pauseOnHover, :position, :progressClassName, :progressStyle, :style, :theme, :toastClassName, :type, :visible]
        wild_props = Symbol[]
        return Component("''_fefferyfancynotification", "FefferyFancyNotification", "feffery_utils_components", available_props, wild_props; kwargs...)
end

''_fefferyfancynotification(children::Any; kwargs...) = ''_fefferyfancynotification(;kwargs..., children = children)
''_fefferyfancynotification(children_maker::Function; kwargs...) = ''_fefferyfancynotification(children_maker(); kwargs...)

