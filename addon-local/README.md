# Local add-on build of this fork

Copy this folder to `/addons/govee2mqtt_availfix` on Home Assistant OS, together with
`govee` (static arm64 musl binary built from this branch), `assets/` and `AmazonRootCA1.pem`
from the repository root. Without an `image:` key the Supervisor builds it locally.
