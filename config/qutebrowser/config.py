# Documentation:
#   qute://help/configuring.html
#   qute://help/settings.html

import pywalQute.draw

config.load_autoconfig()

pywalQute.draw.color(c, {
    'spacing': {
        'vertical': 6,
        'horizontal': 8
    }
})

# Specifically set a Chrome user agent for YouTube only
with config.pattern('https://www.youtube.com/*') as p:
    p.content.headers.user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'

# Change the argument to True to still load settings configured via autoconfig.yml
config.load_autoconfig(False)

# Aliases for commands. The keys of the given dictionary are the
# aliases, while the values are the commands they map to.
# Type: Dict
c.aliases = {'q': 'close', 'qa': 'quit', 'w': 'session-save', 'wq': 'quit --save', 'wqa': 'quit --save'}

# Tell qutebrowser to use the system's proxy/DNS settings
config.set('content.proxy', 'system')

# Optional: Enable DNS prefetching to slightly speed up browsing
config.set('content.dns_prefetch', True)

# enabling darkmode
config.set("colors.webpage.darkmode.enabled", True)

# When to show a changelog after qutebrowser was upgraded.
# Type: String
# Valid values:
#   - major: Show changelog for major upgrades (e.g. v2.0.0 -> v3.0.0).
#   - minor: Show changelog for major and minor upgrades (e.g. v2.0.0 -> v2.1.0).
#   - patch: Show changelog for major, minor and patch upgrades (e.g. v2.0.0 -> v2.0.1).
#   - never: Never show changelog after upgrades.
c.changelog_after_upgrade = 'minor'

# Which cookies to accept. With QtWebEngine, this setting also controls
# other features with tracking capabilities similar to those of cookies;
# including IndexedDB, DOM storage, filesystem API, service workers, and
# AppCache. Note that with QtWebKit, only `all` and `never` are
# supported as per-domain values. Setting `no-3rdparty` or `no-
# unknown-3rdparty` per-domain on QtWebKit will have the same effect as
# `all`. If this setting is used with URL patterns, the pattern gets
# applied to the origin/first party URL of the page making the request,
# not the request URL. With QtWebEngine 5.15.0+, paths will be stripped
# from URLs, so URL patterns using paths will not match. With
# QtWebEngine 5.15.2+, subdomains are additionally stripped as well, so
# you will typically need to set this setting for `example.com` when the
# cookie is set on `somesubdomain.example.com` for it to work properly.
# To debug issues with this setting, start qutebrowser with `--debug
# --logfilter network --debug-flag log-cookies` which will show all
# cookies being set.
# Type: String
# Valid values:
#   - all: Accept all cookies.
#   - no-3rdparty: Accept cookies from the same origin only. This is known to break some sites, such as GMail.
#   - no-unknown-3rdparty: Accept cookies from the same origin only, unless a cookie is already set for the domain. On QtWebEngine, this is the same as no-3rdparty.
#   - never: Don't accept cookies at all.
config.set('content.cookies.accept', 'all', 'chrome-devtools://*')

# Which cookies to accept. With QtWebEngine, this setting also controls
# other features with tracking capabilities similar to those of cookies;
# including IndexedDB, DOM storage, filesystem API, service workers, and
# AppCache. Note that with QtWebKit, only `all` and `never` are
# supported as per-domain values. Setting `no-3rdparty` or `no-
# unknown-3rdparty` per-domain on QtWebKit will have the same effect as
# `all`. If this setting is used with URL patterns, the pattern gets
# applied to the origin/first party URL of the page making the request,
# not the request URL. With QtWebEngine 5.15.0+, paths will be stripped
# from URLs, so URL patterns using paths will not match. With
# QtWebEngine 5.15.2+, subdomains are additionally stripped as well, so
# you will typically need to set this setting for `example.com` when the
# cookie is set on `somesubdomain.example.com` for it to work properly.
# To debug issues with this setting, start qutebrowser with `--debug
# --logfilter network --debug-flag log-cookies` which will show all
# cookies being set.
# Type: String
# Valid values:
#   - all: Accept all cookies.
#   - no-3rdparty: Accept cookies from the same origin only. This is known to break some sites, such as GMail.
#   - no-unknown-3rdparty: Accept cookies from the same origin only, unless a cookie is already set for the domain. On QtWebEngine, this is the same as no-3rdparty.
#   - never: Don't accept cookies at all.
config.set('content.cookies.accept', 'all', 'devtools://*')

# Value to send in the `Accept-Language` header. Note that the value
# read from JavaScript is always the global value.
# Type: String
config.set('content.headers.accept_language', '', 'https://matchmaker.krunker.io/*')

