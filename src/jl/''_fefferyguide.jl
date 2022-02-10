# AUTO GENERATED FILE - DO NOT EDIT

export ''_fefferyguide

"""
    ''_fefferyguide(;kwargs...)

A FefferyGuide component.

Keyword arguments:
- `id` (optional)
- `arrow` (optional)
- `className` (optional)
- `closable` (optional)
- `hotspot` (optional)
- `loading_state` (optional)
- `localKey` (optional)
- `locale` (optional)
- `mask` (optional)
- `maskClassName` (optional)
- `modalClassName` (optional)
- `nextText` (optional)
- `okText` (optional)
- `prevText` (optional)
- `setProps` (optional): Dash-assigned callback that should be called to report property changes
to Dash, to make them available for callbacks.
- `showPreviousBtn` (optional)
- `step` (optional)
- `stepText` (optional)
- `steps` (optional)
- `style` (optional)
"""
function ''_fefferyguide(; kwargs...)
        available_props = Symbol[:id, :arrow, :className, :closable, :hotspot, :loading_state, :localKey, :locale, :mask, :maskClassName, :modalClassName, :nextText, :okText, :prevText, :showPreviousBtn, :step, :stepText, :steps, :style]
        wild_props = Symbol[]
        return Component("''_fefferyguide", "FefferyGuide", "feffery_utils_components", available_props, wild_props; kwargs...)
end

