def erretiratu(saldoa, zenbatekoa):
    """Kontu batetik zenbateko bat erretiratu eta saldo berria edo errore-mezua itzultzen du."""
    if zenbatekoa <= 0:
        return "Errorea: Zenbateko baliogabea"
    if zenbatekoa > saldoa:
        return "Errorea: Saldo nahikorik ez"
    return saldoa - zenbatekoa
