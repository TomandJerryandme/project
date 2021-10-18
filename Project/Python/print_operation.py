import win32print
import tempfile
import win32api

file_name = tempfile.mkdtemp(".txt")
open(file_name, "w").write("Something to write")
win32api.ShellExecute(
    0,
    "printto",
    file_name,
    '"%s"' % win32print.GetDefaultPrinter(),
    ".",
    0
)