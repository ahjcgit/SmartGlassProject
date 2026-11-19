# Smart Glass Project

Shared spatial annotations on RayNeo smart glasses — UCLA ECE M202A.

## Experiment and current results

[Project website](https://ahjcgit.github.io/SmartGlassProject/) · [Website source and publishing guide](website/README.md)

The November 10 Milestone 3 pilot contains **11 physical-camera trials and 229 sampled frames** of a sanitizer bottle, a toy motorcycle, and an empty scene. The site presents condition-level detection results, a paired NanoDet / YOLOX-S recorded-image comparison, CPU processing times, annotation provenance, and limitations. The larger detector improved recognition in these scenes but took about five times longer per median CPU model call. Results are preliminary: one instance per class, one trial per condition, and 211 of 229 reference annotations await independent human verification.

## Spatial annotations application

[Browse the application and setup guide](https://github.com/ahjcgit/spatial-annotations/blob/60d0496d106b4f45bb692756f18d6e77ab71824e/README.md)

The native Android client, FastAPI/SQLite backend, and browser companion support persistent public, private, and group notes. The current live demonstration uses RayNeo color capture and computer-hosted category detection with explicit selection of the registered object. QR UUIDs remain available for unique instance identity. Category detection alone cannot distinguish identical objects. World tracking and persistent AR anchors are not implemented.

The application is the [`spatial-annotations/`](./spatial-annotations) Git submodule, with its own setup, tests, and history. It now pins the H0–H4 identity experiment (`60d0496`), including the recorded-frame comparison and browser viewer. This experiment is offline; the live RayNeo bottle demonstration remains available separately.

## Clone and run

```bash
git clone --recurse-submodules https://github.com/ahjcgit/SmartGlassProject.git
cd SmartGlassProject/spatial-annotations
```

Follow the experiment's README to start the backend and build the Android app.
For an existing clone, run from the **SmartGlassProject root**:

```bash
git pull --ff-only
git submodule update --init --recursive
```

### H0–H4 comparison on a laptop

From `SmartGlassProject/spatial-annotations`, follow the
[H0–H4 setup and run guide](spatial-annotations/docs/IDENTITY_H0_H4.md).
Its software demonstration creates a Python environment, generates a synthetic
dataset, runs all five methods with mock providers, and starts the viewer on port
8026. Open **http://localhost:8026** on the laptop running that command. The viewer
also listens on `0.0.0.0` for LAN access; choose a free port and leave 5173 reserved.

Generated datasets, credentials, databases, APKs, and local run artifacts are not
stored in Git. Recreate the synthetic results with the guide's commands; those
checks require no glasses or paid inference. They do not establish real laptop
recognition or VLM accuracy. For physical glasses capture and the live bottle demo,
use the application README instead.

## Update the experiment

The submodule pins a specific commit so a checkout is reproducible. To advance it
to the latest `experiment/h0-h4-identity` revision configured in `.gitmodules`,
run from the SmartGlassProject root:

```bash
git submodule update --init --remote spatial-annotations
git add spatial-annotations
git commit -m "Update spatial annotations experiment"
```

Commit and push code changes from inside the experiment repository first, then
commit and push the updated submodule pointer here.
