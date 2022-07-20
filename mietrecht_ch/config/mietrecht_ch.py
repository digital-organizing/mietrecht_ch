from __future__ import unicode_literals
from frappe import _


def get_data():
    return[
        {
            "label": _("Heiz-und Nebenkosten"),
            "icon": "fa fa-money",
            "items": [
                {
                    "type": "doctype",
                    "name": "Heizolpreise",
                    "label": _("Heizolpreise Liste"),
                    "description": _("Heizolpreise Liste")
                },
                {
                    "type": "doctype",
                    "name": "Heizolpreise",
                    "label": _("Neue Heizolpreise"),
                    "description": _("Neue Heizolpreise"),
                    "link": _("Form/Heizolpreise/New Heizolpreise 1")
                },
                {
                    "type": "doctype",
                    "name": "Heizgradtagzahlen",
                    "label": _("Heizgradtagzahlen Liste"),
                    "description": _("Heizgradtagzahlen Liste")
                },
                {
                    "type": "doctype",
                    "name": "Heizgradtagzahlen",
                    "label": _("Neue Heizgradtagzahlen"),
                    "description": _("Neue Heizgradtagzahlen"),
                    "link": _("Form/Heizgradtagzahlen/New Heizgradtagzahlen 1")
                }
            ]
        },
        {
            "label": _("Lebensdauer"),
            "icon": "fa fa-money",
            "items": [
                {
                    "type": "doctype",
                    "name": "LebensdauerGruppe",
                    "label": _("Gruppe Liste"),
                    "description": _("Gruppe Liste")
                },
                {
                    "type": "doctype",
                    "name": "LebensdauerGruppe",
                    "label": _("Neue Gruppe"),
                    "description": _("Neue Gruppe"),
                    "link": _("Form/LebensdauerGruppe/New LebensdauerGruppe 1")
                },
                {
                    "type": "doctype",
                    "name": "LebensdauerObjekte",
                    "label": _("Objekte Liste"),
                    "description": _("Objekte Liste")
                },
                {
                    "type": "doctype",
                    "name": "LebensdauerObjekte",
                    "label": _("Neue Objekte"),
                    "description": _("Neue Objekte"),
                    "link": _("Form/LebensdauerObjekte/New LebensdauerObjekte 1")
                },
            ]
        },
        {
            "label": _("Landesindex"),
            "icon": "fa fa-money",
            "items": [
                {
                    "type": "doctype",
                    "name": "Aktualisierungsdaten",
                    "label": _("Aktualisierungsdaten Liste"),
                    "description": _("Aktualisierungsdaten Liste")
                },
                {
                    "type": "doctype",
                    "name": "Aktualisierungsdaten",
                    "label": _("Neue Aktualisierungsdaten"),
                    "description": _("Neue Aktualisierungsdaten"),
                    "link": _("Form/Aktualisierungsdaten/New Aktualisierungsdaten 1")
                },
                {
                    "type": "doctype",
                    "name": "Teuerung",
                    "label": _("Teuerung Liste"),
                    "description": _("Teuerung Liste")
                },
                {
                    "type": "doctype",
                    "name": "Teuerung",
                    "label": _("Neue Teuerung"),
                    "description": _("Neue Teuerung"),
                    "link": _("Form/Teuerung/New Teuerung 1")
                },
                {
                    "type": "doctype",
                    "name": "TeuerungBasis",
                    "label": _("Teuerung Basis Liste"),
                    "description": _("Teuerung Basis Liste")
                },
                {
                    "type": "doctype",
                    "name": "TeuerungBasis",
                    "label": _("Neue TeuerungBasis"),
                    "description": _("Neue Teuerung Basis"),
                    "link": _("Form/TeuerungBasis/New TeuerungBasis 1")
                }
            ]
        },
        {
            "label": _("Hypo-Referenzzins"),
            "icon": "fa fa-money",
            "items": [
                {
                    "type": "doctype",
                    "name": "HypoReferenzzins",
                    "label": _("Hypo-Referenzzins Liste"),
                    "description": _("Hypo-Referenzzins Liste")
                },
                {
                    "type": "doctype",
                    "name": "HypoReferenzzins",
                    "label": _("Neue Hypo-Referenzzins"),
                    "description": _("Neue Hypo-Referenzzins"),
                    "link": _("Form/HypoReferenzzins/New HypoReferenzzins 1")
                },
                {
                    "type": "doctype",
                    "name": "Hypothekarzins",
                    "label": _("Hypothekarzins Liste"),
                    "description": _("Hypothekarzins Liste")
                },
                {
                    "type": "doctype",
                    "name": "Hypothekarzins",
                    "label": _("Neue Hypothekarzins"),
                    "description": _("Neue Hypothekarzins"),
                    "link": _("Form/Hypothekarzins/New Hypothekarzins 1")
                },
                {
                    "type": "doctype",
                    "name": "Hypothekarzins Aktualisierungsdaten",
                    "label": _("Nächste Hypothekarzins Aktualisierungsdaten"),
                    "description": _("Nächste Hypothekarzins Aktualisierungsdaten"),
                    "link": _("Form/Hypothekarzins Aktualisierungsdaten")
                }
            ]
        },
        {
            "label": _("Einstellungen"),
            "icon": "fa fa-money",
            "items": [
                {
                    "type": "doctype",
                    "name": "Wetterstationen",
                    "label": _("Wetterstationen Liste"),
                    "description": _("Wetterstationen Liste")
                },
                {
                    "type": "doctype",
                    "name": "Wetterstationen",
                    "label": _("Neue Wetterstationen"),
                    "description": _("Neue Wetterstationen"),
                    "link": _("Form/Wetterstationen/New Wetterstationen 1")
                }
            ]
        },
        {
            "label": _("Stichworte"),
            "icon": "fa fa-money",
            "items": [
                {
                    "type": "doctype",
                    "name": "Stichworte",
                    "label": _("Stichworte Liste"),
                    "description": _("Stichworte Liste")
                },
                {
                    "type": "doctype",
                    "name": "Stichworte",
                    "label": _("Neue Stichworte"),
                    "description": _("Neue Stichworte"),
                    "link": _("Form/Stichworte/New Stichworte 1")
                }
            ]
        },
        {
            "label": _("PAK"),
            "icon": "fa fa-money",
            "items": [
                {
                    "type": "doctype",
                    "name": "Voucher",
                    "label": _("Voucher Liste"),
                    "description": _("Voucher Liste")
                },
                {
                    "type": "doctype",
                    "name": "Pak",
                    "label": _("Pak Liste"),
                    "description": _("Pak Liste")
                }
            ]
        },
        {
            "label": _("Entscheid"),
            "icon": "fa fa-money",
            "items": [
                {
                    "type": "doctype",
                    "name": "Entscheid",
                    "label": _("Entscheid Liste"),
                    "description": _("Entscheid Liste")
                },
                {
                    "type": "doctype",
                    "name": "Entscheid",
                    "label": _("Neue Entscheid"),
                    "description": _("Neue Entscheid"),
                    "link": _("Form/Entscheid/New Entscheid 1")
                }
            ]
        },
        {
            "label": _("Gesetze"),
            "icon": "fa fa-money",
            "items": [
                {
                    "type": "doctype",
                    "name": "Gesetze",
                    "label": _("Gesetze Liste"),
                    "description": _("Gesetze Liste")
                },
                {
                    "type": "doctype",
                    "name": "Gesetze",
                    "label": _("Neue Gesetze"),
                    "description": _("Neue Gesetze"),
                    "link": _("Form/Gesetze/New Gesetze 1")
                }
            ]
        }
    ]