# Build instructions

This entry was built in small steps:

1. `main.py` was written to copy the bundled `entry.png` to `/output/entry.png`.
2. `main.py` was extended to verify the copy by comparing the SHA-256 hashes of the source and destination files, raising an error on mismatch.
3. Documentation was added: `README.md`, `LICENSE` (MIT), `.makefun/owner.json`, and this note.

No secrets are stored in this repository.
