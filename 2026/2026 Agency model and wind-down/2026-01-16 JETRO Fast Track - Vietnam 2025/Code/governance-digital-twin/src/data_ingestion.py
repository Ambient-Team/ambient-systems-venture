"""
Step 1: Data Ingestion Module

Parses JSON/text input (simulating PVN process manuals, regulations, anonymized dossiers)
into structured entities and relationships for the governance graph.
"""

import json
import logging
from typing import Any, Dict, List, Optional, Tuple
from dataclasses import dataclass, asdict
from pathlib import Path
from enum import Enum

from src.logger import setup_logger

logger = setup_logger(__name__)


class EntityType(Enum):
    """Valid entity types for the governance graph."""
    DEPARTMENT = "Department"
    ROLE = "Role"
    DOSSIER = "Dossier"
    PROCESS_STEP = "ProcessStep"
    POLICY = "Policy"
    REGULATION = "Regulation"
    STATE = "State"


class RelationType(Enum):
    """Valid relationship types for the governance graph."""
    SUBMITTED_TO = "SUBMITTED_TO"
    REQUIRES_APPROVAL_FROM = "REQUIRES_APPROVAL_FROM"
    FORWARDS_TO = "FORWARDS_TO"
    DEPENDS_ON = "DEPENDS_ON"
    HAS_CONSTRAINT = "HAS_CONSTRAINT"


@dataclass
class Entity:
    """Represents a node in the governance graph."""
    entity_type: EntityType
    identifier: str  # Unique ID
    name: str
    properties: Dict[str, Any]  # Additional properties (e.g., department_code, role_level)
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert entity to dictionary."""
        return {
            "entity_type": self.entity_type.value,
            "identifier": self.identifier,
            "name": self.name,
            "properties": self.properties,
        }


@dataclass
class Relationship:
    """Represents an edge in the governance graph."""
    relationship_type: RelationType
    source_id: str
    target_id: str
    properties: Dict[str, Any]  # E.g., lag_days, approval_status
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert relationship to dictionary."""
        return {
            "relationship_type": self.relationship_type.value,
            "source_id": self.source_id,
            "target_id": self.target_id,
            "properties": self.properties,
        }


