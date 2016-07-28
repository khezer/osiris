import os
from pyramid.scaffolds import PyramidTemplate


class OsirisProjectTemplate(PyramidTemplate):
    _template_dir = 'osirisproject'
    summary = 'A osiris project can be used for a new project'

    def pre(self, command, output_dir, vars):
        return PyramidTemplate.pre(self, command, output_dir, vars)

    def run(self, command, output_dir, vars):
        project_dir = output_dir.lower()
        self.pre(command, project_dir, vars)
        self.write_files(command, project_dir, vars)
        self.post(command, project_dir, vars)


class OsirisAppTemplate(PyramidTemplate):
    _template_dir = 'osirisapp'
    summary = 'A osiris app can be used for a new app in Osiris Project'

    def pre(self, command, output_dir, vars):
        base_dir = os.path.dirname(output_dir)
        vars['osirisproject'] = base_dir.split('/')[-2]
        return PyramidTemplate.pre(self, command, output_dir, vars)

    def run(self, command, output_dir, vars):
        base_dir = os.path.dirname(output_dir)
        project_dir = base_dir.split('/')[-1]
        app_dir = base_dir + '/' + project_dir + '/apps/' + vars['package']
        self.pre(command, app_dir, vars)
        self.write_files(command, app_dir, vars)
        self.post(command, app_dir, vars)