# User agent to send.  The following placeholders are defined:  *
# `{os_info}`: Something like "X11; Linux x86_64". * `{webkit_version}`:
# The underlying WebKit version (set to a fixed value   with
# QtWebEngine). * `{qt_key}`: "Qt" for QtWebKit, "QtWebEngine" for
# QtWebEngine. * `{qt_version}`: The underlying Qt version. *
# `{upstream_browser_key}`: "Version" for QtWebKit, "Chrome" for
# QtWebEngine. * `{upstream_browser_version}`: The corresponding
# Safari/Chrome version. * `{qutebrowser_version}`: The currently
# running qutebrowser version.  The default value is equal to the
# unchanged user agent of QtWebKit/QtWebEngine.  Note that the value
# read from JavaScript is always the global value. With QtWebEngine
# between 5.12 and 5.14 (inclusive), changing the value exposed to
# JavaScript requires a restart.
# Type: FormatString
# c.content.headers.user_agent = 'Mozilla/6.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'

# User agent to send.  The following placeholders are defined:  *
# `{os_info}`: Something like "X11; Linux x86_64". * `{webkit_version}`:
# The underlying WebKit version (set to a fixed value   with
# QtWebEngine). * `{qt_key}`: "Qt" for QtWebKit, "QtWebEngine" for
# QtWebEngine. * `{qt_version}`: The underlying Qt version. *
# `{upstream_browser_key}`: "Version" for QtWebKit, "Chrome" for
# QtWebEngine. * `{upstream_browser_version}`: The corresponding
# Safari/Chrome version. * `{qutebrowser_version}`: The currently
# running qutebrowser version.  The default value is equal to the
# unchanged user agent of QtWebKit/QtWebEngine.  Note that the value
# read from JavaScript is always the global value. With QtWebEngine
# between 5.12 and 5.14 (inclusive), changing the value exposed to
# JavaScript requires a restart.
# Type: FormatString
# config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}; rv:90.0) Gecko/20100101 Firefox/90.0', 'https://accounts.google.com/*')

# User agent to send.  The following placeholders are defined:  *
# `{os_info}`: Something like "X11; Linux x86_64". * `{webkit_version}`:
# The underlying WebKit version (set to a fixed value   with
# QtWebEngine). * `{qt_key}`: "Qt" for QtWebKit, "QtWebEngine" for
# QtWebEngine. * `{qt_version}`: The underlying Qt version. *
# `{upstream_browser_key}`: "Version" for QtWebKit, "Chrome" for
# QtWebEngine. * `{upstream_browser_version}`: The corresponding
# Safari/Chrome version. * `{qutebrowser_version}`: The currently
# running qutebrowser version.  The default value is equal to the
# unchanged user agent of QtWebKit/QtWebEngine.  Note that the value
# read from JavaScript is always the global value. With QtWebEngine
# between 5.12 and 5.14 (inclusive), changing the value exposed to
# JavaScript requires a restart.
# Type: FormatString
# config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99 Safari/537.36', 'https://*.slack.com/*')

# Load images automatically in web pages.
# Type: Bool
config.set('content.images', True, 'chrome-devtools://*')

# Load images automatically in web pages.
# Type: Bool
config.set('content.images', True, 'devtools://*')

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'chrome-devtools://*')

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'devtools://*')

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'chrome://*/*')

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'qute://*/*')

## --- GitHub Fixes & Optimization ---

# 1. Ensure JavaScript is enabled (required for modern GitHub UI)
config.set('content.javascript.enabled', True, 'github.com')
config.set('content.blocking.enabled', False, 'github.com')

c.qt.args = [
    'enable-features=dns-over-https<DoHTrial',
    'force-fieldtrials=DoHTrial/Group1',
    'force-fieldtrial-params=DoHTrial.Group1:server/https%3A%2F%2Fcloudflare-dns.com%2Fdns-query/method/POST'
    'ignore-gpu-blocklist', 'enable-gpu-rasterization', 'enable-accelerated-video-decode'
]

# Position of the tab bar.
# Type: Position
# Valid values:
#   - top
#   - bottom
#   - left
#   - right
c.tabs.position = 'left'

# Width (in pixels or as percentage of the window) of the tab bar if
# it's vertical.
# Type: PercOrInt
c.tabs.width = '9%'

# Minimum width (in pixels) of tabs (-1 for the default minimum size
# behavior). This setting only applies when tabs are horizontal. This
# setting does not apply to pinned tabs, unless `tabs.pinned.shrink` is
# False.
# Type: Int
c.tabs.min_width = -1

