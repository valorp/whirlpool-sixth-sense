import logging
from enum import Enum
from typing import Callable

from .appliance import Appliance

LOGGER = logging.getLogger(__name__)

ATTR_CYCLE_TIME_REMAINING = "Cavity_TimeStatusEstTimeRemaining"
ATTR_DELAY_TIME_REMAINING = "Cavity_TimeStatusDelayTimeRemaining"

ATTR_CYCLE_STATUS_SENSING = "WashCavity_CycleStatusSensing"
ATTR_CYCLE_STATUS_FILLING = "WashCavity_CycleStatusFilling"
ATTR_CYCLE_STATUS_SOAKING = "WashCavity_CycleStatusSoaking"
ATTR_CYCLE_STATUS_WASHING = "WashCavity_CycleStatusWashing"
ATTR_CYCLE_STATUS_RINSING = "WashCavity_CycleStatusRinsing"
ATTR_CYCLE_STATUS_SPINNING = "WashCavity_CycleStatusSpinning"
ATTR_MACHINE_STATE = "Cavity_CycleStatusMachineState"

ATTRVAL_MACHINE_STATE_STANDBY = "0"
ATTRVAL_MACHINE_STATE_SETTING = "1"
ATTRVAL_MACHINE_STATE_DELAYCOUNTDOWNMODE = "2"
ATTRVAL_MACHINE_STATE_DELAYPAUSE = "3"
ATTRVAL_MACHINE_STATE_SMARTDELAY = "4"
ATTRVAL_MACHINE_STATE_SMARTGRIDPAUSE = "5"
ATTRVAL_MACHINE_STATE_PAUSE = "6"
ATTRVAL_MACHINE_STATE_RUNNINGMAINCYCLE = "7"
ATTRVAL_MACHINE_STATE_RUNNINGPOSTCYCLE = "8"
ATTRVAL_MACHINE_STATE_EXCEPTIONS = "9"
ATTRVAL_MACHINE_STATE_COMPLETE = "10"
ATTRVAL_MACHINE_STATE_POWERFAILURE = "11"
ATTRVAL_MACHINE_STATE_SERVICEDIAGNOSTIC = "12"
ATTRVAL_MACHINE_STATE_FACTORYDIAGNOSTIC = "13"
ATTRVAL_MACHINE_STATE_LIFETEST = "14"
ATTRVAL_MACHINE_STATE_CUSTOMERFOCUSMODE = "15"
ATTRVAL_MACHINE_STATE_DEMOMODE = "16"
ATTRVAL_MACHINE_STATE_HARDSTOPORERROR = "17"
ATTRVAL_MACHINE_STATE_SYSTEMINIT = "18"


class MachineState(Enum):
    Standby = 0
    Setting = 1
    DelayCountdownMode = 2
    DelayPause = 3
    SmartDelay = 4
    SmartGridPause = 5
    Pause = 6
    RunningMainCycle = 7
    RunningPostCycle = 8
    Exceptions = 9
    Complete = 10
    PowerFailure = 11
    ServiceDiagnostic = 12
    FactoryDiagnostic = 13
    LifeTest = 14
    CustomerFocusMode = 15
    DemoMode = 16
    HardStopOrError = 17
    SystemInit = 18

MACHINE_STATE_MAP = {
    MachineState.Standby: ATTRVAL_MACHINE_STATE_STANDBY,
    MachineState.Setting: ATTRVAL_MACHINE_STATE_SETTING,
    MachineState.DelayCountdownMode: ATTRVAL_MACHINE_STATE_DELAYCOUNTDOWNMODE,
    MachineState.DelayPause: ATTRVAL_MACHINE_STATE_DELAYPAUSE,
    MachineState.SmartDelay: ATTRVAL_MACHINE_STATE_SMARTDELAY,
    MachineState.SmartGridPause: ATTRVAL_MACHINE_STATE_SMARTGRIDPAUSE,
    MachineState.Pause: ATTRVAL_MACHINE_STATE_PAUSE,
    MachineState.RunningMainCycle: ATTRVAL_MACHINE_STATE_RUNNINGMAINCYCLE,
    MachineState.RunningPostCycle: ATTRVAL_MACHINE_STATE_RUNNINGPOSTCYCLE,
    MachineState.Exceptions: ATTRVAL_MACHINE_STATE_EXCEPTIONS,
    MachineState.Complete: ATTRVAL_MACHINE_STATE_COMPLETE,
    MachineState.PowerFailure: ATTRVAL_MACHINE_STATE_POWERFAILURE,
    MachineState.ServiceDiagnostic: ATTRVAL_MACHINE_STATE_SERVICEDIAGNOSTIC,
    MachineState.FactoryDiagnostic: ATTRVAL_MACHINE_STATE_FACTORYDIAGNOSTIC,
    MachineState.LifeTest: ATTRVAL_MACHINE_STATE_LIFETEST,
    MachineState.CustomerFocusMode: ATTRVAL_MACHINE_STATE_CUSTOMERFOCUSMODE,
    MachineState.DemoMode: ATTRVAL_MACHINE_STATE_DEMOMODE,
    MachineState.HardStopOrError: ATTRVAL_MACHINE_STATE_HARDSTOPORERROR,
    MachineState.SystemInit: ATTRVAL_MACHINE_STATE_SYSTEMINIT,
}

