# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['MTFProcessor.py'],
             pathex=['C:\\Users\\raen7\\GitHub\\MTF-Processor-GUI'],
             binaries=[mkl_dlls],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=['PySide2'],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='MTFProcessor',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )

mkl_dlls = [('C:\\Users\\raen7\\AppData\\Local\\Programs\\Python\\Python38\\Lib\\site-packages\\numpy\\DLLs\\mkl_avx.dll', ''),
		 ('C:\\Users\\raen7\\AppData\\Local\\Programs\\Python\\Python38\\Lib\\site-packages\\numpy\\DLLs\\mkl_avx2.dll', ''),
		 ('C:\\Users\\raen7\\AppData\\Local\\Programs\\Python\\Python38\\Lib\\site-packages\\numpy\\DLLs\\mkl_avx512.dll', ''),
		 ('C:\\Users\\raen7\\AppData\\Local\\Programs\\Python\\Python38\\Lib\\site-packages\\numpy\\DLLs\\mkl_core.dll', ''),
		 ('C:\\Users\\raen7\\AppData\\Local\\Programs\\Python\\Python38\\Lib\\site-packages\\numpy\\DLLs\\mkl_def.dll', ''),
		 ('C:\\Users\\raen7\\AppData\\Local\\Programs\\Python\\Python38\\Lib\\site-packages\\numpy\\DLLs\\mkl_intel_thread.dll', ''),
		 ('C:\\Users\\raen7\\AppData\\Local\\Programs\\Python\\Python38\\Lib\\site-packages\\numpy\\DLLs\\mkl_mc.dll', ''),
		 ('C:\\Users\\raen7\\AppData\\Local\\Programs\\Python\\Python38\\Lib\\site-packages\\numpy\\DLLs\\mkl_mc3.dll', ''),
		 ('C:\\Users\\raen7\\AppData\\Local\\Programs\\Python\\Python38\\Lib\\site-packages\\numpy\\DLLs\\mkl_rt.dll', ''),
		 ('C:\\Users\\raen7\\AppData\\Local\\Programs\\Python\\Python38\\Lib\\site-packages\\numpy\\DLLs\\mkl_sequential.dll', ''),
		 ('C:\\Users\\raen7\\AppData\\Local\\Programs\\Python\\Python38\\Lib\\site-packages\\numpy\\DLLs\\mkl_tbb_thread.dll', ''),
		 ('C:\\Users\\raen7\\AppData\\Local\\Programs\\Python\\Python38\\Lib\\site-packages\\numpy\\DLLs\\mkl_vml_avx.dll', ''),
		 ('C:\\Users\\raen7\\AppData\\Local\\Programs\\Python\\Python38\\Lib\\site-packages\\numpy\\DLLs\\mkl_vml_avx2.dll', ''),
		 ('C:\\Users\\raen7\\AppData\\Local\\Programs\\Python\\Python38\\Lib\\site-packages\\numpy\\DLLs\\mkl_vml_avx512.dll', ''),
		 ('C:\\Users\\raen7\\AppData\\Local\\Programs\\Python\\Python38\\Lib\\site-packages\\numpy\\DLLs\\mkl_vml_cmpt.dll', ''),
		 ('C:\\Users\\raen7\\AppData\\Local\\Programs\\Python\\Python38\\Lib\\site-packages\\numpy\\DLLs\\mkl_vml_def.dll', ''),
		 ('C:\\Users\\raen7\\AppData\\Local\\Programs\\Python\\Python38\\Lib\\site-packages\\numpy\\DLLs\\mkl_vml_mc.dll', ''),
		 ('C:\\Users\\raen7\\AppData\\Local\\Programs\\Python\\Python38\\Lib\\site-packages\\numpy\\DLLs\\mkl_vml_mc2.dll', ''),
		 ('C:\\Users\\raen7\\AppData\\Local\\Programs\\Python\\Python38\\Lib\\site-packages\\numpy\\DLLs\\mkl_vml_mc3.dll', ''),
		 ('C:\\Users\\raen7\\AppData\\Local\\Programs\\Python\\Python38\\Lib\\site-packages\\numpy\\DLLs\\libiomp5md.dll', '')]