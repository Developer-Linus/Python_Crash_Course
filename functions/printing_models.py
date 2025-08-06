def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move the printed design to completed models
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        """
        Simulate printing a 3D model from design
        """
        print("Printing model: " + current_design)
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """
    Show all the models that were printed
    """
    print("The following models have been printed")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs[:], completed_models)
print(unprinted_designs)
show_completed_models(completed_models)
