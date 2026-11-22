# Leonida Mapping Math

**Three cameras see the same landmark. Where is it in 3D?** Give the solver their positions and viewing directions to estimate a point and measure how closely the rays agree.

## Reconstruct the example landmark

```sh
python -m pip install -r requirements.txt
python triangulate.py rays.json
```

The three observations in [rays.json](rays.json) meet at **(3, 4, 2)**, up to floating-point precision. Change one direction and rerun the command to see how the estimate and the RMS error move.

| Input per observation | Output |
|---|---|
| Camera origin `x, y, z` and direction `dx, dy, dz` | Estimated landmark `xyz` |
| Two or more observations in one coordinate frame | RMS perpendicular distance in the input units |

## Calibrate your own observations

Provide camera poses independently, using the same axes and units throughout. Choose well-separated viewpoints. The solver rejects zero vectors, nearly parallel rays and estimates behind an observer. High residual error is a reason to recheck a bearing before placing the landmark.

---

[Explore the GTA VI project collection](https://github.com/Berserk-hub150/gta6-resource-index) · Independent fan project. Grand Theft Auto is a trademark of its respective owners.
