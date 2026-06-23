# -*- coding: utf-8 -*-
{
    'name': 'UMH Connector — WhatsApp & Telegram',
    'version': '17.0.1.0.0',
    'category': 'Sales/CRM',
    'summary': 'WhatsApp & Telegram Nachrichten direkt aus der Kundenkarte via Unified Messenger Hub',
    'description': """
UMH Connector für Odoo
=======================
Verbindet Odoo-Kunden mit dem Unified Messenger Hub (UMH) — WhatsApp & Telegram
direkt aus der Kontaktkarte heraus.

Funktionen
----------
- Legt automatisch das Feld "Telegram Chat-ID" auf Kontakten an
- Zwei Smart-Buttons (WhatsApp, Telegram) öffnen die passende Konversation in UMH
- WhatsApp-Erkennung läuft über die bestehenden Telefon-/Mobil-Felder
- UMH-URL einmalig unter Einstellungen → Allgemeine Einstellungen konfigurierbar
""",
    'author': 'Vitalij Haun IT HUB',
    'website': 'https://messengerhub.de',
    'license': 'GPL-3',
    'depends': ['base', 'contacts'],
    'data': [
        'views/res_partner_views.xml',
        'views/res_config_settings_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
