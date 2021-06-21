from sage.all import *

def vector_simplify(vector, use_canonical_form=False):
    # Applies simplify_full to each element
    if use_canonical_form == True:
        # Uses Canonical Form of Multi-Valued Functions
        return vector.apply_map(lambda x: x.simplify_full().canonicalize_radical())
    else:
        # Uses Standard Simplification
        return vector.apply_map(lambda x: x.simplify_full())

def get_vector_arguments(vector):
    # Obtains arguments of vector or parametric curve
    parameters = set()
    for coordinate in vector:
        parameters.update(list(coordinate.arguments()))
    return parameters

def pretty_results(*argv, use_colon=False, centered=True):
    expressions = ""
    
    # Use Colon or Equal Sign for Separating Expression Names and Values?
    if use_colon:
        separator = LatexExpr(r":& \quad")
    else:
        separator = LatexExpr(r"&=")
    
    # Generate LaTeX Representations for Expressions
    for (latex_name, value) in argv:
        expressions += LatexExpr(latex_name) + separator + latex(value) + LatexExpr(r"\\")
    
    # Wrap Expressions with LaTeX align Enviroment
    formatted_string = LatexExpr(r"\begin{align*}") + expressions + LatexExpr(r"\end{align*}")
    
    # Center Expressions or Use Default Left-align?
    if centered:
        formatted_string += LatexExpr(r"\\")
    
    return formatted_string