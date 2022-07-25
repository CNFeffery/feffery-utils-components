# AUTO GENERATED FILE - DO NOT EDIT

export ''_fefferylocation

"""
    ''_fefferylocation(;kwargs...)

A FefferyLocation component.

Keyword arguments:
- `id` (String; required): The ID of this component, used to identify dash components
in callbacks. The ID needs to be unique across all of the
components in an app.
- `hash` (String; optional): hash in window.location - e.g., "#myhash"
- `href` (String; optional): href in window.location - e.g., "/my/full/pathname?myargument=1#myhash"
- `includePathnames` (Array of Strings; optional)
- `pathname` (String; optional): pathname in window.location - e.g., "/my/full/pathname"
- `refresh` (Bool; optional): Refresh the page when the location is updated?
- `search` (String; optional): search in window.location - e.g., "?myargument=1"
"""
function ''_fefferylocation(; kwargs...)
        available_props = Symbol[:id, :hash, :href, :includePathnames, :pathname, :refresh, :search]
        wild_props = Symbol[]
        return Component("''_fefferylocation", "FefferyLocation", "feffery_utils_components", available_props, wild_props; kwargs...)
end

