# -*- coding: utf-8 -*-
from urllib.parse import quote

from odoo import fields, models
from odoo.exceptions import UserError

DEFAULT_UMH_URL = 'https://saas.messengerhub.de'


class ResPartner(models.Model):
    _inherit = 'res.partner'

    x_whatsapp_number = fields.Char(
        string='WhatsApp-Nummer',
        help='Wird für den WhatsApp-Button benötigt — auch eintragen, wenn identisch mit Telefon/Mobil. '
             'Ohne dieses Feld kein automatischer Versand, damit nie versehentlich an eine '
             'Festnetznummer ohne WhatsApp geschrieben wird. Format: +49123456789',
    )

    x_telegram_chat_id = fields.Char(
        string='Telegram Chat-ID',
        help='Numerische Telegram Chat-ID aus dem UMH-Kontaktprofil (z.B. 123456789). '
             'Nicht der @Benutzername.',
    )

    def _umh_base_url(self):
        url = self.env['ir.config_parameter'].sudo().get_param(
            'umh_connector.url', DEFAULT_UMH_URL,
        )
        return (url or DEFAULT_UMH_URL).rstrip('/')

    def action_open_umh_whatsapp(self):
        self.ensure_one()
        if not self.x_whatsapp_number:
            raise UserError(
                'Keine WhatsApp-Nummer hinterlegt — bitte zuerst eintragen (auch wenn identisch mit '
                'Telefon/Mobil). Ohne dieses Feld kein Versand, damit nie versehentlich an eine '
                'Festnetznummer ohne WhatsApp geschrieben wird.'
            )
        url = f'{self._umh_base_url()}/inbox?phone={quote(self.x_whatsapp_number)}'
        return {
            'type': 'ir.actions.act_url',
            'url': url,
            'target': 'new',
        }

    def action_open_umh_telegram(self):
        self.ensure_one()
        if not self.x_telegram_chat_id:
            raise UserError('Keine Telegram Chat-ID hinterlegt — bitte zuerst eintragen.')
        url = f'{self._umh_base_url()}/inbox?telegram={quote(self.x_telegram_chat_id)}'
        return {
            'type': 'ir.actions.act_url',
            'url': url,
            'target': 'new',
        }
