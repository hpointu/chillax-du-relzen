set background=dark

highlight clear
if exists("syntax_on")
    syntax reset
endif
let g:colors_name="chillax_du_relzen"

{{#scheme}}
hi {{name}} {{#conf.fg}}ctermfg={{conf.fg}}{{/conf.fg}} {{#conf.bg}}ctermbg={{conf.bg}}{{/conf.bg}} {{#conf.fg_gui}}guifg={{conf.fg_gui}}{{/conf.fg_gui}} {{#conf.bg_gui}}guibg={{conf.bg_gui}}{{/conf.bg_gui}} {{#conf.style}}cterm={{conf.style}}{{/conf.style}}
{{/scheme}}
