### PdfMerge
###### Combine pdf files into one pdf
---
### Installation

- Standalone executable:
    - Download [pdfmerge.exe](https://github.com/SaadBadr/pdfmerge/raw/master/dist/pdfmerge.exe)
    - You can add its location to the PATH Environment Variable and use it anywhere from terminal
- If you want to run the script `pdfmerge.py`, make sure to install [merge_pdf](https://pypi.org/project/merge-pdf/) first.




### Run

##### Merge all PDFs in `/currentDirectory` to `/currentDirectory/output.pdf`
```
pdfmerge
```
##### Merge all PDFs in `/<inputpath>` to `/<outputpath>`
```
pdfmerge -i <inputpath> -o <outputpath>
```
##### Merge all PDFs in `/<inputpath>` to `/<inputpath>/output.pdf`
```
pdfmerge -x <inputpath>
```
