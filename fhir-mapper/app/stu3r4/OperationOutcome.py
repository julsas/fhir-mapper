from fhir.resources.operationoutcome import (OperationOutcome, OperationOutcomeIssue)

operation_outcome_example = {
  "resourceType": "OperationOutcome",
  "issue": [
    {
      "severity": "error",
      "code": "code-invalid"
    }
  ]
}

issue_example = {
    "severity": "error",
    "code": "code-invalid"
}

def resource_type_not_supported():
    operation_outcome = OperationOutcome.parse_obj(operation_outcome_example)
    issue = OperationOutcomeIssue.parse_obj(issue_example)
    issue.severity = 'information'
    issue.code = 'not-supported'
    issue.diagnostics = 'The provided resource is not within the scope of this mapping engine.'
    operation_outcome.issue = [issue]
    return operation_outcome