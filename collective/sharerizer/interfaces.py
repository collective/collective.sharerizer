from zope.interface import Interface

class ISharerizerBrowserLayer(Interface):
    """Marker applied to the request during traversal of sites that
       have collective.sharerizer installed
    """
