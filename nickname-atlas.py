
from pyscript import document

countries = ['Brunei', 'Cambodia', 'Indonesia', 'Laos', 'Malaysia', 'Myanmar (Burma)', 'Philippines', 'Singapore', 'Thailand', 'Timor-Leste (East Timor)', 'Vietnam']
nicknames = ['Land of Unexpected Treasures', 'Kingdom of Wonder', 'Emerald of the Equator', 'Land of a Million Elephants', 'Land of Indigenous Malay', 'Golden Land', 'Pearl of the Orient Seas', 'The Lion City', 'Land of Smiles', 'Land of the Sleeping Crocodile', 'Land of the Blue Dragon']

def show_nickname(e):
    index = int(document.getElementById("country").value)
    document.getElementById("result").innerHTML = f"""
        <p class="result-country">{countries[index]}</p>
        <h3>{nicknames[index]}</h3>
    """
