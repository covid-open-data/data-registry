#!/usr/bin/env python3
import yaml
import sys
import os
import tempfile
import argparse
import sh
import shutil


class GenerateRegistry:
    def __init__(self, yml_file, docs_path):
        self.yml_file = os.path.abspath(os.path.expanduser(yml_file))
        self.docs_path = os.path.abspath(os.path.expanduser(docs_path))
        self.errors = []

        if not os.path.isfile(self.yml_file):
            raise FileNotFoundError(self.yml_file)

        if not os.path.exists(self.docs_path):
            print('Creating directory: {0}'.format(self.docs_path))
            os.makedirs(self.docs_path)

    def execute(self):
        print("Registry file: {0}".format(self.yml_file))
        print("Docs directory: {0}".format(self.docs_path))
        yml_data = self.load_yml(self.yml_file)

        md_file_path = os.path.join(self.docs_path, 'registry.md')

        md_lines = ['# Registry']
        for source in yml_data['sources']:
            md_lines.append('## Type: {0}'.format(source['type']))
            md_lines.append(source['description'])
            for repo in source['repos']:
                self._add_repos_to_md(repo, md_lines)

        print('')
        if not self.errors:
            with open(md_file_path, mode='w') as f:
                f.writelines(os.linesep.join(md_lines))
            print('Doc created: {0}'.format(md_file_path))
        else:
            print('Encountered errors. Doc not updated.')

    def _add_repos_to_md(self, repo_url, md_lines):
        # Fix up the URL so the local user can SSH clone the repo from GitHub.
        repo_clone_url = repo_url
        repo_clone_url = repo_clone_url + '.git'
        repo_clone_url = repo_clone_url.replace('https://github.com/', 'git@github.com:')

        print('=' * 80)
        print('Processing repo: {0}'.format(repo_clone_url))
        temp_dir = tempfile.mkdtemp()
        try:
            sh.git.bake(_cwd=temp_dir).clone(repo_clone_url, temp_dir)
            print('Repo cloned to: {0}'.format(temp_dir))

            xform_yml_path = os.path.join(temp_dir, 'xform.yml')
            if not os.path.isfile(xform_yml_path):
                print('WARNING: xform.yml not found.')
                return False
            yml_data = self.load_yml(xform_yml_path)
            md_lines.append(os.linesep)
            md_lines.append('### {0}'.format(yml_data['source_organization']))
            md_lines.append(os.linesep)
            md_lines.append('Xform URL: {0}'.format(repo_url))
            md_lines.append(os.linesep)
            md_lines.append('Source: {0}'.format(yml_data['source_url']))
            md_lines.append(os.linesep)
            md_lines.append('Terms of Use: {0}'.format(yml_data['terms_of_use']))
            md_lines.append(os.linesep)
            md_lines.append('#### Outputs')

            outputs_yml = yml_data['outputs']

            is_extended_table = next(
                (o for o in outputs_yml if
                 o.get('source_organization', None) or o.get('source_url', None) or o.get('terms_of_use', None)),
                None) is not None

            if is_extended_table:
                md_lines.append(
                    '| Source Org. | Source | Terms of Use | Description | Type | File | Admin Level | Schema |')
                md_lines.append('|---|---|---|---|---|---|---|---|')
            else:
                md_lines.append('| Description | Type | File | Admin Level | Schema |')
                md_lines.append('|---|---|---|---|---|')

            for output_yml in outputs_yml:
                output_source_organization = output_yml.get('source_organization', '')
                output_source_url = output_yml.get('source_url', '')
                output_terms_of_use = output_yml.get('terms_of_use', '')
                output_description = output_yml['description']
                output_type = output_yml['type']
                output_file = output_yml['file']
                output_admin_level = output_yml['admin_level']
                output_schema = output_yml['schema']

                if is_extended_table:
                    md_lines.append('| {} | {} | {} | {} | {} | {} | {} | {} |'.format(
                        output_source_organization,
                        output_source_url,
                        output_terms_of_use,
                        output_description,
                        output_type,
                        output_file,
                        output_admin_level,
                        output_schema
                    ))
                else:
                    md_lines.append('| {} | {} | {} | {} | {} |'.format(
                        output_description,
                        output_type,
                        output_file,
                        output_admin_level,
                        output_schema
                    ))

        except Exception as ex:
            err = 'Error processing repo: {0}'.format(ex)
            print(err)
            self.errors.append(err)
        finally:
            if os.path.isdir(temp_dir):
                shutil.rmtree(temp_dir)

    def load_yml(self, path):
        with open(path, mode='r') as f:
            return yaml.full_load(f)


def main():
    parser = argparse.ArgumentParser(description='Generate registry documentation.')
    parser.add_argument('yml', help='The path to registry.yml')
    parser.add_argument('docs', help='The path to the docs directory.')

    args = parser.parse_args()
    GenerateRegistry(args.yml, args.docs).execute()


if __name__ == "__main__":
    main()
