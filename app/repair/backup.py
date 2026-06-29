#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Configuration Backup Manager
Handles backup of device configurations before repair
"""

import logging
import json
import shutil
from pathlib import Path
from datetime import datetime

logger = logging.getLogger(__name__)

class BackupManager:
    """Configuration backup manager"""
    
    def __init__(self, backup_dir: str = None):
        """
        Initialize backup manager
        
        Args:
            backup_dir: Directory to store backups
        """
        self.backup_dir = Path(backup_dir) if backup_dir else Path.home() / '.yaiza-pro' / 'backups'
        self.backup_dir.mkdir(parents=True, exist_ok=True)
        
    def create_backup(self, device_name: str, config_data: Dict) -> str:
        """
        Create configuration backup
        
        Args:
            device_name: Name of device
            config_data: Configuration data to backup
            
        Returns:
            Backup file path
        """
        try:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            backup_file = self.backup_dir / f"{device_name}_{timestamp}.json"
            
            with open(backup_file, 'w') as f:
                json.dump({
                    'device': device_name,
                    'timestamp': timestamp,
                    'config': config_data
                }, f, indent=2)
                
            logger.info(f"Backup created: {backup_file}")
            return str(backup_file)
            
        except Exception as e:
            logger.error(f"Backup failed: {str(e)}")
            return None
            
    def list_backups(self, device_name: str = None) -> List[str]:
        """List available backups"""
        try:
            backups = []
            
            if device_name:
                pattern = f"{device_name}_*.json"
            else:
                pattern = "*.json"
                
            for backup in self.backup_dir.glob(pattern):
                backups.append(str(backup))
                
            logger.info(f"Found {len(backups)} backup(s)")
            return sorted(backups, reverse=True)
            
        except Exception as e:
            logger.error(f"Failed to list backups: {str(e)}")
            return []
            
    def restore_backup(self, backup_file: str) -> Dict:
        """
        Restore configuration from backup
        
        Args:
            backup_file: Path to backup file
            
        Returns:
            Restored configuration data
        """
        try:
            with open(backup_file, 'r') as f:
                data = json.load(f)
                
            logger.info(f"Backup restored from: {backup_file}")
            return data['config']
            
        except Exception as e:
            logger.error(f"Restore failed: {str(e)}")
            return {}
            
    def cleanup_old_backups(self, keep_count: int = 10) -> int:
        """Remove old backups keeping only recent ones"""
        try:
            backups = sorted(self.backup_dir.glob("*.json"), key=lambda x: x.stat().st_mtime, reverse=True)
            
            if len(backups) > keep_count:
                for old_backup in backups[keep_count:]:
                    old_backup.unlink()
                    logger.info(f"Deleted old backup: {old_backup}")
                    
                return len(backups) - keep_count
                
            return 0
            
        except Exception as e:
            logger.error(f"Cleanup failed: {str(e)}")
            return 0
