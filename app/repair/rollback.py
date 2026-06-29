#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Rollback Manager
Handles rollback of changes if repair fails
"""

import logging
from typing import Dict, List, Tuple
from pathlib import Path

logger = logging.getLogger(__name__)

class RollbackManager:
    """Rollback manager for failed repairs"""
    
    def __init__(self):
        self.rollback_history = []
        self.snapshots = {}
        
    def create_snapshot(self, device_name: str, config: Dict) -> str:
        """
        Create a snapshot before making changes
        
        Args:
            device_name: Name of device
            config: Configuration to snapshot
            
        Returns:
            Snapshot ID
        """
        try:
            snapshot_id = f"{device_name}_{len(self.snapshots)}"
            self.snapshots[snapshot_id] = {
                'device': device_name,
                'config': config,
                'status': 'active'
            }
            
            logger.info(f"Snapshot created: {snapshot_id}")
            return snapshot_id
            
        except Exception as e:
            logger.error(f"Snapshot creation failed: {str(e)}")
            return None
            
    def rollback_to_snapshot(self, snapshot_id: str) -> Tuple[bool, Dict]:
        """
        Rollback to a previous snapshot
        
        Args:
            snapshot_id: ID of snapshot to rollback to
            
        Returns:
            Tuple of (success, restored_config)
        """
        try:
            if snapshot_id not in self.snapshots:
                logger.error(f"Snapshot not found: {snapshot_id}")
                return False, {}
                
            snapshot = self.snapshots[snapshot_id]
            logger.info(f"Rolling back to snapshot: {snapshot_id}")
            
            self.rollback_history.append({
                'snapshot_id': snapshot_id,
                'device': snapshot['device'],
                'status': 'rolled_back'
            })
            
            logger.info("✓ Rollback completed successfully")
            return True, snapshot['config']
            
        except Exception as e:
            logger.error(f"Rollback failed: {str(e)}")
            return False, {}
            
    def get_rollback_points(self, device_name: str = None) -> List[Dict]:
        """Get available rollback points"""
        try:
            points = []
            
            for snapshot_id, snapshot in self.snapshots.items():
                if device_name is None or snapshot['device'] == device_name:
                    points.append({
                        'snapshot_id': snapshot_id,
                        'device': snapshot['device'],
                        'status': snapshot['status']
                    })
                    
            logger.info(f"Found {len(points)} rollback point(s)")
            return points
            
        except Exception as e:
            logger.error(f"Failed to get rollback points: {str(e)}")
            return []
            
    def cleanup_snapshots(self, keep_count: int = 5) -> int:
        """Clean up old snapshots"""
        try:
            snapshot_list = list(self.snapshots.items())
            
            if len(snapshot_list) > keep_count:
                to_remove = len(snapshot_list) - keep_count
                
                for i in range(to_remove):
                    snapshot_id = snapshot_list[i][0]
                    del self.snapshots[snapshot_id]
                    logger.info(f"Deleted old snapshot: {snapshot_id}")
                    
                return to_remove
                
            return 0
            
        except Exception as e:
            logger.error(f"Snapshot cleanup failed: {str(e)}")
            return 0
