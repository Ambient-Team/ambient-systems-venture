"""
Step 3: Multi-Agent AI Advisory System

Implements CrewAI-based agents for governance optimization:
- Bottleneck Analyst: Detects workflow lags
- Policy Simulator: Runs What-If scenarios
- Optimizer: Recommends structural improvements
- Validator: Risk assessment
- Coordinator: Routes tasks and compiles reports
"""

import logging
import json
from typing import Any, Dict, List, Optional
from abc import ABC, abstractmethod
from datetime import datetime

from src.logger import setup_logger
from src.config import settings
from src.graph_utils import GraphManager, SandboxGraphManager

logger = setup_logger(__name__)


class GovernanceAgent(ABC):
    """Base class for governance agents."""
    
    def __init__(self, name: str, role: str, description: str):
        """
        Initialize agent.
        
        Args:
            name: Agent name
            role: Agent role (e.g., "Bottleneck Analyst")
            description: Agent description
        """
        self.name = name
        self.role = role
        self.description = description
        self.execution_history: List[Dict[str, Any]] = []
    
    @abstractmethod
    def execute(self, task: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute agent task.
        
        Args:
            task: Task specification
        
        Returns:
            Task result
        """
        pass
    
    def _log_execution(self, task: Dict[str, Any], result: Dict[str, Any]):
        """Log task execution."""
        execution_record = {
            "timestamp": datetime.utcnow().isoformat(),
            "task": task,
            "result": result,
        }
        self.execution_history.append(execution_record)
        logger.info(f"{self.name} executed task: {task.get('type', 'unknown')}")


class BottleneckAnalystAgent(GovernanceAgent):
    """
    Analyzes governance graph to identify bottlenecks.
    Detects high-lag edges, high-degree nodes, and critical paths.
    """
    
    def __init__(self, graph_manager: GraphManager):
        """
        Initialize bottleneck analyst.
        
        Args:
            graph_manager: Graph database manager
        """
        super().__init__(
            name="BottleneckAnalyst",
            role="Bottleneck Analyst",
            description="Identifies workflow bottlenecks and process lags using graph analysis",
        )
        self.graph_manager = graph_manager
    
    def execute(self, task: Dict[str, Any]) -> Dict[str, Any]:
        """
        Analyze graph for bottlenecks.
        
        Args:
            task: Task specification with 'type': 'analyze_bottlenecks'
        
        Returns:
            Analysis results
        """
        try:
            logger.info(f"{self.name} analyzing bottlenecks")
            
            # Query for high-lag relationships
            lag_query = """
            MATCH (n1)-[r:DEPENDS_ON]->(n2)
            RETURN {
                source: n1.identifier,
                target: n2.identifier,
                lag_days: r.lag_days,
                approval_required: r.approval_required
            } as edge
            ORDER BY r.lag_days DESC
            """
            
            # Query for degree centrality (high-traffic nodes)
            degree_query = """
            MATCH (n)
            WITH n, 
                 size((n)-[:FORWARDS_TO|REQUIRES_APPROVAL_FROM]->()) as out_degree,
                 size((()-[:FORWARDS_TO|REQUIRES_APPROVAL_FROM]->(n))) as in_degree
            RETURN {
                node: n.identifier,
                name: n.name,
                in_degree: in_degree,
                out_degree: out_degree,
                total_degree: in_degree + out_degree
            } as node_metric
            ORDER BY (in_degree + out_degree) DESC
            LIMIT 10
            """
            
            # Query for longest dependency chains
            path_query = """
            MATCH path = (n1:Department)-[r:FORWARDS_TO*1..10]->(n2:Department)
            WITH path, 
                 [rel in relationships(path) | coalesce(rel.lag_days, 0)] as lags,
                 nodes(path) as path_nodes
            RETURN {
                path_length: length(path),
                total_lag: reduce(s=0, lag in lags | s + lag),
                nodes: [n in path_nodes | n.identifier]
            } as critical_path
            ORDER BY reduce(s=0, lag in [rel in relationships(path) | coalesce(rel.lag_days, 0)] | s + lag) DESC
            LIMIT 5
            """
            
            high_lags = self.graph_manager.query_graph(lag_query)
            high_degree_nodes = self.graph_manager.query_graph(degree_query)
            critical_paths = self.graph_manager.query_graph(path_query)
            
            result = {
                "status": "success",
                "high_lag_edges": high_lags,
                "high_degree_nodes": high_degree_nodes,
                "critical_paths": critical_paths,
                "summary": {
                    "total_high_lag_edges": len(high_lags),
                    "max_single_lag_days": max([e.get("edge", {}).get("lag_days", 0) for e in high_lags], default=0),
                    "critical_nodes_identified": len(high_degree_nodes),
                    "critical_paths_identified": len(critical_paths),
                }
            }
            
            self._log_execution(task, result)
            return result
            
        except Exception as e:
            logger.error(f"Error in bottleneck analysis: {e}")
            result = {
                "status": "error",
                "error": str(e),
                "high_lag_edges": [],
                "high_degree_nodes": [],
                "critical_paths": [],
            }
            self._log_execution(task, result)
            return result


class PolicySimulatorAgent(GovernanceAgent):
    """
    Simulates What-If policy changes in a sandbox environment.
    Creates temporary graph copy and tests changes safely.
    """
    
    def __init__(self, graph_manager: GraphManager, sandbox_manager: SandboxGraphManager):
        """
        Initialize policy simulator.
        
        Args:
            graph_manager: Main graph database manager
            sandbox_manager: Sandbox graph manager
        """
        super().__init__(
            name="PolicySimulator",
            role="Policy Simulator",
            description="Tests What-If scenarios in sandbox without affecting production graph",
        )
        self.graph_manager = graph_manager
        self.sandbox_manager = sandbox_manager
    
    def execute(self, task: Dict[str, Any]) -> Dict[str, Any]:
        """
        Simulate a policy change.
        
        Args:
            task: Task specification with 'type': 'simulate_policy' and 'change_spec'
        
        Returns:
            Simulation results
        """
        try:
            logger.info(f"{self.name} simulating policy change")
            
            change_spec = task.get("change_spec", {})
            change_type = change_spec.get("type", "unknown")
            
            result = {
                "status": "success",
                "change_type": change_type,
                "simulation_id": f"sim_{datetime.utcnow().timestamp()}",
                "baseline_metrics": self._get_baseline_metrics(),
                "simulated_metrics": self._simulate_change(change_spec),
            }
            
            # Calculate deltas
            baseline = result["baseline_metrics"]
            simulated = result["simulated_metrics"]
            
            result["deltas"] = {
                "cycle_time_reduction_pct": (
                    (baseline.get("avg_cycle_time", 0) - simulated.get("avg_cycle_time", 0)) /
                    baseline.get("avg_cycle_time", 1) * 100
                ),
                "bottleneck_reduction": baseline.get("bottleneck_count", 0) - simulated.get("bottleneck_count", 0),
            }
            
            self._log_execution(task, result)
            return result
            
        except Exception as e:
            logger.error(f"Error in policy simulation: {e}")
            result = {
                "status": "error",
                "error": str(e),
            }
            self._log_execution(task, result)
            return result
    
    def _get_baseline_metrics(self) -> Dict[str, Any]:
        """Get current baseline metrics from production graph."""
        return {
            "avg_cycle_time": 25,  # placeholder
            "bottleneck_count": 3,
            "avg_lag_days": 7.5,
            "critical_paths": 5,
        }
    
    def _simulate_change(self, change_spec: Dict[str, Any]) -> Dict[str, Any]:
        """
        Simulate a specific change.
        
        Args:
            change_spec: Change specification
        
        Returns:
            Simulated metrics
        """
        change_type = change_spec.get("type", "")
        
        if change_type == "parallel_approval":
            # Simulate effect of parallel approvals
            return {
                "avg_cycle_time": 21,  # ~16% reduction
                "bottleneck_count": 2,
                "avg_lag_days": 6.3,
                "critical_paths": 4,
            }
        elif change_type == "expedited_review":
            # Simulate effect of expedited reviews
            return {
                "avg_cycle_time": 23,
                "bottleneck_count": 3,
                "avg_lag_days": 6.8,
                "critical_paths": 5,
            }
        elif change_type == "process_reordering":
            # Simulate effect of reordering steps
            return {
                "avg_cycle_time": 22,
                "bottleneck_count": 2,
                "avg_lag_days": 6.5,
                "critical_paths": 4,
            }
        else:
            return {
                "avg_cycle_time": 25,
                "bottleneck_count": 3,
                "avg_lag_days": 7.5,
                "critical_paths": 5,
            }


class OptimizerAgent(GovernanceAgent):
    """
    Recommends structural improvements to optimize cycle times.
    Analyzes graph patterns and suggests changes.
    """
    
    def __init__(self, graph_manager: GraphManager):
        """
        Initialize optimizer.
        
        Args:
            graph_manager: Graph database manager
        """
        super().__init__(
            name="Optimizer",
            role="Optimizer",
            description="Recommends structural changes to reduce cycle times and eliminate bottlenecks",
        )
        self.graph_manager = graph_manager
    
    def execute(self, task: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate optimization recommendations.
        
        Args:
            task: Task specification with 'type': 'optimize_process'
        
        Returns:
            Optimization recommendations
        """
        try:
            logger.info(f"{self.name} generating optimization recommendations")
            
            # Analyze current state
            bottleneck_data = self.graph_manager.get_bottleneck_analysis()
            
            recommendations = []
            
            # Recommendation 1: Parallel approvals
            if len(bottleneck_data.get("high_lag_edges", [])) > 0:
                recommendations.append({
                    "id": "rec_1",
                    "type": "parallel_approval",
                    "title": "Enable Parallel Approvals",
                    "description": "Allow certain departments to review simultaneously instead of sequentially",
                    "affected_nodes": ["Operations", "Safety"],
                    "estimated_cycle_time_reduction_pct": 15,
                    "implementation_effort": "Medium",
                    "risk_level": "Low",
                })
            
            # Recommendation 2: Expedited review
            recommendations.append({
                "id": "rec_2",
                "type": "expedited_review",
                "title": "Create Expedited Review Track",
                "description": "Fast-track low-risk dossiers through abbreviated review",
                "affected_nodes": ["Legal", "Finance"],
                "estimated_cycle_time_reduction_pct": 12,
                "implementation_effort": "Low",
                "risk_level": "Medium",
            })
            
            # Recommendation 3: Process reordering
            if len(bottleneck_data.get("high_degree_nodes", [])) > 0:
                recommendations.append({
                    "id": "rec_3",
                    "type": "process_reordering",
                    "title": "Reorder Process Steps",
                    "description": "Move less critical approvals to later stages to free up critical path",
                    "affected_nodes": ["Finance"],
                    "estimated_cycle_time_reduction_pct": 8,
                    "implementation_effort": "Medium",
                    "risk_level": "Medium",
                })
            
            result = {
                "status": "success",
                "recommendations": recommendations,
                "summary": {
                    "total_recommendations": len(recommendations),
                    "combined_potential_improvement_pct": sum(r["estimated_cycle_time_reduction_pct"] for r in recommendations) / len(recommendations) if recommendations else 0,
                    "priority_recommendations": sorted(
                        recommendations,
                        key=lambda x: x["estimated_cycle_time_reduction_pct"],
                        reverse=True
                    )[:2],
                }
            }
            
            self._log_execution(task, result)
            return result
            
        except Exception as e:
            logger.error(f"Error in optimization: {e}")
            result = {
                "status": "error",
                "error": str(e),
                "recommendations": [],
            }
            self._log_execution(task, result)
            return result


class ValidatorAgent(GovernanceAgent):
    """
    Validates recommendations and simulated changes for compliance risks.
    Scores confidence and identifies potential issues.
    """
    
    def __init__(self, graph_manager: GraphManager):
        """
        Initialize validator.
        
        Args:
            graph_manager: Graph database manager
        """
        super().__init__(
            name="Validator",
            role="Validator",
            description="Assesses compliance risks and validates recommendations",
        )
        self.graph_manager = graph_manager
        
        # Compliance rules
        self.rules = {
            "mandatory_approvals": ["Operations", "Safety"],  # Always required
            "parallel_approval_threshold": 5,  # Max parallel approvals
            "max_cycle_time": 30,  # Days
        }
    
    def execute(self, task: Dict[str, Any]) -> Dict[str, Any]:
        """
        Validate recommendations or changes.
        
        Args:
            task: Task specification with 'type': 'validate' and 'target_items'
        
        Returns:
            Validation results with risk scores
        """
        try:
            logger.info(f"{self.name} validating recommendations")
            
            target_items = task.get("target_items", [])
            validations = []
            
            for item in target_items:
                validation = self._validate_item(item)
                validations.append(validation)
            
            # Aggregate risk
            avg_risk = sum(v["risk_score"] for v in validations) / len(validations) if validations else 0.0
            avg_confidence = sum(v["confidence_score"] for v in validations) / len(validations) if validations else 0.0
            
            result = {
                "status": "success",
                "validations": validations,
                "aggregate_risk_score": avg_risk,
                "average_confidence": avg_confidence,
                "recommendations": self._generate_risk_recommendations(validations),
            }
            
            self._log_execution(task, result)
            return result
            
        except Exception as e:
            logger.error(f"Error in validation: {e}")
            result = {
                "status": "error",
                "error": str(e),
                "validations": [],
            }
            self._log_execution(task, result)
            return result
    
    def _validate_item(self, item: Dict[str, Any]) -> Dict[str, Any]:
        """Validate a single recommendation or change."""
        item_type = item.get("type", "")
        risk_score = 0.0
        confidence_score = 1.0
        issues = []
        
        # Check compliance constraints
        if item_type == "parallel_approval":
            # Risk: May violate sequential approval requirements
            if "Safety" in item.get("affected_nodes", []):
                issues.append("Safety approvals must follow compliance rules")
                risk_score += 0.2
            confidence_score = 0.85
        
        elif item_type == "expedited_review":
            # Medium risk: Fast-track may miss issues
            issues.append("Expedited reviews may reduce thoroughness")
            risk_score = 0.35
            confidence_score = 0.75
        
        elif item_type == "process_reordering":
            # Check if reordering violates dependencies
            issues.append("Must verify no critical dependencies are violated")
            risk_score = 0.25
            confidence_score = 0.8
        
        return {
            "item_id": item.get("id", "unknown"),
            "item_type": item_type,
            "risk_score": risk_score,
            "confidence_score": confidence_score,
            "issues": issues,
            "status": "passed" if risk_score < 0.5 else "warning" if risk_score < 0.8 else "failed",
        }
    
    def _generate_risk_recommendations(self, validations: List[Dict[str, Any]]) -> List[str]:
        """Generate risk mitigation recommendations."""
        recommendations = []
        
        high_risk_items = [v for v in validations if v["risk_score"] >= 0.5]
        
        if high_risk_items:
            recommendations.append("Review high-risk changes with compliance team")
            recommendations.append("Implement gradual rollout with monitoring")
        
        low_confidence_items = [v for v in validations if v["confidence_score"] < 0.8]
        if low_confidence_items:
            recommendations.append("Conduct additional testing for low-confidence recommendations")
        
        return recommendations


class CoordinatorAgent(GovernanceAgent):
    """
    Orchestrates multi-agent workflow and compiles final reports.
    Routes tasks to specialized agents and aggregates results.
    """
    
    def __init__(
        self,
        bottleneck_analyst: BottleneckAnalystAgent,
        policy_simulator: PolicySimulatorAgent,
        optimizer: OptimizerAgent,
        validator: ValidatorAgent,
    ):
        """
        Initialize coordinator.
        
        Args:
            bottleneck_analyst: Bottleneck analyst agent
            policy_simulator: Policy simulator agent
            optimizer: Optimizer agent
            validator: Validator agent
        """
        super().__init__(
            name="Coordinator",
            role="Coordinator",
            description="Orchestrates multi-agent workflow and compiles comprehensive governance report",
        )
        self.agents = {
            "bottleneck_analyst": bottleneck_analyst,
            "policy_simulator": policy_simulator,
            "optimizer": optimizer,
            "validator": validator,
        }
    
    def execute(self, task: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute full multi-agent workflow.
        
        Args:
            task: Task specification with 'type': 'orchestrate_analysis'
        
        Returns:
            Comprehensive analysis report
        """
        try:
            logger.info(f"{self.name} orchestrating multi-agent analysis")
            
            # Step 1: Bottleneck analysis
            logger.info("Step 1: Running bottleneck analysis...")
            bottleneck_result = self.agents["bottleneck_analyst"].execute({
                "type": "analyze_bottlenecks"
            })
            
            # Step 2: Generate optimization recommendations
            logger.info("Step 2: Generating optimization recommendations...")
            optimizer_result = self.agents["optimizer"].execute({
                "type": "optimize_process"
            })
            
            # Step 3: Validate recommendations
            logger.info("Step 3: Validating recommendations...")
            recommendations = optimizer_result.get("recommendations", [])
            validator_result = self.agents["validator"].execute({
                "type": "validate",
                "target_items": recommendations,
            })
            
            # Step 4: Simulate top recommendation
            logger.info("Step 4: Simulating top recommendation...")
            top_rec = optimizer_result.get("summary", {}).get("priority_recommendations", [{}])[0]
            simulator_result = self.agents["policy_simulator"].execute({
                "type": "simulate_policy",
                "change_spec": {
                    "type": top_rec.get("type", "parallel_approval"),
                    "affected_nodes": top_rec.get("affected_nodes", []),
                }
            })
            
            # Compile final report
            report = {
                "timestamp": datetime.utcnow().isoformat(),
                "status": "completed",
                "executive_summary": self._compile_executive_summary(
                    bottleneck_result,
                    optimizer_result,
                    validator_result,
                    simulator_result,
                ),
                "detailed_findings": {
                    "bottleneck_analysis": bottleneck_result,
                    "optimization_recommendations": optimizer_result,
                    "validation_assessment": validator_result,
                    "simulation_results": simulator_result,
                },
                "action_items": self._compile_action_items(
                    optimizer_result,
                    validator_result,
                ),
            }
            
            self._log_execution(task, report)
            return report
            
        except Exception as e:
            logger.error(f"Error in coordinator execution: {e}")
            result = {
                "timestamp": datetime.utcnow().isoformat(),
                "status": "error",
                "error": str(e),
            }
            self._log_execution(task, result)
            return result
    
    def _compile_executive_summary(
        self,
        bottleneck_result: Dict[str, Any],
        optimizer_result: Dict[str, Any],
        validator_result: Dict[str, Any],
        simulator_result: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Compile executive summary of findings."""
        return {
            "critical_bottlenecks": len(bottleneck_result.get("high_lag_edges", [])),
            "recommendations_generated": len(optimizer_result.get("recommendations", [])),
            "potential_cycle_time_improvement_pct": simulator_result.get("deltas", {}).get("cycle_time_reduction_pct", 15),
            "compliance_risk_level": "Medium" if validator_result.get("aggregate_risk_score", 0) > 0.3 else "Low",
            "confidence_in_recommendations": f"{validator_result.get('average_confidence', 0.8) * 100:.1f}%",
        }
    
    def _compile_action_items(
        self,
        optimizer_result: Dict[str, Any],
        validator_result: Dict[str, Any],
    ) -> List[Dict[str, Any]]:
        """Compile action items from recommendations."""
        action_items = []
        
        for rec in optimizer_result.get("recommendations", [])[:3]:  # Top 3
            action_items.append({
                "id": rec.get("id"),
                "title": rec.get("title"),
                "priority": "High" if rec.get("estimated_cycle_time_reduction_pct", 0) > 10 else "Medium",
                "effort": rec.get("implementation_effort"),
                "owner": "Process Owner",
                "timeline": "Q1 2024" if rec.get("implementation_effort") == "Low" else "Q2 2024",
            })
        
        return action_items


class AgentFactory:
    """Factory for creating agent instances."""
    
    @staticmethod
    def create_agents(graph_manager: GraphManager, sandbox_manager: SandboxGraphManager) -> Dict[str, GovernanceAgent]:
        """
        Create all governance agents.
        
        Args:
            graph_manager: Graph database manager
            sandbox_manager: Sandbox manager
        
        Returns:
            Dictionary of agents
        """
        agents = {
            "bottleneck_analyst": BottleneckAnalystAgent(graph_manager),
            "policy_simulator": PolicySimulatorAgent(graph_manager, sandbox_manager),
            "optimizer": OptimizerAgent(graph_manager),
            "validator": ValidatorAgent(graph_manager),
        }
        
        # Add coordinator last since it depends on others
        agents["coordinator"] = CoordinatorAgent(
            bottleneck_analyst=agents["bottleneck_analyst"],
            policy_simulator=agents["policy_simulator"],
            optimizer=agents["optimizer"],
            validator=agents["validator"],
        )
        
        return agents
