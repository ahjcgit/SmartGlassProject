# Smart Glass Project

Glasses experiments and capability tests.

## Spatial annotations

[Browse the spatial annotations experiment](https://github.com/ahjcgit/spatial-annotations#readme)
— a RayNeo Android app, FastAPI backend, and browser companion for QR-linked notes.
It tests camera scanning, display/input, and multi-user sharing. Notes use a
screen-space panel; world tracking and persistent AR anchors are not implemented.

The experiment is contained in the [`spatial-annotations/`](./spatial-annotations)
Git submodule. It has its own setup instructions, dependencies, tests, and history.
On GitHub, clicking that directory opens the pinned experiment revision; the link
above opens the latest version.

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
