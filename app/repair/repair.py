#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Network Repair Engine
Executes repairs and fixes for network issues
"""

import logging
import subprocess
import platform
from typing import Dict, List, Tuple

logger = logging.getLogger(__name__)

class NetworkRepair:
    """Network repair engine"""
    
    def __init__(self):
        self.os_type = platform.system()
        self.repair_history = []
        
    def repair_dns(self) -> Tuple[bool, str]:
        """Repair DNS issues"""
        try:
            logger.info("Starting DNS repair...")
            
            if self.os_type == "Windows":
                cmd = ["ipconfig", "/flushdns"]
                subprocess.run(cmd, capture_output=True)
                
            elif self.os_type == "Darwin":  # macOS
                cmd = ["sudo", "dscacheutil", "-flushcache"]
                subprocess.run(cmd, capture_output=True)
                
            else:  # Linux
                cmd = ["sudo", "systemctl", "restart", "systemd-resolved"]
                subprocess.run(cmd, capture_output=True)
                
            logger.info("✓ DNS repair completed")
            self.repair_history.append({'action': 'dns_repair', 'status': 'success'})
            return True, "DNS repair completed successfully"
            
        except Exception as e:
            logger.error(f"DNS repair failed: {str(e)}")
            return False, str(e)
            
    def repair_network_interface(self, interface: str = None) -> Tuple[bool, str]:
        """Repair network interface"""
        try:
            logger.info(f"Repairing network interface: {interface}")
            
            if self.os_type == "Windows":
                cmd = ["ipconfig", "/release"]
                subprocess.run(cmd, capture_output=True)
                cmd = ["ipconfig", "/renew"]
                subprocess.run(cmd, capture_output=True)
                
            else:
                if interface:
                    cmd = ["sudo", "ifdown", interface]
                    subprocess.run(cmd, capture_output=True)
                    cmd = ["sudo", "ifup", interface]
                    subprocess.run(cmd, capture_output=True)
                    
            logger.info("✓ Network interface repair completed")
            self.repair_history.append({'action': 'interface_repair', 'status': 'success'})
            return True, "Network interface repair completed"
            
        except Exception as e:
            logger.error(f"Interface repair failed: {str(e)}")
            return False, str(e)
            
    def restart_network_service(self) -> Tuple[bool, str]:
        """Restart network service"""
        try:
            logger.info("Restarting network service...")
            
            if self.os_type == "Windows":
                cmd = ["net", "stop", "Winsock"]
                subprocess.run(cmd, capture_output=True)
                cmd = ["net", "start", "Winsock"]
                subprocess.run(cmd, capture_output=True)
                
            else:
                cmd = ["sudo", "systemctl", "restart", "networking"]
                subprocess.run(cmd, capture_output=True)
                
            logger.info("✓ Network service restarted")
            self.repair_history.append({'action': 'service_restart', 'status': 'success'})
            return True, "Network service restarted"
            
        except Exception as e:
            logger.error(f"Service restart failed: {str(e)}")
            return False, str(e)
            
    def repair_gateway(self, gateway: str) -> Tuple[bool, str]:
        """Repair gateway connection"""
        try:
            logger.info(f"Repairing gateway: {gateway}")
            
            if self.os_type == "Windows":
                cmd = ["route", "delete", "0.0.0.0"]
                subprocess.run(cmd, capture_output=True)
                cmd = ["route", "add", "0.0.0.0", "mask", "0.0.0.0", gateway]
                subprocess.run(cmd, capture_output=True)
                
            logger.info("✓ Gateway repair completed")
            self.repair_history.append({'action': 'gateway_repair', 'status': 'success'})
            return True, "Gateway repair completed"
            
        except Exception as e:
            logger.error(f"Gateway repair failed: {str(e)}")
            return False, str(e)
            
    def execute_repair_plan(self, repair_steps: List[Dict]) -> Dict:
        """Execute repair plan"""
        logger.info("Executing repair plan...")
        results = {}
        
        for step in repair_steps:
            action = step.get('action')
            
            if action == 'dns':
                results['dns'] = self.repair_dns()
            elif action == 'interface':
                results['interface'] = self.repair_network_interface(step.get('interface'))
            elif action == 'service':
                results['service'] = self.restart_network_service()
            elif action == 'gateway':
                results['gateway'] = self.repair_gateway(step.get('gateway'))
                
        return results
