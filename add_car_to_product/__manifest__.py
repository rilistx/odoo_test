# -*- coding: utf-8 -*-
{
	'name' : "Add Car To Product",
	'category': 'add_car_to_product',
	'application': True,
	'installable': True,
	'sequence': 1,
	'version': '1.0',
	'license': 'LGPL-3',
	'depends': [
		'fleet',
		'repair',
		'product',
		'website_sale',
	],
	'demo': [],
	'data' : [
		# Security
		'security/security.xml',
		'security/ir.model.access.csv',
		# Views
		'views/fleet_vehicle_model_views.xml',
		'views/product_template_views.xml',
		'views/product_product_views.xml',
		'views/website_sale_templates.xml',
	],
    'assets': {
		'web.assets_backend': [
			'add_car_to_product/static/src/**/*.scss',
		],
        'web.assets_frontend': [
            'add_car_to_product/static/src/**/*.js',
        ],
    },
}
