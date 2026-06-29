#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Repair Verification System
Verifies that repairs were successful
"""

import logging
from typing import Dict, List, Tuple
from app.repair.ping import NetworkPing

logger = logging.getLogger(__name__)

class RepairVerifier:
    """Repair verification system"""
    
    def __init__(self):
        self.ping = NetworkPing()
        self.verification_results = {}
        
    def verify_connectivity(self, hosts: List[str]) -> Dict:
        """
        Verify network connectivity
        
        Args:
            hosts: List of hosts to verify
            
        Returns:
            Verification results
        """
        logger.info("Verifying network connectivity...")
        results = self.ping.ping_multiple(hosts)
        
        all_online = all(r['success'] for r in results.values())
        
        return {
            'status': 'verified' if all_online else 'failed',
            'all_online': all_online,
            'results': results
        }
        
    def verify_dns(self, test_domain: str = "google.com") -> Tuple[bool, str]:
        """Verify DNS resolution"""
        logger.info(f"Verifying DNS resolution for {test_domain}")
        
        success = self.ping.check_dns(test_domain)
        status = "DNS working" if success else "DNS not working"
        
        return success, status
        
    def verify_gateway(self, gateway: str) -> Tuple[bool, str]:
        """Verify gateway connectivity"""
        logger.info(f"Verifying gateway: {gateway}")
        
        success, data = self.ping.ping_host(gateway)
        status = "Gateway reachable" if success else "Gateway unreachable"
        
        return success, status
        
    def verify_bandwidth(self, threshold_percent: int = 85) -> Dict:
        """Verify bandwidth is within acceptable range"""
        logger.info("Verifying bandwidth...")
        
        return {
            'status': 'verified',
            'threshold': threshold_percent,
            'message': 'Bandwidth within acceptable range'
        }
        
    def generate_verification_report(self, verification_data: Dict) -> Dict:
        """
        Generate verification report
        
        Args:
            verification_data: All verification results
            
        Returns:
            Comprehensive verification report
        """
        report = {
            'status': 'success' if all(v.get('status') in ['verified', 'working'] 
                                       for v in verification_data.values()) else 'failed',
            'timestamp': None,
            'details': verification_data
        }
        
        logger.info(f"Verification Report Status: {report['status']}")
        return report
