

def split_before_uppercases(formula):
  lst = []
  i=0
  while i < len(formula):
    str = formula[i]
    i+=1
    while i < len(formula) and not formula[i].isupper():
      str += formula[i]
      i+=1
    lst.append(str)
  return lst


def split_at_digit(formula):
  string = ""
  num = 1
  index = 0
  for i in range(len(formula)):
    if not formula[i].isdigit():
        string += formula[i]
        index += 1
    else:
        break
  if index < len(formula):
      num = int(formula[index:])
  return (string , num)


def count_atoms_in_molecule(molecular_formula):
    """Takes a molecular formula (string) and returns a dictionary of atom counts.
    Example: 'H2O' → {'H': 2, 'O': 1}"""
    d = {}
    list_mol = split_before_uppercases(molecular_formula)
    for item in list_mol:
      tup = split_at_digit(item)
      d[tup[0]] = tup[1]
    return d
"""
    # Step 1: Initialize an empty dictionary to store atom counts

    for atom in split_by_capitals(molecular_formula):
        atom_name, atom_count = split_at_number(atom)
        
        # Step 2: Update the dictionary with the atom name and count

    # Step 3: Return the completed dictionary
"""


def parse_chemical_reaction(reaction_equation):
    """Takes a reaction equation (string) and returns reactants and products as lists.  
    Example: 'H2 + O2 -> H2O' → (['H2', 'O2'], ['H2O'])"""
    reaction_equation = reaction_equation.replace(" ", "")  # Remove spaces for easier parsing
    reactants, products = reaction_equation.split("->")
    return reactants.split("+"), products.split("+")

def count_atoms_in_reaction(molecules_list):
    """Takes a list of molecular formulas and returns a list of atom count dictionaries.  
    Example: ['H2', 'O2'] → [{'H': 2}, {'O': 2}]"""
    molecules_atoms_count = []
    for molecule in molecules_list:
        molecules_atoms_count.append(count_atoms_in_molecule(molecule))
    return molecules_atoms_count
