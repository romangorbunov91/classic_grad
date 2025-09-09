# version 1.2 by romangorbunov91
# 09-Sep-2025

import numpy as np
import re

def update_readme_section(tbl_df, readme_path, tbl_name, section):
    markdown_table = tbl_df.to_markdown(index=False)

    with open(readme_path, 'r', encoding="utf-8-sig") as f:
        content = f.read()

    # Define start and end markers.
    start_marker = f'<!-- START_{section.upper()} -->'
    end_marker = f'<!-- END_{section.upper()} -->'

    # Wrap the table with headers and markers.
    new_section = f'\n{start_marker} \n### {tbl_name}\n{markdown_table}\n{end_marker}'
    
    # Remove any previous content between the markers.
    pattern = re.compile(f'{re.escape(start_marker)}.*?{re.escape(end_marker)}', re.DOTALL)
    updated_content = pattern.sub("", content)

    # Insert the new section to the end of the file.
    updated_content += new_section

    with open(readme_path, 'w', encoding="utf-8-sig") as f:
        f.write(updated_content)

        
def funtion_generator(M, cond_number, seed=None):
    # M - (order).
    # cond_number - condition number µ.
    if seed is not None:
        np.random.seed(seed)

    if cond_number < 1:
        raise ValueError('Condition number must be >= 1.')
    
    # Generate M random eigenvalues.
    #eigvals_float = np.linspace(1.0, cond_number, M)
    eigvals_float = [np.random.uniform(1+0.01, cond_number-0.01) for _ in range(M)]
    eigvals_float[0] = 1.0
    eigvals_float[-1] = cond_number
    
    # Generate random orthogonal matrix using QR-decomposition.
    Q, _ = np.linalg.qr(np.random.randn(M, M))

    # Build system matrix A.
    A = Q @ np.diag(eigvals_float) @ Q.T
    
    # Generate random b-vector (M-dimensional).
    b = np.random.randn(M)
    
    # Generate random constant.
    c = np.random.uniform(-100.0, 100.0)
    
    # Finally, define function and its gradient.
    
    def func(x):
        return 0.5 * x @ A @ x - b @ x + c

    def grad_func(x):
        return A @ x - b

    return np.matrix(A), np.matrix(b), c, func, grad_func