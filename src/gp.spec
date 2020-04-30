# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['gp.py'],
             pathex=['/Users/hasegawakaito/ken_works/get_production/src'],
             binaries=[ ( '/usr/local/bin/chromedriver', './driver' ) ],
             datas=[('/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/eel/eel.js', 'eel'), ('web', 'web')],
             hiddenimports=['bottle_websocket'],
             hookspath=[],
             runtime_hooks=[],
             excludes=['FixTk', 'tcl', 'tk', '_tkinter', 'tkinter', 'Tkinter'],
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
          name='gp',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False )
app = BUNDLE(exe,
             name='gp.app',
             icon=None,
             bundle_identifier=None)
