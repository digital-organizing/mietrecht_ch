import frappe
from mietrecht_ch.models.calculatorMasterResult import CalculatorMasterResult
from mietrecht_ch.models.calculatorResult import CalculatorResult
from mietrecht_ch.models.lebensdauer import LebensdauerEntry, LebensdauerRemedy, LebensdauerResult

@frappe.whitelist(allow_guest=True)
def get_all_by_group(groupId):
    return CalculatorMasterResult( 
        {'groupId':groupId}, 
        [CalculatorResult(get_fake_data(), None)]
    )


@frappe.whitelist(allow_guest=True)
def get_all_by_keyword(keyword):
    return CalculatorMasterResult( 
        {'keyword':keyword}, 
        [CalculatorResult(get_fake_data(), None)]
    )


def get_fake_data():
    agregateChildren = [
        LebensdauerEntry('für Warmluftcheminée', lifetime=20),
        LebensdauerEntry('zur Wärmerückgewinnung', lifetime=20),
    ]

    chemineeChildren = [
        LebensdauerEntry('Cheminée, Cheminéeofen, Schwedenofen', lifetime=25),
        LebensdauerEntry('Schamottsteinauskleidung', lifetime=15, remedy=LebensdauerRemedy('Neuauskleidung', 'm²', 800))
    ]

    chemineeEntries = [
        LebensdauerEntry('Aggregate', agregateChildren),
        LebensdauerEntry('Cheminéeabschluss', comment="Metallgitter, Glas", lifetime=20),
        LebensdauerEntry('Cheminées', chemineeChildren),
        LebensdauerEntry('Ventilator', comment='Zu Rauchabzug', lifetime=20),
    ]

    otherChildren = [
        LebensdauerEntry('Kunststoft', lifetime=15, remedy=LebensdauerRemedy('Ersatz', 'Stk.', 75)),
        LebensdauerEntry('Metall', lifetime=20, remedy=LebensdauerRemedy('Ersatz', 'Stk.', 75)),
    ]

    otherEntries = [
        LebensdauerEntry('Abdeckungen zu Lüftungsanlagen/-gittern', otherChildren),
    ]

    return [
        LebensdauerResult('Cheminée', chemineeEntries),
        LebensdauerResult('Heizung / Lüftung / Klima', otherEntries),
        ]