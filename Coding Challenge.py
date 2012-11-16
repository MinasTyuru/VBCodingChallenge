from re import sub

def normalize(path):
    """Normalize a file path.

    All single dot components of the path must be removed. For
    example, "foo/./bar" should be normalized to "foo/bar".
    
    All double dots components of the path must be removed,
    along with their parent directory, if any.  For example,
    "foo/bar/../baz" should be normalized to "foo/baz".

    >>> normalize("foo/./bar")
    'foo/bar'
    >>> normalize("foo/bar/../baz")
    'foo/baz'
    >>> normalize("foo//bar")
    'foo//bar'

    >>> normalize("/..")
    ''
    >>> normalize("/../")
    '/'
    >>> normalize("foo/..")
    ''

    #No-ops
    >>> normalize(".bar")
    '.bar'
    >>> normalize("/..bar")
    '/..bar'
    >>> normalize("/..bar/")
    '/..bar/'

    """

    #Remove double-dot components
    path = sub('/[^/]+/\.\.(?=/|$)', '', path) #Match '/bar/..'
    path = sub('([^/]+/)?\.\./', '', path) #Match 'bar/../' or beginning '../'
    path = sub('^[^/]*/?\.\.$', '', path) #Match beginning 'bar/..' and '..'
    
    #Remove single-dot components
    path = sub('(?=/|^)\./', '', path) #Match ./
    path = sub('/\.(?=/|$)', '', path) #Match /.

    return path

while True:
    print(normalize(input()))
