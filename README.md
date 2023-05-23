# 3DCV : An unstructured attempt to revisit traditional CV pipelines

What does this repo include:
* Feature Matching: Using SIFT, SURF, ORB to detect features and bfMatcher, FLANN matcher to match these features in subsequent frames.
* Epipolar Geometry: Understanding the 5 point and 8 point algorithms and how can we recover the information we need.
* Recovering Fundamental and Essential matrix: When and where both are needed and for what tasks.
* Visual Odometry: Relative camera motion in a video sequence.
* Structure from Motion: Given multi-view photographs, how to create the 3D structure.
* Mapping: How to get locally consistent maps.
* Localization: Given a map, how to localise in that coordinate frame.
* SLAM: Doing Localization and Mapping iteratively.

# RoadMap
- [x] Basic repo using pypoetry
- [x] Understanding Feature Matching
- [ ] Basics of Epipolar geometry
- [ ] Using camera intrinsics and determining Essential matrix
- [ ] Visual Odometry (basic)
- [ ] Visual Odemetry with bundle adjustment
- [ ] Monocular SFM (basic)
- [ ] SFM with depth maps (advanced)
- [ ] Mapping
- [ ] SLAM (basic)
- [ ] SLAM + notes on loop closure

# How to use this repo

You should have python installed on your machine.
1. Install pypoetry
```
$ pip install poetry
```

2. Navigate to the root folder of this repo.
```
$ poetry shell
$ poetry install
```

3. Run the individual code
```
$ python 3dcv/feature_matching.py
```