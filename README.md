# pcd-lidar2video

The following open-source projects were forked to fit our data.

* [PCD-Tools](https://github.com/alirezaasvadi/PCD-Tools);
* [pcd2bin](https://github.com/Yuseung-Na/pcd2bin).

---
### Build & run

0. Install all dependencies (simply activate python venv with `source bin/activate` or equivalent). If running Windows and WSL2, plotting requires a X11 server on host (e.g. [VcXsrv](https://sourceforge.net/projects/vcxsrv/));
2. Convert PCD file format to bin using `src/pcd2bin.py`;
3. Pipe bin file to `src/pcd-tools.py` to plot scenes. For the hackathon this is fixed to an 8-frame range;
4. Export desired scenes to PNG;
5. Convert PNGs to `m4v` video using `ffmpeg` at 2 frames per second:

```
ffmpeg -start_number 1 -y -r 1 -i "video-%1d.png" -vf scale=1920:-1 -vcodec libx264 -b:v 10000k -r 1 outputhd.m4v
```

---

### Route details

* **Location**: University of Oxford's Computer Science Department (starting at the entrance to the University Parks);
* **Avg. speed**: 29.5mph;
* **Timeline**: Tue Jan 21 2020 11:20:35 GMT+0.

Render of the LIDAR data route taken.

![](data/video.gif)
