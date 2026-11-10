# Smart Glass Project

Shared spatial annotations on RayNeo smart glasses — UCLA ECE M202A.

## Experiment and current results

[Project website](https://ahjcgit.github.io/SmartGlassProject/) · [Website source and publishing guide](website/README.md)

The November 10 Milestone 3 pilot contains **11 physical-camera trials and 229 sampled frames** of a sanitizer bottle, a toy motorcycle, and an empty scene. The site presents condition-level detection results, a paired NanoDet / YOLOX-S recorded-image comparison, CPU processing times, annotation provenance, and limitations. The larger detector improved recognition in these scenes but took about five times longer per median CPU model call. Results are preliminary: one instance per class, one trial per condition, and 211 of 229 reference annotations await independent human verification.

## Spatial annotations application

[Browse the application and setup guide](https://github.com/ahjcgit/spatial-annotations/blob/a4b59406fc0871657621972ffbf2693e544329e9/README.md)

The native Android client, FastAPI/SQLite backend, and browser companion support persistent public, private, and group notes. The current live demonstration uses RayNeo color capture and computer-hosted category detection with explicit selection of the registered object. QR UUIDs remain available for unique instance identity. Category detection alone cannot distinguish identical objects. World tracking and persistent AR anchors are not implemented.

The application is the [`spatial-annotations/`](./spatial-annotations) Git submodule, with its own setup, tests, and history. Its pinned revision may differ from the current experiment revision linked above.

## Clone and run

```bash
git clone --recurse-submodules https://github.com/ahjcgit/SmartGlassProject.git
cd SmartGlassProject/spatial-annotations
```

Follow the experiment's README to start the backend and build the Android app.
For an existing clone:

```bash
git pull --ff-only
git submodule update --init --recursive
```

## Update the experiment

The submodule pins a specific commit so a checkout is reproducible. To advance it
to the experiment's latest `main`, run from the SmartGlassProject root:

```bash
git submodule update --init --remote spatial-annotations
git add spatial-annotations
git commit -m "Update spatial annotations experiment"
```

Commit and push code changes from inside the experiment repository first, then
commit and push the updated submodule pointer here.
