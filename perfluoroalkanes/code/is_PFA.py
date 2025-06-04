from rdkit import Chem

def is_PFA(mol, alkane_only = True, print_reason = False, cyclic = False):
    mol = Chem.AddHs(mol)
    mol = Chem.RWMol(mol)
    if mol.HasSubstructMatch(Chem.MolFromSmarts('[13C,14C,8C,9C,10C,11C,15C,16C,17C,18C,19C,20C,21C,22C]')):
        if print_reason: print("Carbon isotope")
        return False
    elif mol.HasSubstructMatch(Chem.MolFromSmarts('[13F,14F,15F,16F,17F,18F,20F,21F,22F,23F,24F,25F,26F,27F,28F,29F,30F,31F]')):
        if print_reason: print("Fluorine isotope")
        return False
    if alkane_only:
        if mol.HasSubstructMatch(Chem.MolFromSmarts('[!#6;!#9]')):
            if print_reason: print("Atom that is not C or F")
            return False
        elif mol.HasSubstructMatch(Chem.MolFromSmarts('*!-*')):
            if print_reason: print("Bond, that is not single")
            return False
        elif mol.HasSubstructMatch(Chem.MolFromSmarts('[*-]')):
            if print_reason: print("Negative charge")
            return False
        elif mol.HasSubstructMatch(Chem.MolFromSmarts('[*+]')):
            if print_reason: print("Positive charge")
            return False
        if not cyclic:
            if mol.HasSubstructMatch(Chem.MolFromSmarts('[R]')):
                if print_reason: print("Cycle")
                return False
        n_H = sum(1 for atom in mol.GetAtoms() if atom.GetAtomicNum() == 1)
        # n_F = sum(1 for atom in mol.GetAtoms() if atom.GetAtomicNum() == 9)
        # print(n_C, n_F)
        if(n_H > 0):
            if print_reason: print("Not fully fluorinated")
            return False
    if mol.HasSubstructMatch(Chem.MolFromSmarts('C(F)(F)(F)')):
        return True
    elif mol.HasSubstructMatch(Chem.MolFromSmarts('CC(F)(F)C')):
        return True
    

    # perfluorinated alkanes CnF2n+2
    # hydrofluorocarbons CnF2n+1-CmH2m+1
    
    return False