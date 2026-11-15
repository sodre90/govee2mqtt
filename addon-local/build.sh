#!/bin/bash
set -e
VERSION=$(sed -n 's/^version: "\(.*\)"/\1/p' "$(dirname "$0")/config.yaml")
cd "$(dirname "$0")/.."
docker run --rm --platform linux/arm64 \
  -v "$PWD":/src -w /src \
  -v govee2mqtt-cargo-registry:/usr/local/cargo/registry \
  -e CARGO_TARGET_DIR=/src/target-linux-arm64 \
  -e GOVEE_CI_TAG="$VERSION" \
  rust:1-alpine sh -c '
    apk add --no-cache build-base perl cmake linux-headers git >/dev/null
    cargo test --release 2>&1 | tail -25
    cargo build --release --bin govee
  '
cp target-linux-arm64/release/govee addon-local/govee
cp -R assets AmazonRootCA1.pem addon-local/
file addon-local/govee
ls -la addon-local/govee
echo BUILD_OK
