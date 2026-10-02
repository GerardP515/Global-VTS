# VTS source evidence

Start with `../VTS_RESEARCH_PROMPT.md`.
The existing SOURCE_REGISTER.csv and SOURCE_REGISTER.md remain unchanged by this scaffold.
They identify sources; they do not, by themselves, prove that copies are held or inspected.

## Folder roles

| Folder | Content |
|---|---|
| archive/pdf | Original validated PDF bytes |
| archive/html | Original webpage responses and clearly identified permitted rendered captures |
| archive/structured | Original published JSON, XML, CSV or geospatial responses |
| extracted | Mechanical text/table derivatives tied to an original snapshot |
| renders | Page images and screen captures required for visual verification |
| translations | Labelled translations retaining original-language traceability |
| manifests | Per-snapshot acquisition records and storage configuration |

Use immutable snapshot filenames and full SHA-256 values in manifests.
One source snapshot can support multiple services and directions.
Never create a source extraction by writing a summary.
Do not place draft guides, invented documents, test fixtures or credentials in these folders.

The folders are initially empty except for instructions and metadata templates.
No source downloads are claimed by their creation.
The default store is this repository. A sibling source repository may be configured later through an approved migration.

Retain failed acquisition outcomes. Do not delete their catalogue entries or call them evidence of absence.
Do not store restricted content without permission. Record permitted access locations where copies cannot be archived here.
