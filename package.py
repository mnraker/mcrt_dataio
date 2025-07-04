# Copyright 2024 DreamWorks Animation LLC
# SPDX-License-Identifier: Apache-2.0

# -*- coding: utf-8 -*-
import os, sys

unittestflags = (['@run_all', '--unittest-xml']
                 if os.environ.get('BROKEN_CUSTOM_ARGS_UNITTESTS') else [])

name = 'mcrt_dataio'

if 'early' not in locals() or not callable(early):
    def early(): return lambda x: x

@early()
def version():
    """
    Increment the build in the version.
    """
    _version = '15.7'
    from rezbuild import earlybind
    return earlybind.version(this, _version)

description = 'Mcrt dataio package'

authors = [
    'PSW Rendering and Shading',
    'moonbase-dev@dreamworks.com',
    'Toshi.Kato@dreamworks.com'
]

help = ('For assistance, '
        "please contact the folio's owner at: moonbase-dev@dreamworks.com")

variants = [
    ['os-rocky-9', 'opt_level-optdebug', 'refplat-vfx2023.1', 'gcc-11.x'],
    ['os-rocky-9', 'opt_level-debug',    'refplat-vfx2023.1', 'gcc-11.x'],
    ['os-rocky-9', 'opt_level-optdebug', 'refplat-vfx2023.1', 'clang-17.0.6.x'],
    ['os-rocky-9', 'opt_level-optdebug', 'refplat-vfx2022.0', 'gcc-9.3.x.1'],
    ['os-rocky-9', 'opt_level-optdebug', 'refplat-vfx2024.0', 'gcc-11.x'],

    ['os-CentOS-7', 'opt_level-optdebug', 'refplat-vfx2022.0', 'gcc-9.3.x.1'],
    ['os-CentOS-7', 'opt_level-debug',    'refplat-vfx2022.0', 'gcc-9.3.x.1'],
]

conf_rats_variants = variants[0:2]
conf_CI_variants = variants

requires = [
    'arras4_core-4.10',
    'freetype-2',
    'mcrt_denoise-6.7',
    'mcrt_messages-14.2',
    'scene_rdl2-15.7'
]

private_build_requires = [
    'cmake_modules-1.0',
    'cppunit',
]

commandstr = lambda i: "cd build/"+os.path.join(*variants[i])+"; ctest -j $(nproc)"
testentry = lambda i: ("variant%d" % i,
                       { "command": commandstr(i),
                         "requires": ["cmake-3.23"] + variants[i] } )
testlist = [testentry(i) for i in range(len(variants))]
tests = dict(testlist)

def commands():
    prependenv('CMAKE_MODULE_PATH', '{root}/lib64/cmake')
    prependenv('LD_LIBRARY_PATH', '{root}/lib64')
    prependenv('PATH', '{root}/bin')

uuid = '2e6694ba-3c4d-4d2d-bc67-e5b031886c38'

config_version = 0
