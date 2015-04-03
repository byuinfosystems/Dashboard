# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428104231.514244
_enable_loop = True
_template_filename = 'C:\\Users\\benwillard17\\Documents\\GitHub\\Sprint3\\test_dmp\\homepage\\templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['meta', 'content_left', 'content_center', 'content_right', 'content', 'jumbotron', 'title']


from django_mako_plus.controller import static_files 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        self = context.get('self', UNDEFINED)
        def content_center():
            return render_content_center(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        def jumbotron():
            return render_jumbotron(context._locals(__M_locals))
        def title():
            return render_title(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        def content_left():
            return render_content_left(context._locals(__M_locals))
        def content_right():
            return render_content_right(context._locals(__M_locals))
        def meta():
            return render_meta(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n')
        static_renderer = static_files.StaticRenderer(self) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['static_renderer'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\r\n\r\n<!DOCTYPE html>\r\n<html>\r\n  \r\n  ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'meta'):
            context['self'].meta(**pageargs)
        

        __M_writer('\r\n  \r\n  <head>\r\n  \r\n  ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('\r\n\r\n\r\n')
        __M_writer('    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>\r\n\r\n    <!-- Latest compiled and minified CSS (BOOTSTRAP) -->\r\n    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.min.css">\r\n\r\n    <!-- Latest compiled and minified JavaScript -->\r\n    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/js/bootstrap.min.js"></script>\r\n\r\n    <!-- add a jquery form plug in for ajax calls - http://malsup.com/jquery/form/#download -->\r\n    <script src="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/jquery.form.js"></script>\r\n\r\n    <!-- add a jquery form plug in for modals - https://github.com/doconix/jquery.loadmodal.js/blob/master/jquery.loadmodal.js -->\r\n    <script src="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/jquery.loadmodal.js"></script>\r\n\r\n    <!--Favicon -->\r\n    <link rel="icon" type="image/icon" href="/static/homepage/media/favicon.ico" />\r\n\r\n\r\n')
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_css(request, context)  ))
        __M_writer('\r\n\r\n  </head>\r\n  <body>\r\n\r\n')
        __M_writer('    <header class="navbar navbar-inverse navbar-fixed-top">\r\n      <div class="container-fluid">\r\n        <!-- Brand and toggle get grouped for better mobile display -->\r\n        <div class="navbar-header">\r\n          <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">\r\n            <span class="sr-only">Toggle navigation</span>\r\n            <span class="icon-bar"></span>\r\n            <span class="icon-bar"></span>\r\n            <span class="icon-bar"></span>\r\n          </button>\r\n          <a class="navbar-brand" href="/homepage/index">CHF</a>\r\n        </div>\r\n\r\n        <!-- Collect the nav links, forms, and other content for toggling -->\r\n        <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">\r\n          <ul class="nav navbar-nav">\r\n')
        if request.user.is_authenticated():
            __M_writer('            <li><a href="/homepage/productlist"><span class ="glyphicon glyphicon-list"></span>  Products</a></li>\r\n            <li><a href="/homepage/itemlist"><span class ="glyphicon glyphicon-list"></span>  Rentals</a></li>\r\n            <li><a href="/homepage/return"><span class ="glyphicon glyphicon-transfer"></span>  Returns</a></li>\r\n            <li><a href="/homepage/overdue"><span class ="glyphicon glyphicon-transfer"></span>  Reports</a></li>\r\n            <li><a href="/homepage/festivals"><span class ="glyphicon glyphicon-transfer"></span>  Festivals</a></li>\r\n            <a href="/homepage/links/">Links</a>\r\n')
        else:
            __M_writer('            <li><a href="/homepage/productlist"><span class ="glyphicon glyphicon-list"></span>  Products</a></li>\r\n            <li><a href="/homepage/itemlist"><span class ="glyphicon glyphicon-list"></span>  Rentals</a></li>\r\n            <li><a href="/homepage/festivals"><span class ="glyphicon glyphicon-transfer"></span>  Festivals</a></li>\r\n\r\n')
        __M_writer('          </ul>\r\n\r\n')
        if request.user.is_authenticated():
            __M_writer('          <ul class="nav navbar-nav navbar-right">\r\n            <li class =""><a id="button_view_shopping_cart" href="/homepage/shoppingcart/"><span class ="glyphicon glyphicon-shopping-cart"></span>  Shopping Cart</a></li>\r\n            <li class="dropdown">\r\n              <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-expanded="false"><span class="glyphicon glyphicon-user"></span> ')
            __M_writer(str(request.user.get_full_name() ))
            __M_writer(' <span class="caret"></span></a>\r\n              <ul class="dropdown-menu" role="menu">\r\n                <li><a href="/homepage/accounts/">My Account</a></li>\r\n                <li class="divider"></li>\r\n                <li><a href="/homepage/logout">Log Out</a></li>\r\n              </ul>\r\n            </li>\r\n          </ul>\r\n')
        else:
            __M_writer('          <ul class="nav navbar-nav navbar-right">\r\n            <li class =""><a id="button_view_shopping_cart" href="/homepage/shoppingcart/"><span class ="glyphicon glyphicon-shopping-cart"></span>  Shopping Cart</a></li>\r\n            <li class="dropdown">\r\n              <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-expanded="false"><span class="glyphicon glyphicon-user"></span> My Account <span class="caret"></span></a>\r\n              <ul class="dropdown-menu" role="menu">\r\n                <li><a href="/homepage/users.newaccount/" class="btn btn-block btn-link">Create Account</a></li>\r\n                <li class="divider"></li>\r\n                <li><button id="show_login_dialog" class="btn btn-block btn-link">Login</button></li>\r\n              </ul>\r\n            </li>\r\n          </ul>\r\n')
        __M_writer('\r\n\r\n        </div><!-- /.navbar-collapse -->\r\n      </div><!-- /.container-fluid -->\r\n    </header>\r\n\r\n')
        __M_writer('    <div class = "jumbotron">\r\n      <div class = "container-fluid">\r\n        <div class="row">\r\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'jumbotron'):
            context['self'].jumbotron(**pageargs)
        

        __M_writer('\r\n        </div>\r\n      </div>\r\n    </div>\r\n\r\n')
        __M_writer('    <div class="container">\r\n      <div class="row-fluid">\r\n        <div class="col-xs-12 bg-default">\r\n          ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n        </div>\r\n      </div>\r\n    </div>\r\n\r\n')
        __M_writer('    <div class="container">\r\n      <div class="row-fluid">\r\n        <div class="col-xs-4 bg-default">\r\n          ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_left'):
            context['self'].content_left(**pageargs)
        

        __M_writer('\r\n        </div>\r\n        <div class="col-xs-4 bg-default">\r\n          ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_center'):
            context['self'].content_center(**pageargs)
        

        __M_writer('\r\n        </div>\r\n        <div class="col-xs-4 bg-default">\r\n          ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_right'):
            context['self'].content_right(**pageargs)
        

        __M_writer('\r\n        </div>\r\n      </div>\r\n    </div>\r\n\r\n')
        __M_writer('    <footer class = "navbar navbar-inverse navbar-fixed-bottom">\r\n      <div class="container">\r\n        <p class = "navbar-text pull-left">&copy; 2015 Colonial Heritage Foundation</p>\r\n        \r\n        <p class = "navbar-text pull-right"><a href="/homepage/links/">Links</a> | Terms of Use | Privacy</p>\r\n      </div>\r\n    </footer>\r\n\r\n')
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_js(request, context)  ))
        __M_writer('\r\n\r\n  </body>\r\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_meta(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def meta():
            return render_meta(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <meta name="" description="" charset="UTF-8">\r\n  ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_left():
            return render_content_left(context)
        __M_writer = context.writer()
        __M_writer('\r\n          ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_center():
            return render_content_center(context)
        __M_writer = context.writer()
        __M_writer('\r\n          ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_right(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_right():
            return render_content_right(context)
        __M_writer = context.writer()
        __M_writer('\r\n          ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n              Center Content\r\n          ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_jumbotron(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def jumbotron():
            return render_jumbotron(context)
        __M_writer = context.writer()
        __M_writer('\r\n              <h1>WELCOME!</h1>\r\n              <p>This is where the description goes.</p>\r\n              <a class = "btn btn-success">Success!</a>\r\n              <a class = "btn btn-primary">Primary</a>\r\n            ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <title>Colonial Heritage Foundation</title>\r\n  ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "base.htm", "line_map": {"133": 138, "193": 16, "139": 142, "16": 4, "145": 142, "18": 0, "151": 146, "157": 146, "163": 127, "40": 2, "41": 4, "42": 5, "199": 193, "46": 5, "175": 113, "51": 12, "181": 113, "56": 18, "57": 22, "58": 31, "59": 31, "60": 34, "61": 34, "62": 41, "63": 41, "64": 41, "65": 47, "66": 63, "67": 64, "68": 70, "69": 71, "70": 76, "71": 78, "72": 79, "73": 82, "74": 82, "75": 90, "76": 91, "77": 103, "78": 110, "83": 118, "84": 124, "89": 129, "90": 135, "95": 139, "187": 16, "100": 143, "105": 147, "106": 153, "107": 162, "108": 162, "109": 162, "115": 10, "169": 127, "121": 10, "127": 138}, "source_encoding": "ascii", "filename": "C:\\Users\\benwillard17\\Documents\\GitHub\\Sprint3\\test_dmp\\homepage\\templates/base.htm"}
__M_END_METADATA
"""
