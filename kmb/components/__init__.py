from enaml.backends.qt.constructors import QT_CONSTRUCTORS
from enaml.core.constructor import Constructor


def new_web_view():
    from .webview import WebView
    return WebView

def new_qt_web_view():
    from .webview import QtWebView
    return QtWebView

QT_CONSTRUCTORS['WebView'] = Constructor(new_web_view, new_qt_web_view)
