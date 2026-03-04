# IP Info CLI

A command-line tool to lookup IP address information. Get detailed information about any IP address or your own public IP directly from your terminal.

## Features

- **IP Lookup** - Get detailed information about any IP address
- **Own IP** - Lookup your own public IP address
- **JSON Output** - Output results as JSON for scripting
- **Fast** - Uses ip-api.com for quick lookups

## Requirements

- Python 3.8 or higher
- Internet connection (for API requests)

## Installation

### Quick Install (macOS/Linux/Windows)

```bash
pipx install git+https://github.com/hemanthsingh003/ipinfo.git
```

### Requirements

- Python 3.8 or higher
- Internet connection (for API requests)
- [pipx](https://pipx.pypa.io/) (install via: `python -m pip install pipx`)

### Uninstall

```bash
pipx uninstall ipinfo-cli
```

## Usage

### Get your own IP info

```bash
ipinfo
```

### Lookup a specific IP address

```bash
ipinfo 8.8.8.8
```

### Output as JSON

```bash
ipinfo 8.8.8.8 --json
ipinfo 8.8.8.8 -j
```

## Output Example

```
IP: 8.8.8.8
Version: IPv4
City: Mountain View
Region: California
Country: United States
Country Code: US
Latitude: 37.386
Longitude: -122.0838
Timezone: America/Los_Angeles
ISP: Google LLC
Organization: Google Public DNS
```

## Command-Line Options

| Option | Description |
|--------|-------------|
| `ip` | IP address to lookup (optional - omit for your own IP) |
| `--json`, `-j` | Output as JSON |

## Project Structure

```
ipinfo/
├── pyproject.toml          # Project metadata and dependencies
├── README.md               # This file
├── ipinfo/
│   └── __init__.py         # CLI logic and core functionality
└── dist/                   # Built distributions
```

## License

MIT License
