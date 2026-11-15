import json, time, urllib.request, sys
TOKEN = open("/config/.claude_token").read().strip()
LIGHTS = ["light.h619a_2a3d", "light.h7070_253e", "light.workroom_ceiling_govee"]
def call(path, body=None):
    req = urllib.request.Request("http://localhost:8123/api/" + path, method="POST" if body is not None else "GET",
        data=json.dumps(body).encode() if body is not None else None,
        headers={"Authorization": "Bearer " + TOKEN, "Content-Type": "application/json"})
    return json.load(urllib.request.urlopen(req, timeout=10))
def states():
    return " ".join(call("states/" + l)["state"] for l in LIGHTS)
def publish(payload):
    call("services/mqtt/publish", {"topic": "gv2mqtt/availability", "payload": payload, "retain": False})
now = lambda: time.strftime("%H:%M:%S", time.gmtime())
label = sys.argv[1] if len(sys.argv) > 1 else ""
print(f"=== {label} {now()} before: {states()}", flush=True)
publish("offline"); time.sleep(3)
print(f"=== {now()} after offline: {states()}", flush=True)
for t in range(10, 101, 10):
    time.sleep(10)
    s = states()
    print(f"=== +{t}s {now()}: {s}", flush=True)
    if "unavailable" not in s:
        print("=== RECOVERED by itself"); break
else:
    print("=== NOT recovered by itself after 100 s — publishing online by hand")
    publish("online"); time.sleep(3)
    print(f"=== {now()} after manual online: {states()}")
