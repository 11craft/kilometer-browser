from abc import abstractmethod

from enaml.components.control import Control, AbstractTkControl
from enaml.backends.qt.qt import QtWebKit
from enaml.backends.qt.qt_control import QtControl

from traits.api import Instance, Str


class AbstractTkWebView(AbstractTkControl):
    """
    The abstract toolkit WebView interface.
    """

    @abstractmethod
    def shell_url_changed(self, source):
        """
        Change handler for 'url' attribute of shell object.
        """
        raise NotImplementedError


class WebView(Control):
    """
    A widget for displaying a WebKit view.
    """

    url = Str

    abstract_obj = Instance(AbstractTkWebView)


class QtWebView(QtControl, AbstractTkWebView):
    """
    A Qt implementation of WebView.
    """

    # Setup
    # =====

    def create(self, parent):
        """
        Creates the underlying widget.
        """
        self.widget = QtWebKit.QWebView(parent)

    def initialize(self):
        """
        Initialize the attributes of the control.
        """
        super(QtWebView, self).initialize()

    def bind(self):
        """
        Bind toolkit events to handlers on this object.
        """
        super(QtWebView, self).bind()
        widget = self.widget
        widget.urlChanged.connect(self.on_url_changed)

    # Shell object change handlers
    # ----------------------------

    def shell_url_changed(self, url):
        print 'Loading', url
        self.widget.load(url)

    # Signal handlers
    # ---------------

    def on_url_changed(self, url):
        url = url.toString()
        print 'URL is now', url
        self.shell_obj.url = url


if __name__ == '__main__':
    import kmb.components
    import enaml
    with enaml.imports():
        from webview_test import Main
    main_window = Main()
    main_window.show()
