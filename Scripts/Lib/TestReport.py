# Free to use
#

import datetime
import os.path
import TestGlobal
import Log
from TestResult import TestResult

# Constant
OK = TestGlobal.OK
ERROR = TestGlobal.ERROR

NO_RUN = "NO_RUN"


REPORT_CSV_HEADER = "Suite;Case;Description;Priority;Type;Keywords;Preconditions;Postconditions;Expected;Status;Details;Time;Duration;"

SYNTHESIS_CSV_HEADER = "Time;Specified;Run;Pass;Fail;Duration;"

# Define a test report
class TestReport:
    
    def __init__(self, suite_dict):
        self.suite_dict = suite_dict
        self.number_test = 0
        self.number_run = 0
        self.number_pass = 0
        self.number_fail = 0
        self.timestamp = ""
        self.total_duration = 0.0

    # Create Junit XML file report
    def CreateJunitReport(self, file_name):
        ret = OK
        return ret
    
    # Create CSV file report
    def CreateCsvReport(self, file_name):
        ret = OK
        report_string = REPORT_CSV_HEADER + '\n'
        self.timestamp = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
        
        suite = ""
        case = ""
        description = ""
        priority = ""
        type = ""
        keywords = ""
        pre = ""
        post = ""
        expected = ""
        status = NO_RUN
        details = ""
        time = ""
        duration = ""
        other = ""
        
        Log.Log(Log.DEBUG, "Creating CSV report: " + file_name)
        for suite in self.suite_dict:
            ts = self.suite_dict[suite]
            suite = ts.suite
            type = ts.type
            for case in ts.test_case_dict:
                tc = ts.test_case_dict[case]
                self.number_test += 1
                case = tc.case
                description = tc.description
                priority = tc.priority
                keywords = tc.keywords
                pre = tc.preconditions
                post = tc.postconditions
                expected = tc.expected
                if tc.test_case_result:
                    # Test report
                    status = tc.test_case_result.status
                    details = tc.test_case_result.details
                    time = tc.test_case_result.timestamp
                    duration = tc.test_case_result.duration
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
                    other = ""

                
                case_string = suite + ';' + case + ';' + description + ';' + priority + ';' + type + ';' + keywords + ';' + pre + ';' + post + ';' + expected + ';' + status + ';' + details + ';' + time + ';' + duration + ';' + other
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
            
        synthesis_string = self.timestamp + ';' + str(self.number_test) + ';' + str(self.number_run) + ';' + str(self.number_pass) + ';' + str(self.number_fail) + ';' + str(self.total_duration)
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