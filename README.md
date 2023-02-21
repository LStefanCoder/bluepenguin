# BluePenguin

Takes a PDF file with A4-sized pages, and converts it into into an A6 or A7-sized printable booklet.
Available under https://github.com/LStefanCoder/bluepenguin.

## Usage

Open a PDF file with "Open file", select "4-page-layout" (A6) or "8-page-layout" (A7), click "Convert!", and finally "Save file".

## Notes

At the moment, only PDF files with A4-sized pages are supported.

For A6-sized booklets, the program will add empty pages until the number of pages is divisible by 8, and for A7-sized ones, until it is divisible by 16.

## Compiling

The dependencies are:

- tkinter (built-in)
- os (built-in)
- sys (built-in)
- PyPDF2
- ttkthemes

On Linux, for some reason the window size needs to be increased (.geometry and .minsize methods for both the main window and the about window).

## License

Released under the GPL v. 3.0 license (see https://www.gnu.org/licenses/gpl-3.0.txt).