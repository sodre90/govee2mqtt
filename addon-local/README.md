# Local add-on build of this fork

Copy this folder to `/addons/govee2mqtt_availfix` on Home Assistant OS, together with
`govee` (static arm64 musl binary built from this branch), `assets/` and `AmazonRootCA1.pem`
from the repository root. Without an `image:` key the Supervisor builds it locally.

`build.sh` builds the binary in docker (`rust:1-alpine`, linux/arm64) with the version from
`config.yaml` and copies it, `assets/` and `AmazonRootCA1.pem` here. If Docker Desktop's
credential helper hangs on the pull, run it with `DOCKER_CONFIG` set to a directory whose
`config.json` is `{}`.

`test_availability.py` is the regression check: run it inside the Home Assistant core
container (`docker exec -i homeassistant python3 - <label> < test_availability.py`). It
publishes a non-retained `offline` to `gv2mqtt/availability` and expects the lights to be
available again within about 60 s. The light entity ids in it are this installation's.
