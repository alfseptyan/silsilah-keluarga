

class KeluargaDjupri:
    def __init__(self, nama, partner=None):
        self.nama = nama
        self.partner = partner
        self.anak = []

    def add_anak(self, anak):
        if isinstance(anak, KeluargaDjupri):
            self.anak.append(anak)
        else:
            print("Error: anak harus menjadi bagian family node")

    def add_partner(self, partner):
        self.partner = partner

    def get_anak(self):
        return self.anak

    def get_partner(self):
        return self.partner

    def get_nama(self):
        return self.nama

def print_family_tree(node, level=0):
    if node.get_partner():
        print("  " * level + "- " + node.get_nama() + " & " + node.get_partner())
    else:
        print("  " * level + "- " + node.get_nama())
    for anak in node.get_anak():
        print_family_tree(anak, level + 1)

djupri = KeluargaDjupri("Djupri", "Ponimah")
ponimah = KeluargaDjupri("Ponimah", "Djupri")
djupri.add_partner("Ponimah")
ponimah.add_partner("Djupri")

ali = KeluargaDjupri("Ali", "Waqiah")
khusnan = KeluargaDjupri("Khusnan", "Rini")
edy = KeluargaDjupri("Edy", "Ida")
mulyadi = KeluargaDjupri("Mulyadi", "Lia")
nurul = KeluargaDjupri("Nurul", "Ririn")

djupri.add_anak(ali)
djupri.add_anak(khusnan)
djupri.add_anak(edy)
djupri.add_anak(mulyadi)
djupri.add_anak(nurul)

nizar = KeluargaDjupri("Nizar")
septyan = KeluargaDjupri("Septyan")

edy.add_anak(nizar)
edy.add_anak(septyan)

print("Keluarga Djupri dan Ponimah:")
print_family_tree(djupri)
