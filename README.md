# UMH Connector for Odoo

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Odoo](https://img.shields.io/badge/Odoo-17.0-purple)](https://www.odoo.com)

Connect your Odoo contacts to **[Unified Messenger Hub](https://messengerhub.de)** — send and receive WhatsApp & Telegram messages directly from the contact card.

---

## What it does

- **Adds "WhatsApp-Nummer" and "Telegram Chat-ID" fields** to every contact (`res.partner`)
- **Two Smart Buttons** in the contact form header — WhatsApp and Telegram
- One click opens the matching UMH conversation in a new browser tab
- Configurable UMH instance URL under **Settings → General Settings**

## Requirements

- Odoo 17.0 (Community or Enterprise)
- An active account at [messengerhub.de](https://messengerhub.de)

## Installation

1. Download or clone this repository
2. Copy the `umh_connector` folder into your Odoo `addons` path
3. Activate developer mode, then **Apps → Update Apps List**
4. Search for **UMH Connector** → Install
5. Go to **Settings → General Settings → UMH Connector** → enter your UMH instance URL

## How it works

### WhatsApp
- **The "Open WhatsApp" button always requires `x_whatsapp_number` to be filled in** — even if it's the same as phone/mobile. There is no fallback here on purpose: a business-initiated WhatsApp template costs money, and silently sending it to a landline number that isn't on WhatsApp means the customer never receives it while you wait for a reply that will never come.
- **Incoming-message recognition** (the "known customer" badge in UMH, and linking new leads/quotes/tickets/orders to the right contact) is more lenient: it checks `x_whatsapp_number` first, then falls back to the standard phone/mobile fields — there's no sending risk there, only lookup.
- Make sure whichever number is used is stored in a recognizable format (e.g. `+49 123 456789`).

### Telegram
The module adds a `x_telegram_chat_id` field. The numeric Chat-ID is visible in the UMH contact profile and must be entered once per contact — it is **not** the same as the Telegram @username.

## License

GNU General Public License v3.0 — see [LICENSE](LICENSE)

## Author

**Vitalij Haun IT HUB** · [messengerhub.de](https://messengerhub.de) · [info@messengerhub.de](mailto:info@messengerhub.de)