MACHINE_STATE_MAP_PRETTY = {
    MachineState.Standby: "Standby",
    MachineState.Setting: "Setting",
    MachineState.DelayCountdownMode: "Delay - Countdown",
    MachineState.DelayPause: "Delay - Paused",
    MachineState.SmartDelay: "Delay - Completion time specified",
    MachineState.SmartGridPause: "Delay - Smart grid pause",
    MachineState.Pause: "Paused",
    MachineState.RunningMainCycle: "Running - Main cycle",
    MachineState.RunningPostCycle: "Running - Post cycle",
    MachineState.Exceptions: "Error - Exception",
    MachineState.Complete: "Complete",
    MachineState.PowerFailure: "Error - Power failure",
    MachineState.ServiceDiagnostic: "Diagnostic - Service",
    MachineState.FactoryDiagnostic: "Diagnostic - Factory",
    MachineState.LifeTest: "Diagnostic - Life test",
    MachineState.CustomerFocusMode: "Special mode - Customer Focus",
    MachineState.DemoMode: "Special Mode - Demo",
    MachineState.HardStopOrError: "Error - Hard stop",
    MachineState.SystemInit: "Initializing",
}

class WashCycleState (Enum):
    Sensing = False
    Filling = False
    Soaking = False
    Washing = False
    Rinsing = False
    Spinning= False

class DryCycleState (Enum):
    Sensing = False
    Wet     = False
    Damp    = False
    CoolDown= False


WASH_CYCLE_STATE_MAP = {
    WashCycleState.Sensing: ATTR_CYCLE_STATUS_SENSING,
    WashCycleState.Filling: ATTR_CYCLE_STATUS_FILLING,
    WashCycleState.Soaking: ATTR_CYCLE_STATUS_SOAKING,
    WashCycleState.Washing: ATTR_CYCLE_STATUS_WASHING,
    WashCycleState.Rinsing: ATTR_CYCLE_STATUS_RINSING,
    WashCycleState.Spinning: ATTR_CYCLE_STATUS_SPINNING,
}
WASH_CYCLE_STATE_MAP_PRETTY = {
    WashCycleState.Sensing: "Sensing",
    WashCycleState.Filling: "Filling",
    WashCycleState.Soaking: "Soaking",
    WashCycleState.Washing: "Washing",
    WashCycleState.Rinsing: "Rinsing",
    WashCycleState.Spinning: "Spinning",    
}

class WasherDryer(Appliance):
    def __init__(self, backend_selector, auth, said, attr_changed: Callable):
        Appliance.__init__(self, backend_selector, auth, said, attr_changed)

    def get_machine_state(self):
        state_raw = self.get_attribute(ATTR_MACHINE_STATE)
        for k, v in MACHINE_STATE_MAP.items():
            if v == state_raw:
                return k
        return None

    def get_machine_state_pretty(self):
        machine_state = self.get_machine_state()
        machine_state_raw = self.get_attribute(ATTR_MACHINE_STATE)
        machine_state_pretty = ""
        try:
            machine_state_pretty = MACHINE_STATE_MAP_PRETTY[machine_state]
        except:
            return None

        # Fix Maytag Machine bug -- Time remaining shows 0 (cycle complete) but state continues to be "Running Post Cycle"
        if machine_state_raw == ATTRVAL_MACHINE_STATE_RUNNINGPOSTCYCLE:
            print (machine_state_raw, ATTRVAL_MACHINE_STATE_RUNNINGPOSTCYCLE)
            if self.get_time_remaining_mins() == 0:
                return MACHINE_STATE_MAP_PRETTY[MachineState.Complete]
        return machine_state_pretty


    def get_time_remaining_mins(self):
        return self.attr_value_secs_to_mins_int(self.get_attribute(ATTR_CYCLE_TIME_REMAINING))

    #Handles delay time
    def get_delay_time_remaining_mins(self):
        try: 
            return self.attr_value_secs_to_mins_int(self.get_attribute(ATTR_DELAY_TIME_REMAINING))
        except:
            return 0

    def get_total_delay_and_cycle_time_remaining_mins(self):
        delay_time_remaining = self.get_delay_time_remaining_mins()
        cycle_time_remaining = self.get_time_remaining_mins()
        return delay_time_remaining + cycle_time_remaining

    def get_total_delay_and_cycle_time_remaining_mins_pretty(self):
        total_time_remaining = self.get_total_delay_and_cycle_time_remaining_mins()
        hours = total_time_remaining // 60
        minutes = total_time_remaining % 60
        if minutes < 10:
            minutes = "0" + str(minutes)
        time = "{}:{}".format(hours, minutes)
        return time

    def get_cycle_status_pretty(self):
        for state in WASH_CYCLE_STATE_MAP.items():
            print(state, self.attr_value_to_bool(self.get_attribute(state)))

    def get_cycle_status_sensing(self):
        return self.attr_value_to_bool(self.get_attribute(ATTR_CYCLE_STATUS_SENSING))

    def get_cycle_status_filling(self):
        return self.attr_value_to_bool(self.get_attribute(ATTR_CYCLE_STATUS_FILLING))

    def get_cycle_status_soaking(self):
        return self.attr_value_to_bool(self.get_attribute(ATTR_CYCLE_STATUS_SOAKING))

    def get_cycle_status_washing(self):
        return self.attr_value_to_bool(self.get_attribute(ATTR_CYCLE_STATUS_WASHING))

    def get_cycle_status_rinsing(self):
        return self.attr_value_to_bool(self.get_attribute(ATTR_CYCLE_STATUS_RINSING))

    def get_cycle_status_spinning(self):
        return self.attr_value_to_bool(self.get_attribute(ATTR_CYCLE_STATUS_SPINNING))
