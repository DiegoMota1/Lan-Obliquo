import cx_Freeze

executables = [cx_Freeze.Executable('main.py')]

cx_Freeze.setup(
        name = "aula lanc obliquo",
        options = {'build_exe': {'packages': ['pygame'],
                                 'include_files':['Moto_class.py', 'Fontes.py', 'parametros.py', 'attack_1.png', 'icon.png']}},
        executables = executables
    )