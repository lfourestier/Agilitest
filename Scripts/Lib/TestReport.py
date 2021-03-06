# Free to use
#

import datetime
import os.path
import TestGlobal
import Log
from TestRules import TestRules
from TestResult import TestResult

# Constant
OK = TestGlobal.OK
ERROR = TestGlobal.ERROR

NO_RUN = TestResult.NO_RUN


REPORT_CSV_HEADER = "Suite,Case,Description,Priority,Type,Keywords,Preconditions,Postconditions,Expected,Status,Details,Time,Duration"

SYNTHESIS_CSV_HEADER = "Time,Specified,Run,Pass,Fail,Duration,Tag"

# Define a test report
class TestReport:
    
    def __init__(self, tag, suite_dict, rules):
        self.suite_dict = suite_dict
        if rules:
            self.rules = rules
        else:
            self.rules = TestRules(None, None)
        self.number_test = 0
        self.number_run = 0
        self.number_pass = 0
        self.number_fail = 0
        self.timestamp = ""
        self.total_duration = 0.0
        if tag:
            self.tag = tag
        else:
            self.tag = " "

    # Create Junit XML file report
    def CreateJunitReport(self, file_name):
        ret = OK
        return ret
    
    # Create CSV file report
    def CreateCsvReport(self, file_name):
        ret = OK
        self.timestamp = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
        report_string = str(self.tag) + ',' + str(self.timestamp) + '\n' + REPORT_CSV_HEADER + '\n'
        
        if not self.suite_dict:
            return ERROR
        
        suite = ""
        case = ""
        description = ""
        priority = ""
        suite_type = ""
        keywords = ""
        pre = ""
        post = ""
        expected = ""
        status = NO_RUN
        details = ""
        time = ""
        duration = ""
        
        Log.Log(Log.DEBUG, "Creating CSV report: " + file_name)
        for s in self.suite_dict:
            ts = self.suite_dict[s]
            if not self.rules.IsSuiteIncluded(ts) or self.rules.IsSuiteIgnored(ts):
                continue
            suite = TestGlobal.StripComas(ts.suite)
            suite_type = TestGlobal.StripComas(ts.type)
            if not ts.test_case_dict:
                continue
            for c in ts.test_case_dict:
                tc = ts.test_case_dict[c]
                if not self.rules.IsCaseIncluded(tc) or self.rules.IsCaseIgnored(tc):
                    continue
                self.number_test += 1
                case = TestGlobal.StripComas(tc.case)
                description = TestGlobal.StripComas(tc.description)
                priority = TestGlobal.StripComas(tc.priority)
                keywords = TestGlobal.ComaToSemicolon(tc.keywords)
                pre = TestGlobal.StripComas(tc.preconditions)
                post = TestGlobal.StripComas(tc.postconditions)
                expected = TestGlobal.StripComas(tc.expected)
                if tc.test_case_result:
                    # Test report
                    status = tc.test_case_result.status
                    details = TestGlobal.StripComas(tc.test_case_result.details)
                    time = TestGlobal.StripComas(tc.test_case_result.timestamp)
                    duration = TestGlobal.StripComas(tc.test_case_result.duration)
                    # Synthesis
                    self.number_run += 1
                    if status == TestResult.PASS:
                        self.number_pass += 1
                    else:
                        self.number_fail += 1
                    self.total_duration += float(tc.test_case_result.duration)
                else:
                    status = NO_RUN
                    details = ""
                    time = ""
                    duration = ""

                
                case_string = suite + ',' + case + ',' + description + ',' + priority + ',' + suite_type + ',' + keywords + ',' + pre + ',' + post + ',' + expected + ',' + status + ',' + details + ',' + time + ',' + duration 
                Log.Log(Log.DEBUG, case_string)
                report_string += case_string  + '\n'
        
        f = open(file_name, "w+")
        if f:
            f.write(report_string)
            f.close()
        else:
            Log.Log(Log.ERROR, "Cannot open report file: " + file_name)
            ret = ERROR
        return ret
    
    # Update synthesis CSV file report
    def UpdateSynthesisReport(self, file_name):
        ret = OK
        Log.Log(Log.DEBUG, "Creating synthesis report: " + file_name)
        
        # Some sanity check
        if self.number_run != (self.number_pass + self.number_fail):
            Log.Log(Log.WARNING, "Incoherences between numbers of test run, passed and failed!")
            
        synthesis_string = self.timestamp + ',' + str(self.number_test) + ',' + str(self.number_run) + ',' + str(self.number_pass) + ',' + str(self.number_fail) + ',' + str(self.total_duration) + ',' + str(self.tag)
        Log.Log(Log.DEBUG, synthesis_string)
        
        if os.path.exists(file_name):
            f = open(file_name, "a")
            if f:
                f.write(synthesis_string  + '\n')
                f.close()
            else:
                Log.Log(Log.ERROR, "Cannot open report file: " + file_name)
                ret = ERROR
        else:
            f = open(file_name, "w+")
            if f:
                f.write(SYNTHESIS_CSV_HEADER + '\n')
                f.write(synthesis_string  + '\n')
                f.close()
            else:
                Log.Log(Log.ERROR, "Cannot open report file: " + file_name)
                ret = ERROR
        return ret