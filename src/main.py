"""Entrypoint script for querying the conversation graph."""

from .graph_builder import ConversationGraphBuilder
from .models import NodeType


def main() -> None:
    builder = ConversationGraphBuilder()
    builder.build_initial_clusters()

    print(f"Graph initialized with {len(builder.nodes)} nodes and {len(builder.clusters)} clusters.")
    for cluster_id, cluster in builder.clusters.items():
        print(f" - {cluster.cluster_id}: {cluster.title} (Hub: {cluster.hub_node_id})")


if __name__ == "__main__":
    main()
