from enum import Enum


class ClientMessageWorkflowNodeStartedType(str, Enum):
    WORKFLOW_NODE_STARTED = "workflow.node.started"

    def __str__(self) -> str:
        return str(self.value)
