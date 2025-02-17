import os

config = {
    'default_actions': [
        'get-secrets',
        'build',
        'check-test',
    ],
    'app_ini_path': '%(obj_dir)s/dist/bin/application.ini',
    'vcs_share_base': os.path.join('y:', os.sep, 'hg-shared'),
    'max_build_output_timeout': 60 * 80,

    'env': {
        'BINSCOPE': os.path.join(
            os.environ['ProgramFiles'], 'Microsoft BinScope 2014', 'Binscope.exe'
        ),
        'HG_SHARE_BASE_DIR': os.path.join('y:', os.sep, 'hg-shared'),
        'MOZBUILD_STATE_PATH': os.path.join(os.getcwd(), '.mozbuild'),
        'MOZ_CRASHREPORTER_NO_REPORT': '1',
        'MOZ_OBJDIR': '%(abs_obj_dir)s',
        'TINDERBOX_OUTPUT': '1',
        'TOOLTOOL_CACHE': 'c:/builds/tooltool_cache',
        'TOOLTOOL_HOME': '/c/builds',
        'MSYSTEM': 'MINGW32',
        'WORKSPACE': '%(base_work_dir)s',
    },
    'upload_env': {
        'UPLOAD_PATH': os.path.join(os.getcwd(), 'public', 'build'),
    },
    'secret_files': [
        {'filename': 'gapi.data',
         'secret_name': 'project/releng/gecko/build/level-%(scm-level)s/gapi.data',
         'min_scm_level': 1},
        {'filename': 'mozilla-desktop-geoloc-api.key',
         'secret_name': 'project/releng/gecko/build/level-%(scm-level)s/mozilla-desktop-geoloc-api.key',
         'min_scm_level': 2, 'default': 'try-build-has-no-secrets'},
    ],
}
