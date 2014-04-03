from django.conf import settings


if settings.DEBUG and getattr(settings, 'HIDE_TECHNICAL_ERROR_INFO', True):
    # Override debug templates.

    from django.views import debug

    debug.TECHNICAL_404_TEMPLATE = debug.TECHNICAL_404_TEMPLATE.replace(
        '</style>',
        '#short_message {display: none;}'
        'body.hidden * {display: none;} '
        'body.hidden #short_message {display: block;}'
        '</style>'
    ).replace(
        '<body>',
        '<body onkeypress="if (event.keyCode == 101 || event.which == 101) '
        '{ document.body.className = \'\'; }" class="hidden">'
        '<h1 id="short_message">Page not found <span>(404)</span></h1>'
    )
    debug.TECHNICAL_500_TEMPLATE = debug.TECHNICAL_500_TEMPLATE.replace(
        '</style>',
        '#short_message {display: none;} body.hidden * {display: none;} '
        'body.hidden #short_message {display: block;}</style>'
    ).replace(
        '<body>',
        '<body onkeypress="if (event.keyCode == 101 || event.which == 101) '
        '{ document.body.className = \'\'; }" class="hidden">'
        '<h1 id="short_message">Server error <span>(500)</span></h1>'
    )
