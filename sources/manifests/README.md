# Acquisition manifests

Create one JSON record per source snapshot, using source_record.template.json.
Template and storage files are configuration, not acquired sources.
This scaffold makes no HELD claims and allocates no new SRC IDs.

Reuse bibliographic IDs from the existing source register where appropriate.
Reserve new IDs against the current branch before allocation.
Keep snapshot identity separate from bibliographic identity.

A HELD record requires actual bytes, storage path, full SHA-256, byte count and a real retrieval timestamp.
A failure requires an explicit result and reason, not a fabricated empty original.
Do not turn an unsuccessful re-fetch into deletion of an older held snapshot.

Track possession, inspection, currency and rights independently.
A byte-identical live response does not prove that later notices do not exist.
The manifest must link every derivative to the exact original.

Generated catalogue summaries should be built from these records, not hand-counted.
No catalogue generation script or downloader is installed by this change.
