from matplotlib.colors import LinearSegmentedColormap

# visual tool available at
# http://jdherman.github.io/colormap/

# heart-rate
hr_cdict = {    'red' :    ((0.0,  1.0,    1.0),
                            (1.0,  1.0,    1.0)),

               'green' :   ((0.0,  1.0,    1.0),
                            (0.25, 0.875,  0.875),
                            (0.5,  0.75,   0.75),
                            (0.75, 0.5,    0.5),
                            (1.0,  0.0,    0.0)),

               'blue' :    ((0.0,  0.5,   0.5),
                            (0.25, 0.375, 0.375),
                            (0.5,  0.25 , 0.25),
                            (0.75, 0.125, 0.125),
                            (1.0,  0.0,    0.0))}

hr_cmap = LinearSegmentedColormap('hr_colormap', hr_cdict, 256)
