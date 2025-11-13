# -*- mode: python ; coding: utf-8 -*-


block_cipher = None

a = Analysis(
    ['Grammer.py'],
    pathex=[
    r'D:\grammer',
    r'D:\grammer\src'
    ],  # 项目根目录
    binaries=[],
    datas=[],  # 可以在这里添加数据文件
    hiddenimports=[
        'src',
        'src.module',
        'src.module.DomainGrammer',
        'src.module.IcpGrammer',
        'src.module.IpGrammer',
        'src.module.KeyWordGrammer',
        'src.module.wrapper',
        # 添加所有自定义模块
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='Grammer',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,  # 使用UPX压缩，减小文件体积
    console=True,  # 如果是有控制台的程序设为True，GUI程序设为False
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='微信图片_2025-11-13_122332_919.jpg',  # ！！！在这里指定图标文件 ！！！
)
