# -*- coding: utf-8 -*-
from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    umh_connector_url = fields.Char(
        string='UMH App-URL',
        config_parameter='umh_connector.url',
        default='https://saas.messengerhub.de',
        help='URL Ihrer Unified Messenger Hub Instanz.',
    )
