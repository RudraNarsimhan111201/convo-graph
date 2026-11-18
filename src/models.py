"""Data models representing conversation graph entities and relations."""

from dataclasses import dataclass, field
from enum import Enum
from typing import List, Dict, Optional, Any


class NodeType(str, Enum):
    CONCEPT = "concept"
    TOOL = "tool"
    ACTION = "action"
    PLATFORM = "platform"
    METHOD = "method"


@dataclass
class KnowledgeNode:
    """Represents a node in the conversation knowledge graph."""
    id: str
    label: str
    node_type: NodeType
    source_file: str
    attributes: Dict[str, Any] = field(default_factory=dict)

    def describe(self) -> str:
        return f"[{self.node_type.value.upper()}] {self.label} (source: {self.source_file})"


@dataclass
class KnowledgeEdge:
    """Represents a directed link between two knowledge nodes."""
    source_id: str
    target_id: str
    relation: str
    weight: float = 1.0


@dataclass
class ConversationCluster:
    """Represents a clustered group of related concepts."""
    cluster_id: str
    hub_node_id: str
    title: str
    member_ids: List[str] = field(default_factory=list)
