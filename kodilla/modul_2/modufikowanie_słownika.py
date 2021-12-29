salads = {
    "owocowa": ["ananas", "truskawka", "jagody"],
    "moja_buraczana": ["buraki", "ser kozi", "rukola"],
    "mamina": ["groszek", "kukurydza", "majonez", "ziemniaki"]
}
print(salads["moja_buraczana"])
# Dodawanie elmentów:
salads["mięsna"] = ["szynka", "kurczak", "ryż", "ogórek"]
print(salads.keys())
# Podmiana:
salads["owocowa"] = ["ananas", "truskawka", "jagody", "cukier"]
print(salads["owocowa"])
salads["owocowa"].append("majonez")
print(salads["owocowa"])
# Usuwanie
del salads["mamina"]
print(salads.keys())
