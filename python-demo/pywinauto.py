from pywinauto.application import Application
app = Application(backend="win32").start("notepad.exe")
app.UntitledNotepad.type_keys("%FX")


