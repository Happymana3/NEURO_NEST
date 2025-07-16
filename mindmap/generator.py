from pyvis.network import Network
from typing import Dict

class MindMapGenerator:
    def create_mindmap(self, topics: Dict) -> str:
        """Generate interactive mind map from topics"""
        net = Network(height="400px", width="100%", bgcolor="#222222", font_color="white")
        
        # Add central node
        net.add_node("center", label="Journal Entry", color="#ff6b6b", size=30)
        
        # Add topic nodes
        for topic_id, topic_data in topics.items():
            net.add_node(topic_id, label=topic_data["main"], color="#4ecdc4", size=20)
            net.add_edge("center", topic_id)
        
        # Generate HTML
        html = net.generate_html()
        return html