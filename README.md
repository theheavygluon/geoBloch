# geoBloch

geoBloch is a small script written by user qfilo and I. As the name suggests, it is a function that takes an address as an input and plots the address on a Bloch Sphere. It essentially utilizes geopy to convert the physical address into longitude/latitude coordinates which are then passed as inputs to qiskit's plot_bloch_vector() function. The applications to this are probably non-existent but it's still fun to play around with. 

# Example usage

geoBloch('China')

# Modules required

-geopy

-qiskit

