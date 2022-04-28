# Copyright 2019 LevelPrime
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

{
    "name": "POS Custom Aychi Skit",
    "summary": "Add button to set priority to orders.",
    "author": "Pedro Guirao, Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/pos",
    "category": "Point of Sale",
    "maintainers": ["pedroguirao"],
    "version": "14.0.1.0.0",
    "license": "LGPL-3",
    "depends": ["pos_restaurant",
                #"pos_line_priority_srikesh"
                ],
    "data": [
        'views/pos_custom_templates.xml',
        #'views/assets.xml',
        #'views/pos_session.xml',
             ],
    "qweb": [
        #"static/src/xml/multiprint.xml",
             ],
}
