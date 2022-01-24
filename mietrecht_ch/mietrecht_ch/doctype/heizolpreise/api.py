import frappe


@frappe.whitelist(allow_guest=True)
def get_single_oil_price(quantity, year, month):
    return frappe.db.sql("""SELECT `monat` as `month`, `{quantity}` as `price`, '{quantity}' as `quantity`
                            FROM `tabHeizolpreise` 
                            WHERE `monat` LIKE '{date}';""".format(quantity=quantity, date=__buildFullDate(year, month)), as_dict=True)

@frappe.whitelist(allow_guest=True)
def get_multiple_oil_price(quantity, fromYear, fromMonth, toYear, toMonth):
    fromFull = __buildFullDate(fromYear, fromMonth)
    toFull = __buildFullDate(toYear, toMonth)

    if fromFull > toFull :
        tmp = toFull
        toFull = fromFull
        fromFull = tmp

    return frappe.db.sql("""SELECT `monat` as `month`, `{quantity}` as `price`, '{quantity}' as `quantity`
                            FROM `tabHeizolpreise` 
                            WHERE `monat` BETWEEN '{fromFull}' AND '{toFull}' ;"""
                            .format(quantity=quantity, fromFull=fromFull, toFull=toFull), as_dict=True)

def __buildFullDate(year, month):
    return year + '-' + str.zfill(month, 2) + '-01'
