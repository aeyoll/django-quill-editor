DEFAULT_CONFIG = {
    "theme": "snow",
    "modules": {
        "syntax": True,
        "toolbar": [
            [
                {"font": []},
                {"header": []},
                {"align": []},
                "bold",
                "italic",
                "underline",
                "strike",
                "blockquote",
                {"color": []},
                {"background": []},
            ],
            ["code-block", "link", "image", "video"],
            ["clean"],
        ],
        # quill-image-compress
        "imageCompressor": {
            "quality": 0.8,
            "maxWidth": 2000,
            "maxHeight": 2000,
            "imageType": "image/jpeg",
            "debug": False,
            "suppressErrorLogging": True,
        },
    },
}
MEDIA_JS = [
    'django_quill/vendor/highlight.min.js',
    'django_quill/vendor/quill.js',
    'django_quill/vendor/quill.imageCompressor.min.js',
    'django_quill/django_quill.js',
]
MEDIA_CSS = [
    'django_quill/vendor/quill.snow.css',
    'django_quill/vendor/highlight.css',
    'django_quill/django_quill.css',
]
