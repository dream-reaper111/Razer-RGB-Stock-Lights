# Razer RGB Stock Lights

> Restore, control, and experiment with stock Razer RGB lighting behavior on Linux.

Razer RGB Stock Lights is a small utility project focused on managing the factory lighting behavior of supported Razer devices without needing a full heavyweight RGB software stack.

The goal is to keep things simple:

- restore stock lighting behavior
- apply basic effects
- test device compatibility
- provide a lightweight Linux-friendly control layer
- document working configurations and fixes

---

## Features

- Restore stock/default Razer lighting
- Apply simple RGB modes
- Test device detection
- Lightweight Python-based control
- Linux-friendly workflow
- Easy to expand with additional effects

---

## Project Goals

This repo is intended for users who want a small, transparent RGB controller for Razer hardware.

Instead of relying on a large GUI application, the project focuses on direct control and simple scripts.

Potential supported modes include:

```text
Static
Breathing
Spectrum
Wave
Reactive
Off
Stock / Default
```

---

## Requirements

Recommended:

```bash
Python 3.10+
Linux
OpenRazer
Python bindings for supported devices
```

Depending on the implementation, you may need:

```bash
sudo apt install openrazer-meta
```

Then install the Python bindings:

```bash
pip install openrazer
```

On some distributions, OpenRazer packages may already provide the required Python module.

---

## Example Usage

Basic execution:

```bash
python3 razer_rgb.py
```

Restore default lighting:

```bash
python3 razer_rgb.py --stock
```

Static color:

```bash
python3 razer_rgb.py --static 255 0 0
```

Spectrum mode:

```bash
python3 razer_rgb.py --spectrum
```

Turn lighting off:

```bash
python3 razer_rgb.py --off
```

---

## Planned Structure

```text
Razer-RGB-Stock-Lights/
├── README.md
├── requirements.txt
├── razer_rgb.py
├── devices/
│   └── device_profiles.py
├── effects/
│   ├── static.py
│   ├── spectrum.py
│   ├── breathing.py
│   └── wave.py
└── examples/
    └── startup.sh
```

---

## Auto Start

The utility can eventually be launched automatically when Linux starts.

Example:

```bash
~/.config/autostart/
```

or through `systemd`:

```bash
systemctl --user enable razer-rgb.service
systemctl --user start razer-rgb.service
```

This can be useful for automatically restoring your preferred lighting profile after login.

---

## Roadmap

Planned additions:

- [ ] Automatic device discovery
- [ ] Restore factory lighting mode
- [ ] Static RGB support
- [ ] Spectrum cycling
- [ ] Breathing effect
- [ ] Reactive lighting
- [ ] Wave effects
- [ ] Per-device profiles
- [ ] Startup persistence
- [ ] Systemd user service
- [ ] CLI device selector
- [ ] Saved presets
- [ ] Keyboard / mouse / headset support
- [ ] OpenRazer compatibility detection
- [ ] Configuration file support
- [ ] Simple terminal UI

---

## Why This Exists

Linux RGB support can sometimes be more complicated than it needs to be.

This project exists as a lightweight playground for controlling Razer lighting while keeping the code easy to understand, modify, and troubleshoot.

No giant RGB suite.

No unnecessary background services beyond what the hardware interface requires.

Just:

```text
DEVICE
  ↓
OPENRAZER
  ↓
PYTHON
  ↓
RGB
```

---

## Compatibility

Compatibility depends on OpenRazer support for the specific device.

Typical device categories may include:

- Razer keyboards
- Razer mice
- Razer headsets
- Razer mousepads
- Razer Chroma accessories

Device support varies by model.

---

## Troubleshooting

Check whether OpenRazer detects your hardware:

```bash
lsusb | grep -i razer
```

Check daemon status:

```bash
systemctl --user status openrazer-daemon
```

Restart the daemon:

```bash
systemctl --user restart openrazer-daemon
```

Check available devices:

```bash
python3 -c "from openrazer.client import DeviceManager; print(DeviceManager().devices)"
```

---

## Contributing

Pull requests, device compatibility reports, and effect improvements are welcome.

Useful contributions include:

- new device profiles
- additional RGB effects
- Linux distro compatibility fixes
- startup/service improvements
- cleaner device detection

---

## Disclaimer

This project is unofficial and is not affiliated with or endorsed by Razer Inc.

Use at your own risk.

---

## License

MIT License recommended.

---

```text
[ DEADBYTE LAB ]

RGB STATUS: ONLINE
DEVICE BUS: ACTIVE
CHROMA LINK: ESTABLISHED
LIGHTS: ARMED
```
