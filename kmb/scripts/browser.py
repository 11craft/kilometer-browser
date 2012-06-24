import enaml

import kmb.components


def main():
    with enaml.imports():
        from kmb.components.browser import BrowserMainWindow
    main_window = BrowserMainWindow()
    main_window.show()


if __name__ == '__main__':
    main()
