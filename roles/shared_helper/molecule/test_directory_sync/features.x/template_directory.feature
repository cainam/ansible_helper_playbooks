Feature: Template directory synchronization

  Scenario: Deploy templates to target directory
    Given sample templates exist
    When the template_directory task is applied
    Then the templates should exist in the destination directory
    And the templates should contain the correct rendered content

