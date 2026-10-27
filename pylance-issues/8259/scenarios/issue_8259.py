"""Partial executable input for https://github.com/microsoft/pylance-release/issues/8259.

The helper and four assignments below are copied verbatim from the pinned
AirfRANS dataset.py. See ../README.md and ../LICENSE-AirfRANS.txt.
The wrapper and numeric smoke inputs are investigation additions, NOT reporter
inputs. This reduction has not been shown to preserve the editor failure.
Use ../dataset.py for the primary scroll/hover verification.
"""

import numpy as np

def cell_sampling_1d(line_points, line_attr = None):
    '''
    Sample points in a one dimensional cell via linear sampling and interpolation.

    Args:
        line_points (array): Edges of the 1 dimensional cells. Shape (N, 2) for N cells with 2 edges.
        line_attr (array, optional): Features of the edges of the 1 dimensional cells. Shape (N, 2, k) for N cells with 2 edges and k features.
            If given shape (N, 2) it will resize it automatically in a (N, 2, 1) array. Default: ``None``
    '''
    # Linear sampling
    u = np.random.uniform(size = (len(line_points), 1))
    sampled_point = u*line_points[:, 0] + (1 - u)*line_points[:, 1]

    # Linear interpolation
    if line_attr is not None:   
        if len(line_attr.shape) == 2:
            line_attr = line_attr[:, :, None]
        sampled_attr = u*line_attr[:, 0] + (1 - u)*line_attr[:, 1]

    return np.hstack([sampled_point[:, :2], sampled_attr]) if line_attr is not None else sampled_point[:, :2]


def screenshot_assignments(line_points, surf_attr):
    surf_sampled_points = cell_sampling_1d(line_points, surf_attr)
    surf_pos = surf_sampled_points[:, :2]
    surf_init = surf_sampled_points[:, :7]
    surf_target = surf_sampled_points[:, 7:]
    return surf_sampled_points, surf_pos, surf_init, surf_target


if __name__ == "__main__":
    # Synthetic shape-compatible inputs only; no CFD dataset required.
    line_points = np.arange(24, dtype=np.float64).reshape(4, 2, 3)
    surf_attr = np.arange(72, dtype=np.float64).reshape(4, 2, 9)
    arrays = screenshot_assignments(line_points, surf_attr)
    names = ("surf_sampled_points", "surf_pos", "surf_init", "surf_target")
    expected_shapes = ((4, 11), (4, 2), (4, 7), (4, 4))
    for name, array, expected_shape in zip(names, arrays, expected_shapes):
        assert array.shape == expected_shape
        assert array.dtype == np.dtype(np.float64)
        print(f"{name}: shape={array.shape}, dtype={array.dtype}")