# Maximum width (in pixels) of tabs (-1 for no maximum). This setting
# only applies when tabs are horizontal. This setting does not apply to
# pinned tabs, unless `tabs.pinned.shrink` is False. This setting may
# not apply properly if max_width is smaller than the minimum size of
# tab contents, or smaller than tabs.min_width.
# Type: Int
c.tabs.max_width = 1

# Page to open if :open -t/-b/-w is used without URL. Use `about:blank`
# for a blank page.
# Type: FuzzyUrl
c.url.default_page = 'https://www.google.com/'

# custom themes css
# c.content.user_stylesheets = ["~/.config/qutebrowser/styles/youtube-tweaks.css"]
c.content.user_stylesheets = ["~/.config/qutebrowser/styles/github-materia.css"]

# Search engines which can be used via the address bar.  Maps a search
# engine name (such as `DEFAULT`, or `ddg`) to a URL with a `{}`
# placeholder. The placeholder will be replaced by the search term, use
# `{{` and `}}` for literal `{`/`}` braces.  The following further
# placeholds are defined to configure how special characters in the
# search terms are replaced by safe characters (called 'quoting'):  *
# `{}` and `{semiquoted}` quote everything except slashes; this is the
# most   sensible choice for almost all search engines (for the search
# term   `slash/and&amp` this placeholder expands to `slash/and%26amp`).
# * `{quoted}` quotes all characters (for `slash/and&amp` this
# placeholder   expands to `slash%2Fand%26amp`). * `{unquoted}` quotes
# nothing (for `slash/and&amp` this placeholder   expands to
# `slash/and&amp`). * `{0}` means the same as `{}`, but can be used
# multiple times.  The search engine named `DEFAULT` is used when
# `url.auto_search` is turned on and something else than a URL was
# entered to be opened. Other search engines can be used by prepending
# the search engine name to the search term, e.g. `:open google
# qutebrowser`.
# Type: Dict
c.url.searchengines = {'DEFAULT': 'https://www.google.com/?q={}'}

# Page(s) to open at the start.
# Type: List of FuzzyUrl, or FuzzyUrl
c.url.start_pages = 'https://www.google.com'

# Set the main window background to transparent.  This allows having a
# transparent tab- or statusbar (might require a compositor such as
# picom). However, it breaks some functionality such as dmenu embedding
# via its `-w` option. On some systems, it was additionally reported
# that main window transparency negatively affects performance.  Note
# this setting only affects windows opened after setting it.
# Type: Bool
c.window.transparent = True

# palette = {
#     "background": "#000b1e",
#     "backgroundalt": "#B3000b1e",
#     "foreground": "#0abdc6",
#     "color0": "#B3123e7c", 
#     "color1": "#ff0000",
#     "color2": "#ea00d9",
#     "color3": "#f57800",
#     "color4": "#123e7c",
#     "color5": "#711c91",
#     "color6": "#0abdc6",
#     "color7": "#d7d7d5",
#     "color8": "#1c61c2",
#     "color9": "#ff0000",
#     "color10": "#d300c4",
#     "color11": "#f57800",
#     "color12": "#00ff00",
#     "color13": "#711c91",
#     "color14": "#0abdc6",
#     "color15": "#d7d7d5"
#         }

#c colors for the status bar on the bottom
c.colors.statusbar.normal.bg = palette["backgroundalt"]
c.colors.statusbar.command.bg = palette["backgroundalt"]
c.colors.statusbar.command.fg = palette["foreground"]
c.colors.statusbar.normal.fg = palette["color14"]
c.colors.statusbar.passthrough.fg = palette["color14"]
c.colors.statusbar.url.fg = palette["color2"]
c.colors.statusbar.url.success.https.fg = palette["color2"]
c.colors.statusbar.url.hover.fg = palette["color2"]

# colors for the tabs bar
c.colors.tabs.even.bg = palette["color0"] # transparent tabs!!
c.colors.tabs.odd.bg = palette["color0"]
c.colors.tabs.bar.bg = palette["color0"]
c.colors.tabs.even.fg = palette["color0"]
c.colors.tabs.odd.fg = palette["color0"]
c.colors.tabs.selected.even.bg = palette["foreground"]
c.colors.tabs.selected.odd.bg = palette["foreground"]
c.colors.tabs.selected.even.fg = palette["background"]
c.colors.tabs.selected.odd.fg = palette["background"]

# colors for tab indicator
c.colors.tabs.indicator.start = palette["color2"]
c.colors.tabs.indicator.stop = palette["color5"]
c.colors.tabs.indicator.error = palette["color1"]