class DataIngestionEngine:
    """
    Ingests and parses process data into structured entities and relationships.
    Handles JSON and text formats.
    """
    
    def __init__(self):
        """Initialize the ingestion engine."""
        self.entities: List[Entity] = []
        self.relationships: List[Relationship] = []
        self.metadata: Dict[str, Any] = {
            "data_source": None,
            "timestamp": None,
            "anonymized": True,
        }
    
    def ingest_json(self, json_data: Dict[str, Any]) -> Tuple[List[Entity], List[Relationship]]:
        """
        Parse JSON process definition into entities and relationships.
        
        Expected JSON structure:
        {
            "process_name": "Regulatory Approval",
            "departments": [...],
            "roles": [...],
            "dossiers": [...],
            "steps": [...],
            "workflows": [
                {
                    "source": "dept_id",
                    "target": "dept_id",
                    "relationship_type": "FORWARDS_TO",
                    "lag_days": 5
                }
            ]
        }
        
        Args:
            json_data: Dictionary containing process data
        
        Returns:
            Tuple of (entities, relationships)
        """
        logger.info(f"Ingesting JSON data: {json_data.get('process_name', 'Unknown')}")
        
        try:
            # Process departments
            for dept in json_data.get("departments", []):
                entity = Entity(
                    entity_type=EntityType.DEPARTMENT,
                    identifier=dept["id"],
                    name=dept["name"],
                    properties={
                        "code": dept.get("code", ""),
                        "description": dept.get("description", ""),
                        "manager": dept.get("manager", ""),
                    }
                )
                self.entities.append(entity)
            
            # Process roles
            for role in json_data.get("roles", []):
                entity = Entity(
                    entity_type=EntityType.ROLE,
                    identifier=role["id"],
                    name=role["name"],
                    properties={
                        "level": role.get("level", ""),
                        "permissions": role.get("permissions", []),
                    }
                )
                self.entities.append(entity)
            
            # Process dossiers
            for dossier in json_data.get("dossiers", []):
                entity = Entity(
                    entity_type=EntityType.DOSSIER,
                    identifier=dossier["id"],
                    name=dossier["name"],
                    properties={
                        "status": dossier.get("status", "Submitted"),
                        "submission_date": dossier.get("submission_date", ""),
                        "applicant_id": dossier.get("applicant_id", ""),  # Anonymized
                    }
                )
                self.entities.append(entity)
            
            # Process steps
            for step in json_data.get("steps", []):
                entity = Entity(
                    entity_type=EntityType.PROCESS_STEP,
                    identifier=step["id"],
                    name=step["name"],
                    properties={
                        "description": step.get("description", ""),
                        "sla_days": step.get("sla_days", 10),
                        "required": step.get("required", True),
                    }
                )
                self.entities.append(entity)
            
            # Process policies/regulations
            for policy in json_data.get("policies", []):
                entity = Entity(
                    entity_type=EntityType.POLICY,
                    identifier=policy["id"],
                    name=policy["name"],
                    properties={
                        "version": policy.get("version", "1.0"),
                        "domain": policy.get("domain", ""),
                        "effective_date": policy.get("effective_date", ""),
                    }
                )
                self.entities.append(entity)
            
            # Process workflows (relationships)
            for workflow in json_data.get("workflows", []):
                relationship = Relationship(
                    relationship_type=RelationType[workflow.get("relationship_type", "FORWARDS_TO")],
                    source_id=workflow["source"],
                    target_id=workflow["target"],
                    properties={
                        "lag_days": workflow.get("lag_days", 0),
                        "approval_required": workflow.get("approval_required", False),
                        "parallel": workflow.get("parallel", False),
                    }
                )
                self.relationships.append(relationship)
            
            logger.info(f"Successfully ingested {len(self.entities)} entities and {len(self.relationships)} relationships")
            
        except KeyError as e:
            logger.error(f"Missing required field in JSON: {e}")
            raise ValueError(f"Invalid JSON structure: missing {e}")
        except Exception as e:
            logger.error(f"Error ingesting JSON data: {e}")
            raise
        
        return self.entities, self.relationships
    
    def ingest_text(self, text_content: str) -> Tuple[List[Entity], List[Relationship]]:
        """
        Parse text content (e.g., process manual) into basic entities.
        Uses simple pattern matching and heuristics.
        
        Args:
            text_content: Raw text content
        
        Returns:
            Tuple of (entities, relationships)
        """
        logger.info("Ingesting text data (heuristic-based parsing)")
        
        try:
            lines = text_content.strip().split("\n")
            
            for line in lines:
                line = line.strip()
                if not line:
                    continue
                
                # Simple heuristics for entity extraction
                if line.startswith("DEPARTMENT:"):
                    dept_info = line.replace("DEPARTMENT:", "").strip()
                    parts = dept_info.split("|")
                    entity = Entity(
                        entity_type=EntityType.DEPARTMENT,
                        identifier=f"dept_{len(self.entities)}",
                        name=parts[0] if parts else dept_info,
                        properties={"description": parts[1] if len(parts) > 1 else ""}
                    )
                    self.entities.append(entity)
                
                elif line.startswith("STEP:"):
                    step_info = line.replace("STEP:", "").strip()
                    parts = step_info.split("|")
                    entity = Entity(
                        entity_type=EntityType.PROCESS_STEP,
                        identifier=f"step_{len(self.entities)}",
                        name=parts[0] if parts else step_info,
                        properties={
                            "sla_days": int(parts[1]) if len(parts) > 1 else 10,
                        }
                    )
                    self.entities.append(entity)
            
            logger.info(f"Extracted {len(self.entities)} entities from text")
            
        except Exception as e:
            logger.error(f"Error ingesting text data: {e}")
            raise
        
        return self.entities, self.relationships
    
    def load_json_file(self, file_path: str) -> Dict[str, Any]:
        """
        Load and parse JSON file.
        
        Args:
            file_path: Path to JSON file
        
        Returns:
            Parsed JSON data
        """
        path = Path(file_path)
        
        if not path.exists():
            logger.error(f"File not found: {file_path}")
            raise FileNotFoundError(f"Data file not found: {file_path}")
        
        try:
            with open(path, "r") as f:
                data = json.load(f)
            logger.info(f"Loaded JSON file: {file_path}")
            return data
        except json.JSONDecodeError as e:
            logger.error(f"Invalid JSON in file {file_path}: {e}")
            raise ValueError(f"Invalid JSON file: {e}")
        except Exception as e:
            logger.error(f"Error loading file {file_path}: {e}")
            raise
    
    def export_structured_data(self, output_path: Optional[str] = None) -> Dict[str, Any]:
        """
        Export ingested data in structured format.
        
        Args:
            output_path: Optional path to save JSON output
        
        Returns:
            Dictionary containing entities and relationships
        """
        export_data = {
            "metadata": self.metadata,
            "entities": [e.to_dict() for e in self.entities],
            "relationships": [r.to_dict() for r in self.relationships],
        }
        
        if output_path:
            path = Path(output_path)
            path.parent.mkdir(parents=True, exist_ok=True)
            with open(path, "w") as f:
                json.dump(export_data, f, indent=2)
            logger.info(f"Exported structured data to {output_path}")
        
        return export_data
    
    def clear(self):
        """Clear all ingested data."""
        self.entities = []
        self.relationships = []
        logger.info("Cleared all ingested data")
