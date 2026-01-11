# Hashlib Examples

Python implementations of cryptographic hash functions using the hashlib library.

## Installation

```bash
python3 -m venv .venv
source .venv/bin/activate
# No external dependencies required
```

## sha512.py

Calculate SHA-512 hash of a file, producing output identical to the `sha512sum` command.

### Usage

```python
from sha512 import sha512_of_file

hash_value = sha512_of_file("myfile.tar.gz")
print(hash_value)
```

### Verification

```bash
# Python
python sha512.py

# Linux command (produces same hash)
sha512sum myfile.tar.gz
```

## Features

- Chunked file reading for memory efficiency with large files
- Handles file not found errors gracefully
- Returns hexadecimal digest string

## Requirements

- Python 3.x
