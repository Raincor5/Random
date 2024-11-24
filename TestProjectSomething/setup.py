from cx_Freeze import setup, Executable

setup(
    name="CSV Uploader for GrG",
    version="1.1",
    description="Davai",
    executables=[Executable("UI.py", base="Win32GUI")], requires=['tkinterdnd2']
)