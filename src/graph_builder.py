"""Graph builder that parses conversation structures into interconnected nodes and edges."""

import json
from pathlib import Path
from typing import Dict, List, Optional
from .models import KnowledgeNode, KnowledgeEdge, ConversationCluster, NodeType


class ConversationGraphBuilder:
    """Builds and queries the conversation knowledge graph."""

    def __init__(self, data_dir: Optional[Path] = None):
        self.data_dir = data_dir or Path(__file__).resolve().parent.parent / "raw"
        self.nodes: Dict[str, KnowledgeNode] = {}
        self.edges: List[KnowledgeEdge] = []
        self.clusters: Dict[str, ConversationCluster] = {}

    def add_node(self, node_id: str, label: str, node_type: NodeType, source_file: str) -> KnowledgeNode:
        node = KnowledgeNode(id=node_id, label=label, node_type=node_type, source_file=source_file)
        self.nodes[node_id] = node
        return node

    def add_edge(self, source_id: str, target_id: str, relation: str = "relates_to") -> KnowledgeEdge:
        edge = KnowledgeEdge(source_id=source_id, target_id=target_id, relation=relation)
        self.edges.append(edge)
        return edge

    def build_initial_clusters(self) -> None:
        """Constructs the canonical clusters identified from the conversation turns."""
        hubs = [
            ("cluster_1", "hub_user_intent", "User Intent: Connect Graphify to Claude"),
            ("cluster_2", "hub_installation", "Installation Steps Executed"),
            ("cluster_3", "hub_platform_setup", "Graphify Platform Setup"),
            ("cluster_4", "hub_integration_methods", "Graphify-Claude Integration Methods"),
            ("cluster_5", "hub_web_templates", "Modern Minimalist Free Webpage Templates"),
            ("cluster_6", "hub_convo_flow", "Conversation Flow and Actions"),
        ]

        for cluster_id, hub_id, title in hubs:
            self.add_node(hub_id, title, NodeType.CONCEPT, f"raw/{cluster_id}.md")
            self.clusters[cluster_id] = ConversationCluster(
                cluster_id=cluster_id,
                hub_node_id=hub_id,
                title=title,
                member_ids=[hub_id]
            )

    def find_shortest_path(self, start_id: str, end_id: str) -> List[str]:
        """Simple breadth-first search path traversal across nodes."""
        if start_id not in self.nodes or end_id not in self.nodes:
            return []

        adjacency: Dict[str, List[str]] = {nid: [] for nid in self.nodes}
        for edge in self.edges:
            adjacency[edge.source_id].append(edge.target_id)
            adjacency[edge.target_id].append(edge.source_id)

        visited = {start_id}
        queue = [[start_id]]

        while queue:
            path = queue.pop(0)
            node = path[-1]
            if node == end_id:
                return path
            for neighbor in adjacency.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(path + [neighbor])

        return []
