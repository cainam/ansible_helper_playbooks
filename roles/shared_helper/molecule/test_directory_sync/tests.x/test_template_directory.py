import os
from pytest_bdd import scenarios, given, when, then

# Link the feature file
scenarios('../features/template_directory.feature')

deploy_dir = "/tmp/deploy_test/templates"
sample_templates = os.path.join(os.path.dirname(__file__), "../../sample_data/templates")
expected_outputs = os.path.join(os.path.dirname(__file__), "../../sample_data/output")

@given("sample templates exist")
def templates_exist():
    # In this example, sample templates are pre-existing in sample_data
    return sample_template

@when("the template_directory task is applied")
def run_playbook(ansible_playbook):
    ansible_playbook('../../converge.yml')

@then("the templates should exist in the destination directory")
def check_files_exist(host):
    f = host.file(f"{deploy_dir}/config.conf")
    assert f.exists
    assert f.is_file

@then("the templates should contain the correct rendered content")
def check_content(host):
    f = host.file(f"{deploy_dir}/config.conf")
    expected_file = os.path.join(expected_outputs, "config.conf")
    with open(expected_file) as ef:
        expected_content = ef.read().strip()
    assert f.content_string.strip() == expected_content

