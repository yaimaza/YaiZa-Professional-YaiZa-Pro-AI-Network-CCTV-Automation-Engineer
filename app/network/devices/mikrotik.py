#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Mikrotik Router Integration
Handles Mikrotik router operations and network management
"""

import logging
import paramiko
from typing import Dict, List, Optional

logger = logging.getLogger(__name__)

class MikrotikRouter:
    """Mikrotik router controller"""
    
    def __init__(self, host: str, username: str, password: str, port: int = 22):
        """
        Initialize Mikrotik router
        
        Args:
            host: Router IP address
            username: SSH username
            password: SSH password
            port: SSH port (default: 22)
        """
        self.host = host
        self.username = username
        self.password = password
        self.port = port
        self.ssh = None
        
    def connect(self) -> bool:
        """Connect to Mikrotik router"""
        try:
            logger.info(f"Connecting to Mikrotik router at {self.host}")
            self.ssh = paramiko.SSHClient()
            self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh.connect(self.host, port=self.port, username=self.username, password=self.password, timeout=10)
            logger.info("Connected to Mikrotik router successfully")
            return True
        except Exception as e:
            logger.error(f"Failed to connect to Mikrotik: {str(e)}")
            return False
            
    def disconnect(self):
        """Disconnect from router"""
        if self.ssh:
            self.ssh.close()
            logger.info("Disconnected from Mikrotik router")
            
    def execute_command(self, command: str) -> str:
        """Execute command on router"""
        try:
            stdin, stdout, stderr = self.ssh.exec_command(command)
            return stdout.read().decode('utf-8')
        except Exception as e:
            logger.error(f"Failed to execute command: {str(e)}")
            return ""
            
    def get_interfaces(self) -> List[Dict]:
        """Get network interfaces"""
        try:
            output = self.execute_command("/interface print")
            interfaces = []
            # Parse interface data
            return interfaces
        except Exception as e:
            logger.error(f"Failed to get interfaces: {str(e)}")
            return []
            
    def get_bandwidth(self) -> Dict:
        """Get bandwidth usage"""
        try:
            output = self.execute_command("/queue simple print")
            return {'bandwidth': output}
        except Exception as e:
            logger.error(f"Failed to get bandwidth: {str(e)}")
            return {}
            
    def get_firewall_rules(self) -> List[Dict]:
        """Get firewall rules"""
        try:
            output = self.execute_command("/ip firewall filter print")
            return []
        except Exception as e:
            logger.error(f"Failed to get firewall rules: {str(e)}")
            return []
            
    def get_status(self) -> Dict:
        """Get router status"""
        return {
            'online': True,
            'host': self.host,
            'device_type': 'Mikrotik',
            'interfaces': len(self.get_interfaces())
        }
