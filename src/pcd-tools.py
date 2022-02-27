# load and display image and point cloud data

# packages
import numpy as np
import mayavi.mlab

for i in range(2, 10):
    pcd = np.fromfile(f'../data/bin/lidar_points_235.bin_0000{i}.bin', dtype=np.float32).reshape((-1, 4))
    mayavi.mlab.figure(bgcolor=(0.3, 0.3, 0.3))
    mayavi.mlab.points3d(pcd[:, 0], pcd[:, 1], pcd[:, 2], pcd[:, 2], mode="point")
    mayavi.mlab.view(
        azimuth=33.6,
        elevation=106,
        distance=155.5,
        focalpoint='auto'
    )

    mayavi.mlab.savefig(f'../data/png/lidar_points_235.bin_0000{i}.png', size=(1920,1080))

mayavi.mlab.show()

