# Leonida Mapping Math

Estimate a landmark’s 3D coordinates from camera rays by least squares.

## Quick start

```sh
python -m pip install -r requirements.txt
python triangulate.py rays.json
```

## Using your own material

Provide camera positions and forward bearing vectors in a common coordinate frame. The example converges on [3,4,2]. RMS is the perpendicular distance to the viewing lines in your input units. Camera poses must be supplied independently.

Independent fan project. Grand Theft Auto is a trademark of its respective owners.
