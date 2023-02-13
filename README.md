# laplace

The program takes a two-dimensional plate divided into four cells with boundary conditions a, b, c, and d, and uses it to calculate the heat distribution across the plate. For each cell, the Laplace equation is solved. This is repeated until the values of the cells converge, i.e., the difference between the new and old values of the cell differs by less than 1E-11. Finally, the values for T11, T12, T21, and T22 are printed to the screen.

Cell | Temperature (Celsius)
--- | ---
T11 | 1.50
T12 | 0.75
T21 | 2.25
T22 | 1.50

The program finds that T21 has the highest temperature, T12 the lowest, and T11 and T22 are the same. The temperature values all fall between the boundary conditions of 0 and 3 degrees Celsius because no heat is being added to the system, and the existing heat energy distributes across the plates according to the Laplace equation. There is symmetry in the results; T11 and T22 are equal.
