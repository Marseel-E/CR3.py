# CR3.py
A CR3 file format parser written in Python


# CR3 File Structure
### `FTYP` - File Type Box.
| Offset | Type | Size | Content				 |
| :----: | :--: | :--: | :---------------------- |
| 0		 | Int  | 4    | `ftyp` length			 |
| 4		 | Str  | 4    | `ftyp` tag				 |
| 8		 | Int  | 4    | Major Brand			 |
| 12	 | Int  | 4    | Minor Version			 |
| 16	 | Str  | 4    | `N/A`					 |
| 20	 | Str  | 4    | `N/A`					 |
### `moov` - Container box whose sub-boxes define the metadata for a presentation.
| Offset | Type | Size | Content 		|
| :----: | :--: | :--: | :------------- |
| 0		 | Int	| 4	   | `moov` length	|
| 4		 | str	| 4	   | `moov` tag		|
| 8		 | Int	| 4	   | `uuid` length	|
| 12	 | Int	| 4	   | `uuid` tag		|
| 16	 | Int	| 8:12 | `uuid` data	|
### uuid - `XPacket` data.
| Offset | Type | Size | Content			 |
| :----: | :--: | :--: | :------------------ |
| 0		 | Int	| 4	   | XPacket data length |
| 4		 | Str	| 4	   | `uuid` tag			 |
| 8		 | Int	| 0:4  | `uuid`				 |
### uuid - `Preview` data.
| Offset | Type | Size | Content				|
| :----: | :--: | :--: | :--------------------- |
| 0		 | Int	| 4	   | Preview data length	|
| 4		 | Str  | 4	   | `uuid` tag				|
| 8		 | Int	| 0:4  | `uuid`					|
### `mdat` - Main data.

# Credits
- [lclevy -> canon_cr3](https://github.com/lclevy/canon_cr3?tab=readme-ov-file#cr3-file-Structure)