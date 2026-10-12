"""
Main orchestration script for the Governance Digital Twin PoC.

Runs all three steps:
1. Data Ingestion - Parse process data from JSON/text
2. Graph Mapping - Build Neo4j knowledge graph and detect bottlenecks
3. Multi-Agent Analysis - Run AI advisory system with sandbox simulations
"""

import json
import logging
import sys
from pathlib import Path
from typing import Optional

from src.config import settings
from src.logger import setup_logger
from src.data_ingestion import DataIngestionEngine
from src.graph_utils import GraphManager, SandboxGraphManager
from src.agents import AgentFactory

logger = setup_logger(__name__)


class GovernanceDigitalTwinOrchestrator:
    """Main orchestrator for the governance digital twin PoC."""
    
    def __init__(self):
        """Initialize the orchestrator."""
        self.ingestion_engine = DataIngestionEngine()
        self.graph_manager: Optional[GraphManager] = None
        self.sandbox_manager: Optional[SandboxGraphManager] = None
        self.agents = {}
        
        logger.info("Initialized Governance Digital Twin Orchestrator")
    
    def step_1_data_ingestion(self, data_source: str) -> bool:
        """
        Step 1: Data Ingestion
        
        Parse input data (JSON or text) into structured entities and relationships.
        
        Args:
            data_source: Path to JSON file or raw text data
        
        Returns:
            True if successful
        """
        try:
            logger.info("="*80)
            logger.info("STEP 1: DATA INGESTION - Parse process data")
            logger.info("="*80)
            
            # Check if input is a file path or raw text
            source_path = Path(data_source)
            
            if source_path.exists() and source_path.suffix == ".json":
                logger.info(f"Ingesting from JSON file: {data_source}")
                json_data = self.ingestion_engine.load_json_file(data_source)
                entities, relationships = self.ingestion_engine.ingest_json(json_data)
            else:
                logger.info("Ingesting from text input")
                entities, relationships = self.ingestion_engine.ingest_text(data_source)
            
            logger.info(f"✓ Ingested {len(entities)} entities and {len(relationships)} relationships")
            
            # Export ingested data
            output_path = Path("data/ingested_data.json")
            self.ingestion_engine.export_structured_data(str(output_path))
            
            return True
            
        except Exception as e:
            logger.error(f"✗ Data ingestion failed: {e}")
            return False
    
    def step_2_graph_mapping(self, sandbox: bool = False) -> bool:
        """
        Step 2: Graph Mapping (Digital Twin)
        
        Build Neo4j property graph with nodes and relationships.
        Run centrality algorithms to detect bottlenecks.
        
        Args:
            sandbox: If True, creates sandbox copy for testing
        
        Returns:
            True if successful
        """
        try:
            logger.info("="*80)
            logger.info("STEP 2: GRAPH MAPPING - Build knowledge graph and detect bottlenecks")
            logger.info("="*80)
            
            # Initialize graph manager
            self.graph_manager = GraphManager()
            self.sandbox_manager = SandboxGraphManager(self.graph_manager)
            
            logger.info("Creating graph nodes and relationships...")
            
            # Ingest entities and relationships into Neo4j
            self.graph_manager.ingest_entities_and_relationships(
                self.ingestion_engine.entities,
                self.ingestion_engine.relationships,
                sandbox=False,
            )
            
            logger.info(f"✓ Created graph with {len(self.ingestion_engine.entities)} nodes")
            
            # Run bottleneck analysis
            logger.info("Running bottleneck analysis (centrality measures)...")
            bottleneck_analysis = self.graph_manager.get_bottleneck_analysis(sandbox=False)
            
            logger.info(f"✓ Detected {len(bottleneck_analysis.get('high_lag_edges', []))} high-lag edges")
            logger.info(f"✓ Identified {len(bottleneck_analysis.get('high_degree_nodes', []))} critical nodes")
            logger.info(f"✓ Found {len(bottleneck_analysis.get('longest_paths', []))} critical paths")
            
            # Log findings
            if bottleneck_analysis.get("high_lag_edges"):
                logger.info("\nTop bottlenecks (by lag days):")
                for edge in bottleneck_analysis["high_lag_edges"][:3]:
                    edge_data = edge.get("edge", {})
                    logger.info(f"  - {edge_data.get('source')} → {edge_data.get('target')}: {edge_data.get('lag_days')} days")
            
            # Create sandbox copy if requested
            if sandbox:
                logger.info("Creating sandbox copy for What-If simulations...")
                self.sandbox_manager.create_sandbox_copy()
                logger.info("✓ Sandbox copy created successfully")
            
            return True
            
        except Exception as e:
            logger.error(f"✗ Graph mapping failed: {e}")
            return False
    
    def step_3_multi_agent_analysis(self) -> dict:
        """
        Step 3: Multi-Agent AI Advisory & Sandbox Simulations
        
        Run CrewAI-based agents:
        - Bottleneck Analyst: Detect lags and critical nodes
        - Policy Simulator: Run What-If scenarios
        - Optimizer: Recommend structural changes
        - Validator: Assess compliance risks
        - Coordinator: Compile comprehensive report
        
        Returns:
            Final governance analysis report
        """
        try:
            logger.info("="*80)
            logger.info("STEP 3: MULTI-AGENT AI ANALYSIS - Advisory & What-If simulations")
            logger.info("="*80)
            
            if not self.graph_manager:
                raise RuntimeError("Graph manager not initialized. Run Step 2 first.")
            
            # Create agents
            logger.info("Initializing multi-agent system...")
            self.agents = AgentFactory.create_agents(self.graph_manager, self.sandbox_manager)
            logger.info(f"✓ Created {len(self.agents)} specialized agents")
            
            # Run coordinator workflow
            logger.info("\nLaunching multi-agent analysis workflow...")
            coordinator = self.agents["coordinator"]
            
            report = coordinator.execute({
                "type": "orchestrate_analysis"
            })
            
            # Log key findings
            logger.info("\n" + "="*80)
            logger.info("ANALYSIS RESULTS")
            logger.info("="*80)
            
            if report.get("status") == "completed":
                exec_summary = report.get("executive_summary", {})
                logger.info(f"✓ Bottlenecks identified: {exec_summary.get('critical_bottlenecks')}")
                logger.info(f"✓ Recommendations generated: {exec_summary.get('recommendations_generated')}")
                logger.info(f"✓ Potential cycle time improvement: {exec_summary.get('potential_cycle_time_improvement_pct', 15):.1f}%")
                logger.info(f"✓ Compliance risk level: {exec_summary.get('compliance_risk_level')}")
                
                # Log action items
                action_items = report.get("action_items", [])
                if action_items:
                    logger.info(f"\nTop {min(3, len(action_items))} Action Items:")
                    for i, item in enumerate(action_items[:3], 1):
                        logger.info(f"  {i}. {item.get('title')} (Priority: {item.get('priority')})")
            else:
                logger.error(f"Analysis failed: {report.get('error')}")
            
            return report
            
        except Exception as e:
            logger.error(f"✗ Multi-agent analysis failed: {e}")
            return {
                "status": "error",
                "error": str(e),
            }
    
    def run_full_poc(self, data_source: str) -> bool:
        """
        Run complete PoC pipeline: Steps 1, 2, 3.
        
        Args:
            data_source: Path to example data JSON file
        
        Returns:
            True if all steps completed successfully
        """
        logger.info("\n" + "="*80)
        logger.info("GOVERNANCE DIGITAL TWIN - PROOF OF CONCEPT")
        logger.info("="*80 + "\n")
        
        try:
            # Step 1
            if not self.step_1_data_ingestion(data_source):
                return False
            
            logger.info("")
            
            # Step 2
            if not self.step_2_graph_mapping(sandbox=settings.app.sandbox_mode):
                return False
            
            logger.info("")
            
            # Step 3
            final_report = self.step_3_multi_agent_analysis()
            
            # Export final report
            self.export_final_report(final_report)
            
            logger.info("\n" + "="*80)
            logger.info("✓ GOVERNANCE DIGITAL TWIN PoC COMPLETED SUCCESSFULLY")
            logger.info("="*80)
            
            return True
            
        except Exception as e:
            logger.error(f"✗ PoC execution failed: {e}")
            return False
    
    def export_final_report(self, report: dict):
        """
        Export final analysis report to JSON.
        
        Args:
            report: Analysis report dictionary
        """
        try:
            output_path = Path("data/final_report.json")
            output_path.parent.mkdir(parents=True, exist_ok=True)
            
            with open(output_path, "w") as f:
                json.dump(report, f, indent=2, default=str)
            
            logger.info(f"\n✓ Final report exported to {output_path}")
            
        except Exception as e:
            logger.error(f"Failed to export report: {e}")
    
    def cleanup(self):
        """Cleanup resources."""
        try:
            if self.graph_manager:
                self.graph_manager.close()
                logger.info("✓ Closed Neo4j connection")
        except Exception as e:
            logger.error(f"Error during cleanup: {e}")


def main():
    """Main entry point."""
    try:
        # Get data source from command line or use default
        if len(sys.argv) > 1:
            data_source = sys.argv[1]
        else:
            data_source = "data/example_process.json"
        
        # Run orchestrator
        orchestrator = GovernanceDigitalTwinOrchestrator()
        success = orchestrator.run_full_poc(data_source)
        orchestrator.cleanup()
        
        sys.exit(0 if success else 1)
        
    except KeyboardInterrupt:
        logger.info("\n✗ Execution interrupted by user")
        sys.exit(1)
    except Exception as e:
        logger.error(f"✗ Fatal error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
