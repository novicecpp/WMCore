#!/usr/bin/env python

import unittest
import logging

from WMCore.Services.PhEDEx.PhEDEx import PhEDEx
from WMCore.Services.PhEDEx.DataStructs.SubscriptionList import PhEDExSubscription
from WMCore.Services.PhEDEx.DataStructs.SubscriptionList import SubscriptionList


class PhEDExTest(unittest.TestCase):
    """
    Provide setUp and tearDown for Reader package module
    
    """
    def setUp(self):
        """
        setUP global values
        """
        #dsUrl = "http://cmswttest.cern.ch:7701/phedex/datasvc/xml/tbedi"
        #dsUrl = "https://cmsweb.cern.ch/phedex/datasvc/xml/tbedi"
        #self.phedexTestDS = "http://cmswttest.cern.ch/phedex/datasvc/xml/tbedi"
        self.phedexTestDS = "http://cmswttest.cern.ch/phedex/datasvc/json/tbedi"
        
        self.dbsTestUrl = "http://cmssrv49.fnal.gov:8989/DBS/servlet/DBSServlet"
        self.testNode = "TX_Test1_Buffer"
        
    def testInjection(self):
        dict = {}
        dict['endpoint'] = self.phedexTestDS
        phedexApi = PhEDEx(dict)
        
        print phedexApi.injectBlocks(self.dbsTestUrl, self.testNode, "/Cosmics/Sryu_Test/RAW")   

    def testSubscription(self):
        dict = {}
        dict['endpoint'] = self.phedexTestDS
        phedexApi = PhEDEx(dict)
        print phedexApi.injectBlocks(self.dbsTestUrl, self.testNode, "/Cosmics/Sryu_Test/RAW")   
        print phedexApi.injectBlocks(self.dbsTestUrl, self.testNode, "/Cosmics/Sryu_Test/RECO")   
        
        sub1 = PhEDExSubscription(self.dbsTestUrl, "/Cosmics/Sryu_Test/RAW", self.testNode)
        sub2 = PhEDExSubscription(self.dbsTestUrl, "/Cosmics/Sryu_Test/RECO", self.testNode)
        subList = SubscriptionList()
        subList.addSubscription(sub1)
        subList.addSubscription(sub2)
        print subList
        for sub in subList.getSubscriptionList():
            print sub
            print phedexApi.subscribe(self.dbsTestUrl, sub)   
    
if __name__ == '__main__':
        
    unittest.main()
