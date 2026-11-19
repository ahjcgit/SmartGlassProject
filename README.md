# Smart Glass Project

Shared spatial annotations on RayNeo smart glasses — UCLA ECE M202A.

## Experiment and current results

[Project website](https://ahjcgit.github.io/SmartGlassProject/) · [Website source and publishing guide](website/README.md)

The November 19 Codex-to-glasses pilot now preserves **six completed timed trials,
three failed attempts, and four earlier qualitative snapshots**. It includes original
frames, approximate boxes, brief visual rationales, display screenshots, separate
host/device clocks, sampled process resources, and wearer feedback. See the
[portable dataset, report and server analysis instructions](spatial-annotations/experiments/codex-glasses/2026-11-19/README.md).
The large-text bottle trials took a median 10.187 seconds from capture orchestration
to display-commit acknowledgement, including Codex review/tools; post-response
delivery took a median 184.5 ms. Isolated inference and optical latency were not
measured. Text was reported readable, but physical object alignment remains open.

The November 10 Milestone 3 pilot contains **11 physical-camera trials and 229 sampled frames** of a sanitizer bottle, a toy motorcycle, and an empty scene. The site presents condition-level detection results, a paired NanoDet / YOLOX-S recorded-image comparison, CPU processing times, annotation provenance, and limitations. The larger detector improved recognition in these scenes but took about five times longer per median CPU model call. Results are preliminary: one instance per class, one trial per condition, and 211 of 229 reference annotations await independent human verification.

## Spatial annotations application

[Browse the application and setup guide](https://github.com/ahjcgit/spatial-annotations/blob/experiment/codex-glasses-latency/README.md)

The native Android client, FastAPI/SQLite backend, and browser companion support persistent public, private, and group notes. The current live demonstration uses RayNeo color capture and computer-hosted category detection with explicit selection of the registered object. QR UUIDs remain available for unique instance identity. Category detection alone cannot distinguish identical objects. World tracking and persistent AR anchors are not implemented.

The application is the [`spatial-annotations/`](./spatial-annotations) Git submodule,
with its own setup, tests, and history. It pins the Codex-to-glasses measurement
experiment on `experiment/codex-glasses-latency`, which also retains the offline
H0–H4 comparison and the separate live RayNeo bottle demonstration.

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
normally stored in Git. The explicitly archived November 19 camera evidence is
versioned under `spatial-annotations/experiments/codex-glasses/2026-11-19/` for
portable analysis. Recreate the synthetic results with the guide's commands; those
checks require no glasses or paid inference. They do not establish real laptop
recognition or VLM accuracy. For physical glasses capture and the live bottle demo,
use the application README instead.

## Update the experiment

The submodule pins a specific commit so a checkout is reproducible. To advance it
to the latest `experiment/codex-glasses-latency` revision configured in `.gitmodules`,
run from the SmartGlassProject root:

```bash
git submodule update --init --remote spatial-annotations
git add spatial-annotations
git commit -m "Update spatial annotations experiment"
```

Commit and push code changes from inside the experiment repository first, then
commit and push the updated submodule pointer here.

For this experiment branch, push in this order from the project root:

```bash
git -C spatial-annotations push -u origin experiment/codex-glasses-latency
git push -u origin experiment/codex-glasses-latency
```
