# Experiment website

A static GitHub Pages site for the M202A Milestone 3 pilot. Source lives in `website/`; `site/` is an ignored build output. No JavaScript framework or package install is required. Browser JavaScript only filters the already-rendered results table; all content remains readable without it.

## Preview and validate

Check port availability first, then:

```bash
python3 website/build.py
python3 website/check.py
python3 -m http.server 8020 --bind 0.0.0.0 --directory site
```

Open `http://localhost:8020`, or `http://<computer-LAN-IP>:8020` from another device.

## Update measurements

From the parent repository, with the completed pilot available locally:

```bash
python3 website/build.py --pilot spatial-annotations/artifacts/evaluation/pilot
python3 website/check.py
```

The builder copies an explicit allowlist of aggregate fields into `website/results.json`. It never publishes raw JPEGs, notes, credentials, or capture endpoint addresses. The snapshot records the source archive and analysis hashes. Review the HTML narrative and headline values when importing a new experiment: this page describes the November 10 pilot, not arbitrary future datasets.

All detector accuracy and placement values currently use 18 original user annotations and 211 AI visual annotations without independent human verification. Preserve that qualification. Report one trial per condition and avoid interpreting sampled frames as independent repetitions. Timing is from the recorded CPU replay, not sensor-to-display latency.

## Publish

GitHub Actions builds and checks pull requests. Changes to `website/` or the workflow on `main` deploy only the generated `site/` directory. The application submodule is not required to build the website; its checked-in evidence snapshot is sufficient.

One-time repository setup: **Settings → Pages → Build and deployment → Source: GitHub Actions**. This requires an owner, maintainer, or account with permission to manage Pages settings. If Pages is disabled, the build can pass while the deployment fails until that setting is enabled. After enabling, rerun the failed deployment or dispatch **Build and deploy experiment website** from Actions.

Expected URL: https://ahjcgit.github.io/SmartGlassProject/

Application documentation links are pinned to `a4b59406fc0871657621972ffbf2693e544329e9`, the source revision associated with this pilot. The website update does not change the parent repository's submodule pointer.
