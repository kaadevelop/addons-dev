# Copyright 2018 Kolushov Alexandr <https://it-projects.info/team/KolushovAlexandr>
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).
{
    "name": """POS Esign Event Registration""",
    "summary": """Ask Esign For Event Registration in POS""",
    "category": "Point of Sale",
    # "live_test_url": "http://apps.it-projects.info/shop/product/DEMO-URL?version=11.0",
    "images": [],
    "version": "11.0.1.0.0",
    "application": False,

    "author": "IT-Projects LLC, Kolushov Alexandr",
    "support": "apps@it-projects.info",
    "website": "https://it-projects.info/team/KolushovAlexandr",
    "license": "LGPL-3",
    # "price": 9.00,
    # "currency": "EUR",

    "depends": [
        "pos_esign_request",
        "pos_event_registration",
        "website_sign"
    ],
    "external_dependencies": {"python": [], "bin": []},
    "data": [
        "views/views.xml",
        "views/assets.xml"
    ],
    "demo": [
    ],
    "qweb": [
        "static/src/xml/pos_esign.xml",
    ],

    "post_load": None,
    "pre_init_hook": None,
    "post_init_hook": None,
    "uninstall_hook": None,

    "auto_install": False,
    "installable": True,

    # "demo_title": "POS Esign Event Registration",
    # "demo_addons": [
    # ],
    # "demo_addons_hidden": [
    # ],
    # "demo_url": "DEMO-URL",
    # "demo_summary": "Ask Esign For Event Registration in POS",
    # "demo_images": [
    #    "images/MAIN_IMAGE",
    # ]
}
